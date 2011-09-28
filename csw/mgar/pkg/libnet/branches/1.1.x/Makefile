NAME = libnet
VERSION = 1.1.5
CATEGORIES = lib

DESCRIPTION = The libnet packet construction library
define BLURB
  Libnet is a high-level API (toolkit) allowing the application programmer to
  construct and inject network packets. It provides a portable and simplified
  interface for low-level network packet shaping, handling and injection.
  Libnet hides much of the tedium of packet creation from the application
  programmer such as multiplexing, buffer management, arcane packet header
  information, byte-ordering, OS-dependent issues, and much more.
  Libnet features portable packet creation interfaces at both the IP-layer
  and link-layer, as well as a host of supplementary and complementary
  functionality. 
endef

SF_PROJ = libnet-dev
MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += libnet.so.1.0.2.i
DISTFILES += libnet.so.1.0.2.s
PATCHFILES = 0001-Fix-missing-uint-instead-of-u_int.patch

LICENSE = doc/COPYING

VENDOR_URL = http://github.com/sam-github/libnet

PACKAGES += CSWlibnet
SPKG_DESC_CSWlibnet = Libnet package construction library (legacy), libnet.so
SPKG_VERSION_CSWlibnet = 1.0.2a
PKGFILES_CSWlibnet += $(libdir)/libnet.so
PKGFILES_CSWlibnet += $(libdir)/libnet.so.1.0.2

# These overrides are for the legacy library which should just
# stay the way it is.
CHECKPKG_OVERRIDES_CSWlibnet += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libnet.so
CHECKPKG_OVERRIDES_CSWlibnet += bad-rpath-entry
# CHECKPKG_OVERRIDES_CSWlibnet += bad-rpath-entry|$ORIGIN/../lib|opt/csw/lib/libnet.so.1.0.2
CHECKPKG_OVERRIDES_CSWlibnet += shared-lib-pkgname-mismatch|file=opt/csw/lib/libnet.so.1.0.2|soname=libnet.so.1.0.2|pkgname=CSWlibnet|expected=CSWlibnet1-0-2
CHECKPKG_OVERRIDES_CSWlibnet += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libnet.so

PACKAGES += CSWlibnet1
SPKG_DESC_CSWlibnet1 = Libnet package construction library, libnet.so.1
# Explicitly do *not* include libnet.so.1.0.2
PKGFILES_CSWlibnet1  = $(call baseisadirs,$(libdir),libnet\.so\.1)
PKGFILES_CSWlibnet1 += $(call baseisadirs,$(libdir),libnet\.so\.1\.6(\.\d+)*)

PACKAGES += CSWlibnet-dev
SPKG_DESC_CSWlibnet-dev = Development files for libnet.so.1
# PKGFILES is catchall
# The general layout of CSWlibnet-dev is non-standard. Please see here for a rationale:
#   http://wiki.opencsw.org/project-libnet
RUNTIME_DEP_PKGS_CSWlibnet-dev += CSWlibnet1
OBSOLETED_BY_CSWlibnet-dev += CSWlibnetdevel
CATALOGNAME_CSWlibnetdevel = libnet_devel_stub

BUILD64 = 1

include gar/category.mk

post-install-isa-sparcv8:
	ginstall -d $(DESTDIR)$(libdir)
	cp $(WORKDIR)/libnet.so.1.0.2.s $(DESTDIR)$(libdir)/libnet.so.1.0.2
	rm $(DESTDIR)$(libdir)/libnet.so
	ln -s libnet.so.1.0.2 $(DESTDIR)$(libdir)/libnet.so
	mkdir $(DESTDIR)$(libdir)/libnet-new
	ln -s ../libnet.so.1 $(DESTDIR)$(libdir)/libnet-new/libnet.so
	@$(MAKECOOKIE)

post-install-isa-i386:
	ginstall -d $(DESTDIR)$(libdir)
	cp $(WORKDIR)/libnet.so.1.0.2.i $(DESTDIR)$(libdir)/libnet.so.1.0.2
	rm $(DESTDIR)$(libdir)/libnet.so
	ln -s libnet.so.1.0.2 $(DESTDIR)$(libdir)/libnet.so
	mkdir $(DESTDIR)$(libdir)/libnet-new
	ln -s ../libnet.so.1 $(DESTDIR)$(libdir)/libnet-new/libnet.so
	@$(MAKECOOKIE)
