# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = pypcap
VERSION = 1.1
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Simplified object-oriented Python extension module for libpcap

MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Strings-must-not-be-thrown-as-exceptions.patch
PATCHFILES += 0002-Use-a-shared-object-if-available.patch
PATCHFILES += 0003-include-pcap-must-be-first-to-pick-pcap_file.patch

CONFIGURE_ARGS = --with-pcap=/opt/csw
CONFIGURE_SCRIPTS = $(WORKSRC)/setup.py

PACKAGES = CSWpy-pcap

TEST_SCRIPTS =

LICENSE = LICENSE

RUNTIME_DEP_PKGS_CSWpy-pcap += CSWlibpython2-7-1-0
RUNTIME_DEP_PKGS_CSWpy-pcap += CSWlibpcap1
RUNTIME_DEP_PKGS_CSWpy-pcap += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-pcap += CSWlibgcc-s1

include gar/category.mk

