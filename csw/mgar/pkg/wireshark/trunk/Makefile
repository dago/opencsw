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

PATCHFILES = 0001-Solaris-9-doesn-t-have-stdint.h.patch

VENDOR_URL = http://www.wireshark.org/

PACKAGES += CSWwireshark
SPKG_DESC_CSWwireshark = Wireshark (was Ethereal) is a free network protocol analyzer
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWwireshark += CSWgcrypt
RUNTIME_DEP_PKGS_CSWwireshark += CSWglib2
RUNTIME_DEP_PKGS_CSWwireshark += CSWgpgerr
RUNTIME_DEP_PKGS_CSWwireshark += CSWgtk2
RUNTIME_DEP_PKGS_CSWwireshark += CSWpango
RUNTIME_DEP_PKGS_CSWwireshark += CSWzlib
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibintl8
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibcares2
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibpcap1
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibwireshark0
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibwiretap0
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibwsutil0

PACKAGES += CSWlibwireshark0
PKGFILES_CSWlibwireshark0 += $(call pkgfiles_lib,libwireshark.so.0)
SPKG_DESC_CSWlibwireshark0 += Wireshark library, libwireshark.so.0
RUNTIME_DEP_PKGS_CSWlibwireshark0 += CSWlibsmi2
RUNTIME_DEP_PKGS_CSWlibwireshark0 += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibwireshark0 += CSWlua
RUNTIME_DEP_PKGS_CSWlibwireshark0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibwireshark0 += CSWzlib
RUNTIME_DEP_PKGS_CSWlibwireshark0 += CSWlibwiretap0
RUNTIME_DEP_PKGS_CSWlibwireshark0 += CSWlibwsutil0
RUNTIME_DEP_PKGS_CSWlibwireshark0 += CSWlibgnutls26
RUNTIME_DEP_PKGS_CSWlibwireshark0 += CSWgcrypt
RUNTIME_DEP_PKGS_CSWlibwireshark0 += CSWlibcares2
RUNTIME_DEP_PKGS_CSWlibwireshark0 += CSWkrb5lib
RUNTIME_DEP_PKGS_CSWlibwireshark0 += CSWosslrt
RUNTIME_DEP_PKGS_CSWlibwireshark0 += CSWglib2
# This dependency can not be verified by checkpkg
RUNTIME_DEP_PKGS_CSWlibwireshark0 += CSWlibsmi-mibs
CHECKPKG_OVERRIDES_CSWlibwireshark0 += surplus-dependency|CSWlibsmi-mibs

PACKAGES += CSWlibwiretap0
PKGFILES_CSWlibwiretap0 += $(call pkgfiles_lib,libwiretap.so.0)
SPKG_DESC_CSWlibwiretap0 += Wireshark library, libwiretap.so.0
RUNTIME_DEP_PKGS_CSWlibwiretap0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibwiretap0 += CSWglib2
RUNTIME_DEP_PKGS_CSWlibwiretap0 += CSWlibwsutil0
RUNTIME_DEP_PKGS_CSWlibwiretap0 += CSWzlib

PACKAGES += CSWlibwsutil0
PKGFILES_CSWlibwsutil0 += $(call pkgfiles_lib,libwsutil.so.0)
SPKG_DESC_CSWlibwsutil0 += Wireshark library, libwsutil.so.0
RUNTIME_DEP_PKGS_CSWlibwsutil0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibwsutil0 += CSWglib2
RUNTIME_DEP_PKGS_CSWlibwsutil0 += CSWzlib

# This is almost empty, do not split for now
#PACKAGES += CSWwireshark-dev
#SPKG_DESC_CSWwireshark-dev = Development files for Wireshark
#PKGFILES_CSWwireshark-dev += $(PKGFILES_DEVEL)
#RUNTIME_DEP_PKGS_CSWwireshark-dev += CSWwireshark
#RUNTIME_DEP_PKGS_CSWwireshark-dev += CSWlibwiretap0
#RUNTIME_DEP_PKGS_CSWwireshark-dev += CSWlibwireshark0
#RUNTIME_DEP_PKGS_CSWwireshark-dev += CSWlibwsutil0

# This is probably from kerberos, revalidate after re-release of krb5 library
CHECKPKG_OVERRIDES_CSWwireshark += bad-rpath-entry|/opt/csw/lib/|opt/csw/bin/dftest
CHECKPKG_OVERRIDES_CSWwireshark += bad-rpath-entry|/opt/csw/lib/|opt/csw/bin/rawshark
CHECKPKG_OVERRIDES_CSWwireshark += bad-rpath-entry|/opt/csw/lib/|opt/csw/bin/tshark
CHECKPKG_OVERRIDES_CSWwireshark += bad-rpath-entry|/opt/csw/lib/|opt/csw/bin/wireshark
CHECKPKG_OVERRIDES_CSWlibwireshark0 += bad-rpath-entry|/opt/csw/lib/|opt/csw/lib/libwireshark.so.0.0.1

# example, \fI/usr/local/share/wireshark/preferences\fR) on UNIX-compatible
CHECKPKG_OVERRIDES_CSWwireshark += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/rawshark.1
CHECKPKG_OVERRIDES_CSWwireshark += file-with-bad-content|/usr/local|root/opt/csw/share/wireshark/rawshark.html

# \&\fI/usr/local/lib/wireshark/plugins/$VERSION\fR), and then
# example, \fI/usr/local/share/wireshark/preferences\fR) on UNIX-compatible
CHECKPKG_OVERRIDES_CSWwireshark += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/wireshark.1
CHECKPKG_OVERRIDES_CSWwireshark += file-with-bad-content|/usr/local|root/opt/csw/share/wireshark/wireshark.html

# example, \fI/usr/local/share/wireshark/preferences\fR) on UNIX-compatible
CHECKPKG_OVERRIDES_CSWwireshark += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/tshark.1
CHECKPKG_OVERRIDES_CSWwireshark += file-with-bad-content|/usr/local|root/opt/csw/share/wireshark/tshark.html

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-usr-local=no
CONFIGURE_ARGS += --with-ssl=/opt/csw

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

post-extract-modulated:
	@# The path to the libsmi MIBs is hardwired
	perl -pi \
		-e 's,/usr/share/snmp/mibs,/opt/csw/share/mibs,;' \
		$(WORKSRC)/epan/oids.c
