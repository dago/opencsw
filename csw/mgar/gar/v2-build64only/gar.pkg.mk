# vim: ft=make ts=4 sw=4 noet
#
# $Id$
#
# Copyright 2006 Cory Omand
#
# Redistribution and/or use, with or without modification, is
# permitted.  This software is without warranty of any kind.  The
# author(s) shall not be liable in the event that use of the
# software causes damage.
#
# gar.pkg.mk - Build Solaris packages
#
#

ifeq ($(DEBUG_PACKAGING),)
_DBG=@
else
_DBG=
endif

PKGINFO ?= /usr/bin/pkginfo

# You can use either PACKAGES with dynamic gspec-files or explicitly add gspec-files to DISTFILES.
# Do "PACKAGES = CSWmypkg" when you build a package whose NAME is not the package name.
# If no explicit gspec-files have been defined the default name for the package is CSW$(NAME).
# The whole processing is done from _PKG_SPECS, which includes all packages to be build.

# SRCPACKAGE_BASE is the name of the package containing the sourcefiles for all packages
# generated from this GAR recipe. It defaults to the first defined package name or gspec.
# SRCPACKAGE is the name of the package containing the sources

ifeq ($(origin PACKAGES), undefined)
PACKAGES        = $(if $(filter %.gspec,$(DISTFILES)),,CSW$(NAME))
CATALOGNAME    ?= $(if $(filter %.gspec,$(DISTFILES)),,$(subst -,_,$(NAME)))
SRCPACKAGE_BASE = $(firstword $(basename $(filter %.gspec,$(DISTFILES))) $(PACKAGES))
SRCPACKAGE     ?= $(SRCPACKAGE_BASE)-src
SPKG_SPECS     ?= $(basename $(filter %.gspec,$(DISTFILES))) $(PACKAGES) $(if $(NOSOURCEPACKAGE),,$(SRCPACKAGE))
else
CATALOGNAME    ?= $(if $(filter-out $(firstword $(PACKAGES)),$(PACKAGES)),,$(subst -,_,$(patsubst CSW%,%,$(PACKAGES))))
SRCPACKAGE_BASE = $(firstword $(PACKAGES))
SRCPACKAGE     ?= $(SRCPACKAGE_BASE)-src
OBSOLETING_PKGS ?= $(sort $(PACKAGES) $(FOREIGN_PACKAGES))
OBSOLETED_PKGS ?= $(sort $(foreach P,$(OBSOLETING_PKGS),$(OBSOLETED_BY_$P)))
SPKG_SPECS     ?= $(sort $(basename $(filter %.gspec,$(DISTFILES))) $(PACKAGES) $(OBSOLETED_PKGS) $(if $(NOSOURCEPACKAGE),,$(SRCPACKAGE)))
endif

# For creating default pkgnames, e.g. CSWpy-$(DASHED_NAME)
DASHED_NAME    ?= $(subst _,-,$(patsubst CSW%,%,$(NAME)))

# Automatic definitions for source package
CATALOGNAME_$(SRCPACKAGE)   ?= $(patsubst CSW%,%,$(SRCPACKAGE_BASE))_src
SPKG_DESC_$(SRCPACKAGE)     ?= $(SPKG_DESC_$(SRCPACKAGE_BASE)) Source Package
ARCHALL_$(SRCPACKAGE)       ?= 1
# XXX: Use Repository Root instead of fixed URL as base
GARSYSTEMVERSION ?= $(shell $(SVN) propget svn:externals $(CURDIR) | perl -ane 'if($$F[0] eq "gar") { print ($$F[1]=~m(https://gar.svn.sourceforge.net/svnroot/gar/csw/mgar/gar/(.*))),"\n";}')
GARPKG_v1 = CSWgar-v1
GARPKG_v2 = CSWgar-v2
RUNTIME_DEP_PKGS_$(SRCPACKAGE) ?= $(or $(GARPKG_$(GARSYSTEMVERSION)),$(error GAR version $(GARSYSTEMVERSION) unknown))

# Set the catalog release based on hostname.  E.g. building on current9s will
# set CATALOG_RELEASE to 'current'. Used by checkpkg to query the right branch
# in the buildfarm pkgdb. For off-site usage this can default to unstable.
HOSTNAME := $(shell hostname)
CATALOG_RELEASE ?= $(shell echo $(HOSTNAME) | gsed -re 's/[0-9]{1,2}[sx]$$//')
ifeq ($(HOSTNAME),$(CATALOG_RELEASE))
CATALOG_RELEASE=unstable
endif

define obsoleted_pkg
# function 'catalogname' must not be used due to recursive calls to CATALOGNAME_*
CATALOGNAME_$(1) ?= $(subst -,_,$(patsubst CSW%,%,$(1)))_stub
# The length of the description has been limited to 100 characters,
# the string is cut (no longer on word boundaries).
SPKG_DESC_$(1) ?= $(shell echo Transitional package. Content moved to $(foreach P,$(OBSOLETING_PKGS),$(if $(filter $(1),$(OBSOLETED_BY_$P)),$P)) | perl -npe 's/(.{100}).+/substr($$1,0,96) . " ..."/e')
RUNTIME_DEP_PKGS_$(1) = $(foreach P,$(OBSOLETING_PKGS),$(if $(filter $(1),$(OBSOLETED_BY_$P)),$P))
PKGFILES_$(1) = NOFILES
ARCHALL_$(1) = 1
# For legacy packages we know that the dependency is correct because we deliberately set it
# A legacy dependency from another package may not have been released
# The catalog name may not match for legacy packages
# The overridden package may be a devel package, as it is empty it is ok to be archall
$(foreach P,$(OBSOLETING_PKGS),$(if $(filter $(1),$(OBSOLETED_BY_$P)),
CHECKPKG_OVERRIDES_$(1) += surplus-dependency|$P
$(if $(filter $P,$(FOREIGN_PACKAGES)),CHECKPKG_OVERRIDES_$(1) += unidentified-dependency|$P)
))
CHECKPKG_OVERRIDES_$(1) += catalogname-does-not-match-pkgname
CHECKPKG_OVERRIDES_$(1) += archall-devel-package
endef

$(foreach P,$(OBSOLETED_PKGS),$(eval $(call obsoleted_pkg,$P)))

_PKG_SPECS      = $(filter-out $(NOPACKAGE),$(SPKG_SPECS))
$(if $(_PKG_SPECS),,$(error No packages for building defined))

# The is the name of the package containing the sourcefiles for all packages generated from this GAR recipe.
# It defaults to the first defined package name or gspec. SRCPACKAGE_BASE is guaranteed
# to be one of the real packages built.
SRCPACKAGE_BASE = $(if $(PACKAGES),$(firstword $(PACKAGES)),$(firstword $(SPKG_SPECS)))

SRCPACKAGE                  ?= $(SRCPACKAGE_BASE)-src
CATALOGNAME_$(SRCPACKAGE)   ?= $(patsubst CSW%,%,$(SRCPACKAGE_BASE))_src
SPKG_DESC_$(SRCPACKAGE)     ?= $(SPKG_DESC_$(SRCPACKAGE_BASE)) Source Package
ARCHALL_$(SRCPACKAGE)       ?= 1
GARSYSTEMVERSION ?= $(shell $(SVN) propget svn:externals $(CURDIR) | perl -ane 'if($$F[0] eq "gar") { print ($$F[1]=~m(https://gar.svn.sourceforge.net/svnroot/gar/csw/mgar/gar/(.*))),"\n";}')
GARPKG_v1 = CSWgar-v1
GARPKG_v2 = CSWgar-v2
RUNTIME_DEP_PKGS_$(SRCPACKAGE) ?= $(or $(GARPKG_$(GARSYSTEMVERSION)),$(error GAR version $(GARSYSTEMVERSION) unknown))

# Sanity checks for r8335
$(if $(NO_ISAEXEC),$(error The deprecated variable 'NO_ISAEXEC' is defined, this is now the default, please remove the line))
$(if $(NOISAEXEC),$(error The deprecated variable 'NOISAEXEC' is defined, this is now the default, please remove the line))
$(if $(PREREQUISITE_PKGS),$(error The deprecated variable 'PREREQUISITE_PKGS' is defined, please replace it with BUILD_DEP_PKGS))
$(foreach P,$(SPKG_SPECS),$(if $(PREREQUISITE_PKGS_$P),$(error The deprecated variable 'PREREQUISITE_PKGS_$P' is defined, please replace it with BUILD_DEP_PKGS_$P)))
$(if $(REQUIRED_PKGS),$(error The deprecated variable 'REQUIRED_PKGS' is defined, please replace it with RUNTIME_DEP_PKGS))
$(foreach P,$(SPKG_SPECS),$(if $(REQUIRED_PKGS_$P),$(error The deprecated variable 'REQUIRED_PACKAGES_$P' is defined, please replace it with RUNTIME_DEP_PKGS_$P)))

BUNDLE ?= $(NAME)

