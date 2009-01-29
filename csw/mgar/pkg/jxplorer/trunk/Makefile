GARNAME = jxplorer
GARVERSION = 3.2
CATEGORIES = java

DESCRIPTION = JXplorer - A Java Ldap Browser
define BLURB
JXplorer is an open source ldap browser originally developed by Computer Associates' eTrust Directory development lab. It is a standards compliant general purpose ldap browser that can be used to read and search any ldap directory, or any X500 directory with an ldap interface. It is available under a standard OSI-style open source licence.
endef

MASTER_SITES += $(SF_MIRRORS)

# DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES  = JXv$(GARVERSION)deploy.tar.bz2
DISTFILES += $(call admfiles, CSWjxplorer)
DISTFILES += jxconfig.txt.template
DISTFILES += gssapi.conf.template

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=55394
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

PATCHFILES = jxplorer.sh.diff

include gar/category.mk

post-extract:
	( mv $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/$(GARNAME) $(WORKSRC_FIRSTMOD) )
	@$(MAKECOOKIE)

install-custom:
	@ginstall -d $(DESTDIR)$(datadir)/$(GARNAME)
	@ginstall -d $(DESTDIR)$(prefix)/etc/$(GARNAME)
	@gcp -fpr $(WORKSRC)/* $(DESTDIR)$(datadir)/$(GARNAME)
	@cp $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/gssapi.conf.template $(DESTDIR)$(prefix)/etc/$(GARNAME)
	@cp $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/jxconfig.txt.template $(DESTDIR)$(prefix)/etc/$(GARNAME)
	@rm $(DESTDIR)$(datadir)/$(GARNAME)/build.xml
	@rm $(DESTDIR)$(datadir)/$(GARNAME)/jxmac.sh
	@rm $(DESTDIR)$(datadir)/$(GARNAME)/jxplorer.bat
	@rm $(DESTDIR)$(datadir)/$(GARNAME)/jxplorer.ico
	@chmod +x $(DESTDIR)$(datadir)/$(GARNAME)/jxplorer.sh
	@ginstall -d $(DESTDIR)$(datadir)/licences/$(GARNAME)
	@gcp -fp $(WORKSRC)/licence.txt $(DESTDIR)$(datadir)/licences/$(GARNAME)
	@( cd $(DESTDIR)$(datadir)/licences/$(GARNAME) ; \
	   ln -s ../../jxplorer/licence.txt CA_Open_Source_Licence_Version_1.0.txt )
	@$(MAKECOOKIE)
