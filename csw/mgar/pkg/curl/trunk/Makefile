GARNAME = curl
GARVERSION = 7.19.7
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

SPKG_DESC_CSWcurl      = A command line tool and library for client-side URL transfers
SPKG_DESC_CSWcurlrt    = Curl Runtime Libraries
SPKG_DESC_CSWcurldevel = Curl Developer Files

SPKG_SOURCEURL = http://curl.haxx.se

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

EXTRA_CONFIGURE_ARGS_isa-amd64 = --disable-ldap
CONFIGURE_ARGS = $(DIRPATHS) --with-ssl
CONFIGURE_ARGS += $(EXTRA_CONFIGURE_ARGS_isa-$(ISA))

# amd64 is built without openldap because there are no libs available right now (Mantis 3028)
BUILD64 = 1

# We are doing 64 bit only for the libs
NO_ISAEXEC = 1

REQUIRED_PKGS_CSWcurl  = CSWiconv CSWlibidn CSWlibnet CSWoldaprt CSWosslrt
REQUIRED_PKGS_CSWcurl += CSWsasl CSWzlib CSWcurlrt
REQUIRED_PKGS_CSWcurlrt = CSWlibidn CSWlibnet CSWoldaprt CSWosslrt CSWzlib CSWsasl
REQUIRED_PKGS_CSWcurldevel = CSWcurlrt

SKIPTEST = 1

# The 64 bit binary just takes space
EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv9 = $(bindir)/curl
EXTRA_MERGE_EXCLUDE_FILES_isa-amd64 = $(bindir)/curl

EXTRA_PAX_ARGS_32 = -s ",^\.$(includedir)/curl/curlbuild.h$$,.$(includedir)/curl/curlbuild-32.h,p"
EXTRA_PAX_ARGS_64 = -s ",^\.$(includedir)/curl/curlbuild.h$$,.$(includedir)/curl/curlbuild-64.h,p"
EXTRA_PAX_ARGS_isa-sparcv8 = $(EXTRA_PAX_ARGS_32)
EXTRA_PAX_ARGS_isa-sparcv9 = $(EXTRA_PAX_ARGS_64)
EXTRA_PAX_ARGS_isa-i386    = $(EXTRA_PAX_ARGS_32)
EXTRA_PAX_ARGS_isa-amd64   = $(EXTRA_PAX_ARGS_64)

PKGFILES_CSWcurldevel = $(PKGFILES_DEVEL)
PKGFILES_CSWcurlrt = $(PKGFILES_RT)

include gar/category.mk

post-install-isa-sparcv8:
	ginstall $(FILEDIR)/libcurl.so.3.0.0.s $(DESTDIR)$(libdir)/libcurl.so.3.0.0
	ginstall $(FILEDIR)/libcurl.so.2.0.2.s $(DESTDIR)$(libdir)/libcurl.so.2.0.2
	ln -s libcurl.so.3.0.0 $(DESTDIR)$(libdir)/libcurl.so.3
	ln -s libcurl.so.2.0.2 $(DESTDIR)$(libdir)/libcurl.so.2
	@$(MAKECOOKIE)

post-install-isa-i386:
	cp $(FILEDIR)/libcurl.so.3.0.0.i $(DESTDIR)$(libdir)/libcurl.so.3.0.0
	cp $(FILEDIR)/libcurl.so.2.0.2.i $(DESTDIR)$(libdir)/libcurl.so.2.0.2
	ln -s libcurl.so.3.0.0 $(DESTDIR)$(libdir)/libcurl.so.3
	ln -s libcurl.so.2.0.2 $(DESTDIR)$(libdir)/libcurl.so.2
	@$(MAKECOOKIE)

post-merge:
	ginstall $(FILEDIR)/curlbuild.h $(PKGROOT)$(includedir)/curl/curlbuild.h
	@$(MAKECOOKIE)
