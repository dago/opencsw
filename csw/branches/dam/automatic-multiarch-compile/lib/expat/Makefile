GARNAME = expat
PKGVERSION ?= 2.0.1
EXTRA_MODULATORS = PKGVERSION
MODULATIONS_PKGVERSION = 1.95.8 2.0.1
GARVERSION ?= $(PKGVERSION)
CATEGORIES = lib

DESCRIPTION = XML Parser Toolkit
define BLURB
	This is James Clark's Expat XML parser library in C. It is a stream oriented
	parser that requires setting handlers to deal with the structure that the
	parser discovers in the document.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(foreach VERSION,$(MODULATIONS_PKGVERSION),$(GARNAME)-$(VERSION).tar.gz)
DISTFILES += $(call admfiles,CSWexpat,)

# From
#   https://sourceforge.net/tracker/?func=detail&atid=110127&aid=1217217&group_id=10127
#   http://expat.cvs.sourceforge.net/viewvc/expat/expat/Makefile.in?r1=1.47&r2=1.48
PATCHFILES-pkgversion-1.95.8 = patch-libexpat-1.95.8-destdir.diff
PATCHFILES = $(PATCHFILES-pkgversion-$(PKGVERSION))

BUILD64 = 1

# The expat 'check' target tries to compile tests that use GCC
# constructs -- won't compile under Forte without hackery.
TEST_TARGET = check
TEST_SCRIPTS =

CONFIGURE_ARGS = $(DIRPATHS)

MERGE_SCRIPTS_isa-i386-pkgversion-1.95.8 = copy-only
MERGE_DIRS_isa-i386-pkgversion-1.95.8 = $(libdir)
MERGE_SCRIPTS_isa-amd64-pkgversion-1.95.8 = copy-relocated-only
MERGE_DIRS_isa-amd64-pkgversion-1.95.8 = $(libdir)

MERGE_SCRIPTS_isa-i386-pkgversion-2.0.1 = copy-all
MERGE_SCRIPTS_isa-amd64-pkgversion-2.0.1 = copy-relocated-only
MERGE_DIRS_isa-amd64-pkgversion-2.0.1 = $(bindir) $(sbindir) $(libexecdir) $(libdir)

include ../category.mk
