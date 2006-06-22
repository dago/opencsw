GARNAME = svnmailer
GARVERSION = 1.0.8
CATEGORIES = utils

DESCRIPTION = A tool to post subversion repository information.
define BLURB
  Svnmailer is a tool to post subversion repository commit information by
  mail, news or XML (to a CIA tracker).
endef

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS = 
INSTALL_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_ARGS += --root=$(DESTDIR)

MASTER_SITES = http://storage.perlig.de/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWsvnmailer,depend prototype)

CONFIGURE_ARGS = $(DIRPATHS)

include ../category.mk

post-install:
	@mkdir -p $(DESTDIR)$(docdir)
	@cp -R $(WORKSRC)/docs $(DESTDIR)$(docdir)/$(GARNAME)
	@cp $(WORKSRC)/README $(WORKSRC)/LICENSE $(DESTDIR)$(docdir)/$(GARNAME)
	@$(MAKECOOKIE)
