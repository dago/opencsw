GARNAME = neon
CURRENT_VERSION = 0.28.3
LEGACY_VERSIONS = 0.25.4 0.26.4 0.27.2
PKGVERSION ?= $(CURRENT_VERSION)
EXTRA_MODULATORS = PKGVERSION
MODULATIONS_PKGVERSION = $(LEGACY_VERSIONS) $(CURRENT_VERSION)
GARVERSION ?= $(PKGVERSION)
CATEGORIES = lib

DESCRIPTION = Neon HTTP and WebDAV client library
define BLURB
  neon is an HTTP and WebDAV client library for Unix systems, with a C language
  API. It provides high-level interfaces to HTTP/1.1 and WebDAV methods, and a
  low-level interface to HTTP request/response handling, allowing new methods to
  be easily implemented.
endef

MASTER_SITES = http://www.webdav.org/$(GARNAME)/
SOURCEFILES = $(foreach VERSION,$(MODULATIONS_PKGVERSION),$(GARNAME)-$(GARVERSION).tar.gz)
DISTFILES  = $(SOURCEFILES)
DISTFILES += $(call admfiles,CSWneon,depend)
DISTFILES += $(call admfiles,CSWneon-devel,depend)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --with-ssl=openssl
CONFIGURE_ARGS += --with-expat

BUILD64 = 1

MERGE_SCRIPTS_isa-i386-pkgversion-0.25.4 = copy-only
MERGE_DIRS_isa-i386-pkgversion-0.25.4 = $(libdir)
MERGE_SCRIPTS_isa-amd64-pkgversion-0.25.4 = copy-relocated-only
MERGE_DIRS_isa-amd64-pkgversion-0.25.4 = $(libdir)

MERGE_SCRIPTS_isa-i386-pkgversion-0.26.4 = copy-only
MERGE_DIRS_isa-i386-pkgversion-0.26.4 = $(libdir)
MERGE_SCRIPTS_isa-amd64-pkgversion-0.26.4 = copy-relocated-only
MERGE_DIRS_isa-amd64-pkgversion-0.26.4 = $(libdir)

MERGE_SCRIPTS_isa-i386-pkgversion-0.27.2 = copy-only
MERGE_DIRS_isa-i386-pkgversion-0.27.2 = $(libdir)
MERGE_SCRIPTS_isa-amd64-pkgversion-0.27.2 = copy-relocated-only
MERGE_DIRS_isa-amd64-pkgversion-0.27.2 = $(libdir)

MERGE_SCRIPTS_isa-i386-pkgversion-0.28.3 = copy-all
MERGE_SCRIPTS_isa-amd64-pkgversion-0.28.3 = copy-relocated-only
MERGE_DIRS_isa-amd64-pkgversion-0.28.3 = $(bindir) $(sbindir) $(libexecdir) $(libdir)

# Move development stuff to CSWneon-devel and put the rest in CSWneon
PKGFILES_CSWneon-devel_EXCLUSIVE = $(PKGFILES_DEVEL)
PKGFILES_CSWneon-devel_EXCLUSIVE += $(docdir)/.*

include ../category.mk
