GARNAME = htmldoc
GARVERSION = 1.8.27
CATEGORIES = apps

DESCRIPTION = converts HTML files and web pages into indexed HTML PostScript and PDF
define BLURB
	HTMLDOC converts Hyper-Text Markup Language ("HTML") files and web pages into
	indexed HTML, Adobe® PostScript®, or Adobe Portable Document Format ("PDF")
	files.
endef

MASTER_SITES = http://ftp.easysw.com/pub/htmldoc/$(GARVERSION)/
DISTFILES  = $(GARNAME)-$(GARVERSION)-source.tar.bz2

SPKG_SOURCEURL = http://www.htmldoc.org

LICENSE = COPYING.txt

REQUIRED_PKGS = CSWfltk CSWjpeg CSWosslrt CSWpng CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)-source.tar.bz2

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PATCHFILES = mainpatch

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk
