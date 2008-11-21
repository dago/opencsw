GARNAME = memconf
GARVERSION = 2.9
CATEGORIES = utils

DESCRIPTION = perl script that displays memory modules installed
define BLURB
	memconf reports the size of each SIMM/DIMM memory module installed in
	a system. It also reports the system type and any empty memory sockets.
endef

MASTER_SITES = http://myweb.cableone.net/4schmidts/unix/
DISTFILES  = $(GARNAME).gz
DISTFILES += memconf.man
DISTFILES += $(call admfiles,CSWmemconf,)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include ../category.mk

WORKSRC = $(WORKDIR)
SPKG_SOURCEURL = http://www.4schmidts.com/memconf.html

install-custom:
	@echo " ==> Installing $(GARNAME)"
	@rm -rf $(DESTDIR)
	@ginstall -d $(DESTDIR)/opt/csw/bin
	@ginstall -d $(DESTDIR)/opt/csw/share/doc/memconf
	@ginstall -d $(DESTDIR)$(mandir)/man1
	@cp -r $(WORKSRC)/$(GARNAME) $(DESTDIR)/opt/csw/bin/$(GARNAME)
	@cp -r $(WORKSRC)/$(GARNAME).man $(DESTDIR)$(mandir)/man1/$(GARNAME).1
	@cp -r $(FILEDIR)/CSW$(GARNAME).copyright $(DESTDIR)/opt/csw/share/doc/$(GARNAME)/LICENSE
	@chmod 755 $(DESTDIR)/opt/csw/bin/$(GARNAME)
	@chmod 644 $(DESTDIR)$(mandir)/man1/$(GARNAME).1
	@chmod 444 $(DESTDIR)/opt/csw/share/doc/$(GARNAME)/LICENSE
	@$(MAKECOOKIE)
