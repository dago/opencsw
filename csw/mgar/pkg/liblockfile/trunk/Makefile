GARNAME = liblockfile
GARVERSION = 1.08
CATEGORIES = apps

DESCRIPTION = Liblockfile is a shared library with NFS-safe locking functions.
define BLURB
	Liblockfile is a shared library with NFS-safe locking functions. It
	includes the command line utility ``dotlockfile''.
endef

MASTER_SITES = ftp://ftp.debian.org/debian/pool/main/libl/$(GARNAME)/
DISTFILES  = $(GARNAME)_$(GARVERSION).orig.tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# The copyright information is stored in the COPYRIGHT file
LICENSE = COPYRIGHT

# Patches for Makefile.in
PATCHFILES = 0001-Modify-Makefile-to-use-ginstall-instead-of-install.patch 0002-Modify-Makefile.in-to-create-directories-first.patch 0003-Stop-ginstall-setting-ownership.patch

# Need to specify the installation prefix as the configuration script
# doesn't handle different operating systems very well
CONFIGURE_ARGS = $(DIRPATHS) --prefix=opt/csw

# liblockfile doesn't provide any tests so skip these
SKIPTEST=1

# We need to specify the ROOT path for this install
INSTALL_ARGS = ROOT=$(DESTDIR)

include gar/category.mk
