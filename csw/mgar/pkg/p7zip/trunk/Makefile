# $Id$

NAME = p7zip
VERSION = 9.20.1
CATEGORIES = utils
GARTYPE = v2

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

MASTER_SITES = $(SF_MIRROR)
DISTNAME = $(NAME)_$(VERSION)
DISTFILES = $(DISTNAME)_src_all.tar.bz2
PATCHFILES += patch-CPP-7zip-Archive-Zip-ZipHandler.cpp
PATCHFILES += patch-install.sh
PATCHFILES += 0001-Disable-unrecognized-pragma.patch

VENDOR_URL = http://p7zip.sourceforge.net/
LICENSE =UPSTREAM_MASTER_SITES = http://sourceforge.net/projects/p7zip/files/p7zip/
UFILES_REGEX = p7zip_([\d\.]+)

PACKAGING_PLATFORMS = solaris9-i386 solaris9-sparc = DOCS/License.txt

# since there is no configure script, this is intentionally left empty
CONFIGURE_SCRIPTS =

# Defaults taken from makefile.solaris_sparc_CC_32
EXTRA_CPPFLAGS = -s -mt \
        -DHAVE_LONG_LONG \
        -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE \
        -DENV_UNIX \
        -DNDEBUG -D_REENTRANT
EXTRA_CPPFLAGS += -DBREAK_HANDLER -DUNICODE -D_UNICODE
EXTRA_CPPFLAGS += -I../../C

BUILD_OVERRIDE_VARS = CXX CC CC_SHARED LINK_SHARED LOCAL_LIBS LOCAL_LIBS_DLL OBJ_CRC32
BUILD_OVERRIDE_VAR_CXX = $(CXX) $(CPPFLAGS) $(CXXFLAGS)
BUILD_OVERRIDE_VAR_CC = $(CC) $(CPPFLAGS) $(CFLAGS)
BUILD_OVERRIDE_VAR_CC_SHARED = $(LDFLAGS) -KPIC
BUILD_OVERRIDE_VAR_LINK_SHARED = $(LDFLAGS) -KPIC -G
BUILD_OVERRIDE_VAR_LOCAL_LIBS = -lpthread -lCrun
BUILD_OVERRIDE_VAR_LOCAL_LIBS += -norunpath
BUILD_OVERRIDE_VAR_LOCAL_LIBS_DLL = -lpthread -lCrun -ldl
BUILD_OVERRIDE_VAR_LOCAL_LIBS_DLL += -norunpath
BUILD_OVERRIDE_VAR_OBJ_CRC32 = $$(OBJ_CRC32_C)

INSTALL_ARGS = DEST_HOME="$(DESTDIR)$(prefix)"
INSTALL_ARGS += DEST_MAN="$(Dinclude gar/category.mk
