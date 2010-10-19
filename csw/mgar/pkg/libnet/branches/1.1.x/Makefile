GARNAME = libnet
GARVERSION = 1.1.2.1
CATEGORIES = lib

DESCRIPTION = The libnet packet construction library
define BLURB
  Libnet is a high-level API (toolkit) allowing the application programmer to construct and inject network packets. It provides a portable and simplified interface for low-level network packet shaping, handling and injection. Libnet hides much of the tedium of packet creation from the application programmer such as multiplexing, buffer management, arcane packet header information, byte-ordering, OS-dependent issues, and much more. Libnet features portable packet creation interfaces at both the IP-layer and link-layer, as well as a host of supplementary and complementary functionality. 
endef

MASTER_SITES = http://www.packetfactory.net/libnet/dist/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

LICENSE = doc/COPYING

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.packetfactory.net/libnet/

BUILD64 = 1

DISTNAME = libnet

PATCHFILES = buildpatch
PATCHFILES += libnet_pblock_coalesce_leak.patch
PATCHFILES += libnet-cq-end-loop.patch
PATCHFILES += libnet_build_ntp.patch
PATCHFILES += libnet_checksum.c.patch

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk

post-extract-$(MODULATION):
	( cp $(FILEDIR)/ltmain.sh $(WORKROOTDIR)/build-$(MODULATION)/$(DISTNAME) ) 
	( cp $(FILEDIR)/libnet.pc.in $(WORKROOTDIR)/build-$(MODULATION)/$(DISTNAME)/src )
	@$(MAKECOOKIE)

post-install-modulated:
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall -m 444 $(WORKDIR)/$(DISTNAME)/libnet-config $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 444 $(WORKDIR)/$(DISTNAME)/doc/BUGS $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 444 $(WORKDIR)/$(DISTNAME)/doc/CHANGELOG $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 444 $(WORKDIR)/$(DISTNAME)/doc/CONTRIB $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 444 $(WORKDIR)/$(DISTNAME)/doc/COPYING $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 444 $(WORKDIR)/$(DISTNAME)/doc/DESIGN_NOTES $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 444 $(WORKDIR)/$(DISTNAME)/doc/MIGRATION $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 444 $(WORKDIR)/$(DISTNAME)/doc/PACKET_BUILDING $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 444 $(WORKDIR)/$(DISTNAME)/doc/PORTED $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 444 $(WORKDIR)/$(DISTNAME)/doc/RAWSOCKET_NON_SEQUITUR $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 444 $(WORKDIR)/$(DISTNAME)/doc/TODO $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -d $(DESTDIR)$(mandir)/man3
	@ginstall -m 444 $(WORKDIR)/$(DISTNAME)/doc/man/man3/libnet-functions.h.3 $(DESTDIR)$(mandir)/man3
	@ginstall -m 444 $(WORKDIR)/$(DISTNAME)/doc/man/man3/libnet-headers.h.3 $(DESTDIR)$(mandir)/man3
	@ginstall -m 444 $(WORKDIR)/$(DISTNAME)/doc/man/man3/libnet-macros.h.3 $(DESTDIR)$(mandir)/man3
	@ginstall -m 444 $(WORKDIR)/$(DISTNAME)/doc/man/man3/libnet.h.3 $(DESTDIR)$(mandir)/man3
	@ginstall -m 444 $(WORKDIR)/$(DISTNAME)/doc/man/man3/libnet_802_1q_hdr.3 $(DESTDIR)$(mandir)/man3
	@ginstall -m 444 $(WORKDIR)/$(DISTNAME)/doc/man/man3/libnet_802_1x_hdr.3 $(DESTDIR)$(mandir)/man3
	@$(MAKECOOKIE)

post-install-isa-sparcv8:
	@ginstall -d $(DESTDIR)$(libdir)
	@cp $(FILEDIR)/libnet.so.1.0.2.s $(INSTALLISADIR)/opt/csw/lib/libnet.so.1.0.2
	@$(MAKECOOKIE)

post-install-isa-i386:
	@ginstall -d $(DESTDIR)$(libdir)
	@cp $(FILEDIR)/libnet.so.1.0.2.i $(INSTALLISADIR)/opt/csw/lib/libnet.so.1.0.2
	@$(MAKECOOKIE)
