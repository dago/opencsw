NAME = wireshark
VERSION = 1.6.0
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
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibsmi2
RUNTIME_DEP_PKGS_CSWwireshark += CSWkrb5lib
RUNTIME_DEP_PKGS_CSWwireshark += CSWosslrt
RUNTIME_DEP_PKGS_CSWwireshark += CSWlibgnutls26
RUNTIME_DEP_PKGS_CSWwireshark += CSWlua

# No more library splitting unless absolutely necessary
CHECKPKG_OVERRIDES_CSWwireshark += shared-lib-package-contains-so-symlink
CHECKPKG_OVERRIDES_CSWwireshark += non-uniform-lib-versions-in-package

# This is probably from kerberos, revalidate after re-release of krb5 library
CHECKPKG_OVERRIDES_CSWwireshark += bad-rpath-entry

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

# Hardwire largefiles unless this is fixed:
#   https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6012
EXTRA_CPPFLAGS = -D_FILE_OFFSET_BITS=64

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
