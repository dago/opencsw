GARNAME = ngrep
GARVERSION = 1.45
CATEGORIES = net

DESCRIPTION = Network grep
define BLURB
  ngrep strives to provide most of GNU grep's common features,
  applying them to the network layer. ngrep is a pcap-aware tool
  that will allow you to specify extended regular or hexadecimal
  expressions to match against data payloads of packets. It currently
  recognizes IPv4/6, TCP, UDP, ICMPv4/6, IGMP and Raw across Ethernet,
  PPP, SLIP, FDDI, Token Ring and null interfaces, and understands
  BPF filter logic in the same fashion as more common packet sniffing
  tools, such as tcpdump and snoop.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWngrep,depend)
PATCHFILES = gar-base.diff

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=10752
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET =

include gar/category.mk