# pkgname - Get the name of a package from a gspec-name or package-name
#
# This is a safety function. In sane settings it should return the name
# of the package given as argument. However, when gspec-files are in DISTFILES
# it is possible to name the gspec-file differently from the package. This is
# a very bad idea, but we can handle it!
#
# In: arg1 - name of gspec-file or package
# Out: name of package
#
define pkgname
$(strip 
  $(if $(filter $(1),$(PACKAGES)),
    $(1),
    $(shell perl -F'\s+' -ane 'print "$$F[2]" if( $$F[0] eq "%var" && $$F[1] eq "pkgname")' files/$(1).gspec)
  )
)
endef

# catalogname - Get the catalog-name for a package
#
# In: arg1 - name of package
# Out: catalog-name for the package
#
define catalogname
$(strip 
  $(if $(CATALOGNAME_$(1)),
    $(CATALOGNAME_$(1)),
    $(if $(CATALOGNAME),
      $(CATALOGNAME),
      $(if $(filter $(1),$(PACKAGES) $(OBSOLETED_PKGS)),
        $(subst -,_,$(patsubst CSW%,%,$(1))),
        $(if $(realpath files/$(1).gspec),
          $(shell perl -F'\s+' -ane 'print "$$F[2]" if( $$F[0] eq "%var" && $$F[1] eq "bitname")' files/$(1).gspec),
          $(error The catalog name for the package '$1' could not be determined, because it was neither in PACKAGES nor was there a gspec-file)
        )
      )
    )
  )
)
endef

# We do not put this in $(docdir), as the prefix may have been reset to some
# other location and the license should always be in a fixed location.
define licensedir
$(BUILD_PREFIX)/share/doc/$(call catalogname,$(1))
endef

# Set this to your svn binary
SVN  ?= /opt/csw/bin/svn
GAWK ?= /opt/csw/bin/gawk

# We have to deal with four cases here:
# 1. There is no svn binary -> NOSVN
# 2. There is a svn binary, but the directory does not belong to a repository -> NOTVERSIONED
# 3. There is a svn binary, but not everything was committed properly -> UNCOMMITTED
# 4. There is a svn binary and everything was committed -> r<revision>

ifndef SPKG_PACKAGER
  $(warning Please set SPKG_PACKAGER in your .garrc file to your name)
  SPKG_PACKAGER = Unknown
endif

ifndef SPKG_EMAIL
  $(warning Please set SPKG_EMAIL in your .garrc file to your email address)
  SPKG_EMAIL = Unknown
endif

define ALLVERSIONFLAGS
$(if $(VERSION_FLAG_PATCH),p)
endef

ifneq ($(call ALLVERSIONFLAGS),)
SPKG_VERSION_FLAGS ?= ,$(call ALLVERSIONFLAGS)
endif

