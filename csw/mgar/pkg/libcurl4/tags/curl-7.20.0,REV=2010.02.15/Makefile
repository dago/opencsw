GARNAME = curl
GARVERSION = 7.20.0
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

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

PACKAGES = CSWcurl CSWcurlrt CSWcurlrtfull CSWcurldevel
CATALOGNAME_CSWcurl       = curl
CATALOGNAME_CSWcurlrt     = curl_rt
CATALOGNAME_CSWcurlrtfull = curl_rt_full
CATALOGNAME_CSWcurldevel  = curl_devel

SPKG_DESC_CSWcurl       = A command line tool and library for client-side URL transfers
SPKG_DESC_CSWcurlrt     = Curl Runtime Libraries (minimal dependencies)
SPKG_DESC_CSWcurlrtfull = Curl Runtime Libraries (full featured)
SPKG_DESC_CSWcurldevel  = Curl Developer Files

SPKG_SOURCEURL = http://curl.haxx.se

EXTRA_MODULATORS = FEATURES
MODULATIONS_FEATURES = minimal full

# amd64 is built without openldap because there are no libs available right now (Mantis 3028)
EXTRA_CONFIGURE_ARGS_LDAP_isa-sparcv8 = --enable-ldap --enable-ldaps
EXTRA_CONFIGURE_ARGS_LDAP_isa-sparcv9 = --enable-ldap --enable-ldaps
EXTRA_CONFIGURE_ARGS_LDAP_isa-i386    = --enable-ldap --enable-ldaps
EXTRA_CONFIGURE_ARGS_LDAP_isa-amd64   = --disable-ldap

EXTRA_CONFIGURE_ARGS_features-minimal = --disable-ldap --without-libssh2 --disable-ares
EXTRA_CONFIGURE_ARGS_features-full    = --enable-ares --with-spnego=$(libdir)
EXTRA_CONFIGURE_ARGS_features-full   += $(EXTRA_CONFIGURE_ARGS_LDAP_isa-$(ISA))

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl=/opt/csw/ssl
CONFIGURE_ARGS += --with-ca-path=/opt/csw/ssl/certs
CONFIGURE_ARGS += $(EXTRA_CONFIGURE_ARGS_features-$(FEATURES))

BUILD64 = 1

# We are doing 64 bit only for the libs
NOISAEXEC = 1

RUNTIME_DEP_PKGS_CSWcurl = CSWlibidn CSWlibnet CSWoldaprt CSWosslrt CSWzlib CSWsasl CSWcurlrt CSWlibcares CSWlibssh2
RUNTIME_DEP_PKGS_CSWcurlrt = CSWlibidn CSWosslrt CSWzlib 
RUNTIME_DEP_PKGS_CSWcurlrtfull = CSWlibidn CSWoldaprt CSWosslrt CSWzlib CSWlibcares CSWlibssh2 CSWlibfbopenssl
RUNTIME_DEP_PKGS_CSWcurldevel = CSWcurl

BUILD_DEP_PKGS = $(filter-out CSWcurl CSWcurlrt,$(RUNTIME_DEP_PKGS_CSWcurl) $(RUNTIME_DEP_PKGS_CSWcurlrt) $(RUNTIME_DEP_PKGS_CSWcurlrtfull) $(RUNTIME_DEP_PKGS_CSWcurldevel))
BUILD_DEP_PKGS += CSWoldapdevel CSWossldevel CSWlibcaresdevel CSWlibssh2devel

SKIPTEST = 1

# isa-sparcv8-features-minimal isa-sparcv8-features-full isa-sparcv9-features-minimal isa-sparcv9-features-full

