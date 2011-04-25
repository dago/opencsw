NAME = neon
VERSION = 0.29.5
CATEGORIES = lib

EXTRA_MODULATORS = VERSION FEATURES
MODULATIONS_VERSION = 0.26.4 0.29.5
MODULATIONS_FEATURES = minimal full

DESCRIPTION = Neon HTTP and WebDAV client library
define BLURB
  neon is an HTTP and WebDAV client library for Unix systems, with a C language
  API. It provides high-level interfaces to HTTP/1.1 and WebDAV methods, and a
  low-level interface to HTTP request/response handling, allowing new methods to
  be easily implemented.
endef

MASTER_SITES = http://www.webdav.org/$(NAME)/
SOURCEFILES  = $(foreach VERSION,$(MODULATIONS_VERSION), $(NAME)-$(VERSION).tar.gz)
DISTFILES  = $(SOURCEFILES)
DISTFILES += COPYING

NOEXTRACT = $(filter-out $(NAME)-$(VERSION).tar.gz,$(SOURCEFILES))

PACKAGES = CSWneon CSWneonfull CSWneon-devel

CATALOGNAME_CSWneon = neon
CATALOGNAME_CSWneonfull = neon_full
CATALOGNAME_CSWneon-devel = neon_devel

RUNTIME_DEP_PKGS_CSWneon = CSWexpat CSWosslrt CSWzlib CSWggettextrt
RUNTIME_DEP_PKGS_CSWneonfull = CSWexpat CSWosslrt CSWzlib CSWggettextrt CSWpakchois CSWlibproxy CSWkrb5lib
RUNTIME_DEP_PKGS_CSWneon-devel = CSWneon

BUILD_DEP_PKGS = $(sort $(RUNTIME_DEP_PKGS_CSWneon) $(RUNTIME_DEP_PKGS_CSWneonfull))

SPKG_DESC_CSWneon       = Neon HTTP and WebDAV client library (minimal dependencies)
SPKG_DESC_CSWneonfull   = Neon HTTP and WebDAV client library (full featured)
SPKG_DESC_CSWneon-devel = Neon HTTP and WebDAV development support

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS_features-minimal = --without-libproxy --without-pakchois --without-gssapi
CONFIGURE_ARGS_features-full = --with-libproxy --with-packchois

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared --enable-static
CONFIGURE_ARGS += --with-ssl=openssl
CONFIGURE_ARGS += --with-expat
CONFIGURE_ARGS += $(CONFIGURE_ARGS_features-$(FEATURES))

BUILD64 = 1
NOISAEXEC = 1

# Omit version number suffix on docdir
INSTALL_OVERRIDE_VARS = docdir
INSTALL_OVERRIDE_VAR_docdir = $(datadir)/doc/neon

# isa-sparcv8-garversion-0.26.4-features-minimal isa-sparcv8-garversion-0.26.4-features-full isa-sparcv8-garversion-0.29.5-features-minimal isa-sparcv8-garversion-0.29.5-features-full isa-sparcv9-garversion-0.26.4-features-minimal isa-sparcv9-garversion-0.26.4-features-full isa-sparcv9-garversion-0.29.5-features-minimal isa-sparcv9-garversion-0.29.5-features-full

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

MERGE_SCRIPTS_isa-default-garversion-0.29.5-features-minimal = copy-all
MERGE_SCRIPTS_isa-default64-garversion-0.29.5-features-minimal = copy-relocated-only
MERGE_DIRS_isa-default64-garversion-0.29.5-features-minimal = $(bindir) $(sbindir) $(libexecdir) $(libdir)
MERGE_SCRIPTS_isa-default-garversion-0.29.5-features-full = copy-only
MERGE_DIRS_isa-default-garversion-0.29.5-features-full = $(libdir)
MERGE_SCRIPTS_isa-default64-garversion-0.29.5-features-full = copy-relocated-only
MERGE_DIRS_isa-default64-garversion-0.29.5-features-full = $(libdir)

EXTRA_LINKER_FLAGS = -lintl

PKGFILES_CSWneonfull = .*-full.*
PKGFILES_CSWneon-devel = $(PKGFILES_DEVEL)
PKGFILES_CSWneon-devel += $(docdir)/.*


