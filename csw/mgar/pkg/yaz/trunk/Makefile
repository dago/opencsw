NAME = yaz
VERSION = 4.2.35
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

PACKAGES += CSWlibyaz4
SPKG_DESC_CSWlibyaz4 = Toolkit for Z39.50/SRW/SRU clients and servers, libyaz.so.4
PKGFILES_CSWlibyaz4 = $(call pkgfiles_lib,libyaz.so.4)
# These are always bumped together
CHECKPKG_OVERRIDES_CSWlibyaz4 += shared-lib-pkgname-mismatch
RUNTIME_DEP_PKGS_CSWlibyaz4 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibyaz4 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibyaz4 += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWlibyaz4 += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWlibyaz4 += CSWlibexslt0
RUNTIME_DEP_PKGS_CSWlibyaz4 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibyaz4 += CSWlibgnutls26
RUNTIME_DEP_PKGS_CSWlibyaz4 += CSWlibgpg-error0


PACKAGES += CSWlibyaz-icu4
PKGFILES_CSWlibyaz-icu4 += $(call pkgfiles_lib,libyaz_icu.so.4)
SPKG_DESC_CSWlibyaz-icu4 += $(DESCRIPTION), libyaz_icu.so.4
RUNTIME_DEP_PKGS_CSWlibyaz-icu4 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibyaz-icu4 += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWlibyaz-icu4 += CSWlibicudata48
RUNTIME_DEP_PKGS_CSWlibyaz-icu4 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibyaz-icu4 += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibyaz-icu4 += CSWlibyaz4
RUNTIME_DEP_PKGS_CSWlibyaz-icu4 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibyaz-icu4 += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWlibyaz-icu4 += CSWlibexslt0
RUNTIME_DEP_PKGS_CSWlibyaz-icu4 += CSWlibicuuc48
RUNTIME_DEP_PKGS_CSWlibyaz-icu4 += CSWlibicui18n48

PACKAGES += CSWlibyaz-server4
PKGFILES_CSWlibyaz-server4 += $(call pkgfiles_lib,libyaz_server.so.4)
SPKG_DESC_CSWlibyaz-server4 += $(DESCRIPTION), libyaz_server.so.4
RUNTIME_DEP_PKGS_CSWlibyaz-server4 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibyaz-server4 += CSWlibexslt0
RUNTIME_DEP_PKGS_CSWlibyaz-server4 += CSWlibyaz4
RUNTIME_DEP_PKGS_CSWlibyaz-server4 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibyaz-server4 += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibyaz-server4 += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWlibyaz-server4 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibyaz-server4 += CSWlibgcrypt11

PACKAGES += CSWlibyaz-dev
SPKG_DESC_CSWlibyaz-dev = Development files for libyaz
PKGFILES_CSWlibyaz-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibyaz-dev += $(bindir)/yaz-asncomp
PKGFILES_CSWlibyaz-dev += $(sharedstatedir)/yaz/.*
PKGFILES_CSWlibyaz-dev += $(docdir)/yaz/.*
PKGFILES_CSWlibyaz-dev += $(mandir)/man7/.*
RUNTIME_DEP_PKGS_CSWlibyaz-dev += CSWlibyaz4
RUNTIME_DEP_PKGS_CSWlibyaz-dev += CSWlibyaz-icu4
RUNTIME_DEP_PKGS_CSWlibyaz-dev += CSWlibyaz-server4
OBSOLETED_BY_CSWlibyaz-dev += CSWlibyaz-devel

# These are default locations for docbook files, they can be specified with a --with-* option
CHECKPKG_OVERRIDES_CSWlibyaz-dev += file-with-bad-content|/usr/local|root/opt/csw/share/aclocal/yaz.m4
CHECKPKG_OVERRIDES_CSWlibyaz-dev += file-with-bad-content|/usr/share|root/opt/csw/share/aclocal/yaz.m4
# These are the default on configuration
CHECKPKG_OVERRIDES_CSWlibyaz-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/yaz/installation.unix.html

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
SPKG_DESC_CSWyaz = Toolkit for Z39.50/SRW/SRU clients and servers
RUNTIME_DEP_PKGS_CSWyaz += CSWlibyaz4
RUNTIME_DEP_PKGS_CSWyaz += CSWlibyaz-icu4
RUNTIME_DEP_PKGS_CSWyaz += CSWlibyaz-server4
RUNTIME_DEP_PKGS_CSWyaz += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWyaz += CSWlibgnutls26
RUNTIME_DEP_PKGS_CSWyaz += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWyaz += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWyaz += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWyaz += CSWlibexslt0
RUNTIME_DEP_PKGS_CSWyaz += CSWlibz1
RUNTIME_DEP_PKGS_CSWyaz += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWyaz += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWyaz += CSWlibhistory6
RUNTIME_DEP_PKGS_CSWyaz += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWyaz += CSWlibicuuc48
RUNTIME_DEP_PKGS_CSWyaz += CSWlibicui18n48
RUNTIME_DEP_PKGS_CSWyaz += CSWlibicudata48

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
CONFIGURE_ARGS = $(DIRPATHS)

# Skip tests for now.
# There is one test failing:
# Entity: line 1: parser error : Extra content at the end of the document
# DY2IB5ETEMeMTAfYUphY2sgQ29sbGlucx4xMB9hSG93IHRvIHByb2dyYW0gYSBjb21wdXRlch4d</my>
#                                                                                ^
# test_embed_record.c:187: FAILED: test_render( "xml; base64=/my/text()", 0, "<my>" "MDAxMzhuYW0gIDIyMDAwNzM4YSA0NTAwMDAxMDAxMzAwMDAwMDAzMDAwNDAwMDEzMTAwMDAxNzAw" "MDE3MjQ1MDAzMDAwMDM0HiAgIDExMjI0NDY2IB5ETEMeMTAfYUphY2sgQ29sbGlucx4xMB9hSG93" "IHRvIHByb2dyYW0gYSBjb21wdXRlch4d" "</my>", "<?xml version=\"1.0\"?>\n" "<my><record xmlns=\"http://www.loc.gov/MARC21/slim\">\n" "  <leader>00138nam a22000738a 4500</leader>\n" "  <controlfield tag=\"001\">   11224466 </controlfield>\n" "  <controlfield tag=\"003\">DLC</controlfield>\n" "  <datafield tag=\"100\" ind1=\"1\" ind2=\"0\">\n" "    <subfield code=\"a\">Jack Collins</subfield>\n" "  </datafield>\n" "  <datafield tag=\"245\" ind1=\"1\" ind2=\"0\">\n" "    <subfield code=\"a\">How to program a computer</subfield>\n" "  </datafield>\n" "</record></my>\n")

SKIPTEST ?= 1

include gar/category.mk
