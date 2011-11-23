# TBD:
# - Link against new libfbopenssl0
# - Link against new librtmp0

NAME = curl
VERSION = 7.23.1
CATEGORIES = net

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
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

FOREIGN_PACKAGES += CSWlibcurl2
OBSOLETED_BY_CSWlibcurl2 += CSWcurlrt
CATALOGNAME_CSWcurlrt = curl_rt_stub

FOREIGN_PACKAGES += CSWlibcurl3
OBSOLETED_BY_CSWlibcurl3 += CSWcurlrt

PACKAGES += CSWlibcurl4
CATALOGNAME_CSWlibcurl4 = libcurl4
SPKG_DESC_CSWlibcurl4 = Library for client-side URL transfers, libcurl.so.4
PKGFILES_CSWlibcurl4 = $(call pkgfiles_lib,libcurl.so.4)
OBSOLETED_BY_CSWlibcurl4 = CSWcurlrt
RUNTIME_DEP_PKGS_CSWlibcurl4 += CSWosslrt
RUNTIME_DEP_PKGS_CSWlibcurl4 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibcurl4 += CSWlibidn11

PACKAGES += CSWlibcurl4-feature
CATALOGNAME_CSWlibcurl4-feature = libcurl4_feature
SPKG_DESC_CSWlibcurl4-feature = Full-features library for client-side URL transfers superseding libcurl.so.4
PKGFILES_CSWlibcurl4-feature = $(call pkgfiles_lib,libcurl-feature.so.4)
RUNTIME_DEP_PKGS_CSWlibcurl4-feature += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibcurl4-feature += CSWlibfbopenssl0
RUNTIME_DEP_PKGS_CSWlibcurl4-feature += CSWlibidn11
RUNTIME_DEP_PKGS_CSWlibcurl4-feature += CSWosslrt
RUNTIME_DEP_PKGS_CSWlibcurl4-feature += CSWoldaprt
RUNTIME_DEP_PKGS_CSWlibcurl4-feature += CSWlibssh2
RUNTIME_DEP_PKGS_CSWlibcurl4-feature += CSWlibcares2
RUNTIME_DEP_PKGS_CSWlibcurl4-feature += CSWlibrtmp0

# These are artifacts of the feature lib being a regular one.
# As it is never linked against the soname doesn't matter here and the package name
# is obviously different from the soname in this case.
CHECKPKG_OVERRIDES_CSWlibcurl4-feature += shared-lib-pkgname-mismatch
CHECKPKG_OVERRIDES_CSWlibcurl4-feature += soname-not-part-of-filename

PACKAGES += CSWlibcurl-dev
CATALOGNAME_CSWlibcurl-dev = libcurl_dev
SPKG_DESC_CSWlibcurl-dev = Development files for libcurl.so.4
PKGFILES_CSWlibcurl-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibcurl-dev = CSWlibcurl4
OBSOLETED_BY_CSWlibcurl-dev = CSWcurldevel
CATALOGNAME_CSWcurldevel = curl_devel_stub

PACKAGES += CSWcurl
CATALOGNAME_CSWcurl = curl
SPKG_DESC_CSWcurl = A command line tool and library for client-side URL transfers
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWcurl += CSWlibz1
RUNTIME_DEP_PKGS_CSWcurl += CSWlibidn11
RUNTIME_DEP_PKGS_CSWcurl += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWcurl += CSWosslrt
# Double-legacy packages may not even depend on CSWcurlrt, so we must
# also directly depend on CSWlibcurl2 and CSWlibcurl3
RUNTIME_DEP_PKGS_CSWcurl += CSWlibcurl2
RUNTIME_DEP_PKGS_CSWcurl += CSWlibcurl3
CHECKPKG_OVERRIDES_CSWcurl += surplus-dependency|CSWlibcurl2
CHECKPKG_OVERRIDES_CSWcurl += surplus-dependency|CSWlibcurl3

BUILD_DEP_PKGS += CSWoldapdevel
BUILD_DEP_PKGS += CSWossldevel
BUILD_DEP_PKGS += CSWlibcares-dev
BUILD_DEP_PKGS += CSWlibssh2devel
BUILD_DEP_PKGS += CSWlibfbopenssl-dev
BUILD_DEP_PKGS += CSWlibrtmp-dev

VENDOR_URL = http://curl.haxx.se

EXTRA_MODULATORS = FEATURES
MODULATIONS_FEATURES = minimal full

EXTRA_CONFIGURE_ARGS_features-minimal += --disable-ldap
EXTRA_CONFIGURE_ARGS_features-minimal += --without-libssh2
EXTRA_CONFIGURE_ARGS_features-minimal += --disable-ares
EXTRA_CONFIGURE_ARGS_features-minimal += --without-librtmp

EXTRA_CONFIGURE_ARGS_features-full += --enable-ares
EXTRA_CONFIGURE_ARGS_features-full += --with-spnego=$(libdir)
EXTRA_CONFIGURE_ARGS_features-full += --enable-ldap
EXTRA_CONFIGURE_ARGS_features-full += --enable-ldaps

