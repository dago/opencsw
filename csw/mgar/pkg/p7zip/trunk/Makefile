GARNAME = p7zip
GARVERSION = 4.65
CATEGORIES = utils

DESCRIPTION = File archiver with high compression ratio
define BLURB
p7zip is a Unix port of 7-Zip, a file archiver with high compression
ratio (www.7-zip.org) with lots of features:

* 7-Zip is free software distributed under the GNU LGPL
* High compression ratio in new 7z format with LZMA compression
  o Unicode file names
  o Variable dictionary size (up to 4 GB)
  o Compressing speed: about 1 MB/s on 2 GHz CPU
  o Decompressing speed: about 10-20 MB/s on 2 GHz CPU
* Supported formats:
  o Packing / unpacking: 7z, ZIP, GZIP, BZIP2 and TAR
  o Unpacking only: RAR, CAB, ISO, ARJ, LZH, CHM, Z, CPIO, RPM, DEB
    and NSIS
* For ZIP and GZIP formats 7-Zip provides compression ratio that is
  2-10 % better than ratio provided by PKZip and WinZip
* Self-extracting capability for 7z format
endef

MASTER_SITES = http://garr.dl.sourceforge.net/sourceforge/p7zip/
DISTFILES  = $(GARNAME)_$(GARVERSION)_src_all.tar.bz2

# We define upstream file regex so we can be notifed of new upstream software 
# release, atm not used
# UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

# since there is no configure script, this is intentionally left empty
CONFIGURE_SCRIPTS =

# add CFLAGS
BUILD_ARGS = LOCAL_FLAGS="$(CFLAGS)"

# add INSTALL arguments
INSTALL_ARGS = DEST_HOME="$(DESTDIR)/$(prefix)"
INSTALL_ARGS += DEST_MAN="$(DESTDIR)/$(mandir)"

# fix distname
DISTNAME = $(GARNAME)_$(GARVERSION)

# patch files
PATCHFILES  = patch-CPP-7zip-Archive-Zip-ZipHandler.cpp
PATCHFILES += patch-install.sh

include gar/category.mk

# makefile
pre-build-modulated:
	@cp $(WORKSRC)/makefile.solaris_sparc_CC_32 $(WORKSRC)/makefile.machine
