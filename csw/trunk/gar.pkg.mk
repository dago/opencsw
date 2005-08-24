# CVS ID: $Id: gar.pkg.mk,v 1.6 2004/09/16 17:33:24 comand Exp $
#
# gar.pkg.mk - Build Solaris packages
#

SPKG_REVSTAMP  ?= ,REV=$(shell date '+%Y.%m.%d')
SPKG_DESC      ?= $(DESCRIPTION)
SPKG_VERSION   ?= $(GARVERSION)
SPKG_CATEGORY  ?= application
SPKG_VENDOR    ?= Unknown
SPKG_EMAIL     ?= Unknown
SPKG_PSTAMP    ?= $(LOGNAME)@$(HOSTNAME)-$(shell date '+%Y%m%d%H%M%S')
SPKG_BASEDIR   ?= $(prefix)
SPKG_CLASSES   ?= none
SPKG_OSNAME    ?= $(shell uname -s)$(shell uname -r)

SPKG_TIMESTAMP  = $(COOKIEDIR)/spkg.$(GARNAME)-$(GARVERSION).build_stamp
SPKG_EXPORT    ?= $(WORKDIR)
SPKG_DEPEND_DB  = $(GARDIR)/csw/depend.db

# Is this a full or incremental build?
SPKG_INCREMENTAL ?= 1

PKG_EXPORTS  = GARNAME GARVERSION DESCRIPTION CATEGORIES GARCH GARDIR GARBIN
PKG_EXPORTS += CURDIR WORKDIR WORKSRC
PKG_EXPORTS += SPKG_REVSTAMP SPKG_PKGNAME SPKG_DESC SPKG_VERSION SPKG_CATEGORY
PKG_EXPORTS += SPKG_VENDOR SPKG_EMAIL SPKG_PSTAMP SPKG_BASEDIR SPKG_CLASSES
PKG_EXPORTS += SPKG_OSNAME SPKG_TIMESTAMP

PKG_ENV  = $(BUILD_ENV)
PKG_ENV += $(foreach EXP,$(PKG_EXPORTS),$(EXP)="$($(EXP))")

# Target for timestamping
pre-package-timestamp: $(SPKG_TIMESTAMP)
	@$(MAKECOOKIE)
	$(DONADA)

# Call mkpackage for the package step
package:
	@if test "x$(wildcard $(WORKDIR)/*.gspec)" != "x" ; then \
		for spec in `ls -1 $(WORKDIR)/*.gspec` ; do \
			echo "   ==> Processing $$spec" ; \
			$(PKG_ENV) mkpackage --spec $$spec \
								 --destdir $(SPKG_EXPORT) \
								 --workdir $(WORKDIR) \
								 --basedir $(DESTDIR)/ \
								 --nooverwrite ; \
		done ; \
	else \
		echo " ==> No specs defined for $(GARNAME)" ; \
	fi
	$(DONADA)

dependb:
	@dependb --db $(SPKG_DEPEND_DB) \
             --parent $(CATEGORIES)/$(GARNAME) \
             --add $(DEPENDS)

CLEAN_TARGETS += stamp
clean-stamp:
	@echo " ==> Removing $(SPKG_TIMESTAMP)"
	@rm -f $(SPKG_TIMESTAMP)
