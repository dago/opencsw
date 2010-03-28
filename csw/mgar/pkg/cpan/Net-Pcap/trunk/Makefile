GARNAME = Net-Pcap
GARVERSION = 0.16
CATEGORIES = cpan
AUTHOR = SAPER

DESCRIPTION = Interface to pcap(3) LBL packet capture library
define BLURB
  Net::Pcap is a Perl binding to the LBL pcap(3) library. 
  The README for libpcap describes itself as:
endef

PACKAGES = CSWpmnetpcap
CATALOGNAME = pm_netpcap

# depends
RUNTIME_DEP_PKGS     = CSWlibpcap
BUILD_DEP_PKGS       = $(RUNTIME_DEP_PKGS) CSWlibpcapdevel

LICENSE = README

include gar/category.mk
