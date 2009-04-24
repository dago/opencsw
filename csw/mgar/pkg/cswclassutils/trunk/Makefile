GARNAME = cswclassutils
GARVERSION = 1.9
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

CASLIST = cswcpsampleconf cswpreserveconf cswinitsmf cswusergroup

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
	@cp $(FILEDIR)/CSW$(GARNAME).copyright $(DESTDIR)$(docdir)/$(GARNAME)/license
	@$(foreach CAS,$(CASLIST),cp $(FILEDIR)/CSW$(GARNAME).i.$(CAS) $(DESTDIR)/usr/sadm/install/scripts/i.$(CAS);cp $(FILEDIR)/CSW$(GARNAME).r.$(CAS) $(DESTDIR)/usr/sadm/install/scripts/r.$(CAS);)
	@$(MAKECOOKIE)
