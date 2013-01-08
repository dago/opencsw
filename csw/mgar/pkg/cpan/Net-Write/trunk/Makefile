NAME = Net-Write
VERSION = 1.07
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = GOMOR

DESCRIPTION = A portable interface to open and send raw data to network
define BLURB
Net::Write provides a portable interface to open a network interface, and be
able to write raw data directly to the network. It juste provides three methods
when a Net::Write object has been created for an interface: open, send, close.
endef

LICENSE = LICENSE
PACKAGES = CSWpm-net-write
ARCHALL = 1

BUILD_DEP_PKGS += CSWpm-class-gomor
BUILD_DEP_PKGS += CSWpm-net-pcap
BUILD_DEP_PKGS += CSWpm-socket6
RUNTIME_DEP_PKGS += CSWpm-class-gomor
RUNTIME_DEP_PKGS += CSWpm-net-pcap
RUNTIME_DEP_PKGS += CSWpm-socket6

include gar/category.mk
