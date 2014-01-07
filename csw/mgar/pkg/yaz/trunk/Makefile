NAME = yaz
VERSION = 5.0.2
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Toolkit for Z39.50/SRW/SRU clients and servers
define BLURB
  Programmers toolkit supporting the development of Z39.50/SRW/SRU clients and servers
endef

MASTER_SITES = http://ftp.indexdata.dk/pub/yaz/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

VENDOR_URL = https://www.indexdata.com/yaz
LICENSE = LICENSE

# File splitting taken from yaz.spec

PA5
SPKG_DESC_CSWlibyaz5 = Toolkit for Z39.50/SRW/SRU clients and servers, libyaz.so.5
PKGFILES_CSWlibyaz5 = $(call pkgfiles_lib,libyaz.so.5)
RUNTIME_DEP_PKGS_CSWlibyaz5 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibyaz5 += CSWlibexslt0
RUNTIME_DEP_PKGS_CSWlibyaz5 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibyaz5 += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibyaz5 += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWlibyaz5 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibyaz5 += CSWlibgnutls28
RUNTIME_DEP_PKGS_CSWlibyaz5 += CSWlibgcrypt11

PACKAGES += CSWlibyaz-icu5
SPKG_DESC_CSWlibyaz-icu5 += $(DESCRIPTION), libyaz_icu.so.5
PKGFILES_CSWlibyaz-icu5 += $(call pkgfiles_lib,libyaz_icu.so.5)
RUNTIME_DEP_PKGS_CSWlibyaz-icu5 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibyaz-icu5 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibyaz-icu5 += CSWlibyaz4
RUNTIME_DEP_PKGS_CSWlibyaz-icu5 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibyaz-icu5 += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibyaz-icu5 += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWlibyaz-icu5 += CSWlibicui18n52
RUNTIME_DEP_PKGS_CSWlibyaz-icu5 += CSWlibexslt0
RUNTIME_DEP_PKGS_CSWlibyaz-icu5 += CSWlibicuuc52
RUNTIME_DEP_PKGS_CSWlibyaz-icu5 += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWlibyaz-icu5 += CSWlibicudata52

PACKAGES += CSWlibyaz-server5
SPKG_DESC_CSWlibyaz-server5 += $(DESCRIPTION), libyaz_server.so.5
PKGFILES_CSWlibyaz-server5 += $(call pkgfiles_lib,libyaz_server.so.5)
RUNTIME_DEP_PKGS_CSWlibyaz-server5 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibyaz-server5 += CSWlibexslt0
RUNTIME_DEP_PKGS_CSWlibyaz-server5 += CSWlibyaz4
RUNTIME_DEP_PKGS_CSWlibyaz-server5 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibyaz-server5 += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibyaz-server5 += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWlibyaz-server5 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibyaz-server5S_CSWlibyaz-server4 += CSWlibgcrypt11

PACKAGES += CSWlibyaz-dev
SPKG_DESC_CSWlibyaz-dev = Development files for libyaz
PKGFILES_CSWlibyaz-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibyaz-dev += $(bindir)/yaz-asncomp
PKGFILES_CSWlibyaz-dev += $(sharedstatedir)/yaz/.*
PKGFILES_CSWlibyaz-dev += $(docdir)/yaz/.*
PKGFILES_CSWlibyaz-dev += $(mandir)/man7/.*
RUNTIME_DEP_PKGS_CSWliby-icu5
RUNTIME_DEP_PKGS_CSWlibyaz-dev += CSWlibyaz-server5
RUNTIME_DEP_PKGS_CSWlibyaz-dev += CSWlibyaz5
OBSOLETED_BY_CSWlibyaz-dev += CSWlibyaz-devestallation.unix.html

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
SPKG_DESC_CSWyaz = Toolkit for Z39.50/SRW/SRU c# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWyaz += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWyaz += CSWlibyaz-server5
RUNTIME_DEP_PKGS_CSWyaz += CSWlibyaz5
RUNTIME_DEP_PKGS_CSWyaz += CSWlibicui18n52_CSWyaz += CSWlibz1
RUNTIME_DEP_PKGS_CSWyaz += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWyaz += CSWlibreadline6
RUNTIME_DEP_PKyaz-icu5
RUNTIME_DEP_PKGS_CSWyaz += CSWlibicuuc52 +# These are usually not needed, but -z ignore does not work the way it used to
CHECKPKG_OVERRIDES_CSWlibyaz5 += surplus-dependency|CSWlibz1
CHECKPKG_OVERRIDES_CSWlibyaz5 += surplus-dependency|CSWlibgcrypt11
CHECKPKG_OVERRIDES_CSWlibyaz5 += surplus-dependency|CSWlibgpg-error0
CHECKPKG_OVERRIDES_CSWyaz += surplus-dependency|CSWlibiconv2
CHECKPKG_OVERRIDES_CSWlibyaz-server5 += surplus-dependency|CSWlibgcrypt11
CHECKPKG_OVERRIDES_CSWlibyaz-server5 += surplus-dependency|CSWlibiconv2
CHECKPKG_OVERRIDES_CSWlibyaz-server5 += surplus-dependency|CSWlibgpg-error0
CHECKPKG_OVERRIDES_CSWlibyaz-server5 += surplus-dependency|CSWlibexslt0
CHECKPKG_OVERRIDES_CSWlibyaz-server5 += surplus-dependency|CSWlibz1
CHECKPKG_OVERRIDES_CSWlibyaz-server5 += surplus-dependency|CSWlibxslt1
CHECKPKG_OVERRIDES_CSWlibyaz-icu5 += surplus-dependency|CSWlibgcrypt11
CHECKPKG_OVERRIDES_CSWlibyaz-icu5 += surplus-dependency|CSWlibiconv2
CHECKPKG_OVERRIDES_CSWlibyaz-icu5 += surplus-dependency|CSWlibicudata52
CHECKPKG_OVERRIDES_CSWlibyaz-icu5 += surplus-dependency|CSWlibgpg-error0
CHECKPKG_OVERRIDES_CSWlibyaz-icu5 += surplus-dependency|CSWlibexslt0
CHECKPKG_OVERRIDES_CSWlibyaz-icu5 += surplus-dependency|CSWlibz1
CHECKPKG_OVERRIDES_CSWlibyaz-icu5 += surplus-dependency|CSWlibxslt1 += CSWlibicudata48

REINPLACE_USRLOCAL += doc/yaz-config.1

REINPLACEMENTS += usrlocalshare
REINPLACE_MATCH_usrlocalshare = /usr/local/share
REINPLACE_WITH_usrlocalshare = $(sharedstatedir)
REINPLACE_FILES_usrlocalshare += client/client.c
REINPLACE_FILES_usrlocalshare += doc/yaz.7

REINPLACEMENTS += usrshare
REINPLACE_MATCH_usrshare = /usr/share
REINPLACE_WITH_usrshare = $(sharedstatedir)
REINPLACE_FILES_usrshare += doc/yaz-asncomp-man.xml

REINPLACEMENTS += etc
REINPLACE_MATCH_etc = /usr/share/yaz/etc
REINPLACE_WITH_etc = $(sysconfdir)
REINPLACE_FILES_etc += doc/tools.xml

BUILD64_LIBS_ONLY = 1
CONFIGURE_Ainclude gar/category.mk
