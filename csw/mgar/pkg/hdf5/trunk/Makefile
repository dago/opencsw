GARNAME = hdf5
GARVERSION = 1.8.4
CATEGORIES = lib

EXTRA_MODULATORS = GARVERSION
MODULATIONS_GARVERSION = 1.6.10 1.8.4

SKIP_MODULATIONS = isa-sparcv9-garversion-1.6.10
SKIP_MODULATIONS += isa-amd64-garversion-1.6.10

DESCRIPTION = Event notification library
define BLURB
  The libevent API provides a mechanism to execute a callback function when a
  specific event occurs on a file descriptor or after a timeout has been
  reached. Furthermore, libevent also support callbacks due to signals or
  regular timeouts.
endef

MASTER_SITES = http://www.hdfgroup.org/ftp/HDF5/current/src/
MASTER_SITES += http://www.hdfgroup.org/ftp/HDF5/current16/src/
SOURCEFILES = $(foreach V,$(MODULATIONS_GARVERSION),$(GARNAME)-$V.tar.gz)
DISTFILES += $(SOURCEFILES)

NOEXTRACT = $(filter-out $(GARNAME)-$(GARVERSION).tar.gz,$(SOURCEFILES))

PACKAGES = CSWhdf5rt CSWhdf5

REQUIRED_PKGS_CSWhdf5 = CSWhdf5rt

CATALOGNAME_CSWhdf5 = hdf5
CATALOGNAME_CSWhdf5rt = hdf5_rt

SPKG_DESC_CSWhdf5 = HDF5 (Hierarchical Data Format 5) Software Utilities
SPKG_DESC_CSWhdf5rt = HDF5 (Hierarchical Data Format 5) Software Runtime Libraries

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.hdfgroup.org/HDF5/

BUILD64 = 1
NO_ISAEXEC = 1
CONFIGURE_ARGS  = $(DIRPATHS) 

TEST_TARGET = check

MERGE_SCRIPTS_isa-default-garversion-1.6.10 = copy-only
MERGE_DIRS_isa-default-garversion-1.6.10 = $(libdir)
MERGE_SCRIPTS_isa-extra-garversion-1.6.10 = copy-relocated-only
MERGE_DIRS_isa-extra-garversion-1.6.10 = $(libdir)

MERGE_SCRIPTS_isa-default-garversion-1.8.4 = copy-all
MERGE_SCRIPTS_isa-extra-garversion-1.8.4 = copy-relocated-only
MERGE_DIRS_isa-extra-garversion-1.8.4 = $(libdir)

PKGFILES_CSWhdf5rt = $(PKGFILES_RT)

include gar/category.mk

pre-install-modulated:
	ginstall -d $(DESTDIR)$(libdir)
	ginstall -d $(DESTDIR)$(includedir)
	ginstall -d $(DESTDIR)$(bindir)
	@$(MAKECOOKIE)
