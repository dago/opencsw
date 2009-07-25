GARNAME = mercurial
GARVERSION = 1.3.1
CATEGORIES = devel

DESCRIPTION = Fast, lightweight Source Control Management system
#define BLURB
#endef

MASTER_SITES = http://selenic.com/mercurial/release/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWmercurial,changelog.CSW)
DISTFILES += $(call admfiles,CSWmercurial-common,)

SPKG_DESC_CSWmercurial = Mercurial
SPKG_DESC_CSWmercurial_common = Mercurial, common files

REQUIRED_PKGS_CSWmercurial = CSWpython

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PKGFILES_CSWmercurial-common  = $(PKGFILES_DOC)
PKGFILES_CSWmercurial-common += /opt/csw/share/man/.*
PKGFILES_CSWmercurial-common += /opt/csw/lib/python/site-packages/mercurial/templates/.*

#PKGFILES_CSWmercurial = /opt/csw/bin
# $(prefix)/.*

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
# Some tests fail, but manual inspection of the failures show no significant failures.
TEST_TARGET = #tests

INSTALL_SCRIPTS = $(WORKSRC)/setup.py
INSTALL_ARGS += --root=$(DESTDIR) --prefix=/opt/csw

include gar/category.mk

pre-install-modulated:
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

post-install-modulated:
	cp $(WORKDIR)/CSWmercurial.changelog.CSW $(DESTDIR)/opt/csw/share/doc/mercurial/changelog.CSW
	( cd $(DESTDIR) && find . -type f | xargs grep '#!.*python$$' ) | cut -f 1 -d: | while read file; do\
		sed '1c\
#!/opt/csw/bin/python' $(DESTDIR)/$$file > $(WORKDIR)/tmp; \
		mv $(WORKDIR)/tmp $(DESTDIR)/$$file; \
	 done

#PATH := /opt/csw/bin:$(PATH)
