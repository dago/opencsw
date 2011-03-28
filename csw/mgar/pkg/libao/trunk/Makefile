NAME = libao
VERSION = 1.1.0
CATEGORIES = lib

DESCRIPTION = Cross-platform audio library
define BLURB
  libao is a way to easily add cross-platform audio output to your program.
  Output devices are implemented as dynamic plugins, and support for OSS, ESD,
  ALSA, aRTs, Solaris, and Irix outputs are currently supported.
endef

MASTER_SITES = http://downloads.xiph.org/releases/ao/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

VENDOR_URL = http://www.xiph.org/ao/

FOREIGN_PACKAGES += CSWlibao2
OBSOLETED_BY_CSWlibao2 = CSWlibao

PACKAGES += CSWlibao4
CATALOGNAME_CSWlibao4 = libao4
SPKG_DESC_CSWlibao4 = Cross-platform audio library, libao.so.4
PKGFILES_CSWlibao4 += $(call pkgfiles_lib,libao.so.4)
# These are private libraries
PKGFILES_CSWlibao4 += $(call baseisadirs,$(libdir),ao/.*)
PKGFILES_CSWlibao4 += $(sysconfdir)/.*
PKGFILES_CSWlibao4 += $(mandir)/.*
RUNTIME_DEP_PKGS_CSWlibao4 += CSWlibaudiofile0
RUNTIME_DEP_PKGS_CSWlibao4 += CSWlibesd0
OBSOLETED_BY_CSWlibao4 = CSWlibao

PACKAGES += CSWlibao-dev
CATALOGNAME_CSWlibao-dev = libao_dev
SPKG_DESC_CSWlibao-dev = Development files for libao.so.4
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibao-dev = CSWlibao4

# Default is /etc/libao.conf
LIBAO_CONF = $(sysconfdir)/libao.conf
EXTRA_CPPFLAGS = -DAO_SYSTEM_CONFIG=\\\"$(LIBAO_CONF)\\\"

PRESERVECONF = $(LIBAO_CONF)

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

post-install-modulated:
	perl -pi -e 's,/etc/libao.conf,$(LIBAO_CONF),;' \
		$(DESTDIR)$(mandir)/man5/libao.conf.5 \
		$(DESTDIR)$(docdir)/$(DISTNAME)/config.html
	mkdir -p $(DESTDIR)$(dir $(LIBAO_CONF))
	echo "default_driver=sun" > $(DESTDIR)$(LIBAO_CONF).CSW
	@$(MAKECOOKIE)

