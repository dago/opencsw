GARNAME = curl
GARVERSION = 7.19.5
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
DISTFILES += curlbuild.h

PACKAGES = CSWcurl CSWcurlrt CSWcurldevel
CATALOGNAME_CSWcurl = curl
CATALOGNAME_CSWcurlrt = curlrt
CATALOGNAME_CSWcurldevel = curldevel

# Upstream check seem to interfere with build on 8s?
#UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

LIBDEPS += lib/openssl
CONFIGURE_ARGS = $(DIRPATHS) --with-ssl

#Can't build amd64 until openldap has an amd64 build (Mantis 3028)
#BUILD64 = 1
EXTRA_BUILD_ISAS_sparc = sparcv9

REQUIRED_PKGS_CSWcurl = CSWiconv CSWlibidn CSWlibnet CSWoldaprt CSWosslrt
REQUIRED_PKGS_CSWcurl += CSWsasl CSWzlib CSWcurlrt
REQUIRED_PKGS_CSWcurlrt = CSWlibidn CSWlibnet CSWoldaprt CSWosslrt CSWzlib CSWsasl
REQUIRED_PKGS_CSWcurldevel = CSWcurlrt

SKIPTEST = 1

EXTRA_PAX_ARGS_32 = -s ",^\.$(includedir)/curl/curlbuild.h$$,.$(includedir)/curl/curlbuild-32.h,p"
EXTRA_PAX_ARGS_64 = -s ",^\.$(includedir)/curl/curlbuild.h$$,.$(includedir)/curl/curlbuild-64.h,p"
EXTRA_PAX_ARGS_isa-sparcv8 = $(EXTRA_PAX_ARGS_32)
EXTRA_PAX_ARGS_isa-sparcv9 = $(EXTRA_PAX_ARGS_64)
EXTRA_PAX_ARGS_isa-i386 = $(EXTRA_PAX_ARGS_32)
EXTRA_PAX_ARGS_isa-amd64 = $(EXTRA_PAX_ARGS_64)

PKGFILES_CSWcurldevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWcurlrt  = $(PKGFILES_RT)

include gar/category.mk

post-install-isa-sparcv8:
	@ginstall $(FILEDIR)/libcurl.so.3.0.0.s $(INSTALLISADIR)$(libdir)/libcurl.so.3.0.0
	@ginstall $(FILEDIR)/libcurl.so.2.0.2.s $(INSTALLISADIR)$(libdir)/libcurl.so.2.0.2
	@ln -s libcurl.so.3.0.0 $(INSTALLISADIR)$(libdir)/libcurl.so.3
	@ln -s libcurl.so.2.0.2 $(INSTALLISADIR)$(libdir)/libcurl.so.2
	@$(MAKECOOKIE)

post-install-isa-i386:
	@cp $(FILEDIR)/libcurl.so.3.0.0.i $(INSTALLISADIR)/opt/csw/lib/libcurl.so.3.0.0
	@cp $(FILEDIR)/libcurl.so.2.0.2.i $(INSTALLISADIR)/opt/csw/lib/libcurl.so.2.0.2
	@ln -s libcurl.so.3.0.0 $(INSTALLISADIR)$(libdir)/libcurl.so.3
	@ln -s libcurl.so.2.0.2 $(INSTALLISADIR)$(libdir)libcurl.so.2
	@$(MAKECOOKIE)

post-merge:
	ginstall $(FILEDIR)/curlbuild.h $(PKGROOT)$(includedir)/curl/curlbuild.h
	@$(MAKECOOKIE)