FEATURE_LIBRARIES  = libneon.26 libneon64.26
FEATURE_LIBRARIES += libneon.27 libneon64.27
FEATURES_libneon.26  = $(libdir)/libneon.so.26.0.4
FEATURES_libneon.26 += libneon-minimal.so.26.0.4
FEATURES_libneon.26 += libneon-full.so.26.0.4
FEATURES_libneon64.26  = $(libdir)/$(ISA_DEFAULT64)/libneon.so.26.0.4
FEATURES_libneon64.26 += libneon-minimal.so.26.0.4
FEATURES_libneon64.26 += libneon-full.so.26.0.4
FEATURES_libneon.27  = $(libdir)/libneon.so.27.2.3
FEATURES_libneon.27 += libneon-minimal.so.27.2.3
FEATURES_libneon.27 += libneon-full.so.27.2.3
FEATURES_libneon64.27  = $(libdir)/$(ISA_DEFAULT64)/libneon.so.27.2.3
FEATURES_libneon64.27 += libneon-minimal.so.27.2.3
FEATURES_libneon64.27 += libneon-full.so.27.2.3

# This comes from krb5-config --libs
CHECKPKG_OVERRIDES_CSWneonfull += bad-rpath-entry|/opt/csw/lib/|opt/csw/lib/libneon-full.so.26.0.4
CHECKPKG_OVERRIDES_CSWneonfull += bad-rpath-entry|/opt/csw/lib/|opt/csw/lib/libneon-full.so.27.2.3

CHECKPKG_OVERRIDES_CSWneon-devel += surplus-dependency|CSWneon
CHECKPKG_OVERRIDES_CSWneonfull += surplus-dependency|CSWpakchois
CHECKPKG_OVERRIDES_CSWneonfull += surplus-dependency|CSWosslrt
CHECKPKG_OVERRIDES_CSWneonfull += surplus-dependency|CSWggettextrt
CHECKPKG_OVERRIDES_CSWneonfull += surplus-dependency|CSWzlib
CHECKPKG_OVERRIDES_CSWneonfull += surplus-dependency|CSWexpat
CHECKPKG_OVERRIDES_CSWneonfull += surplus-dependency|CSWkrb5lib
CHECKPKG_OVERRIDES_CSWneonfull += surplus-dependency|CSWlibproxy
CHECKPKG_OVERRIDES_CSWneon += surplus-dependency|CSWexpat
CHECKPKG_OVERRIDES_CSWneon += surplus-dependency|CSWosslrt
CHECKPKG_OVERRIDES_CSWneon += surplus-dependency|CSWggettextrt
CHECKPKG_OVERRIDES_CSWneon += surplus-dependency|CSWzlib


include gar/category.mk

#post-install-modulated:
#	rm -f $(DESTDIR)$(libdir)/libneon.so
#	gln -s libneon.so.27 $(DESTDIR)$(libdir)/libneon.so
#	@$(MAKECOOKIE)

# cc -G -c empty.c
# ld -G -h libneon-minimal.so.26 -o stub-libneon.so.26 empty.o
# ld -R /opt/csw/lib -G -h libneon.so.26 -o libneon.so.26 -f libneon-full.so.26 -f libneon-max.so.26 stub-libneon.so.26

# 32/64 bit detection is done by looking at the last directory component and
# guessing by ISA if it is 32 or 64 bit

#post-merge: _LDFLAGS-32=
#post-merge: _LDFLAGS-64=-64
#post-merge:
#post-merge:
#	cd $(WORKDIR); touch empty.c; $(CC) -G -c empty.c
#	cd $(WORKDIR); touch empty64.c; $(CC) -m64 -G -c empty64.c
#	$(foreach L,$(FEATURE_LIBRARIES),\
#		ld $(_LDFLAGS-$(MEMORYMODEL_$(lastword $(subst /, ,$(dir $(firstword $(FEATURES_$L))))))) \
#			-G -h $(word 2,$(FEATURES_$L)) -o $(WORKDIR)/stub-$(notdir $(firstword $(FEATURES_$L))) $(WORKDIR)/empty$(MEMORYMODEL_$(lastword $(subst /, ,$(dir $(firstword $(FEATURES_$L)))))).o;\
#		ld $(_LDFLAGS-$(MEMORYMODEL_$(lastword $(subst /, ,$(dir $(firstword $(FEATURES_$L))))))) \
#			-R $(patsubst %/,%,$(dir $(firstword $(FEATURES_$L)))) \
#			-G -h `/usr/ccs/bin/dump -Lv $(dir $(firstword $(FEATURES_$L)))/$(word 2,$(FEATURES_$L)) | awk '$$2 == "SONAME" { print $$3 }'` \
#			-o $(PKGROOT)$(firstword $(FEATURES_$L)) \
#			$(foreach F,$(wordlist 3,$(words $(FEATURES_$L)),$(FEATURES_$L)),-F $F) \
#			$(WORKDIR)/stub-$(notdir $(firstword $(FEATURES_$L))); \
#	)
#	@$(MAKECOOKIE)

# ld -G -o ~/libtidy-minimal.so -z allextract -h libtidy.so.26 -F libtidy-full.so.26 /opt/csw/lib/libtidy.a 

