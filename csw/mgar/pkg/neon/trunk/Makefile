GARNAME = neon
GARVERSION = 0.28.4
CATEGORIES = lib

EXTRA_MODULATORS = GARVERSION
MODULATIONS_GARVERSION = 0.26.4 0.28.4

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
DISTFILES += $(call admfiles,CSWneon,)
DISTFILES += $(call admfiles,CSWneon-devel,)

REQUIRED_PKGS_CSWneon = CSWexpat CSWkrb5lib CSWosslrt CSWzlib
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

MERGE_SCRIPTS_isa-i386-garversion-0.26.4 = copy-only
MERGE_DIRS_isa-i386-garversion-0.26.4 = $(libdir)
MERGE_SCRIPTS_isa-amd64-garversion-0.26.4 = copy-relocated-only
MERGE_DIRS_isa-amd64-garversion-0.26.4 = $(libdir)

MERGE_SCRIPTS_isa-i386-garversion-0.28.4 = copy-all
MERGE_SCRIPTS_isa-amd64-garversion-0.28.4 = copy-relocated-only
MERGE_DIRS_isa-amd64-garversion-0.28.4 = $(bindir) $(sbindir) $(libexecdir) $(libdir)

MERGE_SCRIPTS_isa-sparcv8-garversion-0.26.4 = copy-only
MERGE_DIRS_isa-sparcv8-garversion-0.26.4 = $(libdir)
MERGE_SCRIPTS_isa-sparcv9-garversion-0.26.4 = copy-relocated-only
MERGE_DIRS_isa-sparcv9-garversion-0.26.4 = $(libdir)

MERGE_SCRIPTS_isa-sparcv8-garversion-0.28.4 = copy-all
MERGE_SCRIPTS_isa-sparcv9-garversion-0.28.4 = copy-relocated-only
MERGE_DIRS_isa-sparcv9-garversion-0.28.4 = $(bindir) $(sbindir) $(libexecdir) $(libdir)

PKGFILES_CSWneon-devel = $(PKGFILES_DEVEL)

EXTRA_LINKER_FLAGS = -lintl

include gar/category.mk
