GARNAME = git
GARVERSION = 1.5.4.2
CATEGORIES = devel

DESCRIPTION = Fast Version Control System
define BLURB
  Git is a popular version control system designed to handle
  very large projects with speed and efficiency; it is used
  mainly for various open source projects, most notably the Linux kernel.
endef

MASTER_SITES = http://kernel.org/pub/software/scm/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWgit,)

#CONFIGURE_SCRIPTS =
#BUILD_SCRIPTS = $(WORKSRC)/setup.py
#TEST_SCRIPTS = 
#INSTALL_SCRIPTS = $(WORKSRC)/setup.py

#INSTALL_ARGS += --root=$(DESTDIR)

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
