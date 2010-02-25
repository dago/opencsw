GARNAME = neon
GARVERSION = 0.29.3
CATEGORIES = lib

EXTRA_MODULATORS = GARVERSION FEATURES
MODULATIONS_GARVERSION = 0.26.4 0.29.3
MODULATIONS_FEATURES = minimal full

DESCRIPTION = Neon HTTP and WebDAV client library
define BLURB
  neon is an HTTP and WebDAV client library for Unix systems, with a C language
  API. It provides high-level interfaces to HTTP/1.1 and WebDAV methods, and a
  low-level interface to HTTP request/response handling, allowing new methods to
  be easily implemented.
endef

MASTER_SITES = http://www.webdav.org/$(GARNAME)/
SOURCEFILES  = $(foreach VERSION,$(MODULATIONS_GARVERSION), $(GARNAME)-$(VERSION).tar.gz)
DISTFILES  = $(SOURCEFILES)
DISTFILES += COPYING

NOEXTRACT = $(filter-out $(GARNAME)-$(GARVERSION).tar.gz,$(SOURCEFILES))

PACKAGES = CSWneon CSWneonfull CSWneon-devel

CATALOGNAME_CSWneon = neon
CATALOGNAME_CSWneonfull = neon_full
CATALOGNAME_CSWneon-devel = neon_devel

RUNTIME_DEP_PKGS_CSWneon = CSWexpat CSWosslrt CSWzlib CSWggettextrt
RUNTIME_DEP_PKGS_CSWneonfull = CSWexpat CSWosslrt CSWzlib CSWggettextrt CSWpakchois CSWlibproxy
RUNTIME_DEP_PKGS_CSWneon-devel = CSWneon

BUILD_DEP_PKGS = $(sort $(RUNTIME_DEP_PKGS_CSWneon) $(RUNTIME_DEP_PKGS_CSWneonfull))

SPKG_DESC_CSWneon       = Neon HTTP and WebDAV client library (minimal dependencies)
SPKG_DESC_CSWneonfull   = Neon HTTP and WebDAV client library (full featured)
SPKG_DESC_CSWneon-devel = Neon HTTP and WebDAV development support

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS_features-minimal = --without-libproxy --without-pakchois --without-gssapi
CONFIGURE_ARGS_features-full = --with-libproxy --with-packchois

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --with-ssl=openssl
CONFIGURE_ARGS += --with-expat
CONFIGURE_ARGS += $(CONFIGURE_ARGS_features-$(FEATURES))

BUILD64 = 1
NOISAEXEC = 1

# Omit version number suffix on docdir
INSTALL_OVERRIDE_VARS = docdir
INSTALL_OVERRIDE_VAR_docdir = $(datadir)/doc/neon

# isa-sparcv8-garversion-0.26.4-features-minimal isa-sparcv8-garversion-0.26.4-features-full isa-sparcv8-garversion-0.29.3-features-minimal isa-sparcv8-garversion-0.29.3-features-full isa-sparcv9-garversion-0.26.4-features-minimal isa-sparcv9-garversion-0.26.4-features-full isa-sparcv9-garversion-0.29.3-features-minimal isa-sparcv9-garversion-0.29.3-features-full

# We select pkgconfig for minimal library bindings. As libneon is self-contained (links
# to all necessary libs directly) the full version can simly be linked in.
EXTRA_PAX_ARGS_features-full = -s ",.*/pkgconfig.*,,"
EXTRA_PAX_ARGS += $(EXTRA_PAX_ARGS_features-$(FEATURES))

EXTRA_PAX_ARGS-32 += -s ",\(\.$(libdir)/libneon\)\(\.so\.26\.0\.4\),\1-$(FEATURES)\2,p"
EXTRA_PAX_ARGS-32 += -s ",\(\.$(libdir)/libneon\)\(\.so\.27\.2\.3\),\1-$(FEATURES)\2,p"
EXTRA_PAX_ARGS-64 += -s ",\.$(libdir)/libneon\(\.so\.26\.0\.4\),.$(libdir_install)/$(ISA)/libneon-$(FEATURES)\1,p"
EXTRA_PAX_ARGS-64 += -s ",\.$(libdir)/libneon\(\.so\.27\.2\.3\),.$(libdir_install)/$(ISA)/libneon-$(FEATURES)\1,p"
EXTRA_PAX_ARGS += $(EXTRA_PAX_ARGS-$(MEMORYMODEL))

