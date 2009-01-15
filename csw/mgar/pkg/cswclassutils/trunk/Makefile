GARNAME = cswclassutils
GARVERSION = 1.3
CATEGORIES = utils

DESCRIPTION = CSW class action utilities

MASTER_SITES = 
DISTFILES += $(call admfiles,CSWcswclassutils,prototype)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

WORKSRC = $(WORKDIR)
SPKG_SOURCEURL = http://www.opencsw.org

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@rm -rf $(DESTDIR)
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -d $(DESTDIR)/usr/sadm/install/scripts
	@ginstall -d $(DESTDIR)/var/opt/csw/svc/manifest
	@ginstall -d $(DESTDIR)/var/opt/csw/svc/method
	@cp $(FILEDIR)/CSW$(GARNAME).csw.smf.sample $(DESTDIR)/etc/opt/csw/init.d/csw.smf.sample
	@cp $(FILEDIR)/CSW$(GARNAME).README.CSW $(DESTDIR)$(docdir)/$(GARNAME)/README.CSW
	@cp $(FILEDIR)/CSW$(GARNAME).copyright $(DESTDIR)$(docdir)/$(GARNAME)/LICENSE
	@cp $(FILEDIR)/CSW$(GARNAME).i.cswcpsampleconf $(DESTDIR)/usr/sadm/install/scripts/i.cswcpsampleconf
	@cp $(FILEDIR)/CSW$(GARNAME).r.cswcpsampleconf $(DESTDIR)/usr/sadm/install/scripts/r.cswcpsampleconf
	@cp $(FILEDIR)/CSW$(GARNAME).i.cswpreserveconf $(DESTDIR)/usr/sadm/install/scripts/i.cswpreserveconf
	@cp $(FILEDIR)/CSW$(GARNAME).r.cswpreserveconf $(DESTDIR)/usr/sadm/install/scripts/r.cswpreserveconf
	@cp $(FILEDIR)/CSW$(GARNAME).i.cswinitsmf $(DESTDIR)/usr/sadm/install/scripts/i.cswinitsmf
	@cp $(FILEDIR)/CSW$(GARNAME).r.cswinitsmf $(DESTDIR)/usr/sadm/install/scripts/r.cswinitsmf
	@$(MAKECOOKIE)
