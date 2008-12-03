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
SPKG_PKGROOT   ?= $(DESTDIR)
SPKG_PKGBASE   ?= $(CURDIR)/$(WORKDIR)
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
PKG_EXPORTS += CURDIR WORKDIR WORKSRC
PKG_EXPORTS += SPKG_REVSTAMP SPKG_PKGNAME SPKG_DESC SPKG_VERSION SPKG_CATEGORY
PKG_EXPORTS += SPKG_VENDOR SPKG_EMAIL SPKG_PSTAMP SPKG_BASEDIR SPKG_CLASSES
PKG_EXPORTS += SPKG_OSNAME SPKG_SOURCEURL SPKG_PACKAGER TIMESTAMP
PKG_EXPORTS += DEPMAKER_EXTRA_ARGS PKGLIB DESTDIR

PKG_ENV  = $(BUILD_ENV)
PKG_ENV += $(foreach EXP,$(PKG_EXPORTS),$(EXP)="$($(EXP))")

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

#
# Targets
#

# timestamp - Create a pre-installation timestamp
#
TIMESTAMP = $(COOKIEDIR)/timestamp
PRE_INSTALL_TARGETS += timestamp
timestamp:
	@echo " ==> Creating timestamp cookie"
	@$(MAKECOOKIE)

remove-timestamp:
	@echo " ==> Removing timestamp cookie"
	@-rm -f $(TIMESTAMP)

# package - Use the mkpackage utility to create Solaris packages
#

SPKG_SPECS     ?= $(basename $(filter %.gspec,$(DISTFILES)))
_PKG_SPECS      = $(filter-out $(NOPACKAGE),$(SPKG_SPECS))

ifneq ($(ENABLE_CHECK),0)
PACKAGE_TARGETS = $(foreach SPEC,$(_PKG_SPECS), package-$(SPEC) pkgcheck-$(SPEC))
else
PACKAGE_TARGETS = $(foreach SPEC,$(_PKG_SPECS), package-$(SPEC))
endif

SPKG_DESTDIRS = $(SPKG_SPOOLDIR) $(SPKG_EXPORT)

$(SPKG_DESTDIRS):
	ginstall -d $@

package: install $(SPKG_DESTDIRS) pre-package $(PACKAGE_TARGETS) post-package
	$(DONADA)

package-%:
	@echo " ==> Processing $*.gspec"
	@( $(PKG_ENV) mkpackage --spec $(WORKDIR)/$*.gspec \
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

# pkgcheck - check if the package is standards compliant
#
pkgcheck: $(addprefix pkgcheck-,$(_PKG_SPECS))
	$(DONADA)

pkgcheck-%:
	@echo " ==> Checking standards compliance: $*"
	@( LC_ALL=C checkpkg $(SPKG_EXPORT)/`$(PKG_ENV) mkpackage -qs $(WORKDIR)/$*.gspec -D pkgfile`.gz ) || exit 2

pkgcheck-p:
	@$(foreach COOKIEFILE,$(PKGCHECK_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)

# pkgreset - reset working directory for repackaging
#
pkgreset: $(addprefix pkgreset-,$(_PKG_SPECS))
	$(DONADA)

pkgreset-%:
	@echo " ==> Reset packaging state for $* ($(DESTIMG))"
	@rm -rf $(foreach T,extract checksum package pkgcheck,$(COOKIEDIR)/*$(T)-$**)
	@rm -rf $(COOKIEDIR)/pre-package $(COOKIEDIR)/post-package
	@rm -rf $(WORKDIR)/$*.*

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
	@$(PKG_ENV) env


# pkglist - list the packages to be built with GAR pathname, catalog name and package name
#

define _pkglist_pkgname
$(shell perl -F'\s+' -ane 'print "$$F[2]" if( $$F[0] eq "%var" && $$F[1] eq "pkgname")' files/$(1).gspec)
endef

define _pkglist_catalogname
$(shell perl -F'\s+' -ane 'print "$$F[2]" if( $$F[0] eq "%var" && $$F[1] eq "bitname")' files/$(1).gspec)
endef

define _pkglist_one
$(shell /usr/bin/echo "$(patsubst $(realpath $(shell pwd)/$(GARDIR))/%,%,$(realpath .))\t$(call _pkglist_catalogname,$(1))\t$(call _pkglist_pkgname,$(1))")
endef

pkglist:
	@echo "G: $(GARDIR) - $(shell pwd) - $(realpath $(shell pwd)/$(GARDIR)) - $(realpath .)"
	@$(foreach SPEC,$(SPKG_SPECS),echo "$(call _pkglist_one,$(SPEC))";)
