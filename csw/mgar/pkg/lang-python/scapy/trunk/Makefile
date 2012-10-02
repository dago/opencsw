# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = scapy
VERSION = 2.2.0
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = A powerful interactive packet manipulation program

MASTER_SITES += http://www.secdev.org/projects/scapy/files/
DISTFILES += $(DISTNAME).tar.gz

VENDOR_URL = http://www.secdev.org/projects/scapy/

PACKAGES += CSWpy-scapy
SPKG_DESC_CSWmypkg = A powerful interactive packet manipulation program
# PKGFILES is catchall
ARCHALL_CSWpy-scapy = 1
# We need this for share/wireshark/manuf
RUNTIME_DEP_PKGS_CSWpy-scapy += CSWwireshark
CHECKPKG_OVERRIDES_CSWpy-scapy += surplus-dependency|CSWwireshark
# We need this for share/nmap/nmap-os-fingerprints
RUNTIME_DEP_PKGS_CSWpy-scapy += CSWnmap
CHECKPKG_OVERRIDES_CSWpy-scapy += surplus-dependency|CSWnmap

REINPLACEMENTS += wireshark-manuf
REINPLACE_MATCH_wireshark-manuf = /usr/share/wireshark/wireshark/manuf
REINPLACE_WITH_wireshark-manuf = /opt/csw/share/wireshark/manuf
REINPLACE_FILES_wireshark-manuf += scapy/data.py
REINPLACE_FILES_wireshark-manuf += scapy/utils6.py

REINPLACEMENTS += nmap-os-fingerprints
REINPLACE_MATCH_nmap-os-fingerprints = /usr/share/nmap/nmap-os-fingerprints
REINPLACE_WITH_nmap-os-fingerprints = /opt/csw/share/nmap/nmap-os-fingerprints
REINPLACE_FILES_nmap-os-fingerprints += scapy/modules/nmap.py

# There is no testsuite
TEST_SCRIPTS =

include gar/category.mk

post-install-modulated:
	-gunzip $(DESTDIR)$(mandir)/man1/scapy.1.gz
	@$(MAKECOOKIE)
