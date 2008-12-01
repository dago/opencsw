GARNAME = elinks
GARVERSION = 0.11.5
CATEGORIES = net

DESCRIPTION = An advanced text mode web browser
define BLURB
  ELinks is an advanced and well-established feature-rich text mode Web 
  (HTTP, FTP, etc.) browser. It can render both frames and tables, is 
  highly customizable, and can be extended via Lua, Guile, Perl, or Ruby 
  scripts. It has limited support for CSS and Javascript.
endef

MASTER_SITES = http://elinks.cz/download/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWelinks,prototype depend)
DISTFILES += changelog.CSW

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

# suppress the rdynamic test which doesn't
# work correctly
# PATCHFILES = configure_no_rdynamic.patch

# Debian security path for CVE-2007-2027
PATCHFILES += elinks-417789.diff

# we use bash instead of sh as the Makefiles
# use "test -e" unsupported with sun sh
CONFIG_SHELL = /bin/bash

GARCOMPILER = GNU
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-88-colors 
CONFIGURE_ARGS += --enable-256-colors 
# ecma support not stable enough
# CONFIGURE_ARGS += --enable-sm-scripting
CONFIGURE_ARGS += --disable-sm-scripting

TEST_SCRIPTS =

include gar/category.mk

# We touch these file to avoid aclocal/autoconf
# configure to be run again
pre-configure:
	touch $(WORKSRC)/aclocal.m4
	touch $(WORKSRC)/configure
	touch $(WORKSRC)/config.status

post-install:
	@ginstall -D $(WORKDIR)/changelog.CSW $(DESTDIR)$(docdir)/$(GARNAME)/changelog.CSW 

