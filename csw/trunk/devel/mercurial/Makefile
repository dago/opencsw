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

INSTALL_ARGS += --root=$(DESTDIR)

include ../category.mk
