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
# Do "PACKAGES = CSWmypkg" when you build a package whose GARNAME is not the package name.
# If no explicit gspec-files have been defined the default name for the package is CSW$(GARNAME).
# The whole processing is done from _PKG_SPECS, which includes all packages to be build.
ifeq ($(origin PACKAGES), undefined)
PACKAGES        = $(if $(filter %.gspec,$(DISTFILES)),,CSW$(GARNAME))
SPKG_SPECS     ?= $(basename $(filter %.gspec,$(DISTFILES))) $(PACKAGES)
else
SPKG_SPECS     ?= $(sort $(basename $(filter %.gspec,$(DISTFILES))) $(PACKAGES))
endif
_PKG_SPECS      = $(filter-out $(NOPACKAGE),$(SPKG_SPECS))

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
  $(if $(filter $(1),$(PACKAGES)),
    $(if $(CATALOGNAME_$(1)),
      $(CATALOGNAME_$(1)),
      $(if $(CATALOGNAME),
        $(CATALOGNAME),
        $(patsubst CSW%,%,$(1))
      )
    ),
    $(if $(realpath files/$(1).gspec),
      $(shell perl -F'\s+' -ane 'print "$$F[2]" if( $$F[0] eq "%var" && $$F[1] eq "bitname")' files/$(1).gspec),
      $(error The catalog name for the package '$1' could not be determined, because it was neither in PACKAGES nor was there a gspec-file)
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

SPKG_DESC      ?= $(DESCRIPTION)
SPKG_VERSION   ?= $(GARVERSION)
SPKG_CATEGORY  ?= application
SPKG_SOURCEURL ?= $(firstword $(MASTER_SITES))
SPKG_PACKAGER  ?= Unknown
SPKG_VENDOR    ?= $(SPKG_SOURCEURL) packaged for CSW by $(SPKG_PACKAGER)
SPKG_EMAIL     ?= Unknown
SPKG_PSTAMP    ?= $(LOGNAME)@$(shell hostname)-$(call _REVISION)-$(shell date '+%Y%m%d%H%M%S')
SPKG_BASEDIR   ?= $(prefix)
SPKG_CLASSES   ?= none
SPKG_OSNAME    ?= $(shell uname -s)$(shell uname -r)

SPKG_SPOOLROOT ?= $(DESTROOT)
SPKG_SPOOLDIR  ?= $(SPKG_SPOOLROOT)/spool.$(GAROSREL)-$(GARCH)
SPKG_EXPORT    ?= $(WORKDIR)
SPKG_PKGROOT   ?= $(PKGROOT)
SPKG_PKGBASE   ?= $(PKGROOT)
SPKG_WORKDIR   ?= $(CURDIR)/$(WORKDIR)

SPKG_DEPEND_DB  = $(GARDIR)/csw/depend.db

PKGGET_DESTDIR ?=

DEPMAKER_EXTRA_ARGS = --noscript --nodep SUNW

# Construct a revision stamp
ifeq ($(GARFLAVOR),DBG)
SPKG_FULL_REVSTAMP=1
endif

ifeq ($(SPKG_FULL_REVSTAMP),1)
SPKG_REVSTAMP  ?= ,REV=$(shell date '+%Y.%m.%d.%H.%M')
else
SPKG_REVSTAMP  ?= ,REV=$(shell date '+%Y.%m.%d')
endif

# Is this a full or incremental build?
SPKG_INCREMENTAL ?= 1

# Where we find our mkpackage global templates
PKGLIB = $(CURDIR)/$(GARDIR)/pkglib

PKG_EXPORTS  = GARNAME GARVERSION DESCRIPTION CATEGORIES GARCH GARDIR GARBIN
PKG_EXPORTS += CURDIR WORKDIR WORKDIR_FIRSTMOD WORKSRC WORKSRC_FIRSTMOD PKGROOT
PKG_EXPORTS += SPKG_REVSTAMP SPKG_PKGNAME SPKG_DESC SPKG_VERSION SPKG_CATEGORY
PKG_EXPORTS += SPKG_VENDOR SPKG_EMAIL SPKG_PSTAMP SPKG_BASEDIR SPKG_CLASSES
PKG_EXPORTS += SPKG_OSNAME SPKG_SOURCEURL SPKG_PACKAGER TIMESTAMP
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
isadirs = $(foreach ISA,$(ISALIST),$(1)/$(ISA)/$(2))

# This is a helper function just like isadirs, but also contains the
# prefix and suffix without an ISA subdirectories inserted.
# usage: $(call isadirs,<prefix>,<suffix>)
# expands to <prefix>/<suffix> <prefix>/<isa1>/<suffix> <prefix>/<isa2>/<suffix> ...
baseisadirs = $(1)/$(2) $(call isadirs,$(1),$(2))

# PKGFILES_RT selects files belonging to a runtime package
PKGFILES_RT += $(call baseisadirs,$(libdir),[^/]*\.so(\.\d+)*)

# PKGFILES_DEVEL selects files belonging to a developer package
PKGFILES_DEVEL += $(call baseisadirs,$(bindir),[^/]*-config)
PKGFILES_DEVEL += $(call baseisadirs,$(libdir),[^/]*\.(a|la))
PKGFILES_DEVEL += $(call baseisadirs,$(libdir),pkgconfig(/.*)?)
PKGFILES_DEVEL += $(includedir)/.*
PKGFILES_DEVEL += $(sharedstatedir)/aclocal/.*
PKGFILES_DEVEL += $(mandir)/man1/.*-config\.1.*
PKGFILES_DEVEL += $(mandir)/man3/.*

# PKGFILES_DOC selects files beloging to a documentation package
PKGFILES_DOC  = $(docdir)/.*

# This function computes the files to be excluded from the package specified
# as argument
define _pkgfiles_exclude
$(strip 
  $(foreach S,$(filter-out $(1),$(_PKG_SPECS)), 
    $(PKGFILES_$(S)) 
    $(EXTRA_PKGFILES_EXCLUDED) 
    $(EXTRA_PKGFILES_EXCLUDED_$(1)) 
    $(_EXTRA_PKGFILES_EXCLUDED) 
  ) 
)
endef

define _pkgfiles_include
$(strip 
  $(PKGFILES_$(1)_SHARED) 
  $(PKGFILES_$(1)) 
)
endef

#
# Targets
#

# prototype - Generate prototype for all installed files
# This can be used to automatically distribute the files to different packages
#

$(foreach SPEC,$(_PKG_SPECS),$(if $(PROTOTYPE_FILTER_$(SPEC)),$(eval _PROTOTYPE_FILTER_$(SPEC) ?= | $(PROTOTYPE_FILTER_$(SPEC)))))
$(foreach SPEC,$(_PKG_SPECS),$(if $(PROTOTYPE_FILTER),$(eval _PROTOTYPE_FILTER_$(SPEC) ?= | $(PROTOTYPE_FILTER))))

# This file contains all installed pathes. This can be used as a starting point
# for distributing files to individual packages.
PROTOTYPE = $(WORKDIR)/prototype

# Dynamic prototypes work like this:
# - A prototype from DISTFILES takes precedence over 

# Pulled in from pkglib/csw_prototype.gspec
$(PROTOTYPE): $(WORKDIR) merge
	$(_DBG)cswproto -r $(PKGROOT) $(PKGROOT)=/ >$@

# The pathfilter rules are as follows:
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
	  (pathfilter $(if $(or $(_PKGFILES_EXCLUDE),$(_PKGFILES_INCLUDE)),-i $(call licensedir,$*)/license) \
		      $(foreach S,$(filter-out $*,$(SPKG_SPECS)),-x $(call licensedir,$S)/license) \
		      $(foreach FILE,$(_PKGFILES_INCLUDE),-i '$(FILE)') \
		      $(if $(_PKGFILES_INCLUDE),-x '.*',$(foreach FILE,$(_PKGFILES_EXCLUDE),-x '$(FILE)')) \
	              $(foreach IE,$(abspath $(ISAEXEC_FILES_$*) $(ISAEXEC_FILES)), \
	                  -e '$(IE)=$(dir $(IE))$(ISA_DEFAULT)/$(notdir $(IE))' \
	               ) \
	              <$(PROTOTYPE); \
	   if [ -n "$(EXTRA_PKGFILES_$*)" ]; then echo "$(EXTRA_PKGFILES_$*)"; fi \
	  ) $(_PROTOTYPE_FILTER_$*) >$@; \
	else \
	  cat $(PROTOTYPE) $(_PROTOTYPE_FILTER_$*) >$@; \
	fi

$(WORKDIR)/%.prototype-$(GARCH): | $(WORKDIR)/%.prototype
	$(_DBG)cat $(WORKDIR)/$*.prototype $(_PROTOTYPE_FILTER_$*) >$@

# Dynamic depends are constructed as follows:
# - Packages the currently constructed one depends on can be specified with
#   REQUIRED_PKGS_<pkg> specifically, or REQUIRED_PKGS for all packages build.
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
$(WORKDIR)/%.depend: $(WORKDIR)
	$(_DBG)$(if $(_EXTRA_GAR_PKGS)$(REQUIRED_PKGS_$*)$(REQUIRED_PKGS)$(INCOMPATIBLE_PKGS)$(INCOMPATIBLE_PKGS_$*), \
		($(foreach PKG,$(INCOMPATIBLE_PKGS_$*) $(INCOMPATIBLE_PKGS),\
			echo "I $(PKG)";\
		)\
		$(foreach PKG,$(_EXTRA_GAR_PKGS) $(REQUIRED_PKGS_$*) $(REQUIRED_PKGS),\
			$(if $(SPKG_DESC_$(PKG)), \
				echo "P $(PKG) $(call catalogname,$(PKG)) - $(SPKG_DESC_$(PKG))";, \
				echo "$(shell (/usr/bin/pkginfo $(PKG) || echo "P $(PKG) - ") | awk '{ $$1 = "P"; print } ')"; \
			) \
		)) >$@)

# Dynamic gspec-files are constructed as follows:
# - Packages using dynamic gspec-files must be listed in PACKAGES
# - There is a default of PACKAGES containing one packages named CSW
#   followed by the GARNAME. It can be changed by setting PACKAGES explicitly.
# - The name of the generated package is always the same as listed in PACKAGES
# - The catalog name defaults to the suffix following CSW of the package name,
#   but can be customized by setting CATALOGNAME_<pkg> = <catalogname-of-pkg>
# - If only one package is build it is sufficient to set CATALOGNAME = <catalogname-of-pkg>
#   It is an error to set CATALOGNAME if more than one package is build.
# - If the package is suitable for all architectures (sparc and x86) this can be
#   flagged with ARCHALL_<pkg> = 1 for a specific package or with ARCHALL = 1
#   for all packages.

# This rule dynamically generates gspec-files
.PRECIOUS: $(WORKDIR)/%.gspec
$(WORKDIR)/%.gspec:
	$(_DBG)$(if $(filter $*.gspec,$(DISTFILES)),,\
		(echo "%var            bitname $(call catalogname,$*)"; \
		echo "%var            pkgname $*"; \
		$(if $(or $(ARCHALL),$(ARCHALL_$*)),echo "%var            arch all";) \
		echo "%include        url file://%{PKGLIB}/csw_dyngspec.gspec") >$@\
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
$(if $(shell if test -x $(SVN); then echo yes; fi),$(shell $(SVN) info . 2>/dev/null | $(GAWK) '$$1 == "URL:" { print $$2 }))
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
$(if $($(1)_$(2)),$($(1)_$(2)),$($(1)))
endef

.PRECIOUS: $(WORKDIR)/%.pkginfo
$(WORKDIR)/%.pkginfo: $(WORKDIR)
	$(_DBG)(echo "PKG=$*"; \
	echo "NAME=$(call catalogname,$*) - $(call pkgvar,SPKG_DESC,$*)"; \
	echo "ARCH=$(if $(or $(ARCHALL),$(ARCHALL_$*)),all,$(call pkgvar,GARCH,$*))"; \
	echo "VERSION=$(call pkgvar,SPKG_VERSION,$*)$(call pkgvar,SPKG_REVSTAMP,$*)"; \
	echo "CATEGORY=$(call pkgvar,SPKG_CATEGORY,$*)"; \
	echo "VENDOR=$(call pkgvar,SPKG_VENDOR,$*)"; \
	echo "EMAIL=$(call pkgvar,SPKG_EMAIL,$*)"; \
	echo "PSTAMP=$(LOGNAME)@$(shell hostname)-$(shell date '+%Y%m%d%H%M%S')"; \
	echo "CLASSES=$(call pkgvar,SPKG_CLASSES,$*)"; \
	echo "HOTLINE=http://www.opencsw.org/bugtrack/"; \
	echo "OPENCSW_REPOSITORY=$(call _URL)@$(call _REVISION)"; \
	echo "OPENCSW_MODE64=$(call mode64,$*)"; \
	) >$@


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
    $(call findlicensefile,$(or $(LICENSE_$(1)),$(LICENSE_FULL_$(1))))
    $(call findlicensefile,$(or $(LICENSE),$(LICENSE_FULL))),
  )
)
endef

merge-license-%: $(WORKDIR)
	$(_DBG)$(if $(and $(LICENSE_$*),$(LICENSE_FULL_$*)),$(error Both LICENSE_$* and LICENSE_FULL_$* have been specified where only one is allowed)) \
		$(if $(and $(filter $*,$(PACKAGES)),$(or $(LICENSE),$(LICENSE_FULL),$(LICENSE_$*),$(LICENSE_FULL_$*))), \
		LICENSEFILE=$(or $(call licensefile,$*),$(if $(_LICENSE_IS_DEFAULT),,$(error Cannot find license file for package $*))); \
		LICENSEDIR=$(call licensedir,$*); \
		if [ -n "$$LICENSEFILE" ]; then \
		$(if $(or $(LICENSE_FULL),$(LICENSE_FULL_$*)), \
		    if [ -f "$$LICENSEFILE" ]; then cp $$LICENSEFILE $(WORKDIR)/$*.copyright; fi;, \
		    echo "Please see $$LICENSEDIR/license for license information." > $(WORKDIR)/$*.copyright; \
		) \
		  mkdir -p $(PKGROOT)$$LICENSEDIR && \
		  cp $$LICENSEFILE $(PKGROOT)$$LICENSEDIR/license; \
		fi \
	)

merge-license: $(foreach SPEC,$(_PKG_SPECS),merge-license-$(SPEC))

# package - Use the mkpackage utility to create Solaris packages
#

ifneq ($(ENABLE_CHECK),0)
PACKAGE_TARGETS = $(foreach SPEC,$(_PKG_SPECS), package-$(SPEC) pkgcheck-$(SPEC))
else
PACKAGE_TARGETS = $(foreach SPEC,$(_PKG_SPECS), package-$(SPEC))
endif

SPKG_DESTDIRS = $(SPKG_SPOOLDIR) $(SPKG_EXPORT)

$(SPKG_DESTDIRS):
	ginstall -d $@

# This is a target used to generate all prototypes for debugging purposes.
# On a normal packaging workflow this is not used.
prototypes: extract merge $(SPKG_DESTDIRS) pre-package $(foreach SPEC,$(_PKG_SPECS),$(WORKDIR)/$(SPEC).prototype-$(GARCH))

# We depend on extract as the additional package files (like .gspec) must be
# unpacked to global/ for packaging. E. g. 'merge' depends only on the specific
# modulations and does not fill global/.
package: extract merge $(SPKG_DESTDIRS) pre-package $(PACKAGE_TARGETS) post-package
	$(DONADA)

# The dynamic pkginfo is only generated for dynamic gspec-files
package-%: $(WORKDIR)/%.gspec $(if $(filter %.gspec,$(DISTFILES)),,$(WORKDIR)/%.pkginfo) $(WORKDIR)/%.prototype-$(GARCH) $(WORKDIR)/%.depend
	@echo " ==> Processing $*.gspec"
	$(_DBG)( $(call _PKG_ENV,$*) mkpackage --spec $(WORKDIR)/$*.gspec \
						 --spooldir $(SPKG_SPOOLDIR) \
						 --destdir  $(SPKG_EXPORT) \
						 --workdir  $(SPKG_WORKDIR) \
						 --pkgbase  $(SPKG_PKGBASE) \
						 --pkgroot  $(SPKG_PKGROOT) \
						 --compress \
						 $(MKPACKAGE_ARGS) ) || exit 2
	@$(MAKECOOKIE)

package-p:
	@$(foreach COOKIEFILE,$(PACKAGE_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)

# pkgcheck - check if the package is compliant
#
pkgcheck: $(addprefix pkgcheck-,$(_PKG_SPECS))
	$(DONADA)

pkgcheck-%:
	@echo " ==> Checking compliance: $*"
	@( LC_ALL=C checkpkg $(SPKG_EXPORT)/`$(call _PKG_ENV,$1) mkpackage -qs $(WORKDIR)/$*.gspec -D pkgfile`.gz ) || exit 2

pkgcheck-p:
	@$(foreach COOKIEFILE,$(PKGCHECK_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)

# pkgreset - reset working directory for repackaging
#
pkgreset: $(addprefix pkgreset-,$(SPKG_SPECS))
	@rm -f $(COOKIEDIR)/extract
	@rm -f $(COOKIEDIR)/extract-archive-*
	$(DONADA)

reset-package: pkgreset

pkgreset-%:
	@echo " ==> Reset packaging state for $* ($(DESTIMG))"
	@rm -rf $(foreach T,extract checksum package pkgcheck,$(COOKIEDIR)/*$(T)-$**)
	@rm -rf $(COOKIEDIR)/pre-package $(COOKIEDIR)/post-package
	@rm -rf $(WORKDIR)/$*.* $(WORKDIR)/prototype
	@rm -f $(WORKDIR)/copyright $(WORKDIR)/*.copyright

repackage: pkgreset package

# dependb - update the dependency database
#
dependb:
	@dependb --db $(SPKG_DEPEND_DB) \
             --parent $(CATEGORIES)/$(GARNAME) \
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
