NAME = libnet
VERSION = 1.1.6
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
DISTFILES  = $(DISTNAME).tar.gz

LICENSE = doc/COPYING

VENDOR_URL = http://github.com/sam-github/libnet

PACKAGES += CSWlibnet1
SPKG_DESC_CSWlibnet1 = Libnet package construction library, libnet.so.1
# Explicitly do *not* include libnet.so.1.0.2
PKGFILES_CSWlibnet1  = $(call pkgfiles_lib,libnet.so.1)

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
	mkdir $(DESTDIR)$(libdir)/libnet-new
	ln -s ../libnet.so.1 $(DESTDIR)$(libdir)/libnet-new/libnet.so
	rm -f $(DESTDIR)$(libdir)/libnet.so
	@$(MAKECOOKIE)

post-install-isa-i386:
	ginstall -d $(DESTDIR)$(libdir)
	mkdir $(DESTDIR)$(libdir)/libnet-new
	ln -s ../libnet.so.1 $(DESTDIR)$(libdir)/libnet-new/libnet.so
	rm -f $(DESTDIR)$(libdir)/libnet.so
	@$(MAKECOOKIE)