MERGE_SCRIPTS_isa-default-garversion-0.26.4-features-minimal = copy-only
MERGE_DIRS_isa-default-garversion-0.26.4-features-minimal = $(libdir)
MERGE_SCRIPTS_isa-default64-garversion-0.26.4-features-minimal = copy-relocated-only
MERGE_DIRS_isa-default64-garversion-0.26.4-features-minimal = $(libdir)
MERGE_SCRIPTS_isa-default-garversion-0.26.4-features-full = copy-only
MERGE_DIRS_isa-default-garversion-0.26.4-features-full = $(libdir)
MERGE_SCRIPTS_isa-default64-garversion-0.26.4-features-full = copy-relocated-only
MERGE_DIRS_isa-default64-garversion-0.26.4-features-full = $(libdir)

MERGE_SCRIPTS_isa-default-garversion-0.29.3-features-minimal = copy-all
MERGE_SCRIPTS_isa-default64-garversion-0.29.3-features-minimal = copy-relocated-only
MERGE_DIRS_isa-default64-garversion-0.29.3-features-minimal = $(bindir) $(sbindir) $(libexecdir) $(libdir)
MERGE_SCRIPTS_isa-default-garversion-0.29.3-features-full = copy-only
MERGE_DIRS_isa-default-garversion-0.29.3-features-full = $(libdir)
MERGE_SCRIPTS_isa-default64-garversion-0.29.3-features-full = copy-relocated-only
MERGE_DIRS_isa-default64-garversion-0.29.3-features-full = $(libdir)

EXTRA_LINKER_FLAGS = -lintl

PKGFILES_CSWneonfull = .*-full.*
PKGFILES_CSWneon-devel = $(PKGFILES_DEVEL)
PKGFILES_CSWneon-devel += $(docdir)/.*

ALTERNATIVES_CSWneon = minimal
ALTERNATIVES_CSWneonfull = full

ALTERNATIVE_minimal  = $(libdir)/libneon.so.27.2.3 neon $(libdir)/libneon-minimal.so.27.2.3 100
ALTERNATIVE_minimal += $(libdir)/$(ISA_DEFAULT64)/libneon.so.27.2.3 neon64 $(libdir)/$(ISA_DEFAULT64)/libneon-minimal.so.27.2.3
ALTERNATIVE_minimal += $(libdir)/libneon.so.26.0.4 neon.26 $(libdir)/libneon-minimal.so.26.0.4
ALTERNATIVE_minimal += $(libdir)/$(ISA_DEFAULT64)/libneon.so.26.0.4 neon64.26 $(libdir)/$(ISA_DEFAULT64)/libneon-minimal.so.26.0.4

ALTERNATIVE_full     = $(libdir)/libneon.so.27.2.3 neon $(libdir)/libneon-full.so.27.2.3 200
ALTERNATIVE_full    += $(libdir)/$(ISA_DEFAULT64)/libneon.so.27.2.3 neon64 $(libdir)/$(ISA_DEFAULT64)/libneon-full.so.27.2.3
ALTERNATIVE_full    += $(libdir)/libneon.so.26.0.4 neon.26 $(libdir)/libneon-full.so.26.0.4
ALTERNATIVE_full    += $(libdir)/$(ISA_DEFAULT64)/libneon.so.26.0.4 neon64.26 $(libdir)/$(ISA_DEFAULT64)/libneon-full.so.26.0.4

include gar/category.mk

#post-install-modulated:
#	rm -f $(DESTDIR)$(libdir)/libneon.so
#	gln -s libneon.so.27 $(DESTDIR)$(libdir)/libneon.so
#	@$(MAKECOOKIE)
