GARNAME = opera
GARVERSION = 9.62
CATEGORIES = apps

DESCRIPTION = Full-featured, standards-compliant browser
define BLURB
  The most full-featured Internet power tool on the market, Opera includes
  pop-up blocking, tabbed browsing, integrated searches, and advanced functions
  like Opera's groundbreaking E-mail program, RSS Newsfeeds and IRC chat
endef

PACKAGES = CSWopera
CATALOGNAME = opera

MASTER_SITES = http://www.opera.com/
DISTFILES  = $(GARNAME)-$(GARVERSION).gcc3-static-qt3.tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PATCHFILES += bin-opera.diff

WORKSRC = $(WORKDIR)/$(DISTNAME)-2466.gcc3-static-qt3

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

install-custom:
	echo " ==> Installing $(GARNAME)"
	ginstall -d $(DESTDIR)$(prefix)/etc
	cp -r $(WORKSRC)/etc/* $(DESTDIR)$(prefix)/etc
	ginstall -d $(DESTDIR)$(prefix)/lib
	cp -r $(WORKSRC)/lib/* $(DESTDIR)$(prefix)/lib
	ginstall -d $(DESTDIR)$(prefix)/share
	cp -r $(WORKSRC)/share/* $(DESTDIR)$(prefix)/share
	ginstall -d $(DESTDIR)$(prefix)/bin
	ginstall -m 755 $(WORKSRC)/opera $(DESTDIR)$(prefix)/bin

include gar/category.mk
