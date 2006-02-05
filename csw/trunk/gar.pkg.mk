# vim: ts=4 sw=2 noet
# RCS ID: $Id$
#
# gar.pkg.mk - Build Solaris packages
#

SPKG_REVSTAMP  ?= ,REV=$(shell date '+%Y.%m.%d')
SPKG_DESC      ?= $(DESCRIPTION)
SPKG_VERSION   ?= $(GARVERSION)
SPKG_CATEGORY  ?= application
SPKG_SOURCEURL ?= Unknown
SPKG_PACKAGER  ?= Unknown
SPKG_VENDOR    ?= Unknown
SPKG_EMAIL     ?= Unknown
SPKG_PSTAMP    ?= $(LOGNAME)@$(shell hostname)-$(shell date '+%Y%m%d%H%M%S')
SPKG_BASEDIR   ?= $(prefix)
SPKG_CLASSES   ?= none
SPKG_OSNAME    ?= $(shell uname -s)$(shell uname -r)

SPKG_EXPORT    ?= $(WORKDIR)
SPKG_DEPEND_DB  = $(GARDIR)/csw/depend.db

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
			echo "   ==> Processing $$spec" ; \
			$(PKG_ENV) mkpackage --spec $$spec \
								 --destdir $(SPKG_EXPORT) \
								 --workdir $(WORKDIR) \
								 --compress \
								 -v basedir=$(DESTDIR) || exit 2 ; \
		done ; \
	else \
		echo " ==> No specs defined for $(GARNAME)" ; \
	fi
	$(DONADA)

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

