GARNAME = mercurial
GARVERSION = 0.9.5
CATEGORIES = devel

DESCRIPTION = Fast, lightweight Source Control Management system
#define BLURB
#endef

MASTER_SITES = http://www.selenic.com/mercurial/release
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWmercurial,)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS = 
INSTALL_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_ARGS += --root=$(DESTDIR) --prefix=/opt/csw

include ../category.mk

pre-install:
	mkdir -p $(DESTDIR)/opt/csw/share/man/man1
	mkdir -p $(DESTDIR)/opt/csw/share/man/man5
	mkdir -p $(DESTDIR)/opt/csw/share/doc/mercurial
	cp $(WORKDIR)/$(DISTNAME)/doc/*.1 $(DESTDIR)/opt/csw/share/man/man1
	cp $(WORKDIR)/$(DISTNAME)/doc/*.5 $(DESTDIR)/opt/csw/share/man/man5
	cp -r $(WORKDIR)/$(DISTNAME)/contrib $(DESTDIR)/opt/csw/share/doc/mercurial
	cp -r $(WORKDIR)/$(DISTNAME)/*.cgi $(DESTDIR)/opt/csw/share/doc/mercurial
	rm -rf \
		$(DESTDIR)/opt/csw/share/doc/mercurial/contrib/macosx \
		$(DESTDIR)/opt/csw/share/doc/mercurial/contrib/*rpm* \
		$(DESTDIR)/opt/csw/share/doc/mercurial/contrib/*spec* \
		$(DESTDIR)/opt/csw/share/doc/mercurial/contrib/win32
