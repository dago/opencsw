GARNAME = MailScanner
GARVERSION = 4.77.10
RELEASE = 1
DISTVERSION = $(GARVERSION)-$(RELEASE)
#DISTNAME = $(GARNAME)-$(DISTVERSION)
#WORKSRC = $(WORKDIR)/$(DISTNAME)
CATEGORIES = net

DESCRIPTION = A Free Anti-Virus and Anti-Spam Filter
define BLURB
  A Free Anti-Virus and Anti-Spam Filter
endef

MASTER_SITES = http://www.mailscanner.info/files/4/tar/
DISTFILES  = $(GARNAME)-install-$(DISTVERSION).tar.gz

#LICENSE = COPYRIGHT

PACKAGES = CSWmailscanner
CATALOGNAME = mailscanner

#REQUIRED_PKGS = 

#ARCHALL = 1

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-install-(\d+(?:\.\d+)*)-\d+.tar.gz

#CONFIGURE_SCRIPTS = 
#BUILD_SCRIPTS = 
#TEST_SCRIPTS = 
#INSTALL_SCRIPTS = custom

SPKG_SOURCEURL = http://www.mailscanner.info

include gar/category.mk

#SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)

#install-custom:
#	@echo " ==> Installing $(GARNAME) (custom)"
#	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
#	@cp $(FILEDIR)/CSWbind.cswnamed $(DESTDIR)/etc/opt/csw/init.d/cswnamed
#	@cp $(FILEDIR)/CSWbind.named.conf.CSW $(DESTDIR)/etc/opt/csw/named.conf.CSW
#	@ginstall -d $(DESTDIR)/opt/csw/etc/CSWbind
#	@cp $(FILEDIR)/cswusergroup $(DESTDIR)/opt/csw/etc/CSWbind/
#	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
#	@$(foreach DOC,$(DOCLIST),cp $(FILEDIR)/$(DOC) $(DESTDIR)$(docdir)/$(GARNAME);)
#	( cd $(WORKSRC) ; \
#	  gmake DESTDIR=$(DESTDIR) install )
#	@ginstall -d $(DESTDIR)/var/opt/csw/named
#	@touch $(DESTDIR)/var/opt/csw/named/named.pid
#	@$(MAKECOOKIE)
