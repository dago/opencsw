NAME = yaz
VERSION = 4.1.2
CATEGORIES = utils

DESCRIPTION = Toolkit for Z39.50/SRW/SRU clients and servers
define BLURB
  Programmers toolkit supporting the development of Z39.50/SRW/SRU clients and servers
endef

MASTER_SITES = http://ftp.indexdata.dk/pub/yaz/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = https://www.indexdata.com/yaz
LICENSE = LICENSE

# File splitting taken from yaz.spec

PACKAGES += CSWlibyaz4
CATALOGNAME_CSWlibyaz4 = libyaz4
SPKG_DESC_CSWlibyaz4 = Toolkit for Z39.50/SRW/SRU clients and servers, libyaz.so.4
PKGFILES_CSWlibyaz4 = $(call baseisadirs,$(libdir),libyaz.*\.so\.4(\.\d+)*)
RUNTIME_DEP_PKGS_CSWlibyaz4 += CSWzlib
RUNTIME_DEP_PKGS_CSWlibyaz4 += CSWlibxml2
RUNTIME_DEP_PKGS_CSWlibyaz4 += CSWgcrypt
RUNTIME_DEP_PKGS_CSWlibyaz4 += CSWlibicu46
RUNTIME_DEP_PKGS_CSWlibyaz4 += CSWlibxslt
RUNTIME_DEP_PKGS_CSWlibyaz4 += CSWiconv
RUNTIME_DEP_PKGS_CSWlibyaz4 += CSWgnutls
RUNTIME_DEP_PKGS_CSWlibyaz4 += CSWgpgerr

PACKAGES += CSWlibyaz-devel
CATALOGNAME_CSWlibyaz-devel = libyaz_devel
SPKG_DESC_CSWlibyaz-devel = Development files for libyaz
PKGFILES_CSWlibyaz-devel += $(PKGFILES_DEVEL)
PKGFILES_CSWlibyaz-devel += $(bindir)/yaz-asncomp
PKGFILES_CSWlibyaz-devel += $(sharedstatedir)/yaz/.*
PKGFILES_CSWlibyaz-devel += $(docdir)/yaz/.*
PKGFILES_CSWlibyaz-devel += $(mandir)/man7/.*
RUNTIME_DEP_PKGS_CSWlibyaz-devel += CSWlibyaz4

# %{_bindir}/yaz-config
# %{_bindir}/yaz-asncomp
# %{_includedir}/yaz
# %{_libdir}/pkgconfig/yaz.pc
# %{_libdir}/*.so
# %{_libdir}/*.a
# %{_datadir}/aclocal/yaz.m4
# %{_mandir}/man1/yaz-asncomp.*
# %{_mandir}/man7/yaz.*
# %{_mandir}/man?/yaz-config.*
# %{_datadir}/doc/yaz
# %{_datadir}/yaz

PACKAGES += CSWyaz
CATALOGNAME_CSWyaz = yaz
SPKG_DESC_CSWyaz = Toolkit for Z39.50/SRW/SRU clients and servers
RUNTIME_DEP_PKGS_CSWyaz += CSWlibyaz4
RUNTIME_DEP_PKGS_CSWyaz += CSWiconv
RUNTIME_DEP_PKGS_CSWyaz += CSWgnutls
RUNTIME_DEP_PKGS_CSWyaz += CSWgpgerr
RUNTIME_DEP_PKGS_CSWyaz += CSWncurses
RUNTIME_DEP_PKGS_CSWyaz += CSWlibxslt
RUNTIME_DEP_PKGS_CSWyaz += CSWzlib
RUNTIME_DEP_PKGS_CSWyaz += CSWlibxml2
RUNTIME_DEP_PKGS_CSWyaz += CSWreadline
RUNTIME_DEP_PKGS_CSWyaz += CSWgcrypt
RUNTIME_DEP_PKGS_CSWyaz += CSWlibicu46

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

NOISAEXEC = 1
MERGE_SCRIPTS_isa-extra = copy-relocated-only copy-config-only
MERGE_DIRS_isa-extra = $(libdir)

# This is a bug in checkpkg
CHECKPKG_OVERRIDES_CSWlibyaz4 += shared-lib-pkgname-mismatch
CHECKPKG_OVERRIDES_CSWlibyaz-devel += wrong-docdir|expected=/opt/csw/shared/doc/libyaz_devel/...|in-package=/opt/csw/share/doc/yaz/license.html

# These can go away after CSWlibicu46 has been officially released
CHECKPKG_OVERRIDES_CSWlibyaz4 += soname-not-found
CHECKPKG_OVERRIDES_CSWlibyaz4 += unidentified-dependency|CSWlibicu46
CHECKPKG_OVERRIDES_CSWlibyaz4 += surplus-dependency|CSWlibicu46
CHECKPKG_OVERRIDES_CSWyaz-icu += soname-not-found
CHECKPKG_OVERRIDES_CSWyaz-icu += unidentified-dependency|CSWlibicu46
CHECKPKG_OVERRIDES_CSWyaz-icu += surplus-dependency|CSWlibicu46
CHECKPKG_OVERRIDES_CSWyaz += soname-not-found
CHECKPKG_OVERRIDES_CSWyaz += unidentified-dependency|CSWlibicu46
CHECKPKG_OVERRIDES_CSWyaz += surplus-dependency|CSWlibicu46

include gar/category.mk
