NAME = openexr
VERSION = 1.6.1
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

MASTER_SITES = http://savannah.nongnu.org/download/openexr/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += libIlmImf.so.2.0.2.i
DISTFILES += libIlmImf.so.2.0.2.s

PACKAGES = CSWopenexr CSWopenexrrt CSWopenexrdevel CSWopenexrdoc
CATALOGNAME_CSWopenexr = openexr
CATALOGNAME_CSWopenexrrt = openexr_rt
CATALOGNAME_CSWopenexrdevel = openexr_devel
CATALOGNAME_CSWopenexrdoc = openexr_doc

SPKG_DESC_CSWopenexr += $(DESCRIPTION)
SPKG_DESC_CSWopenexrrt += $(DESCRIPTION) - runtime package
SPKG_DESC_CSWopenexrdevel += $(DESCRIPTION) - developer package
SPKG_DESC_CSWopenexrdoc += $(DESCRIPTION) - documentation

PKGFILES_CSWopenexrrt = $(PKGFILES_RT)
PKGFILES_CSWopenexrdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWopenexrdoc = $(docdir)/OpenEXR.*

ARCHALL_CSWopenexrdoc = 1

RUNTIME_DEP_PKGS_CSWopenexr += CSWopenexrrt
RUNTIME_DEP_PKGS_CSWopenexr += CSWilmbase
RUNTIME_DEP_PKGS_CSWopenexr += CSWzlib
RUNTIME_DEP_PKGS_CSWopenexrrt += CSWilmbase CSWzlib
RUNTIME_DEP_PKGS_CSWopenexrdevel += CSWopenexrrt
RUNTIME_DEP_PKGS_CSWopenexrdoc += 

SPKG_SOURCEURL = http://www.openexr.com

CHECKPKG_OVERRIDES_CSWopenexrdevel += missing-dependency|CSWopenexr

LICENSE = LICENSE 

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PATCHFILES += ltmain.sh.patch
PATCHFILES += makePreview.cpp.patch

EXTRA_LD_FLAGS += -lCstd -lCrun -lc -lm
EXTRA_CXX_FLAGS_isa-i386    = 
EXTRA_CXX_FLAGS_isa-sparcv8 = 
EXTRA_CXX_FLAGS_isa-amd64   = -KPIC
EXTRA_CXX_FLAGS_isa-sparcv9 = -KPIC
EXTRA_CXX_FLAGS += $(EXTRA_LD_FLAGS_$(MODULATION))

BUILD64 = 1

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
