NAME = jhead
VERSION = 2.97
GARTYPE = v2

CATEGORIES = utils

DESCRIPTION = EXIF parser for JPEG images
define BLURB
  Jhead can extract and modify EXIF information contained in JPEG files.
endef

MASTER_SITES = http://www.sentex.net/~mwandel/jhead/
DISTFILES  = $(NAME)PATCHFILES += makefile.patch

GARCOMPILER = GCC4

PACKAGES += CSWjheadES = makefile.patch

# jhead doesn't use configure
CONFIGURE_SCRIPTS = 

# jhead doesn't have SCRIPTS = 

VENDOR_URL = http://www.sentex.net/~mwandel/jhead/
#SPKG_PKGBASE = $(DESTDIR)$(prefix)

include gar/category.mk
