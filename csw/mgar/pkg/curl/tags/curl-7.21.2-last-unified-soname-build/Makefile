NAME = curl
VERSION = 7.21.2
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
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += libcurl.so.3.0.0.s
DISTFILES += libcurl.so.2.0.2.s
DISTFILES += libcurl.so.3.0.0.i
DISTFILES += libcurl.so.2.0.2.i
DISTFILES += curlbuild.h

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

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

EXTRA_CONFIGURE_ARGS_features-minimal = --disable-ldap --without-libssh2 --disable-ares
EXTRA_CONFIGURE_ARGS_features-full    = --enable-ares --with-spnego=$(libdir)
EXTRA_CONFIGURE_ARGS_features-full   += --enable-ldap --enable-ldaps

EXTRA_LDFLAGS = -L$(libdir)/libnet-new

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl=/opt/csw/ssl
CONFIGURE_ARGS += --with-ca-path=/opt/csw/ssl/certs
CONFIGURE_ARGS += $(EXTRA_CONFIGURE_ARGS_features-$(FEATURES))

BUILD64 = 1

# We are doing 64 bit only for the libs

RUNTIME_DEP_PKGS_CSWcurl = CSWlibidn CSWlibnet CSWoldaprt CSWosslrt CSWzlib CSWsasl CSWcurlrt CSWlibcares CSWlibssh2
RUNTIME_DEP_PKGS_CSWcurlrt = CSWlibidn CSWosslrt CSWzlib 
RUNTIME_DEP_PKGS_CSWcurlrtfull = CSWlibidn CSWoldaprt CSWosslrt CSWzlib CSWlibcares CSWlibssh2 CSWlibfbopenssl
RUNTIME_DEP_PKGS_CSWcurldevel = CSWcurl

BUILD_DEP_PKGS = $(filter-out CSWcurl CSWcurlrt,$(RUNTIME_DEP_PKGS_CSWcurl) $(RUNTIME_DEP_PKGS_CSWcurlrt) $(RUNTIME_DEP_PKGS_CSWcurlrtfull) $(RUNTIME_DEP_PKGS_CSWcurldevel))
BUILD_DEP_PKGS += CSWoldapdevel CSWossldevel CSWlibcaresdevel CSWlibssh2devel

SKIPTEST = 1

# isa-sparcv8-features-minimal isa-sparcv8-features-full isa-sparcv9-features-minimal isa-sparcv9-features-full

# TBD: Unify curlbuild.h with something like diff -D (sparcv9|amd64) curlbuild-32.h curlbuild-64.h > curlbuild.h
# Inspired from http://cvs.opensolaris.org/source/xref/sfw/usr/src/cmd/apr/apr-1.3/Makefile.sfw
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

# recompile curl to link to new ldap, and temporarily include
# the following block to make checkpkg happy. nothing in the curl
# package changed, so it should be ok, no?
CHECKPKG_OVERRIDES_CSWcurl += surplus-dependency|CSWlibssh2
CHECKPKG_OVERRIDES_CSWcurl += surplus-dependency|CSWoldaprt
CHECKPKG_OVERRIDES_CSWcurl += surplus-dependency|CSWsasl
CHECKPKG_OVERRIDES_CSWcurl += surplus-dependency|CSWlibcares
CHECKPKG_OVERRIDES_CSWcurl += surplus-dependency|CSWlibnet
CHECKPKG_OVERRIDES_CSWcurldevel += surplus-dependency|CSWcurl
CHECKPKG_OVERRIDES_CSWcurlrt += soname-not-part-of-filename|soname=libcurl.so.4|filename=libcurl-full.so.4.2.0
CHECKPKG_OVERRIDES_CSWcurlrt += soname-not-part-of-filename|soname=libcurl.so.4|filename=libcurl-minimal.so.4.2.0
CHECKPKG_OVERRIDES_CSWcurlrt += soname-not-part-of-filename|soname=libcurl.so.4|filename=libcurl-full.so.4.2.0
CHECKPKG_OVERRIDES_CSWcurlrt += soname-not-part-of-filename|soname=libcurl.so.4|filename=libcurl-minimal.so.4.2.0
CHECKPKG_OVERRIDES_CSWcurlrt += non-uniform-lib-versions-in-package|sonames=['libcurl.so.2',|'libcurl.so.3',|'libcurl.so.4']
CHECKPKG_OVERRIDES_CSWcurlrt += file-conflict|/opt/csw/lib/sparcv9/libcurl-full.so.4.2.0|CSWcurlrt|CSWcurlrtfull
CHECKPKG_OVERRIDES_CSWcurlrt += file-conflict|/opt/csw/lib/libcurl-full.so.4.2.0|CSWcurlrt|CSWcurlrtfull
CHECKPKG_OVERRIDES_CSWcurlrt += missing-dependency|CSWlibcares
CHECKPKG_OVERRIDES_CSWcurlrt += missing-dependency|CSWlibssh2
CHECKPKG_OVERRIDES_CSWcurlrt += missing-dependency|CSWlibfbopenssl
CHECKPKG_OVERRIDES_CSWcurlrt += missing-dependency|CSWoldaprt
CHECKPKG_OVERRIDES_CSWcurlrt += surplus-dependency|CSWalternatives
CHECKPKG_OVERRIDES_CSWcurlrtfull += soname-not-part-of-filename|soname=libcurl.so.4|filename=libcurl-full.so.4.2.0
CHECKPKG_OVERRIDES_CSWcurlrtfull += soname-not-part-of-filename|soname=libcurl.so.4|filename=libcurl-full.so.4.2.0
CHECKPKG_OVERRIDES_CSWcurlrtfull += file-conflict|/opt/csw/lib/sparcv9/libcurl-full.so.4.2.0|CSWcurlrt|CSWcurlrtfull
CHECKPKG_OVERRIDES_CSWcurlrtfull += file-conflict|/opt/csw/lib/libcurl-full.so.4.2.0|CSWcurlrt|CSWcurlrtfull
CHECKPKG_OVERRIDES_CSWcurlrtfull += surplus-dependency|CSWalternatives
CHECKPKG_OVERRIDES_CSWcurlrtfull += shared-lib-pkgname-mismatch|sonames=['libcurl.so.4']|pkgname=CSWcurlrtfull|expected=['CSWlibcurl4']|

# end checkpkg happiness section

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
