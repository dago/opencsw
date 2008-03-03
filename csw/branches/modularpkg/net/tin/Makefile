GARNAME = tin
GARVERSION = 1.8.3
CATEGORIES = net

DESCRIPTION = terminal-based news reader
define BLURB
  tin is an easy-to-use USENET news reader for the console using NNTP.
  It supports threading, scoring, different charsets, and many other
  useful things. It has also support for different languages.
endef

MASTER_SITES = ftp://ftp.tin.org/pub/news/clients/tin/stable/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWtin,prototype depend)

PATCHFILES = configure.patch

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-coffee
CONFIGURE_ARGS += --enable-ipv6 --enable-curses
CONFIGURE_ARGS += --x-includes=/usr/openwin/include
CONFIGURE_ARGS += --x-libraries=/usr/openwin/lib 
CONFIGURE_ARGS += --with-x --with-Xaw3d

# tin requires to run 'make build'
BUILD_ARGS = build

# tin doesn't have a test target
TEST_TARGET =

include ../category.mk

post-install:
	/usr/ccs/bin/strip $(DESTDIR)$(prefix)/bin/tin
	/usr/ccs/bin/mcs -d $(DESTDIR)$(prefix)/bin/tin
