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
DISTFILES += libcurl.so.3.0.0.s
DISTFILES += libcurl.so.2.0.2.s
DISTFILES += libcurl.so.3.0.0.i
DISTFILES += libcurl.so.2.0.2.i
DISTFILES += $(call admfiles,CSWcurl,)
DISTFILES += $(call admfiles,CSWcurlrt,)
DISTFILES += $(call admfiles,CSWcurldevel,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

LIBDEPS += lib/openssl
CONFIGURE_ARGS = $(DIRPATHS) --with-ssl

#Can't build amd64 until openldap has an amd64 build (Mantis 3028)
#BUILD64 = 1
EXTRA_BUILD_ISAS_sparc = sparcv9

REQUIRED_PKGS_CSWcurl = CSWiconv CSWlibidn CSWlibnet CSWoldaprt CSWosslrt
REQUIRED_PKGS_CSWcurl += CSWsasl CSWzlib CSWcurlrt
REQUIRED_PKGS_CSWcurlrt = CSWlibidn CSWlibnet CSWoldaprt CSWosslrt CSWzlib CSWsasl
REQUIRED_PKGS_CSWcurldevel = CSWcurlrt

ENABLE_CHECK = 0
TEST_TARGET = 

PKGFILES_CSWcurldevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWcurlrt  = $(PKGFILES_RT)

include gar/category.mk

post-install-isa-sparcv8:
	@cp $(FILEDIR)/libcurl.so.3.0.0.s $(INSTALLISADIR)/opt/csw/lib/libcurl.so.3.0.0
	@cp $(FILEDIR)/libcurl.so.2.0.2.s $(INSTALLISADIR)/opt/csw/lib/libcurl.so.2.0.2
	@( cd $(INSTALLISADIR)/opt/csw/lib; ln -s libcurl.so.3.0.0 libcurl.so.3 )
	@( cd $(INSTALLISADIR)/opt/csw/lib; ln -s libcurl.so.2.0.2 libcurl.so.2 )

post-install-isa-i386:
	@cp $(FILEDIR)/libcurl.so.3.0.0.i $(INSTALLISADIR)/opt/csw/lib/libcurl.so.3.0.0
	@cp $(FILEDIR)/libcurl.so.2.0.2.i $(INSTALLISADIR)/opt/csw/lib/libcurl.so.2.0.2
	@( cd $(INSTALLISADIR)/opt/csw/lib; ln -s libcurl.so.3.0.0 libcurl.so.3 )
	@( cd $(INSTALLISADIR)/opt/csw/lib; ln -s libcurl.so.2.0.2 libcurl.so.2 )
