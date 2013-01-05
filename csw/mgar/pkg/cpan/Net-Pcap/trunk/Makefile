NAME = Net-Pcap
VERSION = 0.17
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SAPER

DESCRIPTION = Interface to pcap(3) LBL packet capture library
define BLURB
Net::Pcap is a Perl binding to the LBL pcap(3) library and its Win32
counterpart, the WinPcap library. Pcap (packet capture) is a portable API to
capture network packet: it allows applications to capture packets at
link-layer, bypassing the normal protocol stack. It also provides
features like kernel-level packet filtering and access to internal
statistics.
endef

LICENSE_TEXT = This module is licensed under the perl license

PACKAGES += CSWpm-net-pcap
CATALOGNAME_CSWpm-net-pcap = pm_net_pcap
SPKG_DESC_CSWpm-net-pcap = Interface to pcap(3) LBL packet capture library
OBSOLETED_BY_CSWpm-net-pcap += CSWpmnetpcap
CATALOGNAME_CSWpmnetpcap = pm_netpcap_stub

RUNTIME_DEP_PKGS_CSWpm-net-pcap += CSWlibpcap1

include gar/category.mk