# Make sure to link to the new libnet. See for details http://wiki.opencsw.org/project-libnet
EXTRA_LDFLAGS = -L$(libdir)/libnet-new

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --with-ssl=/opt/csw/ssl
CONFIGURE_ARGS += --with-ca-path=/opt/csw/ssl/certs
CONFIGURE_ARGS += $(EXTRA_CONFIGURE_ARGS_features-$(FEATURES))

BUILD64 = 1

# There are some failing tests, ignore for now
SKIPTEST ?= 1

# We do special 32/64 merging for this one, see post-merge
EXTRA_MERGE_EXCLUDE_FILES += $(includedir)/curl/curlbuild.h

EXTRA_PAX_ARGS_isa-sparcv8-features-full += -s ",.*/libcurl\.so(\.\d+)?$$,," -s ",\(\.$(libdir)/libcurl\)\(\.so\.\d+\..*\),\1-feature\2,p"
EXTRA_PAX_ARGS_isa-i386-features-full    += -s ",.*/libcurl\.so(\.\d+)?$$,," -s ",\(\.$(libdir)/libcurl\)\(\.so\.\d+\..*\),\1-feature\2,p"
EXTRA_PAX_ARGS_isa-sparcv9-features-full += -s ",.*/libcurl\.so(\.\d+)?$$,," -s ",\.$(libdir)/libcurl\(\.so\.\d+\..*\),.$(libdir_install)/$(ISA)/libcurl-feature\1,p"
EXTRA_PAX_ARGS_isa-amd64-features-full   += -s ",.*/libcurl\.so(\.\d+)?$$,," -s ",\.$(libdir)/libcurl\(\.so\.\d+\..*\),.$(libdir_install)/$(ISA)/libcurl-feature\1,p"

# We select pkgconfig for minimal library bindings. As libneon is self-contained (links
# to all necessary libs directly) the full version can simly be linked in.
EXTRA_PAX_ARGS_features-full = -s ",.*/pkgconfig.*,,"
EXTRA_PAX_ARGS += $(EXTRA_PAX_ARGS_features-$(FEATURES))

MERGE_SCRIPTS_isa-default-features-minimal = copy-all
MERGE_SCRIPTS_isa-default64-features-minimal = copy-relocated-only copy-config-only
MERGE_DIRS_isa-default64-features-minimal = $(libdir)
MERGE_SCRIPTS_isa-default-features-full = copy-only
MERGE_DIRS_isa-default-features-full = $(libdir)
MERGE_SCRIPTS_isa-default64-features-full = copy-relocated-only
MERGE_DIRS_isa-default64-features-full = $(libdir)

# TBD: Use alternatives on curl-config between minimal and feature as it is possible to
# use options to find out about installed features and protocols by calling it.

include gar/category.mk

# These are not really necessary and they confuse the linker as described in #4550
$(GARCOMPILER)_LD_FLAGS :=

# Rebuild the minimal library with AUX linkage to feature library
post-build-isa-sparcv8-features-minimal post-build-isa-sparcv9-features-minimal post-build-isa-i386-features-minimal post-build-isa-amd64-features-minimal: EXTRA_LD_OPTIONS = -f libcurl-feature.so.4
post-build-isa-sparcv8-features-minimal post-build-isa-sparcv9-features-minimal post-build-isa-i386-features-minimal post-build-isa-amd64-features-minimal: 
	rm -f $(WORKSRC)/lib/libcurl.la
	$(BUILD_ENV) $(MAKE) $(PARALLELMFLAGS) $(foreach TTT,$(BUILD_OVERRIDE_VARS),$(TTT)="$(BUILD_OVERRIDE_VAR_$(TTT))") $(foreach TTT,$(BUILD_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $(WORKSRC)/lib $(BUILD_ARGS)
	@$(MAKECOOKIE)

post-merge:
	@# This is needed because the substitutions from pax args do not change the
	@# contents of the symlink
	rm -f $(PKGROOT)$(libdir)/libcurl-feature.so.4
	ln -s libcurl-feature.so.4.2.0 $(PKGROOT)$(libdir)/libcurl-feature.so.4
	rm -f $(PKGROOT)$(libdir)/$(ISA_DEFAULT64)/libcurl-feature.so.4
	ln -s libcurl-feature.so.4.2.0 $(PKGROOT)$(libdir)/$(ISA_DEFAULT64)/libcurl-feature.so.4
	pwd
	gdiff -D 64bit \
		$(WORKROOTDIR)/install-isa-$(ISA_DEFAULT64)-features-minimal$(includedir)/curl/curlbuild.h \
		$(WORKROOTDIR)/install-isa-$(ISA_DEFAULT)-features-minimal$(includedir)/curl/curlbuild.h \
		| sed -e 's/ifndef 64bit/if defined __amd64 || defined __x86_64 || defined __sparcv9/' \
		> $(PKGROOT)$(includedir)/curl/curlbuild.h
	@$(MAKECOOKIE)
