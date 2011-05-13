NAME = libntlm
VERSION = 1.2
CATEGORIES = lib

DESCRIPTION = Microsoft WinNT domain authentication library
define BLURB
  libntlm is a library that implement Microsoft's NTLM authentication.
  However, the packaging of libntlm lacked certain things, such as having
  build problems, lacking shared library support, lacking autoconf macro
  for use in other applications, lacking pkg-config support, and more.
  So this page distributes an improved version of the library; called Libntlm.
endef

MASTER_SITES = http://josefsson.org/libntlm/releases/
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://josefsson.org/libntlm/

PACKAGES += CSWlibntlm0
SPKG_DESC_CSWlibntlm0 = Microsoft WinNT domain authentication library, libntlm.so.0
PKGFILES_CSWlibntlm0 = $(call pkgfiles_lib,libntlm.so.0)
OBSOLETED_BY_CSWlibntlm0 = CSWlibntlm

PACKAGES += CSWlibntlm-dev
SPKG_DESC_CSWlibntlm-dev = Development files for libntlm.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibntlm-dev += CSWlibntlm0

# We don't need it and if defined the test breaks
LD_OPTIONS =

BUILD64 = 1

include gar/category.mk
