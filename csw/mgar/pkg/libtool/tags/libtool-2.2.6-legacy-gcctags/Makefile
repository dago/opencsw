GARNAME = libtool
RELEASE = a
GARVERSION = 2.2.6
CATEGORIES = devel

EXTRA_MODULATORS = GARVERSION
MODULATIONS_GARVERSION = 1.5.26 2.2.6

FILEVERSION_1.5.26 = 1.5.26
FILEVERSION_2.2.6 = 2.2.6$(RELEASE)

DESCRIPTION = A generic library support tool
define BLURB
  GNU libtool is a generic library support script. Libtool hides the complexity
  of using shared and static libraries behind a consistent, portable interface.
  Libtool supports building static libraries on all platforms.
endef

MASTER_SITES = $(GNU_MIRROR)
SOURCEFILES  = $(foreach VERSION,$(MODULATIONS_GARVERSION),$(GARNAME)-$(FILEVERSION_$(VERSION)).tar.gz)
DISTFILES    = $(SOURCEFILES)
DISTFILES   += $(foreach ARCH,i386 sparc,$(ARCH)-gcc2.conf $(ARCH)-gcc2.tags $(ARCH)-gcc3.conf $(ARCH)-gcc3.tags)

PACKAGES = CSWlibtool CSWlibtoolrt
CATALOGNAME_CSWlibtoolrt = libtool_rt

SPKG_SOURCEURL = http://www.gnu.org/software/libtool/

REQUIRED_PKGS_CSWlibtool = CSWlibtoolrt

SPKG_DESC_CSWlibtool   = A generic library support tool
SPKG_DESC_CSWlibtoolrt = A Generic library support tool runtime libraries

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

BUILD64 = 1
NO_ISAEXEC = 1

SKIPTEST = 1
TEST_TARGET = check

MERGE_SCRIPTS_isa-i386-garversion-1.5.26 = copy-only
MERGE_DIRS_isa-i386-garversion-1.5.26 = $(libdir)
MERGE_SCRIPTS_isa-amd64-garversion-1.5.26 = copy-relocated-only
MERGE_DIRS_isa-amd64-garversion-1.5.26 = $(libdir)

MERGE_SCRIPTS_isa-i386-garversion-2.2.6 = copy-all
MERGE_SCRIPTS_isa-amd64-garversion-2.2.6 = copy-relocated-only
MERGE_DIRS_isa-amd64-garversion-2.2.6 = $(bindir) $(sbindir) $(libexecdir) $(libdir)

MERGE_SCRIPTS_isa-sparcv8-garversion-1.5.26 = copy-only
MERGE_DIRS_isa-sparcv8-garversion-1.5.26 = $(libdir)
MERGE_SCRIPTS_isa-sparcv9-garversion-1.5.26 = copy-relocated-only
MERGE_DIRS_isa-sparcv9-garversion-1.5.26 = $(libdir)

MERGE_SCRIPTS_isa-sparcv8-garversion-2.2.6 = copy-all
MERGE_SCRIPTS_isa-sparcv9-garversion-2.2.6 = copy-relocated-only
MERGE_DIRS_isa-sparcv9-garversion-2.2.6 = $(bindir) $(sbindir) $(libexecdir) $(libdir)

PKGFILES_CSWlibtoolrt = $(PKGFILES_RT)

include gar/category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)

post-install:
	@echo " ==> Fixing install anomalies"
	@rm -f $(DESTDIR)$(infodir)/dir
	@(for f in gcc2.conf gcc2.tags gcc3.conf gcc3.tags; do                                  \
		ginstall -D $(WORKDIR)/$(GARCH)-$$f $(DESTDIR)$(datadir)/$(GARNAME)/$$f;        \
	done)
	@$(MAKECOOKIE)

