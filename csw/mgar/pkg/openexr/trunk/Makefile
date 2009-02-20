GARNAME = openexr
GARVERSION = 1.6.1
CATEGORIES = lib

DESCRIPTION = high dynamic-range (HDR) image file format developed by Industrial Light & Magic
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

MASTER_SITES = http://savannah.nongnu.org/download/openexr/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += libIlmImf.so.2.0.2.i
DISTFILES += libIlmImf.so.2.0.2.s

SPKG_SOURCEURL = http://www.openexr.com
LICENSE = LICENSE 

REQUIRED_PKGS += CSWilmbase CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

LIBS += -lCstd -lCrun -lc -lm
export LIBS

TEST_SCRIPTS =

include gar/category.mk

post-install-isa-sparcv8:
	@cp $(FILEDIR)/libIlmImf.so.2.0.2.s $(INSTALLISADIR)/opt/csw/lib/libIlmImf.so.2.0.2
	@ln -s libIlmImf.so.2.0.2 $(INSTALLISADIR)/opt/csw/lib/libIlmImf.so.2

post-install-isa-i386:
	@cp $(FILEDIR)/libIlmImf.so.2.0.2.i $(INSTALLISADIR)/opt/csw/lib/libIlmImf.so.2.0.2
	@ln -s libIlmImf.so.2.0.2 $(INSTALLISADIR)/opt/csw/lib/libIlmImf.so.2
