GARNAME = mercurial
GARVERSION = 1.0
CATEGORIES = devel

DESCRIPTION = Fast, lightweight Source Control Management system
#define BLURB
#endef

MASTER_SITES = http://www.selenic.com/mercurial/release
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWmercurial,prototype changelog.CSW)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_TARGET =
# Can't get the tests to pass properly
#TEST_TARGET = tests
# TESTFLAGS is used by ./run-tests.py
TESTFLAGS = -p 6666
export TESTFLAGS
INSTALL_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_ARGS += --root=$(DESTDIR) --prefix=/opt/csw

include gar/category.mk

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

post-install:
	cp $(WORKDIR)/CSWmercurial.changelog.CSW $(DESTDIR)/opt/csw/share/doc/mercurial/changelog.CSW
	( cd $(DESTDIR) && find . -type f | xargs grep '#!.*python$$' ) | cut -f 1 -d: | while read file; do\
		sed '1c\
#!/opt/csw/bin/python' $(DESTDIR)/$$file > $(WORKDIR)/tmp; \
		mv $(WORKDIR)/tmp $(DESTDIR)/$$file; \
	 done

PATH := /opt/csw/bin:$(PATH)
