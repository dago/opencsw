GARNAME = clearsilver
GARVERSION = 0.10.4
CATEGORIES = utils

DESCRIPTION = Language-neutral HTML template system
define BLURB
  Clearsilver is a fast, powerful, and language-neutral HTML template system.
  In both static content sites and dynamic HTML applications, it provides a
  separation between presentation code and application logic which makes
  working with your project easier.
endef

MASTER_SITES = http://www.clearsilver.net/downloads/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWcs,depend prototype)
DISTFILES += $(call admfiles,CSWpmcs,depend prototype)
DISTFILES += $(call admfiles,CSWpycs,depend prototype)

# Remove an unneeded linux-only header
PATCHFILES += linuxheader.diff

# Use vendor install for the perl module
PATCHFILES += perlbuild.diff

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-python=$(bindir)/python
CONFIGURE_ARGS += --with-perl=$(bindir)/perl
#CONFIGURE_ARGS += --with-ruby=$(bindir)/ruby
#CONFIGURE_ARGS += --with-java=/usr/jdk/j2se1.4.2_02/j2se
CONFIGURE_ARGS += --enable-gettext

# No c-sharp at the moment
CONFIGURE_ARGS += --disable-csharp
# Module requires apache 1.3.x
CONFIGURE_ARGS += --disable-apache
CONFIGURE_ARGS += --disable-ruby
CONFIGURE_ARGS += --disable-java

# No test target
TEST_SCRIPTS =

include ../category.mk

# The perl binding needs to use the Sun compiler, regardless of whether the
# main extension uses gcc.
ifeq ($(GARCOMPILER),GNU)
PATH := $(PATH):$(SUN_CC_HOME)/bin
export PATH
endif

LIBS += -lintl
export LIBS

