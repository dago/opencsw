GARNAME = liboggz
GARVERSION = 1.1.0
CATEGORIES = lib

DESCRIPTION = A commandline tool for manipulating Ogg files
define BLURB
  Oggz comprises liboggz and the tool oggz, which provides commands to inspect, edit
  and validate Ogg files. The oggz-chop tool can also be used to serve time ranges of
  Ogg media over HTTP by any web server that supports CGI.

  liboggz is a C library for reading and writing Ogg files and streams. It offers various
  improvements over the reference libogg, including support for seeking, validation and
  timestamp interpretation.
endef

MASTER_SITES = http://downloads.xiph.org/releases/liboggz/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
PATCHFILES = 0001-Remove-linker-version.patch
PATCHFILES += 0002-Add-getopt.h.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PREREQUISITE_PKGS = CSWdoxygen
REQUIRED_PKGS = CSWlibogg

BUILD64 = 1
NO_ISAEXEC = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk

# Solaris 10 does have getopt.h which interferes with the shipped one included first.
post-configure-isa-amd64:
	rm -f $(WORKSRC)/include/getopt.h
	@$(MAKECOOKIE)
