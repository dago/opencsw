NAME = libsigsegv
VERSION = 2.9
CATEGORIES = lib
EXTRA_MODULATORS = VERSION
MODULATIONS_VERSION = 2.6 2.9

DESCRIPTION = A library for catching and handling segmentation faults
define BLURB
  This is a library for handling page faults in user mode. A page fault occurs
  when a program tries to access to a region of memory that is currently not available.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

SOURCEFILES = $(foreach VERSION,$(MODULATIONS_VERSION),$(NAME)-$(VERSION).tar.gz)
DISTFILES = $(SOURCEFILES)
NOEXTRACT = $(filter-out $(NAME)-$(VERSION).tar.gz, $(SOURCEFILES))

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES += CSWlibsigsegv0
PACKAGES += CSWlibsigsegv2
PACKAGES += CSWlibsigsegv-devel
PACKAGES += CSWlibsigsegv

CATALOGNAME_CSWlibsigsegv0 = libsigsegv0
CATALOGNAME_CSWlibsigsegv2 = libsigsegv2
CATALOGNAME_CSWlibsigsegv-devel = libsigsegv_devel
CATALOGNAME_CSWlibsigsegv = libsigsegv

SPKG_DESC_CSWlibsigsegv0 = A library for catching and handling segmentation faults, libsigsegv.so.0
SPKG_DESC_CSWlibsigsegv2 = A library for catching and handling segmentation faults, libsigsegv.so.2
SPKG_DESC_CSWlibsigsegv = Empty stub as contents has been moved to CSWlibsigsegv0
SPKG_DESC_CSWlibsigsegv-devel = Development files for libsigsegv

# This is a legacy stub dependency only. Remove after last package to CSWlibsigsegv has been updated.
RUNTIME_DEP_PKGS_CSWlibsigsegv = CSWlibsigsegv0
CHECKPKG_OVERRIDES_CSWlibsigsegv += surplus-dependency|CSWlibsigsegv0

ARCHALL_CSWlibsigsegv = 1

SPKG_SOURCEURL = http://www.gnu.org/software/libsigsegv/

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared --disable-static

TEST_TARGET = check

MERGE_SCRIPTS_isa-default-garversion-2.6 = copy-only
MERGE_DIRS_isa-default-garversion-2.6 = $(libdir)
MERGE_SCRIPTS_isa-default64-garversion-2.6 = copy-relocated-only
MERGE_DIRS_isa-default64-garversion-2.6 = $(libdir)

MERGE_SCRIPTS_isa-default-garversion-2.9 = copy-all
MERGE_SCRIPTS_isa-default64-garversion-2.9 = copy-relocated-only
MERGE_DIRS_isa-default64-garversion-2.9 = $(bindir) $(sbindir) $(libexecdir) $(libdir)

PKGFILES_CSWlibsigsegv0 += $(call baseisadirs,$(libdir),[^/]*\.so\.0\.[0-9\.]+)
PKGFILES_CSWlibsigsegv2 += $(call baseisadirs,$(libdir),[^/]*\.so\.2\.[0-9\.]+)
PKGFILES_CSWlibsigsegv = NOFILES
PKGFILES_CSWlibsigsegv-devel = $(PKGFILES_DEVEL)


include gar/category.mk
