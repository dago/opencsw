GARNAME = jhead
GARVERSION = 2.7
CATEGORIES = utils

DESCRIPTION = EXIF parser for JPEG images
define BLURB
  Jhead can extract and modify EXIF information contained in JPEG files.
endef

MASTER_SITES = http://www.sentex.net/~mwandel/jhead/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWjhead.gspec CSWjhead.prototype

PATCHFILES = makefile.patch

# jhead doesn't use configure
CONFIGURE_SCRIPTS = 

# jhead doesn't have a test target
TEST_TARGET = 

SPKG_SOURCEURL = http://www.sentex.net/~mwandel/jhead/
SPKG_PKGBASE = $(DESTDIR)$(prefix)

include gar/category.mk
