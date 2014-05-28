NAME = curl
VERSION = 7.11.2
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = Command line tool and library for client-side URL transfers
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
DISTFILES += libcurl.so.2.0.2.s
DISTFILES += libcurl.so.2.0.2.i
DISTFILES += COPYING

PACKAGES += CSWlibcurl2
CATALOGNAME_CSWlibcurl2 = libcurl2
SPKG_DESC_CSWlibcurl2 = Library for client-side URL transfers, libcurl.so.2
RUNTIME_DEP_PKGS_CSWlibcurl2 += CSWosslrt
RUNTIME_DEP_PKGS_CSWlibcurl2 += CSWzlib

VENDOR_URL = http://curl.haxx.se

# We just put the existing old libs in place for now
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS =

include gar/category.mk

post-install-isa-sparcv8:
	ginstall -d $(DESTDIR)$(libdir)
	ginstall $(WORKDIR)/libcurl.so.2.0.2.s $(DESTDIR)$(libdir)/libcurl.so.2.0.2
	ln -s libcurl.so.2.0.2 $(DESTDIR)$(libdir)/libcurl.so.2
	@$(MAKECOOKIE)

post-install-isa-i386:
	ginstall -d $(DESTDIR)$(libdir)
	cp $(WORKDIR)/libcurl.so.2.0.2.i $(DESTDIR)$(libdir)/libcurl.so.2.0.2
	ln -s libcurl.so.2.0.2 $(DESTDIR)$(libdir)/libcurl.so.2
	@$(MAKECOOKIE)
