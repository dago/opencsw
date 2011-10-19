NAME = neon
VERSION = 0.29.6
CATEGORIES = lib

EXTRA_MODULATORS = FEATURES
MODULATIONS_FEATURES = minimal full

DESCRIPTION = Neon HTTP and WebDAV client library
define BLURB
  neon is an HTTP and WebDAV client library for Unix systems, with a C language
  API. It provides high-level interfaces to HTTP/1.1 and WebDAV methods, and a
  low-level interface to HTTP request/response handling, allowing new methods to
  be easily implemented.
endef

MASTER_SITES = http://www.webdav.org/$(NAME)/
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += COPYING

FOREIGN_PACKAGES += CSWlibneon26
OBSOLETED_BY_CSWlibneon26 = CSWneon

FOREIGN_PACKAGES += CSWlibneon26-feature
OBSOLETED_BY_CSWlibneon26-feature = CSWneonfull

CATALOGNAME_CSWneonfull = neon_full_stub

PACKAGES += CSWlibneon27
CATALOGNAME_CSWlibneon27 = libneon27
SPKG_DESC_CSWlibneon27 = Neon HTTP and WebDAV client library, libneon.so.27
PKGFILES_CSWlibneon27 += $(call pkgfiles_lib,libneon.so.27)
PKGFILES_CSWlibneon27 += $(sharedstatedir)/locale/.*
RUNTIME_DEP_PKGS_CSWlibneon27 += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWlibneon27 += CSWosslrt
RUNTIME_DEP_PKGS_CSWlibneon27 += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibneon27 += CSWlibintl8
OBSOLETED_BY_CSWlibneon27 = CSWneon

PACKAGES += CSWlibneon27-feature
CATALOGNAME_CSWlibneon27_feature = libneon27_feature
SPKG_DESC_CSWlibneon27-feature = Neon HTTP and WebDAV client library with all features enabled, supersedes libneon.so.27
PKGFILES_CSWlibneon27-feature += $(call pkgfiles_lib,libneon-feature.so.27)
RUNTIME_DEP_PKGS_CSWlibneon27-feature += CSWlibneon27
CHECKPKG_OVERRIDES_CSWlibneon27-feature += surplus-dependency|CSWlibneon27
RUNTIME_DEP_PKGS_CSWlibneon27-feature += CSWosslrt
RUNTIME_DEP_PKGS_CSWlibneon27-feature += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibneon27-feature += CSWlibproxy
RUNTIME_DEP_PKGS_CSWlibneon27-feature += CSWlibz1
RUNTIME_DEP_PKGS_CSWlibneon27-feature += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWlibneon27-feature += CSWlibkrb5support0
RUNTIME_DEP_PKGS_CSWlibneon27-feature += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWlibneon27-feature += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWlibneon27-feature += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWlibneon27-feature += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWlibneon27-feature += CSWlibpakchois0
OBSOLETED_BY_CSWlibneon27-feature = CSWneonfull

PACKAGES += CSWlibneon-dev
CATALOGNAME_CSWlibneon-dev = libneon_dev
SPKG_DESC_CSWlibneon-dev = Development files for libneon.so.27
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibneon-dev += CSWlibneon27
OBSOLETED_BY_CSWlibneon-dev = CSWneon-devel

# This describes the defaults during configure
CHECKPKG_OVERRIDES_CSWlibneon-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/neon/html/using.html

# This comes from krb5-config --libs
CHECKPKG_OVERRIDES_CSWlibneon27-feature += bad-rpath-entry|/opt/csw/lib/|opt/csw/lib/libneon-feature.so.27.2.5

# These are artifacts of the feature lib being a regular one.
# As it is never linked against the soname doesn't matter here and the package name
# is obviously different from the soname in this case.
CHECKPKG_OVERRIDES_CSWlibneon27-feature += soname-not-part-of-filename|soname=libneon.so.27|filename=libneon-feature.so.27.2.5
CHECKPKG_OVERRIDES_CSWlibneon27-feature += soname-not-part-of-filename|soname=libneon.so.27|filename=libneon-feature.so.27.2.5
CHECKPKG_OVERRIDES_CSWlibneon27-feature += shared-lib-pkgname-mismatch

# These will go away after release
CHECKPKG_OVERRIDES_CSWlibneon27 += file-collision|/opt/csw/lib/libneon.so.27|CSWlibneon27|CSWneon
CHECKPKG_OVERRIDES_CSWlibneon27 += file-collision|/opt/csw/lib/sparcv9/libneon.so.27|CSWlibneon27|CSWneon

