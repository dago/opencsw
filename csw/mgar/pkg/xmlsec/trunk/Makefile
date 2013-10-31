# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = xmlsec1
VERSION = 1.2.19
GARTYPE = v2

DESCRIPTION = XML Security Library

MASTER_SITES = http://www.aleksey.com/xmlsec/download/
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://www.aleksey.com/xmlsec/

PACKAGES += CSWxmlsec1
SPKG_DESC_CSWxmlsec1 = XML Security
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWxmlsec1 += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWxmlsec1 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWxmlsec1 += CSWlibxmlsec1-1

PACKAGES += CSWlibxmlsec1-dev
SPKG_DESC_CSWlibxmlsec1-dev = Development files for libxmlsec1.so.1
PKGFILES_CSWlibxmlsec1-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibxmlsec1-dev += $(docdir)/xmlsec1/.*
PKGFILES_CSWlibxmlsec1-dev += $(call baseisadirs,$(libdir),xmlsec1Conf.sh)
RUNTIME_DEP_PKGS_CSWlibxmlsec1-dev += CSWlibxmlsec1-1
RUNTIME_DEP_PKGS_CSWlibxmlsec1-dev += CSWlibxmlsec1gcrypt1
RUNTIME_DEP_PKGS_CSWlibxmlsec1-dev += CSWlibxmlsec1gnutls1
RUNTIME_DEP_PKGS_CSWlibxmlsec1-dev += CSWlibxmlsec1nss1
RUNTIME_DEP_PKGS_CSWlibxmlsec1-dev += CSWlibxmlsec1openssl1

PACKAGES += CSWlibxmlsec1-1
SPKG_DESC_CSWlibxmlsec1-1 = XML security library
PKGFILES_CSWlibxmlsec1-1 += $(call pkgfiles_lib,libxmlsec1.so.1)
RUNTIME_DEP_PKGS_CSWlibxmlsec1-1 += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWlibxmlsec1-1 += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWlibxmlsec1-1 += CSWlibxml2-2

PACKAGES += CSWlibxmlsec1gcrypt1
SPKG_DESC_CSWlibxmlsec1gcrypt1 = XML security library for gcrypt
PKGFILES_CSWlibxmlsec1gcrypt1 += $(call pkgfiles_lib,libxmlsec1-gcrypt.so.1)
RUNTIME_DEP_PKGS_CSWlibxmlsec1gcrypt1 += CSWlibxmlsec1-1
RUNTIME_DEP_PKGS_CSWlibxmlsec1gcrypt1 += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibxmlsec1gcrypt1 += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWlibxmlsec1gcrypt1 += CSWlibxml2-2

# This is on i386 only, some day I need to investigate this
CHECKPKG_OVERRIDES_CSWlibxmlsec1gcrypt1 += surplus-dependency|CSWlibgpg-error0

PACKAGES += CSWlibxmlsec1gnutls1
SPKG_DESC_CSWlibxmlsec1gnutls1 = XML security library for GNU TLS
PKGFILES_CSWlibxmlsec1gnutls1 += $(call pkgfiles_lib,libxmlsec1-gnutls.so.1)
RUNTIME_DEP_PKGS_CSWlibxmlsec1gnutls1 += CSWlibxmlsec1-1
RUNTIME_DEP_PKGS_CSWlibxmlsec1gnutls1 += CSWlibxmlsec1gcrypt1
RUNTIME_DEP_PKGS_CSWlibxmlsec1gnutls1 += CSWlibgnutls28
RUNTIME_DEP_PKGS_CSWlibxmlsec1gnutls1 += CSWlibxml2-2

PACKAGES += CSWlibxmlsec1nss1
SPKG_DESC_CSWlibxmlsec1nss1 = XML security library for NSS
PKGFILES_CSWlibxmlsec1nss1 += $(call pkgfiles_lib,libxmlsec1-nss.so.1)
RUNTIME_DEP_PKGS_CSWlibxmlsec1nss1 += CSWlibsmime3
RUNTIME_DEP_PKGS_CSWlibxmlsec1nss1 += CSWlibxmlsec1-1
RUNTIME_DEP_PKGS_CSWlibxmlsec1nss1 += CSWlibnspr4
RUNTIME_DEP_PKGS_CSWlibxmlsec1nss1 += CSWlibnss3
RUNTIME_DEP_PKGS_CSWlibxmlsec1nss1 += CSWlibxml2-2

PACKAGES += CSWlibxmlsec1openssl1
SPKG_DESC_CSWlibxmlsec1openssl1 = XML security library for OpenSSL
PKGFILES_CSWlibxmlsec1openssl1 += $(call pkgfiles_lib,libxmlsec1-openssl.so.1)
RUNTIME_DEP_PKGS_CSWlibxmlsec1openssl1 += CSWlibxmlsec1-1
RUNTIME_DEP_PKGS_CSWlibxmlsec1openssl1 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWlibxmlsec1openssl1 += CSWlibxml2-2

BUILD64 = 1
ISAEXEC = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

