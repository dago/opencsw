NAME = Net-Pcap
VERSION = 0.16
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SAPER

DESCRIPTION = Interface to pcap(3) LBL packet capture library
define BLURB
  Net::Pcap is a Perl binding to the LBL pcap(3) library. 
  The README for libpcap describes itself as:
endef

PACKAGES = CSWpmnetpcap
CATALOGNAME = pm_netpcap

# add a proper license
 LICENSE = $(FILEDIR)/LICENSE

# depends
RUNTIME_DEP_PKGS     = CSWlibpcap
BUILD_DEP_PKGS       = $(RUNTIME_DEP_PKGS) CSWlibpcapdevel

include gar/category.mk
