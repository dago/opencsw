NAME = resiprocate
VERSION = 1.8.5
CATEGORIES = utils

MASTER_SITES = https://www.resiprocate.org/files/pub/reSIProcate/releases/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

#PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

DESCRIPTION = full-featured reference implementation of SIP in C++
define BLURB
  reSIProcate is a library that aims to fully implement the SIP protocol
  in first class C++.  It is intended for use in other applications,
  such as the repro SIP proxy.
endef

DISTFILES  = $(DISTNAME).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --disable-nls
CONFIGURE_ARGS += --with-ssl
#CONFIGURE_ARGS += --enable-ipv6
CONFIGURE_ARGS += --with-c-ares

BDB_HOME = $(prefix)/bdb48
EXTRA_LIB = $(BDB_HOME)/lib 
EXTRA_INC = $(BDB_HOME)/include

# There are multiple test suites, regular `make check' and tfm
TEST_SCRIPTS = check

include gar/category.mk
