NAME        = remake
VERSION     = 3.82+dbg0.8
CATEGORIES  = devel
GARTYPE = v2

DESCRIPTION = GNU Make debugger
define BLURB
  remake is a patched and modernized version of GNU make utility that adds
  improved error reporting, the ability to trace execution in a comprehensible
  way, and a debugger.
endef

MASTER_SITES   = http://github.com/downloads/rocky/remake/
DISTFILES      = $(NAME)-$(VERSION).tar.gz
VENDOR_URL     = http://bashdb.sourceforge.net/remake/

# FIXME: having errors while compiling with Solaris Studio
GARCOMPILER       = GNU
BUILD_DEP_PKGS   += CSWgcc4core 

BUILD_DEP_PKGS   += CSWggettext-dev
BUILD_DEP_PKGS   += CSWlibiconv-dev
BUILD_DEP_PKGS   += CSWlibncurses-dev
BUILD_DEP_PKGS   += CSWlibreadline-dev

# These are fallback pathes _after_ /opt/csw/include
CHECKPKG_OVERRIDES_CSWremake += file-with-bad-content|/usr/local|root/opt/csw/share/info/remake.info
CHECKPKG_OVERRIDES_CSWremake += file-with-bad-content|/usr/local|root/opt/csw/bin/remake

RUNTIME_DEP_PKGS_CSWremake += CSWlibintl8
RUNTIME_DEP_PKGS_CSWremake += CSWlibreadline6

CONFIGURE_ARGS += $(DIRPATHS)
# Not done yet
# CONFIGURE_ARGS += --with-customs=$(prefix)
CONFIGURE_ARGS += --without-customs

include gar/category.mk

#post-extract-modulated:
#	if test -d $(WORKSRC); then cd $(WORKSRC) && ./autogen.sh; fi
#	@$(MAKECOOKIE)
