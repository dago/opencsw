GARNAME = htmldoc
GARVERSION = 1.8.27
CATEGORIES = apps

DESCRIPTION = converts HTML files and web pages into indexed HTML PostScript and PDF
define BLURB
 HTMLDOC is a program for writing documentation in HTML and producing indexed
 HTML, PostScript, or PDF output (with tables of contents). It supports most
 HTML 3.2 and some HTML 4.0 syntax, as well as GIF, JPEG, and PNG images.
endef

PACKAGES = CSWhtmldoc-common CSWhtmldoc
CATALOGNAME_CSWhtmldoc = $(GARNAME)
CATALOGNAME_CSWhtmldoc-common = $(GARNAME)_common
SPKG_DESC_CSWhtmldoc = $(DESCRIPTION)
SPKG_DESC_CSWhtmldoc-common = This package contains the htmldoc files common to all architectures.
ARCHALL_CSWhtmldoc-common = 1

REQUIRED_PKGS_CSWhtmldoc  = CSWfltk CSWjpeg CSWosslrt CSWpng CSWzlib
REQUIRED_PKGS_CSWhtmldoc += CSWhtmldoc-common
#REQUIRED_PKGS_CSWhtmldoc-common = 

PKGFILES_CSWhtmldoc = $(bindir)/.*
PKGFILES_CSWhtmldoc-common = $(datadir)/.*

MASTER_SITES = http://ftp.easysw.com/pub/htmldoc/$(GARVERSION)/
DISTFILES  = $(GARNAME)-$(GARVERSION)-source.tar.bz2
#DISTFILES    += $(call admfiles,CSWhtmldoc, )
#DISTFILES    += $(call admfiles,CSWhtmldoc-common, )

LICENSE = COPYING.txt

SPKG_SOURCEURL = http://www.htmldoc.org

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)-source.tar.bz2

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PATCHFILES = mainpatch

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

# Disable check until package is released
#ENABLE_CHECK = 0
include gar/category.mk
