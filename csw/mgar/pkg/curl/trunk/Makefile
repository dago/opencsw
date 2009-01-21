GARNAME = curl
GARVERSION = 7.19.3
CATEGORIES = net

DESCRIPTION = Command line tool and library for client-side URL transfers.
define BLURB
  curl and libcurl is a tool for transferring files using URL syntax. It
  supports HTTP, HTTPS, FTP, FTPS, DICT, TELNET, LDAP, FILE, and GOPHER, as
  well as HTTP-post, HTTP-put, cookies, FTP upload, resumed transfers,
  passwords, portnumbers, SSL certificates, Kerberos, and proxies. It is
  powered by libcurl, the client-side URL transfer library. There are
  bindings/interfaces to libcurl for more than a dozen languages and
  environments.
endef

MASTER_SITES = http://curl.haxx.se/download/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWcurl,depend)
DISTFILES += $(call admfiles,CSWcurlrt,depend)
DISTFILES += $(call admfiles,CSWcurldevel,depend)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

LIBDEPS += lib/openssl
CONFIGURE_ARGS = $(DIRPATHS) --with-ssl

#Can't build amd64 until openldap has an amd64 build (Mantis 3028)
#BUILD64 = 1
EXTRA_BUILD_ISAS_sparc = sparcv9

TEST_SCRIPTS =

PKGFILES_CSWcurldevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWcurlrt  = $(PKGFILES_RT)

include gar/category.mk
