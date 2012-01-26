# $Id$
NAME = pacparser
VERSION = 1.2.7
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A library to parse proxy auto-config (PAC) files
define BLURB
  pacparser is a library to parse proxy auto-config (PAC) files. Proxy auto-config
  files are a vastly used proxy configuration method these days. Web browsers can
  use a PAC file to determine which proxy server to use or whether to go direct for
  a given URL. PAC files are written in JavaScript and can be programmed to return
  different proxy methods (e.g. "PROXY proxy1:port; DIRECT") depending upon URL,
  source IP address, protocol, time of the day etc. PAC files introduce a lot of
  possibilities. Look at the wikipedia link above to find out more about them.
endef

MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES  = 0001-Adjust-Makefile.patch

PATCHFILES += 0003-Only-GNU-grep-knows-q.patch
PATCHFILES += 0004-Some-more-Makefile-tweaks.patch
PATCHFILES += 0005-Fix-soname-and-pactester-compilation.patch
PATCHFILES += 0006-Add-flags-to-make-library-self-sufficient.patch
PATCHFILES += 0007-Add-config-for-spidermonkey-i386.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWpacparser CSWlibpacparser1 CSWlibpacparser-devel CSWpy-libpacparser
CATALOGNAME_CSWpacparser = pacparser
CATALOGNAME_CSWlibpacparser1 = libpacparser1
CATALOGNAME_CSWlibpacparser-devel = libpacparser_devel
CATALOGNAME_CSWpy-libpacparser = py_libpacparser

SPKG_DESC_CSWpacparser = $(DESCRIPTION)
SPKG_DESC_CSWlibpacparser1 = Library libpacparser.so.1
SPKG_DESC_CSWlibpacparser-devel = Development Files for libpacparser.so
SPKG_DESC_CSWpy-libpacparser = Python Bindings for libpacparser

RUNTIME_DEP_PKGS_CSWpacparser = CSWlibpacparser1
RUNTIME_DEP_PKGS_CSWlibpacparser-devel = CSWlibpacparser1
RUNTIME_DEP_PKGS_CSWpy-libpacparser = CSWlibpython2-6-1-0 CSWpython

VENDOR_URL = http://code.google.com/p/pacparser/

# There is some Python stuff in the package
PYCOMPILE = 1

NOISALIST = 1

CONFIGURE_SCRIPTS =

BUILD_SCRIPTS = $(WORKSRC)/src/Makefile
BUILD_ARGS = all pymod
BUILD_OVERRIDE_VARS = PREFIX
BUILD_OVERRIDE_VAR_PREFIX = $(prefix)

# Tests are run after build
TEST_SCRIPTS =

INSTALL_SCRIPTS = $(WORKSRC)/src/Makefile
INSTALL_ARGS = install install-pymod
INSTALL_OVERRIDE_DIRS = PREFIX
PREFIX=$(prefix)

PKGFILES_CSWlibpacparser1 = $(PKGFILES_RT)
PKGFILES_CSWlibpacparser-devel  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibpacparser-devel += $(docdir)/pacparser/html/.*
PKGFILES_CSWlibpacparser-devel += .*\.c
PKGFILES_CSWpy-libpacparser  = $(libdir)/python/.*
PKGFILES_CSWpy-libpacparser += .*\.py

include gar/category.mk

# Needed for 'install' during install-phase
PATH := /opt/csw/gnu:$(PATH)

post-extract-modulated:
	@# We have patched something in although the package has not been unpacked.
	@# Make sure it is uncompressed afterwards.
	-cd $(WORKSRC)/src && gtar xzvf spidermonkey/js-?.?.?.tar.gz -C spidermonkey
	$(if $(filter sparc,$(GARCH)),echo "Sparc is fast!!",rm -f $(WORKSRC)/src/spidermonkey/js/src/lock_SunOS.s)
	@$(MAKECOOKIE)
