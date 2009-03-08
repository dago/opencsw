GARNAME = libnet
GARVERSION = 1.1.2.1
CATEGORIES = lib

DESCRIPTION = The libnet packet construction library
define BLURB
  Libnet is a high-level API (toolkit) allowing the application programmer to construct and inject network packets. It provides a portable and simplified interface for low-level network packet shaping, handling and injection. Libnet hides much of the tedium of packet creation from the application programmer such as multiplexing, buffer management, arcane packet header information, byte-ordering, OS-dependent issues, and much more. Libnet features portable packet creation interfaces at both the IP-layer and link-layer, as well as a host of supplementary and complementary functionality. 
endef

MASTER_SITES = http://www.packetfactory.net/libnet/dist/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibnet,)

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.packetfactory.net/libnet/

BUILD64 = 1

DISTNAME = libnet

PATCHFILES = mainpatch

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