SPKG_DESC      ?= $(DESCRIPTION)
SPKG_VERSION   ?= $(subst -,_,$(VERSION)$(SPKG_VERSION_FLAGS))
SPKG_CATEGORY  ?= application
SPKG_SOURCEURL ?= $(firstword $(VENDOR_URL) \
			$(if $(filter $(GNU_MIRROR),$(MASTER_SITES)),http://www.gnu.org/software/$(GNU_PROJ)) \
			$(MASTER_SITES) \
			$(GIT_REPOS))
SPKG_VENDOR    ?= $(SPKG_SOURCEURL) packaged for CSW by $(SPKG_PACKAGER)
SPKG_PSTAMP    ?= $(LOGNAME)@$(shell hostname)-$(call _REVISION)-$(shell date '+%Y%m%d%H%M%S')
SPKG_BASEDIR   ?= $(prefix)
SPKG_CLASSES   ?= none
SPKG_OSNAME    := $(if $(SPKG_OSNAME),$(SPKG_OSNAME),$(shell /usr/bin/uname -s)$(shell /usr/bin/uname -r))

SPKG_SPOOLROOT ?= $(DESTROOT)
SPKG_SPOOLDIR  ?= $(SPKG_SPOOLROOT)/spool.$(GAROSREL)-$(GARCH)
SPKG_EXPORT    ?= $(HOME)/staging/build-$(shell date '+%d.%b.%Y')
SPKG_PKGROOT   ?= $(PKGROOT)
SPKG_PKGBASE   ?= $(PKGROOT)
SPKG_WORKDIR   ?= $(CURDIR)/$(WORKDIR)
SPKG_TMPDIR    ?= /tmp

SPKG_DEPEND_DB  = $(GARDIR)/csw/depend.db

SPKG_PKGFILE ?= %{bitname}-%{SPKG_VERSION},%{SPKG_REVSTAMP}-%{SPKG_OSNAME}-%{arch}-$(or $(filter $(call _REVISION),UNCOMMITTED NOTVERSIONED NOSVN),CSW).pkg

MIGRATECONF ?= $(strip $(foreach S,$(SPKG_SPECS),$(if $(or $(MIGRATE_FILES_$S),$(MIGRATE_FILES)),/etc/opt/csw/pkg/$S/cswmigrateconf)))

# It is NOT sufficient to change the pathes here, they must be adjusted in merge-* also
_USERGROUP_FILES ?= $(strip $(foreach S,$(SPKG_SPECS),$(if $(value $(S)_usergroup),/etc/opt/csw/pkg/$S/cswusergroup)))
_INETDCONF_FILES ?= $(strip $(foreach S,$(SPKG_SPECS),$(if $(value $(S)_inetdconf),/etc/opt/csw/pkg/$S/inetd.conf)))
_ETCSERVICES_FILES ?= $(strip $(foreach S,$(SPKG_SPECS),$(if $(value $(S)_etcservices),/etc/opt/csw/pkg/$S/services)))

USERGROUP += $(_USERGROUP_FILES)
INETDCONF += $(_INETDCONF_FILES)
ETCSERVICES += $(_ETCSERVICES_FILES)

# This is the default path for texinfo pages to be picked up. Extend or replace as necessary.
TEXINFO ?= $(infodir)/.*\.info(?:-\d+)? $(EXTRA_TEXINFO)

# if AP2_MODS is set, files matching this shell glob (passed to find)
# will have 'build' set as their class
AP2_MODFILES ?= opt/csw/apache2/libexec/*so $(EXTRA_AP2_MODFILES)
PHP5_EXTFILES ?= *so $(EXTRA_PHP5_EXTFILES)

# - set class for all config files
_CSWCLASS_FILTER = | perl -ane '\
		$(foreach FILE,$(MIGRATECONF),$$F[1] = "cswmigrateconf" if( $$F[2] =~ m(^$(FILE)$$) );)\
		$(foreach FILE,$(SAMPLECONF:%\.CSW=%),$$F[1] = "cswcpsampleconf" if ( $$F[2] =~ m(^$(FILE)\.CSW$$) );)\
		$(foreach FILE,$(PRESERVECONF:%\.CSW=%),$$F[1] = "cswpreserveconf" if( $$F[2] =~ m(^$(FILE)\.CSW$$) );)\
		$(foreach FILE,$(ETCSERVICES),$$F[1] = "cswetcservices" if( $$F[2] =~ m(^$(FILE)$$) );)\
		$(foreach FILE,$(INETDCONF),$$F[1] = "cswinetd" if( $$F[2] =~ m(^$(FILE)$$) );)\
		$(foreach FILE,$(INITSMF),$$F[1] = "cswinitsmf" if( $$F[2] =~ m(^$(FILE)$$) );)\
		$(foreach FILE,$(ETCSHELLS),$$F[1] = "cswetcshells" if( $$F[2] =~ m(^$(FILE)$$) );)\
		$(foreach FILE,$(USERGROUP),$$F[1] = "cswusergroup" if( $$F[2] =~ m(^$(FILE)$$) );)\
		$(foreach FILE,$(CRONTABS),$$F[1] = "cswcrontab" if( $$F[2] =~ m(^$(FILE)$$) );)\
		$(if $(PYCOMPILE),$(foreach FILE,$(_PYCOMPILE_FILES),$$F[1] = "cswpycompile" if( $$F[2] =~ m(^$(FILE)$$) );))\
		$(foreach FILE,$(TEXINFO),$$F[1] = "cswtexinfo" if( $$F[2] =~ m(^$(FILE)$$) );)\
		$(if $(AP2_MODS),@F = ("e", "build", $$F[2], "?", "?", "?") if ($$F[2] =~ m(^/opt/csw/apache2/ap2mod/.*));) \
		$(if $(PHP5_EXT),@F = ("e", "build", $$F[2], "?", "?", "?") if ($$F[2] =~ m(^/opt/csw/php5/extensions/.*));) \
		$$F[1] = "cswcptemplates" if( $$F[2] =~ m(^/opt/csw/etc/templates/.+$$) and $$F[0] eq "f" ); \
		print join(" ",@F),"\n";'

# If you add another filter above, also add the class to this list. It is used
# to detect if a package needs to depends on CSWcswclassutils by looking at
# files belonging to one of these in the prototype.

# NOTE: Order _can_  be important here.  cswinitsmf and cswinetd should
#	always be the last two added.  The reason for this is that
#	you need to ensure any binaries and config files are already on disk
#	and able to be consumed by a service that might be started.

# NOTE: cswusergroup and ugfiles were moved to have higher priority
# than the conf handling classes.  this allows one to manually set the
# user/group on conf files with prototype modifiers while still
# leveraging the conf handler classes.  this is a priority issue as
# per the above note.  (See bacula for an example of where this is
# required.)

_CSWCLASSES  = cswusergroup ugfiles
_CSWCLASSES += cswmigrateconf cswcpsampleconf cswpreserveconf cswcptemplates
_CSWCLASSES += cswetcservices
_CSWCLASSES += cswetcshells
_CSWCLASSES += cswcrontab
_CSWCLASSES += cswpycompile
_CSWCLASSES += cswinetd
_CSWCLASSES += cswinitsmf
_CSWCLASSES += cswtexinfo
_CSWCLASSES += cswpostmsg

# Make sure the configuration files always have a .CSW suffix and rename the
# configuration files to this if necessary during merge.
_EXTRA_PAX_ARGS += $(foreach FILE,$(SAMPLECONF:%\.CSW=%) $(PRESERVECONF:%\.CSW=%),-s ",^\.\($(FILE)\)$$,.\1\.CSW,p")

PKGGET_DESTDIR ?=

DEPMAKER_EXTRA_ARGS = --noscript --nodep SUNW

# Construct a revision stamp
ifeq ($(GARFLAVOR),DBG)
SPKG_FULL_REVSTAMP=1
endif

ifeq ($(SPKG_FULL_REVSTAMP),1)
$(call SETONCE,SPKG_REVSTAMP,REV=$(shell date '+%Y.%m.%d.%H.%M'))
else
$(call SETONCE,SPKG_REVSTAMP,REV=$(shell date '+%Y.%m.%d'))
endif

# Where we find our mkpackage global templates
PKGLIB = $(GARDIR)/pkglib

PKG_EXPORTS  = NAME VERSION DESCRIPTION CATEGORIES GARCH GARDIR GARBIN
PKG_EXPORTS += CURDIR WORKDIR WORKDIR_FIRSTMOD WORKSRC WORKSRC_FIRSTMOD PKGROOT
PKG_EXPORTS += SPKG_REVSTAMP SPKG_PKGNAME SPKG_DESC SPKG_VERSION SPKG_CATEGORY
PKG_EXPORTS += SPKG_VENDOR SPKG_EMAIL SPKG_PSTAMP SPKG_BASEDIR SPKG_CLASSES
PKG_EXPORTS += SPKG_OSNAME SPKG_SOURCEURL SPKG_PACKAGER SPKG_PKGFILE TIMESTAMP
PKG_EXPORTS += DEPMAKER_EXTRA_ARGS PKGLIB DESTDIR

define _PKG_ENV
$(BUILD_ENV) $(foreach EXP,$(PKG_EXPORTS),$(EXP)="$(if $($(EXP)_$1),$($(EXP)_$1),$($(EXP)))")
endef

# Canned command for generating admin file names
# Usage: $(call admfiles,SUNWpackage,depend copyright)
# pkg.gspec is added by default.
admfiles = $(1).gspec $(foreach PKG,$(1),$(foreach ADM,$(2),$(PKG).$(ADM)))

# Standard sets of admin files for use with admfiles
ADMSTANDARD = prototype depend
ADMISCRIPTS = preinstall postinstall
ADMUSCRIPTS = preremove postremove
ADMSCRIPTS  = $(ADMISCRIPTS) $(ADMUSCRIPTS)
ADMFULLSTD  = $(ADMSTANDARD) $(ADMSCRIPTS) space
ADMADDON    = $(ADMSTANDARD) postinstall preremove

# This is a helper function which inserts subdirectories for each ISA
# between the prefix and the suffix.
# usage: $(call isadirs,<prefix>,<suffix>)
# expands to <prefix>/<isa1>/<suffix> <prefix>/<isa2>/<suffix> ...
isadirs = $(foreach ISA,$(ISALIST),$(1)/$(subst +,\+,$(subst -,\-,$(ISA)))/$(2))

# This is a helper function just like isadirs, but also contains the
# prefix and suffix without an ISA subdirectories inserted.
# usage: $(call isadirs,<prefix>,<suffix>)
# expands to <prefix>/<suffix> <prefix>/<isa1>/<suffix> <prefix>/<isa2>/<suffix> ...
baseisadirs = $(1)/$(2) $(call isadirs,$(1),$(2))

# PKGFILES_RT selects files belonging to a runtime package
PKGFILES_RT += $(call baseisadirs,$(libdir),[^/]*\.so\.\d+(\.\d+)*)

# PKGFILES_LIB selects just one library. The '.' will be escaped automatically!
# Use PKGFILES_CSWlibfoo1 = $(call pkgfiles_lib,libfoo.so.1)
pkgfiles_lib += $(call baseisadirs,$(libdir),$(subst .,\.,$(subst +,\+,$(1)))(\.\d+)*)

# PKGFILES_DEVEL selects files belonging to a developer package
PKGFILES_DEVEL_CONFIG ?= $(call baseisadirs,$(bindir),[^/]*-config)
PKGFILES_DEVEL += $(PKGFILES_DEVEL_CONFIG)
PKGFILES_DEVEL_SHAREDLIBLINK ?= $(call baseisadirs,$(libdir),[^/]*\.so)
PKGFILES_DEVEL += $(PKGFILES_DEVEL_SHAREDLIBLINK)
PKGFILES_DEVEL_STATICLIB ?= $(call baseisadirs,$(libdir),[^/]*\.a)
PKGFILES_DEVEL += $(PKGFILES_DEVEL_STATICLIB)
PKGFILES_DEVEL_LIBTOOL ?= $(call baseisadirs,$(libdir),[^/]*\.la)
PKGFILES_DEVEL += $(PKGFILES_DEVEL_LIBTOOL)
PKGFILES_DEVEL_PKGCONFIG ?= $(call baseisadirs,$(libdir),pkgconfig(/.*)?)
PKGFILES_DEVEL += $(PKGFILES_DEVEL_PKGCONFIG)
PKGFILES_DEVEL_INCLUDEDIR ?= $(includedir)/.*
PKGFILES_DEVEL += $(PKGFILES_DEVEL_INCLUDEDIR)
PKGFILES_DEVEL_ACLOCAL ?= $(sharedstatedir)/aclocal/.*
PKGFILES_DEVEL += $(PKGFILES_DEVEL_ACLOCAL)
PKGFILES_DEVEL_CONFIG_MANPAGE ?= $(mandir)/man1/.*-config\.1.*
PKGFILES_DEVEL += $(PKGFILES_DEVEL_CONFIG_MANPAGE)
PKGFILES_DEVEL_MAN3_MANPAGE ?= $(mandir)/man3/.*\.3.*
PKGFILES_DEVEL += $(PKGFILES_DEVEL_MAN3_MANPAGE)

# PKGFILES_DOC selects files beloging to a documentation package
PKGFILES_DOC  = $(docdir)/.*

# PKGFILES_SRC selects the source archives for building the package
PKGFILES_SRC = $(sourcedir)/$(call catalogname,$(SRCPACKAGE_BASE))/.*

PKGFILES_$(SRCPACKAGE) ?= $(PKGFILES_SRC)

# This function computes the files to be excluded from the package specified
# as argument
define _pkgfiles_exclude
$(strip 
  $(foreach S,$(filter-out $(1),$(_PKG_SPECS)), 
    $(PKGFILES_$(S)) 
  ) 
)
endef

define _pkgfiles_include
$(strip 
  $(PKGFILES_$(1)_SHARED) 
  $(PKGFILES_$(1)) 
)
endef

# This function takes a full path to a filename and returns the package it belongs to.
# The package may be generated during this build or already installed on the system.
# /etc/crypto/certs/SUNWObjectCA=../../../etc/certs/SUNWObjectCA l none SUNWcsr
#perl -ane '$$f=quotemeta("$1");if($$F[0]=~/^$$f(=.*)?$$/){print join(" ",$$F[3..$$#F]),"\n";exit}'</var/sadm/install/contents
#$(shell /usr/sbin/pkgchk -l -p $1 2>/dev/null | $(GAWK) '/^Current/ {p=0} p==1 {print} /^Referenced/ {p=1}' | perl -ane 'print join("\n",@F)')
# 'pkchk -l -p' doesn't work as it concatenates package names with more than 14 characters,
# e. g. SUNWgnome-base-libs-develSUNWgnome-calculatorSUNWgnome-freedb-libsSUNWgnome-cd-burnerSUNWgnome-character-map
define file2pkg
$(shell perl -ane '@l{"s","l","d","b","c","f","x","v","e"}=(3,3,6,8,8,9,6,9,9);$$f=quotemeta("$1");if($$F[0]=~/^$$f(=.*)?$$/){s/^\*// foreach @F;print join(" ",@F[$$l{$$F[1]}..$$#F]),"\n";exit}'</var/sadm/install/contents)
endef

define linktargets
$(shell perl -ane 'if($$F[0] eq "l" && $$F[2]=~/=(.*)$$/){print $$1,"\n"}'<$1)
endef

_test-file2pkg:
	@echo $(call file2pkg,/etc)

_test-linktargets:
	@echo $(call linktargets,work/build-global/CSWlinkbase.prototype)

#
# Targets
#

# prototype - Generate prototype for all installed files
# This can be used to automatically distribute the files to different packages
#

$(foreach SPEC,$(_PKG_SPECS),$(if $(PROTOTYPE_FILTER_$(SPEC)),$(eval _PROTOTYPE_FILTER_$(SPEC) ?= | $(PROTOTYPE_FILTER_$(SPEC)))))
$(foreach SPEC,$(_PKG_SPECS),$(if $(PROTOTYPE_FILTER),$(eval _PROTOTYPE_FILTER_$(SPEC) ?= | $(PROTOTYPE_FILTER))))

# Assemble prototype modifiers
# PROTOTYPE_MODIFIERS = mytweaks
# PROTOTYPE_FTYPE_mytweaks = e
# PROTOTYPE_CLASS_mytweaks = cswconffile
# PROTOTYPE_FILES_mytweaks = $(bindir)/.*\.conf
# PROTOTYPE_PERMS_mytweaks = 0644
# PROTOTYPE_USER_mytweaks = somebody
# PROTOTYPE_GROUP_mytweaks = somegroup

_PROTOTYPE_MODIFIERS = | perl -ane '\
		$(foreach M,$(PROTOTYPE_MODIFIERS),\
			$(if $(PROTOTYPE_FILES_$M),if( $$F[2] =~ m(^$(firstword $(PROTOTYPE_FILES_$M))$(foreach F,$(wordlist 2,$(words $(PROTOTYPE_FILES_$M)),$(PROTOTYPE_FILES_$M)),|$F)$$) ) {)\
				$(if $(PROTOTYPE_FTYPE_$M),$$F[0] = "$(PROTOTYPE_FTYPE_$M)";)\
				$(if $(PROTOTYPE_CLASS_$M),$$F[1] = "$(PROTOTYPE_CLASS_$M)";)\
				$(if $(PROTOTYPE_PERMS_$M),$$F[3] = "$(PROTOTYPE_PERMS_$M)";)\
				$(if $(PROTOTYPE_USER_$M),$$F[4] = "$(PROTOTYPE_USER_$M)";)\
				$(if $(PROTOTYPE_GROUP_$M),$$F[5] = "$(PROTOTYPE_GROUP_$M)";)\
			$(if $(PROTOTYPE_FILES_$M),})\
		)\
		$(foreach F,$(POSTMSG),$$F[1] = "cswpostmsg" if( $$F[2] eq "$F" );)\
		$$F[1] = "cswalternatives" if( $$F[2] =~ m,^/opt/csw/share/alternatives/[^/]+$$, );\
                print join(" ",@F),"\n";'

define checkpkg_override_filter
  | ( cat; if test -f "$(WORKDIR_GLOBAL)/checkpkg_override.$(1)";then echo "i checkpkg_override=checkpkg_override.$(1)"; fi)
endef

define cswreleasenotes_filter
  | ( cat; if test -f "$(WORKDIR_GLOBAL)/$(1).cswreleasenotes";then echo "i cswreleasenotes=$(1).cswreleasenotes"; fi)
endef

define obsoleted_filter
  | ( cat; if test -f "$(WORKDIR_GLOBAL)/$(1).obsolete";then echo "i obsolete=$(1).obsolete"; fi)
endef

# This file contains all installed pathes. This can be used as a starting point
# for distributing files to individual packages.
PROTOTYPE = $(WORKDIR)/prototype

define dontrelocate
	$(shell gsed -i -e 's,\(.\) .* \($(1)[\s/]*\),\1 norelocate /\2,g' $(2))
endef

# Dynamic prototypes work like this:
# - A prototype from DISTFILES takes precedence over 

# Pulled in from pkglib/csw_prototype.gspec
$(PROTOTYPE): $(WORKDIR) merge
	$(_DBG)cswproto -c $(GARDIR)/etc/commondirs-$(GARCH) -r $(PKGROOT) $(PKGROOT)=$(if $(ALLOW_RELOCATE),,'/') >$@ 

# pathfilter lives in bin/pathfilter and takes care of including/excluding paths from
# a prototype (see "perldoc bin/pathfilter"). We employ it here to:
# - include license for current package
# - exclude licenses for all other packages
# - if other includes are given, only include these files
# - if no include is given ("catch all packages") include everything except what
#   is put in other packages
.PRECIOUS: $(WORKDIR)/%.prototype $(WORKDIR)/%.prototype-$(GARCH)
$(WORKDIR)/%.prototype: _PKGFILES_EXCLUDE=$(call _pkgfiles_exclude,$*)
$(WORKDIR)/%.prototype: _PKGFILES_INCLUDE=$(call _pkgfiles_include,$*)
$(WORKDIR)/%.prototype: | $(PROTOTYPE)
	$(_DBG)if [ -n "$(PKGFILES_$*_SHARED)" -o \
	      -n "$(PKGFILES_$*)" -o \
	      -n "$(_PKGFILES_EXCLUDE)" -o \
	      -n "$(ISAEXEC_FILES_$*)" -o \
	      -n "$(ISAEXEC_FILES)" ]; then \
	  (pathfilter $(if $(or $(_PKGFILES_EXCLUDE),$(_PKGFILES_INCLUDE)),\
				-I $(call licensedir,$*)/license \
				-I /etc/opt/csw/pkg/$*/cswmigrateconf \
		      		-I /opt/csw/share/alternatives/$(call catalogname,$*) \
		      )\
		      $(foreach S,$(filter-out $*,$(SPKG_SPECS)),\
				-X $(call licensedir,$S)/license \
				-X /etc/opt/csw/pkg/$S/cswmigrateconf \
				-X /opt/csw/share/alternatives/$(call catalogname,$S) \
		      ) \
		      $(foreach I,$(EXTRA_PKGFILES_INCLUDED) $(EXTRA_PKGFILES_INCLUDED_$*),-i '$I') \
		      $(foreach X,$(EXTRA_PKGFILES_EXCLUDED) $(EXTRA_PKGFILES_EXCLUDED_$*),-x '$X') \
		      $(foreach FILE,$(_PKGFILES_INCLUDE),-i '$(FILE)') \
		      $(if $(_PKGFILES_INCLUDE),-x '.*',$(foreach FILE,$(_PKGFILES_EXCLUDE),-x '$(FILE)')) \
	              $(foreach IE,$(abspath $(ISAEXEC_FILES_$*) $(ISAEXEC_FILES)), \
	                  -e '$(IE)=$(dir $(IE))$(ISA_DEFAULT)/$(notdir $(IE))' \
	               ) \
	              <$(PROTOTYPE); \
	   if [ -n "$(EXTRA_PKGFILES_$*)" ]; then echo "$(EXTRA_PKGFILES_$*)"; fi \
	  ) $(call checkpkg_override_filter,$*) $(call cswreleasenotes_filter,$*) $(call obsoleted_filter,$*) $(_CSWCLASS_FILTER) $(_CATEGORY_FILTER) $(_PROTOTYPE_MODIFIERS) $(_PROTOTYPE_FILTER_$*) >$@; \
	else \
	  cat $(PROTOTYPE) $(call checkpkg_override_filter,$*) $(call cswreleasenotes_filter,$*) $(call obsoleted_filter,$*) $(_CSWCLASS_FILTER) $(_CATEGORY_FILTER) $(_PROTOTYPE_MODIFIERS) $(_PROTOTYPE_FILTER_$*) >$@; \
	fi
	$(if $(ALLOW_RELOCATE),$(call dontrelocate,opt,$(PROTOTYPE)))

$(WORKDIR)/%.prototype-$(GARCH): | $(WORKDIR)/%.prototype
	$(_DBG)cat $(WORKDIR)/$*.prototype >$@

# Dynamic depends are constructed as follows:
# - Packages the currently constructed one depends on can be specified with
#   RUNTIME_DEP_PKGS_<pkg> specifically, or RUNTIME_DEP_PKGS for all packages build.
#   These are flagged as 'P' in the depend file.
# - If multiple packages are build at the same time it is valid to have
#   dependencies between them. In this case it is necessary to define the package
#   desciption for each package with SPKG_DESC_<pkg>, setting it in the gspec-file
#   does not work.
# - Packages that are imcompatible to the currently constructed one can be specified
#   with INCOMPATIBLE_PKGS_<pkg> specifically or with INCOMPATIBLE_PKGS for all
#   packages build.
# - A depend-file from DISTFILES takes precedence, it is not overwritten or
#   appended with dynamic depends.

# $_EXTRA_GAR_PKGS is for dynamic dependencies added by GAR itself (like CSWisaexec or CSWcswclassutils)
.PRECIOUS: $(WORKDIR)/%.depend

# The texinfo filter has been taken out of the normal filters as TEXINFO has a default.
# The dependencies to CSWcswclassutils and CSWtexinfo are only added if there are files
# actually matching the _TEXINFO_FILTER. This is done at the prototype-level.
$(WORKDIR)/%.depend: $(WORKDIR)/$*.prototype
$(WORKDIR)/%.depend: _EXTRA_GAR_PKGS += $(_CATEGORY_RUNTIME_DEP_PKGS)
$(WORKDIR)/%.depend: _EXTRA_GAR_PKGS += $(if $(strip $(shell cat $(WORKDIR)/$*.prototype | perl -ane '$(foreach I,$(ISAEXEC_FILES),print "yes" if( $$F[2] =~ m(^\Q$I\E(=.*)?$$));)')),CSWisaexec)
$(WORKDIR)/%.depend: _EXTRA_GAR_PKGS += $(if $(strip $(shell cat $(WORKDIR)/$*.prototype | perl -ane 'print "yes" if( $$F[1] eq "cswalternatives")')),CSWalternatives)
$(WORKDIR)/%.depend: _EXTRA_GAR_PKGS += $(foreach P,$(strip $(shell cat $(WORKDIR)/$*.prototype | perl -ane '$(foreach C,$(filter-out ugfiles,$(_CSWCLASSES)),print "$C " if( $$F[1] eq "$C");)')),CSWcas-$(subst csw,,$(P)))
$(WORKDIR)/%.depend: _DEP_PKGS=$(or $(RUNTIME_DEP_PKGS_ONLY_$*),$(RUNTIME_DEP_PKGS_ONLY),$(sort $(_EXTRA_GAR_PKGS)) $(or $(RUNTIME_DEP_PKGS_$*),$(RUNTIME_DEP_PKGS),$(DEP_PKGS_$*),$(DEP_PKGS)))
$(WORKDIR)/%.depend: $(WORKDIR)
# The final "true" is for packages without dependencies to make the shell happy as "( )" is not allowed.
$(WORKDIR)/%.depend:
	$(_DBG)$(if $(_DEP_PKGS)$(INCOMPATIBLE_PKGS)$(INCOMPATIBLE_PKGS_$*), \
		($(foreach PKG,$(INCOMPATIBLE_PKGS_$*) $(INCOMPATIBLE_PKGS),\
			echo "I $(PKG)";\
		)\
		$(foreach PKG,$(_DEP_PKGS),\
			$(if $(SPKG_DESC_$(PKG)), \
				echo "P $(PKG) $(call catalogname,$(PKG)) - $(SPKG_DESC_$(PKG))";, \
				echo "$(shell (/usr/bin/pkginfo $(PKG) || echo "P $(PKG) - ") | $(GAWK) '{ $$1 = "P"; print } ')"; \
			) \
		) \
		true) >$@)

# Dynamic gspec-files are constructed as follows:
# - Packages using dynamic gspec-files must be listed in PACKAGES
# - There is a default of PACKAGES containing one packages named CSW
#   followed by the NAME. It can be changed by setting PACKAGES explicitly.
# - The name of the generated package is always the same as listed in PACKAGES
# - The catalog name defaults to the suffix following CSW of the package name,
#   but can be customized by setting CATALOGNAME_<pkg> = <catalogname-of-pkg>
# - If only one package is build it is sufficient to set CATALOGNAME = <catalogname-of-pkg>
#   It is an error to set CATALOGNAME if more than one package is build.
# - If the package is suitable for all architectures (sparc and x86) this can be
#   flagged with ARCHALL_<pkg> = 1 for a specific package or with ARCHALL = 1
#   for all packages.

_CATEGORY_GSPEC_INCLUDE ?= csw_dyngspec.gspec

# This rule dynamically generates gspec-files
.PRECIOUS: $(WORKDIR)/%.gspec
$(WORKDIR)/%.gspec:
	$(_DBG)$(if $(filter $*.gspec,$(DISTFILES)),,\
		(echo "%var            bitname $(call catalogname,$*)"; \
		echo "%var            pkgname $*"; \
		$(if $(or $(ARCHALL),$(ARCHALL_$*)),echo "%var            arch all";) \
		$(if $(_CATEGORY_GSPEC_INCLUDE),echo "%include        url file://%{PKGLIB}/$(_CATEGORY_GSPEC_INCLUDE)")) >$@\
	)


# Dynamic licenses are selected in the following way:
# - Dynamic licenses are only activated for packages listed in PACKAGES or
#   packages which don't have %copyright in their gspec-file. This way the
#   behaviour on existing gspec-files is preserved.
# - The default name for the license is COPYING and it will not be fully printed
# - If no license is explicitly specified in the Makefile and the default can not
#   be found no license will be included
# - If a license is specified it must be found or an error is issued
# - Either LICENSE_<pkg> or LICENSE_FULL_<pkg> may be specified, it is an error
#   to specify both.
# - There is an automatic rule to include only the license for each package that
#   belongs to it.
# - Package-specific defines have precedence over general defines (CATALOGNAME_<pkg>
#   before CATALOGNAME etc.)

# LICENSE may be a path starting with $(WORKROOTDIR) or a filename inside $(WORKSRC)
ifeq ($(origin LICENSE_FULL), undefined)
ifeq ($(origin LICENSE), undefined)
LICENSE = COPYING
_LICENSE_IS_DEFAULT = 1
endif
endif

# Dynamic pkginfo 

# Calculating the revision can be time consuming, so we do this on demand
define _REVISION
$(if $(shell if test -x $(SVN); then echo yes; fi),$(if $(shell $(SVN) info >/dev/null 2>&1; if test $$? -eq 0; then echo YES; fi),$(if $(shell $(SVN) status --ignore-externals 2>/dev/null | grep -v '^X'),UNCOMMITTED,$(shell $(SVN) info --recursive 2>/dev/null | $(GAWK) '$$1 == "Revision:" && MAX < $$2 { MAX = $$2 } END {print MAX }')),NOTVERSIONED),NOSVN)
endef

# URL: https://gar.svn.sf.net/svnroot/gar/csw/mgar/pkg/pcre/trunk
define _URL
$(if $(shell if test -x $(SVN); then echo yes; fi),$(shell $(SVN) info . 2>/dev/null | $(GAWK) '$$1 == "URL:" { print $$2 }'))
endef

# XXX: It is possible that a package is flagged as /isaexec, even
# if the isaexec'ed files are in another package created from the Makefile.
# There should be a warning issued if there is more than one package build and
# it has not explicitly been set.
define mode64
$(shell echo 
  $(if $(MODE64_$(1)),$(MODE64_$(1)), 
    $(if $(filter 32,$(foreach I,$(NEEDED_ISAS),$(MEMORYMODEL_$I))),32) 
    $(if $(filter 64,$(foreach I,$(NEEDED_ISAS),$(MEMORYMODEL_$I))),64) 
    $(if $(abspath $(ISAEXEC_FILES_$*) $(ISAEXEC_FILES)),isaexec) 
  ) | perl -lne 'print join("/", split)'
)
endef

define pkgvar
$(strip $(or $(_CATEGORY_$(1)_$(2)),$(_CATEGORY_$(1)),$($(1)_$(2)),$($(1))))
endef

# Make sure every producable package contains specific descriptions.
# We explicitly ignore NOPACKAGE here to disallow circumventing the check.
$(if $(filter-out $(firstword $(SPKG_SPECS)),$(SPKG_SPECS)),\
	$(foreach P,$(SPKG_SPECS),\
		$(if $(SPKG_DESC_$(P)),,$(error Multiple packages defined and SPKG_DESC_$(P) is not set.))))

# There was a bug here.
# http://sourceforge.net/apps/trac/gar/ticket/56
# The workaround was to add an additional check whether the strings are the
# same or not.
$(foreach P,$(SPKG_SPECS),\
  $(foreach Q,$(filter-out $(P) $(OBSOLETED_PKGS),$(SPKG_SPECS)),\
	$(if $(filter-out $(subst  ,_,$(SPKG_DESC_$(P))),$(subst  ,_,$(SPKG_DESC_$(Q)))),\
	  ,\
	  $(if $(shell if [ "$(SPKG_DESC_$(P))" = "$(SPKG_DESC_$(Q))" ]; then echo bad; fi),\
	    $(error The package descriptions for $(P) [$(if $(SPKG_DESC_$(P)),$(SPKG_DESC_$(P)),<not set>)] and $(Q) [$(if $(SPKG_DESC_$(Q)),$(SPKG_DESC_$(Q)),<not set>)] are identical.  Please make sure that all descriptions are unique by setting SPKG_DESC_<pkg> for each package.),))))

.PRECIOUS: $(WORKDIR)/%.pkginfo

# The texinfo filter has been taken out of the normal filters as TEXINFO has a default.
$(WORKDIR)/%.pkginfo: $(WORKDIR)/%.prototype
$(WORKDIR)/%.pkginfo: SPKG_CLASSES += $(if $(strip $(shell cat $(WORKDIR)/$*.prototype | perl -ane 'print "yes" if( $$F[1] eq "cswalternatives")')),cswalternatives)
$(WORKDIR)/%.pkginfo: SPKG_CLASSES += $(if $(strip $(shell cat $(WORKDIR)/$*.prototype | perl -ane 'print "yes" if( $$F[1] eq "build")')),build)
$(WORKDIR)/%.pkginfo: SPKG_CLASSES += $(shell cat $(WORKDIR)/$*.prototype | perl -e 'while(<>){@F=split;$$c{$$F[1]}++};$(foreach C,$(_CSWCLASSES),print "$C\n" if( $$c{$C});)')

$(WORKDIR)/%.pkginfo: $(WORKDIR)
	$(_DBG)(echo "PKG=$*"; \
	echo "NAME=$(call catalogname,$*) - $(call pkgvar,SPKG_DESC,$*)"; \
	echo "ARCH=$(if $(or $(ARCHALL),$(ARCHALL_$*)),all,$(call pkgvar,GARCH,$*))"; \
	echo "VERSION=$(call pkgvar,SPKG_VERSION,$*),$(call pkgvar,SPKG_REVSTAMP,$*)"; \
	echo "CATEGORY=$(call pkgvar,SPKG_CATEGORY,$*)"; \
	echo "VENDOR=$(call pkgvar,SPKG_VENDOR,$*)"; \
	echo "EMAIL=$(call pkgvar,SPKG_EMAIL,$*)"; \
	echo "PSTAMP=$(LOGNAME)@$(shell hostname)-$(shell date '+%Y%m%d%H%M%S')"; \
	$(if $(ALLOW_RELOCATE),echo "CLASSES=$(call pkgvar,SPKG_CLASSES,$*) norelocate"; \
	,echo "CLASSES=$(call pkgvar,SPKG_CLASSES,$*)";) \
	echo "HOTLINE=http://www.opencsw.org/bugtrack/"; \
	echo "OPENCSW_CATALOGNAME=$(call catalogname,$*)"; \
	echo "OPENCSW_MODE64=$(call mode64,$*)"; \
	echo "OPENCSW_REPOSITORY=$(call _URL)@$(call _REVISION)"; \
	echo "OPENCSW_BUNDLE=$(BUNDLE)"; \
	echo "OPENCSW_OS_RELEASE=$(SPKG_OSNAME)"; \
	echo "OPENCSW_OS_ARCH=$(GARCH)"; \
	$(_CATEGORY_PKGINFO) \
	) >$@
	$(if $(ALLOW_RELOCATE),echo "BASEDIR=$(RELOCATE_PREFIX)" >>$@)


# findlicensefile - Find an existing file for a given license name
#
define findlicensefile
$(strip 
  $(if $(1),$(firstword $(realpath 
    $(1) $(WORKDIR)/$(1) 
    $(foreach M,global $(MODULATIONS),$(WORKROOTDIR)/build-$M/$(1) $(WORKROOTDIR)/build-$M/$(DISTNAME)/$(1)) 
  ))) 
)
endef

define licensefile
$(strip 
  $(or 
    $(call findlicensefile,$(or $(LICENSE_$(1)),$(LICENSE_FULL_$(1)))),
    $(call findlicensefile,$(or $(LICENSE),$(LICENSE_FULL))),
  ) 
)
endef

merge-license-%: $(WORKDIR)
	$(_DBG)$(if $(and $(LICENSE_$*),$(LICENSE_FULL_$*)),$(error Both LICENSE_$* and LICENSE_FULL_$* have been specified where only one is allowed)) \
		$(if $(and $(filter $*,$(_PKG_SPECS)),$(or $(LICENSE),$(LICENSE_FULL),$(LICENSE_$*),$(LICENSE_FULL_$*))), \
		LICENSEFILE=$(or $(call licensefile,$*),$(if $(_LICENSE_IS_DEFAULT),,$(error Cannot find license file for package $*))); \
		LICENSEDIR=$(call licensedir,$*); \
		if [ -n "$$LICENSEFILE" ]; then \
		$(if $(or $(LICENSE_FULL),$(LICENSE_FULL_$*)), \
		    if [ -f "$$LICENSEFILE" ]; then cp $$LICENSEFILE $(WORKDIR)/$*.copyright; fi;, \
		    echo "Please see $$LICENSEDIR/license for license information." > $(WORKDIR)/$*.copyright; \
		) \
		  umask 022 && mkdir -p $(PKGROOT)$$LICENSEDIR && \
		  rm -f $(PKGROOT)$$LICENSEDIR/license && \
		  cp $$LICENSEFILE $(PKGROOT)$$LICENSEDIR/license; \
		fi \
	)
	@$(MAKECOOKIE)

merge-license: $(foreach SPEC,$(_PKG_SPECS),merge-license-$(SPEC))
	@$(DONADA)

reset-merge-license:
	@rm -f $(COOKIEDIR)/merge-license $(foreach SPEC,$(_PKG_SPECS),$(COOKIEDIR)/merge-license-$(SPEC))

merge-distfile-%: $(DOWNLOADDIR)
	$(_DBG_MERGE)if test -f $(DOWNLOADDIR)/$*; then \
		$(foreach P,$(_PKG_SPECS),mkdir -p $(PKGROOT)$(docdir)/$(call catalogname,$P);) \
		$(foreach P,$(_PKG_SPECS),cp $(DOWNLOADDIR)/$* $(PKGROOT)$(docdir)/$(call catalogname,$P)/$*;) \
	fi
	@$(MAKECOOKIE)

.PHONY: reset-merge-distfile-%
reset-merge-distfile-%:
	$(_DBG_MERGE)rm -f $(COOKIEDIR)/merge-distfile-$* $(foreach SPEC,$(_PKG_SPECS),$(PKGROOT)$(docdir)/$(call catalogname,$(SPEC))/$*)

merge-obsolete: $(WORKDIR_GLOBAL)
	$(_DBG_MERGE)$(foreach P,$(OBSOLETED_PKGS),($(foreach Q,$(OBSOLETING_PKGS),$(if $(filter $P,$(OBSOLETED_BY_$Q)), \
		$(if $(filter $Q,$(FOREIGN_PACKAGES)), \
			echo "$Q";, \
			$(if $(SPKG_DESC_$Q), \
				echo "$Q $(call catalogname,$Q) - $(SPKG_DESC_$Q)";, \
				echo "$(shell (/usr/bin/pkginfo $Q || echo "$Q - ") | perl -npe 's/^\S*\s//;s/\s+/ /')"; \
		))))) > $(WORKDIR_GLOBAL)/$P.obsolete; \
	)
	@$(MAKECOOKIE)

.PHONY: reset-merge-obsolete
reset-merge-obsolete:
	$(_DBG)rm -f $(COOKIEDIR)/merge-obsolete $(WORKDIR_GLOBAL)/.*.obsolete

merge-classutils: merge-migrateconf merge-usergroup merge-inetdconf merge-etcservices

reset-merge-classutils: reset-merge-migrateconf reset-merge-usergroup reset-merge-inetdconf reset-merge-etcservices

reset-merge-ap2mod:
	@rm -f $(COOKIEDIR)/post-merge-ap2mod

reset-merge-php5ext:
	@rm -f $(COOKIEDIR)/post-merge-php5ext

merge-migrateconf: $(foreach S,$(SPKG_SPECS),$(if $(or $(MIGRATE_FILES_$S),$(MIGRATE_FILES)),merge-migrateconf-$S))
	@$(MAKECOOKIE)

merge-migrateconf-%:
	@echo "[ Generating cswmigrateconf for package $* ]"
	@echo "X: $(MIGRATE_FILES_$*) Y: $(MIGRATE_FILES)"
	$(_DBG)ginstall -d $(PKGROOT)/etc/opt/csw/pkg/$*
	$(_DBG)(echo "MIGRATE_FILES=\"$(or $(MIGRATE_FILES_$*),$(MIGRATE_FILES))\"";\
		 $(if $(or $(MIGRATE_SOURCE_DIR_$*),$(MIGRATE_SOURCE_DIR)),echo "SOURCE_DIR___default__=\"$(or $(MIGRATE_SOURCE_DIR_$*),$(MIGRATE_SOURCE_DIR))\"";)\
		 $(if $(or $(MIGRATE_DEST_DIR_$*),$(MIGRATE_DEST_DIR)),echo "DEST_DIR___default__=\"$(or $(MIGRATE_DEST_DIR_$*),$(MIGRATE_DEST_DIR))\"";)\
		 $(foreach F,$(or $(MIGRATE_FILES_$*),$(MIGRATE_FILES)),\
			$(if $(MIGRATE_SOURCE_DIR_$F),echo "SOURCE_DIR_$(subst .,_,$F)=\"$(MIGRATE_SOURCE_DIR_$F)\"";)\
			$(if $(MIGRATE_DEST_DIR_$F),echo "DEST_DIR_$(subst .,_,$F)=\"$(MIGRATE_DEST_DIR_$F)\"";)\
		)\
	) >$(PKGROOT)/etc/opt/csw/pkg/$*/cswmigrateconf
	@$(MAKECOOKIE)

reset-merge-migrateconf:
	@rm -f $(COOKIEDIR)/merge-migrateconf $(foreach SPEC,$(_PKG_SPECS),$(COOKIEDIR)/merge-migrateconf-$(SPEC))

_show_classutilvar//%:
	$($*)

merge-usergroup: $(foreach S,$(SPKG_SPECS),$(if $(value $(S)_usergroup),merge-usergroup-$S))
	@$(MAKECOOKIE)

merge-usergroup-%:
	@echo "[ Generating cswusergroup for package $* ]"
	$(_DBG)ginstall -d $(PKGROOT)/etc/opt/csw/pkg/$*
	$(_DBG)$(MAKE) --no-print-directory -n _show_classutilvar//$*_usergroup >$(PKGROOT)/etc/opt/csw/pkg/$*/cswusergroup
	@$(MAKECOOKIE)

reset-merge-usergroup:
	@rm -f $(COOKIEDIR)/merge-usergroup $(foreach SPEC,$(_PKG_SPECS),$(COOKIEDIR)/merge-usergroup-$(SPEC))

merge-inetdconf: $(foreach S,$(SPKG_SPECS),$(if $(value $(S)_inetdconf),merge-inetdconf-$S))

merge-inetdconf-%:
	@echo "[ Generating inetd.conf for package $* ]"
	$(_DBG)ginstall -d $(PKGROOT)/etc/opt/csw/pkg/$*
	$(_DBG)$(MAKE) --no-print-directory -n _show_classutilvar//$*_inetdconf >$(PKGROOT)/etc/opt/csw/pkg/$*/inetd.conf
	@$(MAKECOOKIE)

reset-merge-inetdconf:
	@rm -f $(COOKIEDIR)/merge-inetdconf $(foreach SPEC,$(_PKG_SPECS),$(COOKIEDIR)/merge-inetdconf-$(SPEC))

merge-etcservices: $(foreach S,$(SPKG_SPECS),$(if $(value $(S)_etcservices),merge-etcservices-$S))

merge-etcservices-%:
	@echo "[ Generating services for package $* ]"
	$(_DBG)ginstall -d $(PKGROOT)/etc/opt/csw/pkg/$*
	$(_DBG)$(MAKE) --no-print-directory -n _show_classutilvar//$*_etcservices >$(PKGROOT)/etc/opt/csw/pkg/$*/services
	@$(MAKECOOKIE)

reset-merge-etcservices:
	@rm -f $(COOKIEDIR)/merge-etcservices $(foreach SPEC,$(_PKG_SPECS),$(COOKIEDIR)/merge-etcservices-$(SPEC))

merge-checkpkgoverrides-%:
	@echo "[ Generating checkpkg override for package $* ]"
	$(_DBG)($(foreach O,$(or $(CHECKPKG_OVERRIDES_$*),$(CHECKPKG_OVERRIDES)) $(_CATEGORY_CHECKPKG_OVERRIDES),echo "$O";)) | \
		perl -F'\|' -ane 'unshift @F,"$*"; $$F[0].=":"; print join(" ",@F );' \
		> $(WORKDIR_GLOBAL)/checkpkg_override.$*
	@$(MAKECOOKIE)

merge-checkpkgoverrides: $(foreach S,$(SPKG_SPECS),$(if $(or $(CHECKPKG_OVERRIDES_$S),$(CHECKPKG_OVERRIDES),$(_CATEGORY_CHECKPKG_OVERRIDES)),merge-checkpkgoverrides-$S))

reset-merge-checkpkgoverrides:
	@rm -f $(COOKIEDIR)/merge-checkpkgoverrides $(foreach SPEC,$(_PKG_SPECS),$(COOKIEDIR)/merge-checkpkgoverrides-$(SPEC))
	@rm -f $(foreach S,$(SPKG_SPECS),$(WORKDIR_GLOBAL)/checkpkg_override.$S)

merge-alternatives-%:
	@echo "[ Generating alternatives for package $* ]"
	$(_DBG)ginstall -d $(PKGROOT)/opt/csw/share/alternatives
	$(_DBG)($(if $(ALTERNATIVE),echo "$(ALTERNATIVE)";) \
		$(foreach A,$(or $(ALTERNATIVES_$*),$(ALTERNATIVES)), \
		$(if $(ALTERNATIVE_$A), \
			echo "$(ALTERNATIVE_$A)";, \
			$(error The variable 'ALTERNATIVE_$A' is empty, but must contain an alternative) \
		))) > $(PKGROOT)/opt/csw/share/alternatives/$(call catalogname,$*)
	@$(MAKECOOKIE)

merge-alternatives: $(foreach S,$(SPKG_SPECS),$(if $(or $(ALTERNATIVES_$S),$(ALTERNATIVES),$(ALTERNATIVE)),merge-alternatives-$S))

reset-merge-alternatives:
	@rm -f $(COOKIEDIR)/merge-alternatives $(foreach SPEC,$(_PKG_SPECS),$(COOKIEDIR)/merge-alternatives-$(SPEC))

merge-src: _SRCDIR=$(PKGROOT)$(sourcedir)/$(call catalogname,$(SRCPACKAGE_BASE))
merge-src: fetch
	$(_DBG)mkdir -p $(_SRCDIR)/files
	$(_DBG)-rm -f $(addprefix $(_SRCDIR)/files/,$(DISTFILES) $(PATCHFILES))
	$(_DBG)(cd $(DOWNLOADDIR); cp $(DISTFILES) $(PATCHFILES) $(_SRCDIR)/files)
	$(_DBG)-rm -f $(addprefix $(_SRCDIR)/,Makefile checksums gar)
	$(_DBG)(cd $(CURDIR); cp Makefile checksums $(_SRCDIR))
	$(_DBG)ln -s ../gar/$(GARSYSTEMVERSION) $(_SRCDIR)/gar
	$(MAKECOOKIE)

reset-merge-src:
	@rm -f $(COOKIEDIR)/merge-src


# package - Use the mkpackage utility to create Solaris packages
#

PACKAGE_TARGETS = $(foreach SPEC,$(_PKG_SPECS), package-$(SPEC))

SPKG_DESTDIRS = $(SPKG_SPOOLDIR) $(SPKG_EXPORT)

$(SPKG_DESTDIRS):
	ginstall -d $@

# This is a target used to generate all prototypes for debugging purposes.
# On a normal packaging workflow this is not used.
prototypes: extract merge $(SPKG_DESTDIRS) pre-package $(foreach SPEC,$(_PKG_SPECS),$(WORKDIR)/$(SPEC).prototype-$(GARCH))

# Verify that the host on we are currently packaging is one of the platform
# hosts. If there are no platform hosts defined the test is skipped.
validateplatform:
	$(if $(strip $(foreach P,$(PACKAGING_PLATFORMS),$(PACKAGING_HOST_$P))),\
	  $(if $(filter $(THISHOST),$(foreach P,$(PACKAGING_PLATFORMS),$(PACKAGING_HOST_$P))),\
	    @$(MAKECOOKIE),\
		$(warning *** You are building this package on a non-requested platform host '$(THISHOST)'. The following platforms were requested:)\
		$(foreach P,$(PACKAGING_PLATFORMS),\
			$(warning *** - $P $(if $(PACKAGING_HOST_$P),to be build on host '$(PACKAGING_HOST_$P)',with no suitable host available))\
		)\
		$(error You can execute '$(MAKE) platforms' to automatically build on all necessary platforms.)\
	),@$(MAKECOOKIE))

# We depend on extract as the additional package files (like .gspec) must be
# unpacked to global/ for packaging. E. g. 'merge' depends only on the specific
# modulations and does not fill global/.
ENABLE_CHECK ?= 1

# The files in ISAEXEC_FILES get relocated and will be replaced by the isaexec-wrapper.
# The trick is to delay the calculcation of the variable values until that time
# when PKGROOT has already been populated.
ISAEXEC_EXCLUDE_FILES ?= $(bindir)/%-config $(bindir)/%/%-config
_buildpackage: _ISAEXEC_FILES=$(filter-out $(foreach F,$(ISAEXEC_EXCLUDE_FILES) $(EXTRA_ISAEXEC_EXCLUDE_FILES),$(PKGROOT)$(F)), \
			$(wildcard $(foreach D,$(ISAEXEC_DIRS),$(PKGROOT)$(D)/* )) \
		)
_buildpackage: ISAEXEC_FILES ?= $(if $(_ISAEXEC_FILES),$(patsubst $(PKGROOT)%,%,               \
			$(shell for F in $(_ISAEXEC_FILES); do          \
				if test -f "$$F" -a \! -h "$$F"; then echo $$F; fi;     \
			done)),)
_buildpackage: pre-package $(PACKAGE_TARGETS) post-package $(if $(filter-out 0,$(ENABLE_CHECK)),pkgcheck)

_package: validateplatform extract-global merge $(SPKG_DESTDIRS) _buildpackage
	@$(MAKECOOKIE)

package: _package
	@echo
	@echo "The following packages have been built:"
	@echo
	@$(MAKE) -s GAR_PLATFORM=$(GAR_PLATFORM) _pkgshow
	@echo
	@$(DONADA)

dirpackage: _DIRPACKAGE=1
dirpackage: ENABLE_CHECK=
dirpackage: _package
	@echo "The following packages have been built:"
	@echo
	@$(MAKE) -s GAR_PLATFORM=$(GAR_PLATFORM) _dirpkgshow
	@echo
	@$(DONADA)

_dirpkgshow:
	@$(foreach SPEC,$(_PKG_SPECS),echo "  $(SPKG_SPOOLDIR)/$(SPEC)";)

_pkgshow:
	@$(foreach SPEC,$(_PKG_SPECS),printf "  %-20s %s\n"  $(SPEC) $(SPKG_EXPORT)/$(shell $(call _PKG_ENV,$(SPEC)) $(GARBIN)/mkpackage -qs $(WORKDIR)/$(SPEC).gspec -D pkgfile).gz;)

# The dynamic pkginfo is only generated for dynamic gspec-files
package-%: $(WORKDIR)/%.gspec $(WORKDIR)/%.prototype-$(GARCH) $(WORKDIR)/%.depend $(if $(findstring %.gspec,$(DISTFILES)),,$(WORKDIR)/%.pkginfo)
	@echo " ==> Processing $*.gspec"
	$(_DBG)( $(call _PKG_ENV,$*) mkpackage \
						 --spec $(WORKDIR)/$*.gspec \
						 --spooldir $(SPKG_SPOOLDIR) \
						 --tmpdir   $(SPKG_TMPDIR)  \
						 --destdir  $(SPKG_EXPORT) \
						 --workdir  $(SPKG_WORKDIR) \
						 --pkgbase  $(SPKG_PKGBASE) \
						 --pkgroot  $(SPKG_PKGROOT) \
						 $(EXTRA_MKPACKAGE_OPTS)  \
						-v WORKDIR_FIRSTMOD=../build-$(firstword $(MODULATIONS)) \
						 $(if $(_DIRPACKAGE),--notransfer --nocompress,--compress) \
						 $(MKPACKAGE_ARGS) ) || exit 2
	@$(MAKECOOKIE)

package-p:
	@$(foreach COOKIEFILE,$(PACKAGE_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)

# pkgcheck - check if the package is compliant
#
pkgcheck: $(foreach SPEC,$(_PKG_SPECS),package-$(SPEC))
	$(_DBG)( LC_ALL=C $(GARBIN)/checkpkg \
		--architecture "$(GARCH)" \
		--os-releases "$(SPKG_OSNAME)" \
		--catalog-release "$(CATALOG_RELEASE)" \
		$(foreach SPEC,$(_PKG_SPECS),$(SPKG_EXPORT)/`$(call _PKG_ENV,$(SPEC)) mkpackage --tmpdir $(SPKG_TMPDIR) -qs $(WORKDIR)/$(SPEC).gspec -D pkgfile`.gz ) || exit 2;)
	@$(MAKECOOKIE)

pkgcheck-p:
	@$(foreach COOKIEFILE,$(PKGCHECK_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)

# pkgreset - reset working directory for repackaging
#
pkgreset: $(addprefix pkgreset-,$(SPKG_SPECS))
	@rm -f $(COOKIEDIR)/extract
	@rm -f $(COOKIEDIR)/extract-archive-*

reset-package: pkgreset

# Make sure we don't delete files we deliberately added with DISTFILES. They
# will not be copied to WORKDIR again.
pkgreset-%:
	@echo " ==> Reset packaging state for $* ($(DESTIMG))"
	$(_DBG)rm -rf $(foreach T,extract checksum package pkgcheck,$(COOKIEDIR)/*$(T)-$**)
	$(_DBG)rm -rf $(COOKIEDIR)/pre-package $(COOKIEDIR)/post-package
	$(_DBG)rm -rf $(addprefix $(WORKDIR)/,$(filter-out $(DISTFILES),$(patsubst $(WORKDIR)/%,%,$(wildcard $(WORKDIR)/$*.*)) prototype copyright $*.copyright))

repackage: pkgreset package

redirpackage: pkgreset dirpackage

# This rule automatically logs into every host where a package for this software should
# be built. It is especially suited for automated build bots.

# Heads up: Don't use MAKEFLAGS to propagate -I to remote GAR invocations as
# this will also make it visible to the build environment. Some software builds
# use hard-coded non-GNU make which then errs out on -I (unknown option).

platforms: _PACKAGING_PLATFORMS=$(if $(ARCHALL),$(firstword $(PACKAGING_PLATFORMS)),$(PACKAGING_PLATFORMS))
platforms:
	$(foreach P,$(_PACKAGING_PLATFORMS),\
		$(if $(PACKAGING_HOST_$P),\
			$(if $(filter $(THISHOST),$(PACKAGING_HOST_$P)),\
				$(MAKE) GAR_PLATFORM=$P _package && ,\
				$(SSH) -t $(PACKAGING_HOST_$P) "PATH=$$PATH:/opt/csw/bin $(MAKE) -I $(GARDIR) -C $(CURDIR) GAR_PLATFORM=$P _package" && \
			),\
			$(error *** No host has been defined for platform $P)\
		)\
	) true
	@echo
	@echo "The following packages have been built during this invocation:"
	@echo
	@$(foreach P,$(_PACKAGING_PLATFORMS),\
		echo "* Platform $P\c";\
		$(if $(ARCHALL),echo " (suitable for all architectures)\c";) \
		$(if $(filter $(THISHOST),$(PACKAGING_HOST_$P)),\
			echo " (built on this host)";\
			  $(MAKE) -s GAR_PLATFORM=$P _pkgshow;echo;,\
			echo " (built on host '$(PACKAGING_HOST_$P)')";\
			  $(SSH) $(PACKAGING_HOST_$P) "PATH=$$PATH:/opt/csw/bin $(MAKE) -I $(GARDIR) -C $(CURDIR) -s GAR_PLATFORM=$P _pkgshow";echo;\
		)\
	)
	@$(MAKECOOKIE)

platforms-%: _PACKAGING_PLATFORMS=$(if $(ARCHALL),$(firstword $(PACKAGING_PLATFORMS)),$(PACKAGING_PLATFORMS))
platforms-%:
	$(foreach P,$(_PACKAGING_PLATFORMS),\
		$(if $(PACKAGING_HOST_$P),\
			$(if $(filter $(THISHOST),$(PACKAGING_HOST_$P)),\
				$(MAKE) -s GAR_PLATFORM=$P $* && ,\
				$(SSH) -t $(PACKAGING_HOST_$P) "PATH=$$PATH:/opt/csw/bin $(MAKE) -I $(GARDIR) -C $(CURDIR) GAR_PLATFORM=$P $*" && \
			),\
			$(error *** No host has been defined for platform $P)\
		)\
	) true

replatforms: spotless platforms

# Print relecant informations about the platform
platformenv:
	@$(foreach P,$(PACKAGING_PLATFORMS),\
		echo "* Platform '$P'";\
		$(if $(PACKAGING_HOST_$P),\
			$(if $(filter $(THISHOST),$(PACKAGING_HOST_$P)),\
				echo "  - Package built on this host";,\
				echo "  - Package built on host '$(PACKAGING_HOST_$P)'";\
			),\
			echo "Package can not be built for this platform as there is no host defined";\
		)\
	)

submitpkg: submitpkg-default

submitpkg-%: _PKGURL=$(shell svn info .. | $(GAWK) '$$1 == "URL:" { print $$2 }')
submitpkg-%:
	@$(if $(filter $(call _REVISION),UNCOMMITTED NOTVERSIONED NOSVN),\
		$(error You have local files not in the repository. Please commit everything before submitting a package))
	$(SVN) -m "$(NAME): Tag as release $(SPKG_VERSION),$(SPKG_REVSTAMP)$(if $(filter default,$*),, for project '$*')" cp $(_PKGURL)/trunk $(_PKGURL)/tags/$(if $(filter default,$*),,$*_)$(NAME)-$(SPKG_VERSION),$(SPKG_REVSTAMP)

# dependb - update the dependency database
#
dependb:
	@dependb --db $(SPKG_DEPEND_DB) \
             --parent $(CATEGORIES)/$(NAME) \
             --add $(DEPENDS)

# pkgenv - dump the packaging environment
#
pkgenv:
	@$(foreach SPEC,$(_PKG_SPECS),echo "$(SPEC)";echo;$(call _PKG_ENV,$(SPEC)) env;)


# pkglist - list the packages to be built with GAR pathname, catalog name and package name
#

define _pkglist_one
$(shell /usr/bin/echo "$(shell pwd)\t$(call catalogname,$(1))\t$(call pkgname,$(1))")
endef

pkglist:
	@$(foreach SPEC,$(SPKG_SPECS),echo "$(call _pkglist_one,$(SPEC))";)
