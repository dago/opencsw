# $Id$
NAME = pacparser
VERSION = 1.3.1
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
DISTFILES  = $(D#PATCHFILES  = 0001-Adjust-Makefile.patch

#PATCHFILES += 0003-Only-GNU-grep-knows-q.patch
#PATCHFILES += 0004-Some-more-Makefile-tweaks.patch
#ile-tweaks.patch
PATCHFILES += 0005-Fix-soname-and-pactester-compilation.patch
PATCHFILES += 0006-Add-flags-to-make-library-self-#PATCHFILES += 0007-Add-config-for-spidermonkey-i386.patch

PATCHFILES += 0001-Add-spidermonkey-config-for-Solaris-10.patch
PATCHFILES += 0002-Do-not-add-Wall-unconditionally.patch
PATCHFILES += 0003-Search-libpacparser.so-in-current-directory-first-do.patch

VENDOR_URL = http://code.google.com/p/pacparser/

PACKAGES += CSWpacparser
SPKG_DESC_CSWpacparser = $(DESCRIPTION)
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWpacparser += CSWlibpacparser1

PACKAGES += CSWlibpacparser1
SPKG_DESC_CSWlibpacparser1 = A library to parse proxy auto-config (PAC) files, libpacparser.so.1
PKGFILES_CSWlibpacparser1 += $(call pkgfiles_lib,libpacparser.so.1)

PACKAGES += CSWlibpacparser-dev
SPKG_DESC_CSWlibpacparser-dev = Development Files for libpacparser.so.1
PKGFILES_CSWlibpacparser-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibpacparser-dev += $(docdir)/pacparser/html/.*
PKGFILES_CSWlibpacparser-dev += .*\.c
RUNTIME_DEP_PKGS_CSWlibpacparser-dev += CSWlibpacparser1
OBSOLETED_BY_CSWlibpacparser-dev += CSWlibpacparser-devel

PACKAGES += CSWpy-libpacparser
SPKG_DESC_CSWpy-libpacparser = Python Bindings for libpacparser
PKGFILES_CSWpy-libpacparser += $(libdir)/python/.*
PKGFILES_CSWpy-libpacparser += .*\.py
RUNTIME_DEP_PKGS_CSWpy-libpacparser += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-libpacparser += CSWpython.com/p/pacparser/

# There is some Python stuff in the package
PYCOMPILE = 1

NOISALIST = 1

CONFIGURE_SCRIPTS =

BUILD_SCRIPTS = $(WORKSRC)/src/Makefile
BUILD_ARGS = all pymod
BUILD_OVERRIDE_VARS = PREFIX
BUILD_OVERRIDE_VAR_PREFIX = $(prefix)

# Tests are run after build# Needed for 'install' during build and install-phase
BUILD_ENV_PATH = /opt/csw/gnu:$(PATH)
INSTALL_ENV_PATH = /opt/csw/gnu:$(PATH)ld
TEST_SCRIPTS =

INSTALL_SCRIPTS = $(WORKSRC)/src/Makefile
INSTALL_ARGS = install install-pymod
INSTALL_OVERRIDE_DIRS = PREFIX
Pinclude gar/category.mk

post-extractextract-modulated:
	@# We have patched something in although the package has not been unpacked.
	@# Make sure it is uncompressed afterwards.
	-cd $(WORKSRC)/src && gtar xzvf spidermonkey/js-?.?.?.tar.gz # $(if $(filter sparc,$(GARCH)),echo "Sparc is fast!!",rm -f $(WORKSRC)/src/spidermonkey/js/src/lock_SunOS.s)
	#@$(MAKECOOKIE)
