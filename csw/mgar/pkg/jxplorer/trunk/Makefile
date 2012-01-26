NAME = jxplorer
VERSION = 3.2
CATEGORIES = java
GARTYPE = v2

DESCRIPTION = JXplorer - A Java Ldap Browser
define BLURB
JXplorer is an open source ldap browser originally developed by Computer Associates' eTrust Directory development lab. It is a standards compliant general purpose ldap browser that can be used to read and search any ldap directory, or any X500 directory with an ldap interface. It is available under a standard OSI-style open source licence.
endef

MASTER_SITES += $(SF_MIRRORS)

# DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES  = JXv$(VERSION)deploy.tar.bz2
DISTFILES += $(call admfiles, CSWjxplorer)
DISTFILES += jxconfig.txt.template
DISTFILES += gssapi.conf.template

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=55394
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

PATCHFILES = jxplorer.sh.diff

include gar/category.mk

post-extract:
	( mv $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/$(NAME) $(WORKSRC_FIRSTMOD) )
	@$(MAKECOOKIE)

install-custom:
	@ginstall -d $(DESTDIR)$(bindir)
	@( cd $(DESTDIR)$(bindir) ; \
	   ln -s ../share/jxplorer/jxplorer.sh jxplorer )
	@ginstall -d $(DESTDIR)$(datadir)/$(NAME)
	@ginstall -d $(DESTDIR)$(prefix)/etc/$(NAME)
	@gcp -fpr $(WORKSRC)/* $(DESTDIR)$(datadir)/$(NAME)
	@cp $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/gssapi.conf.template $(DESTDIR)$(prefix)/etc/$(NAME)
	@cp $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/jxconfig.txt.template $(DESTDIR)$(prefix)/etc/$(NAME)
	@rm $(DESTDIR)$(datadir)/$(NAME)/build.xml
	@rm $(DESTDIR)$(datadir)/$(NAME)/jxmac.sh
	@rm $(DESTDIR)$(datadir)/$(NAME)/jxplorer.bat
	@rm $(DESTDIR)$(datadir)/$(NAME)/jxplorer.ico
	@chmod +x $(DESTDIR)$(datadir)/$(NAME)/jxplorer.sh
	@ginstall -d $(DESTDIR)$(datadir)/licences/$(NAME)
	@gcp -fp $(WORKSRC)/licence.txt $(DESTDIR)$(datadir)/licences/$(NAME)
	@( cd $(DESTDIR)$(datadir)/licences/$(NAME) ; \
	   ln -s ../../jxplorer/licence.txt CA_Open_Source_Licence_Version_1.0.txt )
	@$(MAKECOOKIE)
