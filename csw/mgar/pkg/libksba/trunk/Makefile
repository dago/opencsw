NAME = libksba
VERSION = 1.3.0
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Libksba is a CMS and X.509 access library
define BLURB
  Libksba is a library to make the tasks of working with X.509 certificates,
  CMS data and related objects more easy. It provides a highlevel interface
  to the implemented protocols and presents the data in a consistent way.
  There is no more need to worry about all the nasty details of the protocols. 
endef

MASTER_SITES = ftp://ftp.gnupg.org/gcrypt/libksba/
DISTFILES = $(DISTNAME).tar.bz2

VENDOR_URL = http://www.gnupg.org/related_software/libksba/

PACKAGES += CSWlibksba8
SPKG_DESC_CSWlibksba8 = CMS and X.509 access library, libksba.so.8
PKGFILES_CSWlibksba8 = $(call pkgfiles_lib,libksba.so.8)
RUNTIME_DEP_PKGS_CSWlibksba8 += CSWlibgpg-error0
OBSOLETED_BY_CSWlibksba8 += CSWlibksba

PACKAGES += CSWlibksba-dev
SPKG_DESC_CSWlibksba-dev = Development files for libksba.so.8
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibksba-dev += CSWlibksba8

BUILD64_LIBS_ONLY = 1

include gar/category.mk
