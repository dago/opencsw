# $HeadURL$

GARNAME = cswclassutils
GARVERSION = 1.42
CATEGORIES = utils

DESCRIPTION = CSW class action utilities

MASTER_SITES =
DISTFILES = COPYING

ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

SPKG_SOURCEURL = http://www.opencsw.org

CASFILES = $(wildcard $(FILEDIR)/CSW$(GARNAME).[ir].*)
CASLIST = $(foreach F,$(CASFILES), $(subst $(FILEDIR)/CSW$(GARNAME).,,$(F)))
DISTFILES += $(subst $(FILEDIR)/,,$(CASFILES))

PROTOTYPE_MODIFIERS = cas
PROTOTYPE_FILES_cas = /usr/sadm/install/scripts/.*
PROTOTYPE_USER_cas = bin
PROTOTYPE_GROUP_cas = sys

CHECKPKG_OVERRIDES_CSWcswclassutils += init-file-missing-cswinitsmf-class
CHECKPKG_OVERRIDES_CSWcswclassutils += init-file-wrong-location
CHECKPKG_OVERRIDES_CSWcswclassutils += init-file-wrong-location|/opt/csw/etc/init.d/csw.smf.sample

include gar/category.mk

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@rm -rf $(DESTDIR)
	@ginstall -m 0755 -d $(DESTDIR)/opt/csw/etc/init.d
	@ginstall -m 0755 -d $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 0755 -d $(DESTDIR)/usr/sadm/install/scripts
	@ginstall -m 0755 -d $(DESTDIR)/var/opt/csw/svc/manifest
	@ginstall -m 0755 -d $(DESTDIR)/var/opt/csw/svc/method
	@ginstall -m 0755 -d $(DESTDIR)/var/opt/csw/cswclassutils
	@ginstall -m 0755 $(FILEDIR)/CSW$(GARNAME).csw.smf.sample $(DESTDIR)/opt/csw/etc/init.d/csw.smf.sample
	@ginstall -m 0444 $(FILEDIR)/CSW$(GARNAME).README.CSW $(DESTDIR)$(docdir)/$(GARNAME)/README.CSW
	@$(foreach CAS,$(CASLIST),ginstall -m 0555 $(FILEDIR)/CSW$(GARNAME).$(CAS) $(DESTDIR)/usr/sadm/install/scripts/$(CAS);)
	@$(MAKECOOKIE)
