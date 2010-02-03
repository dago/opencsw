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

PACKAGES = CSWopenexr CSWopenexrdevel
CATALOGNAME_CSWopenexr = openexr
CATALOGNAME_CSWopenexrdevel = openexr_devel

SPKG_DESC_CSWopenexr += High dynamic-range (HDR) image file format developed by Industrial Light & Magic
SPKG_DESC_CSWopenexrdevel += High dynamic-range (HDR) image file format developed by Industrial Light & Magic - developer package

PKGFILES_CSWopenexrdevel = $(PKGFILES_DEVEL)

RUNTIME_DEP_PKGS_CSWopenexr += CSWilmbase CSWzlib
RUNTIME_DEP_PKGS_CSWopenexrdevel += CSWopenexr

SPKG_SOURCEURL = http://www.openexr.com

LICENSE = LICENSE 

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PATCHFILES += ltmain.sh.patch
PATCHFILES += makePreview.cpp.patch

EXTRA_LD_FLAGS += -lCstd -lCrun -lc -lm
EXTRA_CXX_FLAGS_isa-i386    = 
EXTRA_CXX_FLAGS_isa-sparcv8 = 
EXTRA_CXX_FLAGS_isa-amd64   = -KPIC
EXTRA_CXX_FLAGS_isa-sparcv9 = -KPIC
EXTRA_CXX_FLAGS += $(EXTRA_LD_FLAGS_$(MODULATION))

BUILD64 = 1
NOISAEXEC = 1

# Check fails if library isn't installed /opt/csw/lib and until a 64-bit
# lib is installed test has to be disabled
#TEST_TARGET = check
TEST_TARGET = 

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

# Until kdeoffice_gcc is rebuilt using new openexr/ilmbase
post-install-isa-sparcv8:
	@cp $(FILEDIR)/libIlmImf.so.2.0.2.s $(INSTALLISADIR)/opt/csw/lib/libIlmImf.so.2.0.2
	@( if [ ! -r $(INSTALLISADIR)$(libdir)/libIlmImf.so.2 ] ; then ln -s libIlmImf.so.2.0.2 $(INSTALLISADIR)/opt/csw/lib/libIlmImf.so.2 ; fi )

post-install-isa-i386:
	@cp $(FILEDIR)/libIlmImf.so.2.0.2.i $(INSTALLISADIR)/opt/csw/lib/libIlmImf.so.2.0.2
	@( if [ ! -r $(INSTALLISADIR)$(libdir)/libIlmImf.so.2 ] ; then ln -s libIlmImf.so.2.0.2 $(INSTALLISADIR)/opt/csw/lib/libIlmImf.so.2 ; fi )
