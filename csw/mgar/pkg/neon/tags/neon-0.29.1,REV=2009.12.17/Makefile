GARNAME = neon
GARVERSION = 0.29.1
CATEGORIES = lib

EXTRA_MODULATORS = GARVERSION
MODULATIONS_GARVERSION = 0.26.4 0.29.1

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

PACKAGES = CSWneon CSWneon-devel

CATALOGNAME_CSWneon = neon
CATALOGNAME_CSWneon-devel = neon_devel

REQUIRED_PKGS_CSWneon = CSWexpat CSWkrb5lib CSWosslrt CSWzlib CSWggettextrt CSWpakchois
REQUIRED_PKGS_CSWneon-devel = CSWneon

SPKG_DESC_CSWneon       = Neon HTTP and WebDAV client library
SPKG_DESC_CSWneon-devel = Neon HTTP and WebDAV development support

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --with-ssl=openssl
CONFIGURE_ARGS += --with-expat

BUILD64 = 1
NO_ISAEXEC = 1

# Omit version number suffix on docdir
INSTALL_OVERRIDE_VARS = docdir
INSTALL_OVERRIDE_VAR_docdir = $(datadir)/doc/neon

MERGE_SCRIPTS_isa-default-garversion-0.26.4 = copy-only
MERGE_DIRS_isa-default-garversion-0.26.4 = $(libdir)
MERGE_SCRIPTS_isa-default64-garversion-0.26.4 = copy-relocated-only
MERGE_DIRS_isa-default64-garversion-0.26.4 = $(libdir)

MERGE_SCRIPTS_isa-default-garversion-0.29.1 = copy-all
MERGE_SCRIPTS_isa-default64-garversion-0.29.1 = copy-relocated-only
MERGE_DIRS_isa-default64-garversion-0.29.1 = $(bindir) $(sbindir) $(libexecdir) $(libdir)

PKGFILES_CSWneon-devel = $(PKGFILES_DEVEL)
PKGFILES_CSWneon-devel += $(docdir)/.*

EXTRA_LINKER_FLAGS = -lintl

include gar/category.mk
