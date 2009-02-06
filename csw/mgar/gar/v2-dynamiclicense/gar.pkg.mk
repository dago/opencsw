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
# The whole processing is done from _SPKG_SPECS, which includes all packages to be build.
PACKAGES ?= CSW$(GARNAME)
SPKG_SPECS     ?= $(sort $(basename $(filter %.gspec,$(DISTFILES))) $(PACKAGES))
_PKG_SPECS      = $(filter-out $(NOPACKAGE),$(SPKG_SPECS))

define pkgname
$(strip 
  $(if $(filter $(1),$(PACKAGES)),
    $(1),
    $(shell perl -F'\s+' -ane 'print "$$F[2]" if( $$F[0] eq "%var" && $$F[1] eq "pkgname")' files/$(1).gspec)
  )
)
endef

define catalogname
$(strip 
  $(if $(filter $(1),$(PACKAGES)),
    $(if $(CATALOGNAME_$(1)),
      $(CATALOGNAME_$(1)),
      $(patsubst CSW%,%,$(1))
    ),
    $(if $(realpath files/$(1).gspec),
      $(shell perl -F'\s+' -ane 'print "$$F[2]" if( $$F[0] eq "%var" && $$F[1] eq "bitname")' files/$(1).gspec),
      $(error The catalog name for the package '$1' could not be determined, because it was neither in PACKAGES nor was there a gspec-file)
    )
  )
)
endef

ifeq ($(origin LICENSE_FULL), undefined)
LICENSE ?= COPYING
endif

define findlicensefile
$(strip 
  $(if $(1),$(firstword $(realpath 
    $(1) $(WORKDIR)/$(1) 
    $(foreach D,$(foreach M,global $(MODULATIONS),build-$M),$(WORKROOTDIR)/$D/$(DISTNAME)/$(1)) 
  ))) 
)
endef

define licensefile
$(strip 
  $(or 
    $(call findlicensefile,$(LICENSE_$(1))),
    $(call findlicensefile,$(LICENSE_FULL_$(1))),
    $(call findlicensefile,$(LICENSE)),
    $(call findlicensefile,$(LICENSE_FULL))
  )
)
endef

ps:
	@echo "L: $(call licensefile,CSWlibtool)"

define licensedir
$(docdir)/$(call catalogname,$(1))
endef

# Set this to your svn binary
SVN  ?= /opt/csw/bin/svn
GAWK ?= /opt/csw/bin/gawk

# We have to deal with four cases here:
# 1. There is no svn binary -> NOSVN
# 2. There is a svn binary, but the directory does not belong to a repository -> NOTVERSIONED
# 3. There is a svn binary, but not everything was committed properly -> UNCOMMITTED
# 4. There is a svn binary and everything was committed -> r<revision>

# Calculating the revision can be time consuming, so we do this on demand
define _REVISION
$(if $(shell if test -x $(SVN); then echo yes; fi),$(if $(shell $(SVN) info >/dev/null 2>&1; if test $$? -eq 0; then echo YES; fi),$(if $(shell $(SVN) status --ignore-externals 2>/dev/null | grep -v '^X'),UNCOMMITTED,$(shell $(SVN) info --recursive 2>/dev/null | $(GAWK) '$$1 == "Revision:" && MAX < $$2 { MAX = $$2 } END {print "r" MAX }')),NOTVERSIONED),NOSVN)
endef

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
PKG_EXPORTS += CURDIR WORKDIR WORKSRC WORKSRC_FIRSTMOD PKGROOT
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

# _PKGFILES_EXCLUDE_<spec> contains the files to be excluded from that package
$(foreach SPEC,$(_PKG_SPECS), \
  $(eval _PKGFILES_EXCLUDE_$(SPEC)=$(strip \
    $(foreach S,$(filter-out $(SPEC),$(_PKG_SPECS)), \
      $(PKGFILES_$(S)) \
      $(call licensedir,$(S))/.* \
      $(EXTRA_PKGFILES_EXCLUDED) \
      $(EXTRA_PKGFILES_EXCLUDED_$(SPEC)) \
      $(_EXTRA_PKGFILES_EXCLUDED) \
    ) \
  )) \
  $(eval _PKGFILES_INCLUDE_$(SPEC)=$(strip \
    $(call licensedir,$(SPEC))/.* \
  )) \
)

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

# Pulled in from pkglib/csw_prototype.gspec
$(PROTOTYPE): $(WORKDIR) merge
	$(_DBG)cswproto -r $(PKGROOT) $(PKGROOT)=/ >$@

