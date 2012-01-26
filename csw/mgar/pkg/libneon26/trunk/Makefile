NAME = neon
VERSION = 0.26.4
CATEGORIES = lib
GARTYPE = v2

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

PACKAGES += CSWlibneon26
CATALOGNAME_CSWlibneon26 = libneon26
SPKG_DESC_CSWlibneon26 = Neon HTTP and WebDAV client library, libneon.so.26
PKGFILES_CSWlibneon26 += $(call pkgfiles_lib,libneon.so.26)
# Depend on the newer package as it contains the locale message files
RUNTIME_DEP_PKGS_CSWlibneon26 += CSWlibneon27
CHECKPKG_OVERRIDES_CSWlibneon26 += surplus-dependency|CSWlibneon27
RUNTIME_DEP_PKGS_CSWlibneon26 += CSWexpat
RUNTIME_DEP_PKGS_CSWlibneon26 += CSWosslrt
RUNTIME_DEP_PKGS_CSWlibneon26 += CSWzlib
RUNTIME_DEP_PKGS_CSWlibneon26 += CSWlibintl8

# These will go away later
CHECKPKG_OVERRIDES_CSWlibneon26 += unidentified-dependency|CSWlibneon27
CHECKPKG_OVERRIDES_CSWlibneon26 += file-collision|/opt/csw/lib/amd64/libneon.so.26|CSWlibneon26|CSWneon

PACKAGES += CSWlibneon26-feature
CATALOGNAME_CSWlibneon26_feature = libneon26_feature
SPKG_DESC_CSWlibneon26-feature = Neon HTTP and WebDAV client library with all features enabled, supersedes libneon.so.26
PKGFILES_CSWlibneon26-feature = $(call pkgfiles_lib,libneon-feature.so.26)
RUNTIME_DEP_PKGS_CSWlibneon26-feature += CSWlibneon26
CHECKPKG_OVERRIDES_CSWlibneon26-feature += surplus-dependency|CSWlibneon26
RUNTIME_DEP_PKGS_CSWlibneon26-feature += CSWexpat
RUNTIME_DEP_PKGS_CSWlibneon26-feature += CSWosslrt
RUNTIME_DEP_PKGS_CSWlibneon26-feature += CSWzlib
RUNTIME_DEP_PKGS_CSWlibneon26-feature += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibneon26-feature += CSWkrb5lib

# This comes from krb5-config --libs
CHECKPKG_OVERRIDES_CSWlibneon26-feature += bad-rpath-entry|/opt/csw/lib/|opt/csw/lib/libneon-feature.so.26.0.4

# These are artifacts of the feature lib being a regular one.
# As it is never linked against the soname doesn't matter here and the package name
# is obviously different from the soname in this case.
CHECKPKG_OVERRIDES_CSWlibneon26-feature += soname-not-part-of-filename|soname=libneon.so.26|filename=libneon-feature.so.26.0.4
CHECKPKG_OVERRIDES_CSWlibneon26-feature += soname-not-part-of-filename|soname=libneon.so.26|filename=libneon-feature.so.26.0.4
CHECKPKG_OVERRIDES_CSWlibneon26-feature += shared-lib-pkgname-mismatch

# These will go away after release
CHECKPKG_OVERRIDES_CSWlibneon26 += file-collision|/opt/csw/lib/libneon.so.26|CSWlibneon26|CSWneon
CHECKPKG_OVERRIDES_CSWlibneon26 += file-collision|/opt/csw/lib/sparcv9/libneon.so.26|CSWlibneon26|CSWneon

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
TEST_OVERRIDE_VARS = TZ
TEST_OVERRIDE_VAR_TZ = GMT

# Omit version number suffix on docdir
INSTALL_OVERRIDE_VARS = docdir
INSTALL_OVERRIDE_VAR_docdir = $(datadir)/doc/neon

EXTRA_PAX_ARGS_isa-sparcv8-features-full += -s ",.*/libneon\.so(\.\d+)?$$,," -s ",\(\.$(libdir)/libneon\)\(\.so\.\d+\..*\),\1-feature\2,p"
EXTRA_PAX_ARGS_isa-i386-features-full    += -s ",.*/libneon\.so(\.\d+)?$$,," -s ",\(\.$(libdir)/libneon\)\(\.so\.\d+\..*\),\1-feature\2,p"
EXTRA_PAX_ARGS_isa-sparcv9-features-full += -s ",.*/libneon\.so(\.\d+)?$$,," -s ",\.$(libdir)/libneon\(\.so\.\d+\..*\),.$(libdir_install)/$(ISA)/libneon-feature\1,p"
EXTRA_PAX_ARGS_isa-amd64-features-full   += -s ",.*/libneon\.so(\.\d+)?$$,," -s ",\.$(libdir)/libneon\(\.so\.\d+\..*\),.$(libdir_install)/$(ISA)/libneon-feature\1,p"

MERGE_SCRIPTS_isa-default-features-minimal = copy-only
MERGE_DIRS_isa-default-features-minimal = $(libdir)
MERGE_SCRIPTS_isa-default64-features-minimal = copy-relocated-only
MERGE_DIRS_isa-default64-features-minimal = $(libdir)
MERGE_SCRIPTS_isa-default-features-full = copy-only
MERGE_DIRS_isa-default-features-full = $(libdir)
MERGE_SCRIPTS_isa-default64-features-full = copy-relocated-only
MERGE_DIRS_isa-default64-features-full = $(libdir)

EXTRA_LINKER_FLAGS = -lintl

include gar/category.mk

post-build-isa-sparcv8-features-minimal post-build-isa-sparcv9-features-minimal post-build-isa-i386-features-minimal post-build-isa-amd64-features-minimal: EXTRA_LD_OPTIONS = -f libneon-feature.so.26
post-build-isa-sparcv8-features-minimal post-build-isa-sparcv9-features-minimal post-build-isa-i386-features-minimal post-build-isa-amd64-features-minimal:
	rm -f $(WORKSRC)/src/libneon.la
	$(BUILD_ENV) $(MAKE) $(PARALLELMFLAGS) $(foreach TTT,$(BUILD_OVERRIDE_VARS),$(TTT)="$(BUILD_OVERRIDE_VAR_$(TTT))") $(foreach TTT,$(BUILD_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $(WORKSRC) $(BUILD_ARGS)
	@$(MAKECOOKIE)

post-merge:
	@# This is needed because the substitutions from pax args do not change the
	@# contents of the symlink
	rm -f $(PKGROOT)$(libdir)/libneon-feature.so.26
	ln -s libneon-feature.so.26.0.4 $(PKGROOT)$(libdir)/libneon-feature.so.26
	rm -f $(PKGROOT)$(libdir)/$(ISA_DEFAULT64)/libneon-feature.so.26
	ln -s libneon-feature.so.26.0.4 $(PKGROOT)$(libdir)/$(ISA_DEFAULT64)/libneon-feature.so.26
