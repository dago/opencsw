# $Id$
GARNAME = adobereader
GARVERSION = 9.3.4
CATEGORIES = apps

DESCRIPTION = Adobe Acrobat Reader
define BLURB
  Long description
endef

MASTER_SITES = ftp://ftp.adobe.com/pub/adobe/reader/unix/9.x/$(GARVERSION)/enu/
DISTFILES  = AdbeRdr$(GARVERSION)-1_i486solaris_enu.tar.bz2
DISTNAME = AdobeReader

# File name regex to get notifications about upstream software releases
# UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

LICENSE = AdobeReader/ReadMe.htm

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(sharedstatedir)
	cd $(WORKSRC) && ./INSTALL --install_path=$(DESTDIR)$(sharedstatedir)
	ginstall -d $(DESTDIR)$(bindir)
	ln -s ../share/Adobe/Reader9/bin/acroread $(DESTDIR)$(bindir)/acroread
	@$(MAKECOOKIE)
