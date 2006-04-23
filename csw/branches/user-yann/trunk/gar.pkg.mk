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

SPKG_REVSTAMP  ?= ,REV=$(shell date '+%Y.%m.%d')
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

SPKG_EXPORT    ?= $(WORKDIR)
SPKG_DEPEND_DB  = $(GARDIR)/csw/depend.db

PKGGET_DESTDIR ?=

DEPMAKER_EXTRA_ARGS = --noscript --nodep SUNW

# Is this a full or incremental build?
SPKG_INCREMENTAL ?= 1

PKG_EXPORTS  = GARNAME GARVERSION DESCRIPTION CATEGORIES GARCH GARDIR GARBIN
PKG_EXPORTS += CURDIR WORKDIR WORKSRC
PKG_EXPORTS += SPKG_REVSTAMP SPKG_PKGNAME SPKG_DESC SPKG_VERSION SPKG_CATEGORY
PKG_EXPORTS += SPKG_VENDOR SPKG_EMAIL SPKG_PSTAMP SPKG_BASEDIR SPKG_CLASSES
PKG_EXPORTS += SPKG_OSNAME SPKG_SOURCEURL SPKG_PACKAGER TIMESTAMP
PKG_EXPORTS += DEPMAKER_EXTRA_ARGS

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

# timestamp - Create a pre-installation timestamp
TIMESTAMP = $(COOKIEDIR)/timestamp
PRE_INSTALL_TARGETS += timestamp
timestamp:
	@echo " ==> Creating timestamp cookie"
	@$(MAKECOOKIE)

remove-timestamp:
	@echo " ==> Removing timestamp cookie"
	@-rm -f $(TIMESTAMP)

# package - Use the mkpackage utility to create Solaris packages
POST_INSTALL_TARGETS += pre-package package-create post-package

# check package, unless ENABLE_CHECK = 0
ifneq ($(ENABLE_CHECK),0)
POST_INSTALL_TARGETS += package-check
endif

package: install
	$(DONADA)
	@$(MAKECOOKIE)

# returns true if package has completed successfully, false otherwise
package-p:
	@$(foreach COOKIEFILE,$(PACKAGE_TARGETS), test -e $(COOKIEDIR)/$(COOKIEFILE) ;)

# Call mkpackage to transmogrify one or more gspecs into packages
package-create:
	@if test "x$(wildcard $(WORKDIR)/*.gspec)" != "x" ; then \
		for spec in `ls -1 $(WORKDIR)/*.gspec` ; do \
			echo " ==> Processing $$spec" ; \
			$(PKG_ENV) mkpackage --spec $$spec \
								 --destdir $(SPKG_EXPORT) \
								 --workdir $(CURDIR)/$(WORKDIR) \
								 --compress \
								 -v basedir=$(DESTDIR) || exit 2 ; \
		done ; \
	else \
		echo " ==> No specs defined for $(GARNAME)" ; \
	fi
	$(DONADA)

# check if the package is blastwave compliant
package-check:
	@echo " ==> Checking blastwave compliance"
	@if test "x$(wildcard $(WORKDIR)/*.gspec)" != "x" ; then \
		for spec in `ls -1 $(WORKDIR)/*.gspec` ; do \
			checkpkg $(SPKG_EXPORT)/`$(PKG_ENV) mkpackage -qs $$spec -D pkgfile`.gz || exit 2 ; \
		done ; \
	fi

# Verify all packages
package-verify: package-check
	@if test "x$(wildcard $(WORKDIR)/*.gspec)" != "x" ; then \
		for spec in `ls -1 $(WORKDIR)/*.gspec` ; do \
			$(PKG_ENV) mkpackage -qs $$spec -D pkgfile >> /tmp/verify.$$ ; \
		done ; \
	fi
	@for file in `cat /tmp/verify.$$` ; do \
		mv $(SPKG_EXPORT)/$$file.gz $(PKGGET_DESTDIR) ; \
		$(MAKE) -C $(PKGGET_DESTDIR)/.. ; \
	done
	@rm -f /tmp/verify.$$

# Install all bitnames from this directory
package-install:
	@if test "x$(wildcard $(WORKDIR)/*.gspec)" != "x" ; then \
		for spec in `ls -1 $(WORKDIR)/*.gspec` ; do \
			$(PKG_ENV) mkpackage -qs $$spec -D bitname >> /tmp/install.$$ ; \
		done ; \
	fi
	echo pkg-get -s $(PKGGET_DESTDIR) -U
	@for bitname in `cat /tmp/install.$$` ; do \
		echo pkg-get -s $(PKGGET_DESTDIR) -f -i $$bitname ; \
	done
	@rm -f /tmp/install.$$

# Reset working directory for repackaging
package-reset:
	@echo " ==> Reset packaging state for $(GARNAME) ($(DESTIMG))"
	@if test -d $(COOKIEDIR) ; then \
		if test -d $(WORKDIR) ; then rm -f $(WORKDIR)/*CSW* ; fi ; \
		rm -f $(COOKIEDIR)/*extract*CSW* \
				  $(COOKIEDIR)/*checksum*CSW* \
					$(COOKIEDIR)/package* ; \
	fi

# Reset and repackage
repackage: package-reset package

# Update the dependency database
dependb:
	@dependb --db $(SPKG_DEPEND_DB) \
             --parent $(CATEGORIES)/$(GARNAME) \
             --add $(DEPENDS)

