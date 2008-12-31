GARNAME = curl
GARVERSION = 7.19.2
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
DISTFILES += $(call admfiles,CSWcurl,prototype depend)
DISTFILES += $(call admfiles,CSWcurlrt,prototype depend)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

LIBDEPS += lib/openssl

CONFIGURE_ARGS = $(DIRPATHS) --with-ssl

# Not gonna do it
TEST_SCRIPTS =

include gar/category.mk
