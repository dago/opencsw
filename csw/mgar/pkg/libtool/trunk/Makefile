PKGVERSION ?= 2.2.4
EXTRA_MODULATORS = PKGVERSION
MODULATIONS_PKGVERSION = 1.5.26 2.2.4
GARNAME = libtool
GARVERSION ?=$(PKGVERSION)
CATEGORIES = devel

DESCRIPTION = A generic library support tool.
define BLURB
  GNU libtool is a generic library support script. Libtool hides the complexity
  of using shared and static libraries behind a consistent, portable interface.
  Libtool supports building static libraries on all platforms.
endef

MASTER_SITES = $(GNU_MIRROR)
SOURCEFILES  = $(foreach VERSION, $(MODULATIONS_PKGVERSION), $(GARNAME)-$(VERSION).tar.gz)
DISTFILES    = $(SOURCEFILES)
DISTFILES   += $(call admfiles,CSWlibtool)
DISTFILES   += $(call admfiles,CSWlibtoolrt)
#NOEXTRACT    = $(filter-out $(GARNAME)-$(GARVERSION).tar.gz, $(SOURCEFILES))

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

BUILD64 = 1

SKIPTEST = 1
TEST_TARGET = check

MERGE_SCRIPTS_isa-i386-pkgversion-1.5.26 = copy-only
MERGE_DIRS_isa-i386-pkgversion-1.5.26 = $(libdir)
MERGE_SCRIPTS_isa-amd64-pkgversion-1.5.26 = copy-relocated-only
MERGE_DIRS_isa-amd64-pkgversion-1.5.26 = $(libdir)

MERGE_SCRIPTS_isa-i386-pkgversion-2.2.4 = copy-all
MERGE_SCRIPTS_isa-amd64-pkgversion-2.2.4 = copy-relocated-only
MERGE_DIRS_isa-amd64-pkgversion-2.2.4 = $(bindir) $(sbindir) $(libexecdir) $(libdir)

MERGE_SCRIPTS_isa-sparcv8-pkgversion-1.5.26 = copy-only
MERGE_DIRS_isa-sparcv8-pkgversion-1.5.26 = $(libdir)
MERGE_SCRIPTS_isa-sparcv9-pkgversion-1.5.26 = copy-relocated-only
MERGE_DIRS_isa-sparcv9-pkgversion-1.5.26 = $(libdir)

MERGE_SCRIPTS_isa-sparcv8-pkgversion-2.2.4 = copy-all
MERGE_SCRIPTS_isa-sparcv9-pkgversion-2.2.4 = copy-relocated-only
MERGE_DIRS_isa-sparcv9-pkgversion-2.2.4 = $(bindir) $(sbindir) $(libexecdir) $(libdir)

# Move runtime stuff to CSWlibtoolrt and put the rest in CSWlibtool
PKGFILES_CSWlibtoolrt_EXCLUSIVE = $(PKGFILES_RT)

include gar/category.mk

#pre-package:
#	@(for VERSION in $(OLD_VERSIONS); do gmake GARVERSION=$$VERSION install; done)
#	@$(MAKECOOKIE)

post-install:
	@echo " ==> Fixing install anomalies"
	@rm -f $(DESTDIR)$(prefix)/share/info/dir
	@$(MAKECOOKIE)

