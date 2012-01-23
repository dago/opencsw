NAME = openexr
VERSION = 1.7.0
CATEGORIES = lib

DESCRIPTION = High dynamic-range (HDR) image file format developed by Industrial Light & Magic
define BLURB
	IlmImf is our "EXR" file format for storing 16-bit FP images.  Libraries in
	this package depend on the IlmBase library.

	See the IlmImfExamples directory for some code that demonstrates how
	to use the IlmImf library to read and write OpenEXR files.  The doc
	directory contains some high-level documentation and history about the
	OpenEXR format.

	If you have questions about using the OpenEXR libraries, you may want
	to join our developer mailing list.  See http://www.openexr.com for
	details.
endef

MASTER_SITES = http://download.savannah.nongnu.org/releases/openexr/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

VENDOR_URL = http://www.openexr.com

LICENSE = LICENSE 

PACKAGES += CSWopenexr
SPKG_DESC_CSWopenexr += $(DESCRIPTION)

#PACKAGES += CSWopenexrrt
CATALOGNAME_CSWopenexrrt = openexr_rt_stub
SPKG_DESC_CSW =

PACKAGES += CSWopenexr-dev
SPKG_DESC_CSWopenexr-dev = Development files for ...
PKGFILES_CSWopenexr-dev += $(PKGFILES_DEVEL)
OBSOLETED_BY_CSWopenexr-dev += CSWopenexrdevel
CATALOGNAME_CSWopenexrdevel = openexr_devel_stub

BUILD64_LIBS_ONLY = 1

include gar/category.mk

