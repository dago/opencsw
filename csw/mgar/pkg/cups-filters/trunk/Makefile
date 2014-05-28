# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = cups-filters
VERSION = 1.0.53
GARTYPE = v2

DESCRIPTION = Backends, filters and other software that was once part of the core CUPS distribution
define BLURB
  This project provides backends, filters, and other software that was once part of the core CUPS distribution but is no longer maintained by Apple Inc. In addition it contains additional filters and software developed independently of Apple, especially filters for the PDF-centric printing workflow introduced by OpenPrinting and a daemon to browse Bonjour broadcasts of remote CUPS printers to make these printers available locally and to provide backward compatibility to the old CUPS broadcasting and browsing of CUPS 1.5.x and older.
endef

MASTER_SITES = http://www.openprinting.org/download/cups-filters/
DISTFILES  = $(DISTNAME).tar.gz

GARCOMPILER = GCC4

BUILD_DEP_PKGS += CSWphp5
BUILD_DEP_PKGS += CSWghostscript
BUILD_DEP_PKGS += CSWlibjpeg-dev
BUILD_DEP_PKGS += CSWlibpng-dev
BUILD_DEP_PKGS += CSWlibtiff-dev

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