.PRECIOUS: $(WORKDIR)/%.prototype $(WORKDIR)/%.prototype-$(GARCH)
$(WORKDIR)/%.prototype: | $(PROTOTYPE)
	$(_DBG)if [ -n "$(PKGFILES_$*_SHARED)" -o \
	      -n "$(PKGFILES_$*)" -o \
	      -n "$(_PKGFILES_EXCLUDE_$*)" -o \
	      -n "$(ISAEXEC_FILES_$*)" -o \
	      -n "$(ISAEXEC_FILES)" ]; then \
	  (pathfilter $(foreach FILE,$(if $(or $(PKGFILES_$*_SHARED),$(PKGFILES_$*)),$(_PKGFILES_INCLUDE_$*)) \
			$(PKGFILES_$*_SHARED) $(PKGFILES_$*),-i '$(FILE)') \
	              $(foreach FILE,$(_PKGFILES_EXCLUDE_$*), -x '$(FILE)') \
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

# $_EXTRA_GAR_PKGS is for dynamic dependencies added by GAR itself (like CSWisaexec or CSWcswclassutils)
.PRECIOUS: $(WORKDIR)/%.depend
$(WORKDIR)/%.depend:
	$(_DBG)$(if $(_EXTRA_GAR_PKGS)$(REQUIRED_PKGS_$*)$(REQUIRED_PKGS), \
		($(foreach PKG,$(INCOMPATIBLE_PKGS_$*) $(INCOMPATIBLE_PKGS),\
			echo "I $(PKG)";\
		)\
		$(foreach PKG,$(_EXTRA_GAR_PKGS) $(REQUIRED_PKGS_$*) $(REQUIRED_PKGS),\
			$(if $(SPKG_DESC_$(PKG)), \
				echo "P $(PKG) $(call catalogname,$(PKG)) - $(SPKG_DESC_$(PKG))";, \
				echo "$(shell /usr/bin/pkginfo $(PKG) | awk '{ $$1 = "P"; print } ')"; \
			) \
		)) >$@)


# This rule dynamically generates gspec-files
.PRECIOUS: $(WORKDIR)/%.gspec
$(WORKDIR)/%.gspec: ARCHALL_$* ?= $(ARCHALL)
$(WORKDIR)/%.gspec:
	$(_DBG)(echo "%var            bitname $(call catalogname,$*)"; \
	echo "%var            pkgname $*"; \
	$(if $(ARCHALL_$*),echo "%var            arch all";) \
	echo "%include        url file://%{PKGLIB}/csw_dyndepend.gspec") >$@

# This rule dynamically generates copyright files
.PRECIOUS: $(WORKDIR)/copyright $(WORKDIR)/%.copyright
# LICENSE may be a path starting with $(WORKROOTDIR) or a filename inside $(WORKSRC)

merge-license-%:
	$(_DBG)LICENSEFILE=$(or $(call licensefile,$*),$(error Cannot find license file for package $*)); \
		LICENSEDIR=$(call licensedir,$*); \
		$(if $(or $(LICENSE_FULL),$(LICENSE_FULL_$*)), \
		    if [ -f "$$LICENSEFILE" ]; then cp $$LICENSEFILE $(WORKDIR)/$*.copyright; fi;, \
		    (echo "This software is copyrighted. Please see the full license at"; \
		     echo "  $$LICENSEDIR/license") > $(WORKDIR)/$*.copyright; \
		) \
		  mkdir -p $(PKGROOT)$$LICENSEDIR && \
		  cp $$LICENSEFILE $(PKGROOT)$$LICENSEDIR/license 

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

package-%: $(WORKDIR)/%.gspec $(WORKDIR)/%.copyright $(WORKDIR)/%.prototype-$(GARCH) $(WORKDIR)/%.depend
	@echo " ==> Processing $*.gspec"
	$(_DBG)( $(call _PKG_ENV,$*) mkpackage --spec $(WORKDIR)/$*.gspec \
						 --spooldir $(SPKG_SPOOLDIR) \
						 --destdir  $(SPKG_EXPORT) \
						 --workdir  $(SPKG_WORKDIR) \
						 --pkgbase  $(SPKG_PKGBASE) \
						 --pkgroot  $(SPKG_PKGROOT) \
						-v WORKDIR_FIRSTMOD=../build-$(firstword $(MODULATIONS)) \
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
