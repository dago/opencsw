NAME        = remake
VERSION     = 3.82+dbg0.8
CATEGORIES  = devel

DESCRIPTION = GNU Make debugger
define BLURB
  remake is a patched and modernized version of GNU make utility that adds
  improved error reporting, the ability to trace execution in a comprehensible
  way, and a debugger.
endef

MASTER_SITES   = http://cloud.github.com/downloads/rocky/remake/
DISTFILES      = $(NAME)-$(VERSION).tar.bz2
SPKG_SOURCEURL = http://bashdb.sourceforge.net/remake/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX   = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

# FIXME: having errors while compiling with Solaris Studio
# FIXME: looks like GCC4 is broken in testing (fallback to GCC3)
GARCOMPILER       = GCC3
BUILD_DEP_PKGS   += CSWgcc3core
BUILD_DEP_PKGS   += CSWggettext-dev
BUILD_DEP_PKGS   += CSWlibiconv-dev
BUILD_DEP_PKGS   += CSWlibncurses-dev
BUILD_DEP_PKGS   += CSWlibreadline-dev

RUNTIME_DEP_PKGS += CSWlibiconv2
RUNTIME_DEP_PKGS += CSWlibintl8
RUNTIME_DEP_PKGS += CSWlibncurses5
RUNTIME_DEP_PKGS += CSWlibreadline6

CONFIGURE_ARGS    = $(DIRPATHS)

include gar/category.mk
