# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = freeipmi
VERSION = 1.2.5

DESCRIPTION = IPMI software based on the IPMI v1.5/2.0 specification

MASTER_SITES = $(GNU_MIRROR)
DISTFILES += $(DISTNAME).tar.gz

# This should better be detected during autoconf time
PATCHFILES += 0001-Add-missing-sighandler_t-on-Solaris.patch

VENDOR_URL = http://www.gnu.org/software/freeipmi/index.html

PACKAGES += CSWfreeipmi
SPKG_DESC_CSWfreeipmi = IPMI software based on the IPMI v1.5/2.0 specification
RUNTIME_DEP_PKGS_CSWfreeipmi += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWfreeipmi += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWfreeipmi += CSWperl

# I don't care for now
CHECKPKG_OVERRIDES_CSWfreeipmi += file-with-bad-content|/usr/local|root/opt/csw/share/doc/freeipmi/README.build
CHECKPKG_OVERRIDES_CSWfreeipmi += file-with-bad-content|/usr/local|root/opt/csw/share/doc/freeipmi/INSTALL
CHECKPKG_OVERRIDES_CSWfreeipmi += file-with-bad-content|/usr/local|root/opt/csw/share/doc/freeipmi/ChangeLog
CHECKPKG_OVERRIDES_CSWfreeipmi += file-with-bad-content|/usr/share|root/opt/csw/share/doc/freeipmi/README.build
CHECKPKG_OVERRIDES_CSWfreeipmi += file-with-bad-content|/usr/share|root/opt/csw/share/doc/freeipmi/contrib/pet/README
CHECKPKG_OVERRIDES_CSWfreeipmi += shared-lib-pkgname-mismatch
CHECKPKG_OVERRIDES_CSWfreeipmi += shared-lib-package-contains-so-symlink
CHECKPKG_OVERRIDES_CSWfreeipmi += init-file-missing-cswinitsmf-class|/etc/opt/csw/init.d/bmc-watchdog|class=none
CHECKPKG_OVERRIDES_CSWfreeipmi += init-file-missing-cswinitsmf-class|/etc/opt/csw/init.d/ipmidetectd|class=none
CHECKPKG_OVERRIDES_CSWfreeipmi += init-file-missing-cswinitsmf-class|/etc/opt/csw/init.d/ipmiseld|class=none

GARCOMPILER = GCC4

CONFIGURE_ARGS = $(DIRPATHS)

# Otherwise it falls back to gcc which interprets the manpage as C code
EXTRA_CONFIGURE_EXPORTS += CPP
CONFIGURE_ENV_CPP = $(bindir)/cpp

include gar/category.mk

