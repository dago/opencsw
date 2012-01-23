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
# These are always bumped together
CHECKPKG_OVERRIDES_CSWlibyaz4 += shared-lib-pkgname-mismatch
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
# These are default locations for docbook files, they can be specified with a --with-* option
CHECKPKG_OVERRIDES_CSWlibyaz-devel += file-with-bad-content|/usr/local|root/opt/csw/share/aclocal/yaz.m4
CHECKPKG_OVERRIDES_CSWlibyaz-devel += file-with-bad-content|/usr/share|root/opt/csw/share/aclocal/yaz.m4
# These are the default on configuration
CHECKPKG_OVERRIDES_CSWlibyaz-devel += file-with-bad-content|/usr/local|root/opt/csw/share/doc/yaz/installation.unix.html

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

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

post-extract-modulated:
	-perl -pi -e 's,/usr/local/share,$(sharedstatedir),;' \
		$(WORKSRC)/client/client.c \
		$(WORKSRC)/doc/yaz.7
	-perl -pi -e 's,/usr/share,$(sharedstatedir),;' \
		$(WORKSRC)/doc/yaz-asncomp-man.xml
	-perl -pi -e 's,/usr/share/yaz/etc,$(sysconfdir),;' \
		$(WORKSRC)/doc/tools.xml
	-perl -pi -e 's,/usr/local,$(prefix),;' \
		$(WORKSRC)/doc/yaz-config.1
	@$(MAKECOOKIE)
