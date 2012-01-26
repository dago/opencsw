NAME = liboggz
VERSION = 1.1.1
CATEGORIES = lib
GARTYPE = v2

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
DISTFILES = $(DISTNAME).tar.gz
PATCHFILES = 0001-Remove-linker-version.patch

VENDOR_URL = http://www.xiph.org/oggz/

BUILD_DEP_PKGS = CSWdoxygen

PACKAGES += CSWliboggz2
SPKG_DESC_CSWliboggz2 = Ogg file manipulatin library, liboggz.so.2
PKGFILES_CSWliboggz2 = $(call pkgfiles_lib,liboggz.so.2)
RUNTIME_DEP_PKGS_CSWliboggz2 += CSWlibogg0

PACKAGES += CSWliboggz-dev
SPKG_DESC_CSWliboggz-dev = Development files for liboggz.so.2
PKGFILES_CSWliboggz-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWliboggz-dev += $(docdir)/.*
RUNTIME_DEP_PKGS_CSWliboggz-dev += CSWliboggz2

PACKAGES += CSWoggz
SPKG_DESC_CSWoggz = Commandline tools for manipulating Ogg files
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWoggz += CSWlibogg0
RUNTIME_DEP_PKGS_CSWoggz += CSWliboggz2
OBSOLETED_BY_CSWoggz = CSWliboggz
CATALOGNAME_CSWliboggz = liboggz_stub

BUILD64_LIBS_ONLY = 1

# This is just docs
CHECKPKG_OVERRIDES_CSWliboggz-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/liboggz/html/group__install.html
CHECKPKG_OVERRIDES_CSWliboggz-dev += file-with-bad-content|/usr/local|root/opt/csw/share/doc/liboggz/latex/group__install.tex

include gar/category.mk
