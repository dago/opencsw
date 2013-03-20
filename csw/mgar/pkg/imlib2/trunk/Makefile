NAME = imlib2
VERSION = 1.4.5
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Imlib 2 is the successor to Imlib, a powerful graphics library
define BLURB
  Imlib 2 is the successor to Imlib. It is NOT a newer version -- it is a completely new library.
  Imlib 2 can be installed alongside Imlib 1.x without any problems since they are effectively
  different libraries which have very similar functionality. Please see the homepage for the
  long description of the differenceECTs.
endef

SF_PROJ = enlightenment
MASTER_SITES = $(SF_MI+= $(NAME)-$(VERSION).tar.bz2

PATCHFILES += 0001-Make-sure-we-have-XK_q.patch

BUILD_DEP_PKGS += CSWlibbz2-dev
BUILD_DEP_PKGS += CSWlibpng-dev
BUILD_DEP_PKGS += CSWlibz-dev
BUILD_DEP_PKGS += CSWlibid3-dev
BUILD_DEP_PKGS += CSWlibfreetype-dev
BUILD_DEP_PKGS += CSWlibtiff-dev
BUILD_DEP_PKGS += CSWlibjpeg-dev
BUILD_DEP_PKGS += CSWlibgif-dev

PACKAGES += CSWlibimlib2-1
SPKG_DESC_CSWlibimlib2-1 = A powerful graphics library, libImlib2.so.1
PKGFILES_CSWlibimlib2-1 += $(call pkgfiles_lib,libImlib2.so.1)
PKGFILES_CSWlibimlib2-1 += $(call baseisadirs,$(libdir),imlib2/.*)
PKGFILES_CSWlibimlib2-1 += $(sharedstatedir)/imlib2/.*
RUNTIME_DEP_PKGS_CSWlibimlib2-1 += CSWlibbz2-1-0
RUNTIME_DEP_PKGS_CSWlibimlib2-1 += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWlibimlib2-1 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibimlib2-1 += CSWlibid3tag
RUNTIME_DEP_PKGS_CSWlibimlib2-1 += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWlibimlib2-1 += CSWlibtiff3
RUNTIME_DEP_PKGS_CSWlibimlib2-1 += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWlibimlib2-1 += CSWlibgif4

# This path is in addition to the correct /usr/openwin/lib/X11/rgb.txt
CHECKPKG_OVERRIDES_CSWlibimlib2-1 += file-with-bad-content|/usr/share|root/opt/csw/lib/imlib2/loaders/xpm.so
CHECKPKG_OVERRIDES_CSWlibimlib2-1 += file-with-bad-content|/usr/share|root/opt/csw/lib/sparcv9/imlib2/loaders/xpm.so
CHECKPKG_OVERRIDES_CSWlibimlib2-1 += file-with-bad-content|/usr/share|root/opt/csw/lib/amd64/imlib2/loaders/xpm.so

PACKAGES += CSWlibimlib2-dev
SPKG_DESC_CSWlibimlib2-dev = Development files for libImlib2.so.1
PKGFILES_CSWlibimlib2-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibimlib2-dev += CSWlibimlib2-1

PACKAGES += CSWimlib2
SPKG_DESC_CSWimlib2 = Imlib2 tools
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWimlib2 += CSWlibimlib2-1

BUILD64 = 1
ISAEXEC = 1

# giflib needs this for stdbool.h
#EXTRA_CFLAGS += -xc99
EXTRA_CPPFLAGS += -xc99

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
