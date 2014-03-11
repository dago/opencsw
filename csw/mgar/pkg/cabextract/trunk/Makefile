NAME = cabextract
VERSION = 1.4

DESCRIPTION = Extract Microsoft cabinet files
define BLURB
  cabextract is Free Software for extracting Microsoft cabinet files, also
  called .CAB files, on UNIX or UNIX-like systems. cabextract is distributed
  under the GPL license. It is based on the portable LGPL libmspack library.
  cabextract supports all special features and all compression formats of
  Microsoft cabinet files.
endef

MASTER_SITES = http://www.cabextract.org.uk/
DISTFILES += $(DISTNAME).tar.gz

VENDOR_URL = http://www.cabextract.org.uk

PACKAGES += CSWcabextract
SPKG_DESC_CSWcabextract = Extract Microsoft cabinet files
# PKGFILES is catchall
OBSOLETED_BY_CSWcabextract += CSWcabex
CATALOGNAME_CSWcabex = cabextract_stub

include gar/category.mk
