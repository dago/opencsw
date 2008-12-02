GARNAME = trac
GARVERSION = 0.10.4
CATEGORIES = apps

DESCRIPTION = Integrated SCM and Project Management
define BLURB
	Trac is an enhanced wiki and issue tracking system for software development
	projects. Trac uses a minimalistic approach to web-based software project
	management. Our mission; to help developers write great software while
	staying out of the way. Trac should impose as little as possible on a team's
	established development process and policies.
endef

MASTER_SITES = http://ftp.edgewall.com/pub/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWtrac,depend prototype)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://trac.edgewall.org/wiki/TracDownload

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom
INSTALL_ARGS = --root=$(DESTDIR)

include gar/category.mk

install-custom:
	@echo " ==> Installing $(GARNAME)"
	@( cd $(WORKSRC) ; $(INSTALL_ENV) python ./setup.py install $(INSTALL_ARGS) )
	$(DONADA)

post-install: copy-docs
	$(DONADA)

copy-docs:
	@install -d $(DESTDIR)$(docdir)/trac
	@cp -R $(WORKSRC)/contrib $(DESTDIR)$(docdir)/trac
	@for f in COPYING ChangeLog INSTALL README README.tracd UPGRADE ; do \
		ginstall -m 0644 $(WORKSRC)/$$f $(DESTDIR)$(docdir)/trac ; \
	done

