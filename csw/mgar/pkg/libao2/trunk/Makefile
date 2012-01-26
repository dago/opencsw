NAME = libao
VERSION = 0.8.8
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Cross-platform audio library
define BLURB
  libao is a way to easily add cross-platform audio output to your program.
  Output devices are implemented as dynamic plugins, and support for OSS, ESD,
  ALSA, aRTs, Solaris, and Irix outputs are currently supported.
endef

MASTER_SITES = http://downloads.xiph.org/releases/ao/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

VENDOR_URL = http://www.xiph.org/ao/

PACKAGES += CSWlibao2
CATALOGNAME_CSWlibao2 = libao2
SPKG_DESC_CSWlibao2 = Cross-platform audio library, libao.so.2
PKGFILES_CSWlibao2 += $(call pkgfiles_lib,libao.so.2)
# These are private libraries
PKGFILES_CSWlibao2 += $(call baseisadirs,$(libdir),ao/.*)
RUNTIME_DEP_PKGS_CSWlibao2 += CSWlibesd0

# Default is /etc/libao.conf
LIBAO_CONF = $(sysconfdir)/libao.conf
EXTRA_CPPFLAGS = -DAO_SYSTEM_CONFIG=\\\"$(LIBAO_CONF)\\\"

# The file libao.conf is delivered with the newer libao4

BUILD64_LIBS_ONLY = 1

include gar/category.mk