EXTRA_PAX_ARGS_32 = -s ",^\.$(includedir)/curl/curlbuild.h$$,.$(includedir)/curl/curlbuild-32.h,p"
EXTRA_PAX_ARGS_64 = -s ",^\.$(includedir)/curl/curlbuild.h$$,.$(includedir)/curl/curlbuild-64.h,p"
EXTRA_PAX_ARGS_32 += -s ",$(libdir)/libcurl\.so\.4\.2\.0$$,$(libdir_install)/libcurl-$(FEATURES).so.4.2.0,p"
EXTRA_PAX_ARGS_64 += -s ",$(libdir)/libcurl\.so\.4\.2\.0$$,$(libdir_install)/$(ISA)/libcurl-$(FEATURES).so.4.2.0,p"
EXTRA_PAX_ARGS = $(EXTRA_PAX_ARGS_$(MEMORYMODEL))

# We select pkgconfig for minimal library bindings. As libneon is self-contained (links
# to all necessary libs directly) the full version can simly be linked in.
EXTRA_PAX_ARGS_features-full = -s ",.*/pkgconfig.*,,"
EXTRA_PAX_ARGS += $(EXTRA_PAX_ARGS_features-$(FEATURES))

MERGE_SCRIPTS_isa-default-features-minimal = copy-all
MERGE_SCRIPTS_isa-default64-features-minimal = copy-relocated-only
MERGE_DIRS_isa-default64-features-minimal = $(libdir)
MERGE_SCRIPTS_isa-default-features-full = copy-only
MERGE_DIRS_isa-default-features-full = $(libdir)
MERGE_SCRIPTS_isa-default64-features-full = copy-relocated-only
MERGE_DIRS_isa-default64-features-full = $(libdir)

ALTERNATIVES_CSWcurlrt = minimal
ALTERNATIVES_CSWcurlrtfull = full
ALTERNATIVE_minimal  = $(libdir)/libcurl.so.4.2.0 curl $(libdir)/libcurl-minimal.so.4.2.0 100
ALTERNATIVE_minimal += $(libdir)/$(ISA_DEFAULT64)/libcurl.so.4.2.0 curl64 $(libdir)/$(ISA_DEFAULT64)/libcurl-minimal.so.4.2.0
ALTERNATIVE_full     = $(libdir)/libcurl.so.4.2.0 curl $(libdir)/libcurl-full.so.4.2.0 200
ALTERNATIVE_full    += $(libdir)/$(ISA_DEFAULT64)/libcurl.so.4.2.0 curl64 $(libdir)/$(ISA_DEFAULT64)/libcurl-full.so.4.2.0

PKGFILES_CSWcurldevel = $(PKGFILES_DEVEL)
PKGFILES_CSWcurlrt = $(PKGFILES_RT)
PKGFILES_CSWcurlrtfull = .*-full.*

include gar/category.mk

post-install-isa-sparcv8-features-minimal:
	ginstall $(FILEDIR)/libcurl.so.3.0.0.s $(DESTDIR)$(libdir)/libcurl.so.3.0.0
	ginstall $(FILEDIR)/libcurl.so.2.0.2.s $(DESTDIR)$(libdir)/libcurl.so.2.0.2
	ln -s libcurl.so.3.0.0 $(DESTDIR)$(libdir)/libcurl.so.3
	ln -s libcurl.so.2.0.2 $(DESTDIR)$(libdir)/libcurl.so.2
	@$(MAKECOOKIE)

post-install-isa-i386-features-minimal:
	cp $(FILEDIR)/libcurl.so.3.0.0.i $(DESTDIR)$(libdir)/libcurl.so.3.0.0
	cp $(FILEDIR)/libcurl.so.2.0.2.i $(DESTDIR)$(libdir)/libcurl.so.2.0.2
	ln -s libcurl.so.3.0.0 $(DESTDIR)$(libdir)/libcurl.so.3
	ln -s libcurl.so.2.0.2 $(DESTDIR)$(libdir)/libcurl.so.2
	@$(MAKECOOKIE)

post-merge:
	ginstall $(FILEDIR)/curlbuild.h $(PKGROOT)$(includedir)/curl/curlbuild.h
	@$(MAKECOOKIE)