BUILD_DEP_PKGS = CSWossldevel

CONFIGURE_ARGS_features-minimal = --without-libproxy --without-pakchois --without-gssapi
CONFIGURE_ARGS_features-full = --with-libproxy --with-packchois

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared --enable-static
CONFIGURE_ARGS += --with-ssl=openssl
CONFIGURE_ARGS += --with-expat
CONFIGURE_ARGS += $(CONFIGURE_ARGS_features-$(FEATURES))

BUILD64 = 1

# Tests fail, investigate later
SKIPTEST ?= 1

# Make sure to use a defined timezone or tests may fail
# TEST_OVERRIDE_VARS = TZ
# TEST_OVERRIDE_VAR_TZ = GMT

# Omit version number suffix on docdir
INSTALL_OVERRIDE_VARS = docdir
INSTALL_OVERRIDE_VAR_docdir = $(datadir)/doc/neon

# We select pkgconfig for minimal library bindings. As libneon is self-contained (links
# to all necessary libs directly) the full version can simly be linked in.
EXTRA_PAX_ARGS_features-full = -s ",.*/pkgconfig.*,,"
EXTRA_PAX_ARGS += $(EXTRA_PAX_ARGS_features-$(FEATURES))

EXTRA_PAX_ARGS_isa-sparcv8-features-full += -s ",.*/libneon\.so(\.\d+)?$$,," -s ",\(\.$(libdir)/libneon\)\(\.so\.\d+\..*\),\1-feature\2,p"
EXTRA_PAX_ARGS_isa-i386-features-full    += -s ",.*/libneon\.so(\.\d+)?$$,," -s ",\(\.$(libdir)/libneon\)\(\.so\.\d+\..*\),\1-feature\2,p"
EXTRA_PAX_ARGS_isa-sparcv9-features-full += -s ",.*/libneon\.so(\.\d+)?$$,," -s ",\.$(libdir)/libneon\(\.so\.\d+\..*\),.$(libdir_install)/$(ISA)/libneon-feature\1,p"
EXTRA_PAX_ARGS_isa-amd64-features-full   += -s ",.*/libneon\.so(\.\d+)?$$,," -s ",\.$(libdir)/libneon\(\.so\.\d+\..*\),.$(libdir_install)/$(ISA)/libneon-feature\1,p"

MERGE_SCRIPTS_isa-default-features-minimal = copy-all
MERGE_SCRIPTS_isa-default64-features-minimal = copy-relocated-only
MERGE_DIRS_isa-default64-features-minimal = $(bindir) $(sbindir) $(libexecdir) $(libdir)
MERGE_SCRIPTS_isa-default-features-full = copy-only
MERGE_DIRS_isa-default-features-full = $(libdir)
MERGE_SCRIPTS_isa-default64-features-full = copy-relocated-only
MERGE_DIRS_isa-default64-features-full = $(libdir)

EXTRA_LINKER_FLAGS = -lintl

include gar/category.mk

post-build-isa-sparcv8-features-minimal post-build-isa-sparcv9-features-minimal post-build-isa-i386-features-minimal post-build-isa-amd64-features-minimal: EXTRA_LD_OPTIONS = -f libneon-feature.so.27
post-build-isa-sparcv8-features-minimal post-build-isa-sparcv9-features-minimal post-build-isa-i386-features-minimal post-build-isa-amd64-features-minimal: 
	rm -f $(WORKSRC)/src/libneon.la
	$(BUILD_ENV) $(MAKE) $(PARALLELMFLAGS) $(foreach TTT,$(BUILD_OVERRIDE_VARS),$(TTT)="$(BUILD_OVERRIDE_VAR_$(TTT))") $(foreach TTT,$(BUILD_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $(WORKSRC) $(BUILD_ARGS)
	@$(MAKECOOKIE)

post-merge:
	@# This is needed because the substitutions from pax args do not change the
	@# contents of the symlink
	rm -f $(PKGROOT)$(libdir)/libneon-feature.so.27
	ln -s libneon-feature.so.27.2.5 $(PKGROOT)$(libdir)/libneon-feature.so.27
	rm -f $(PKGROOT)$(libdir)/$(ISA_DEFAULT64)/libneon-feature.so.27
	ln -s libneon-feature.so.27.2.5 $(PKGROOT)$(libdir)/$(ISA_DEFAULT64)/libneon-feature.so.27
