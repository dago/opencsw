NAME = svnmailer
VERSION = 1.1.0
GARSVNREV  = r1373
GARRELEASE = dev-$(GARSVNREV)
GARTYPE = v1
CATEGORIES = utils

DESCRIPTION = A tool to post subversion repository information.
define BLURB
  Svnmailer is a tool to post subversion repository commit information by
  mail, news or XML (to a CIA tracker).
endef

DISTNAME = $(NAME)-$(VERSION)-$(GARRELEASE)
WORKSRC = $(WORKDIR)/$(DISTNAME)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS = 
INSTALL_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_ARGS += --root=$(DESTDIR)

MASTER_SITES = http://storage.perlig.de/$(NAME)/
DISTFILES  = $(DISTNAME).tar.bz2
DISTFILES += $(call admfiles,CSWsvnmailer,depend)

# Fix doc install paths
PATCHFILES += install-doc.diff

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_$(GARSVNREV)
