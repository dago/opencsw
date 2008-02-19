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

SPKG_SPECS     ?= $(basename $(filter %.gspec,$(DISTFILES)))
_PKG_SPECS      = $(filter-out $(NOPACKAGE),$(SPKG_SPECS))

SPKG_DESC      ?= $(DESCRIPTION)
SPKG_VERSION   ?= $(GARVERSION)
SPKG_CATEGORY  ?= application
SPKG_SOURCEURL ?= $(firstword $(MASTER_SITES))
SPKG_PACKAGER  ?= Unknown
SPKG_VENDOR    ?= $(SPKG_SOURCEURL) packaged for CSW by $(SPKG_PACKAGER)
SPKG_EMAIL     ?= Unknown
SPKG_PSTAMP    ?= $(LOGNAME)@$(shell hostname)-$(shell date '+%Y%m%d%H%M%S')
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

# prototype - Generate prototype for all installed files
# This can be used to automatically distribute the files to different packages
#

# This should go to gar.conf.mk when automatic-multiarch-compile is in place
ISALIST_sparc   = sparcv8plus+fmuladd sparcv8plus+vis2 sparcv8plus+vis sparcv8plus sparcv8 sparcv8-fsmuld
ISALIST_sparcv9 = sparcv9+fmuladd sparcv9+vis2 sparcv9+vis sparcv9 $(ISALIST_sparc)
ISALIST_i386    = pentium_pro+mmx pentium_pro pentium+mmx pentium i486 i386
ISALIST_amd64   = amd64 $(ISALIST_i386)
ISALIST = $(ISALIST_sparcv9) $(ISALIST_amd64)

# PKGFILES_RT selects files belonging to a runtime package
PKGFILES_RT  = $(libdir)/[^/]*\.so(\.\d+)*
PKGFILES_RT += $(foreach ISA,$(ISALIST),$(libdir)/$(ISA)/[^/]*\.so(\.\d+)*)

# PKGFILES_DEVEL selects files belonging to a developer package
PKGFILES_DEVEL  = $(bindir)/[^\/]*-config
PKGFILES_DEVEL += $(foreach ISA,$(ISALIST),$(bindir)/$(ISA)/[^/]*-config)
PKGFILES_DEVEL += $(libdir)/[^\/]*\.(a|la)
PKGFILES_DEVEL += $(foreach ISA,$(ISALIST),$(libdir)/$(ISA)/[^/]*\.(a|la))
PKGFILES_DEVEL += $(libdir)/pkgconfig(/.*)?
PKGFILES_DEVEL += $(foreach ISA,$(ISALIST),$(libdir)/$(ISA)/pkgconfig(/.*)?)
PKGFILES_DEVEL += $(includedir)/.*

# PKGFILES_DOC selects files beloging to a documentation package
PKGFILES_DOC  = $(docdir)

# _PKGFILES_EXCLUDE_<spec> contains the files to be excluded from that package
$(foreach SPEC,$(_PKG_SPECS),$(eval								\
	_PKGFILES_EXCLUDE_$(SPEC)=								\
		$(foreach S,$(filter-out $(SPEC),$(_PKG_SPECS)),$(PKGFILES_$(S)_EXCLUSIVE))	\
		$(EXTRA_PKGFILES_EXCLUDED) $(EXTRA_PKGFILES_EXCLUDED_$(SPEC))			\
))

# This file contains all installed pathes
PROTOTYPE = $(WORKDIR)/prototype

# Pulled in from pkglib/csw_prototype.gspec
$(PROTOTYPE): install
	@cswproto -s $(TIMESTAMP) -r $(DESTDIR) $(DESTDIR)$(prefix) > $(PROTOTYPE)

.PRECIOUS: $(WORKDIR)/%.prototype $(WORKDIR)/%.prototype-$(GARCH)
$(WORKDIR)/%.prototype: $(PROTOTYPE)
	@if [ -n "$(PKGFILES_$*)" -o -n "$(PKGFILES_$*_EXCLUSIVE)" -o -n "$(_PKGFILES_EXCLUDE_$*)" ]; then	\
		pathfilter $(foreach FILE,$(PKGFILES_$*) $(PKGFILES_$*_EXCLUSIVE),-i '$(FILE)')		\
			$(foreach FILE,$(_PKGFILES_EXCLUDE_$*), -x '$(FILE)')				\
		<$(PROTOTYPE) >$@;									\
	else												\
		cp $(PROTOTYPE) $@;									\
	fi

$(WORKDIR)/%.prototype-$(GARCH): $(WORKDIR)/%.prototype
	@cp $(WORKDIR)/$*.prototype $@

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

package: install $(SPKG_DESTDIRS) pre-package $(PACKAGE_TARGETS) post-package
	$(DONADA)

package-%: $(WORKDIR)/%.prototype-$(GARCH)
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

# pkgcheck - check if the package is blastwave compliant
#
pkgcheck: $(addprefix pkgcheck-,$(_PKG_SPECS))
	$(DONADA)

pkgcheck-%:
	@echo " ==> Checking blastwave compilance: $*"
	@( checkpkg $(SPKG_EXPORT)/`$(PKG_ENV) mkpackage -qs $(WORKDIR)/$*.gspec -D pkgfile`.gz ) || exit 2

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

