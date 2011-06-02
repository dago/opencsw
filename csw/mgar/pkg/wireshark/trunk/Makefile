NAME = wireshark
VERSION = 1.4.7
CATEGORIES = apps

DESCRIPTION = Wireshark (was Ethereal) is a free network protocol analyzer
define BLURB
  Wireshark is the world's foremost network protocol analyzer, and is the
  de facto (and often de jure) standard across many industries and
  educational institutions.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

RUNTIME_DEP_PKGS_CSWwireshark += CSWgcrypt CSWgeoip CSWggettextrt CSWglib2
RUNTIME_DEP_PKGS_CSWwireshark += CSWgpgerr CSWgtk2 CSWkrb5lib CSWlibpcap 
RUNTIME_DEP_PKGS_CSWwireshark += CSWlua CSWpango CSWzlib
RUNTIME_DEP_PKGS_CSWwireshark += CSWgnutls CSWlibcares
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibsmi
RUNTIME_DEP_PKGS_CSWwireshark += CSWosslrt

PATCHFILES = 0001-Solaris-9-doesn-t-have-stdint.h.patch

CHECKPKG_OVERRIDES_CSWwireshark += bad-rpath-entry|/opt/csw/lib/|opt/csw/bin/dftest
CHECKPKG_OVERRIDES_CSWwireshark += bad-rpath-entry|/opt/csw/lib/|opt/csw/bin/rawshark
CHECKPKG_OVERRIDES_CSWwireshark += bad-rpath-entry|/opt/csw/lib/|opt/csw/bin/tshark
CHECKPKG_OVERRIDES_CSWwireshark += bad-rpath-entry|/opt/csw/lib/|opt/csw/bin/wireshark
CHECKPKG_OVERRIDES_CSWwireshark += bad-rpath-entry|/opt/csw/lib/|opt/csw/lib/libwireshark.so.0.0.1

VENDOR_URL = http://www.wireshark.org/

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-usr-local=no
CONFIGURE_ARGS += --with-ssl=/opt/csw

# TEST_SCRIPTS =

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
