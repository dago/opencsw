GARNAME = ilmbase
GARVERSION = 1.0.1
CATEGORIES = lib

DESCRIPTION = Base libraries used by OpenEXR
define BLURB
	Half is a class that encapsulates our 16-bit floating-point format.

	IlmThread is a thread abstraction library for use with OpenEXR
	and other software packages.  It currently supports pthreads and
	Windows threads.

	Imath implements 2D and 3D vectors, 3x3 and 4x4 matrices, quaternions
	and other useful 2D and 3D math functions.

	Iex is an exception-handling library.

	If you have questions about using the IlmBase libraries, you may want
	to join our developer mailing list.  See http://www.openexr.com for
	details.
endef

MASTER_SITES = http://download.savannah.nongnu.org/releases/openexr/ 
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += libHalf.so.2.0.2.i
DISTFILES += libHalf.so.2.0.2.s
DISTFILES += libIex.so.2.0.2.i
DISTFILES += libIex.so.2.0.2.s
DISTFILES += libImath.so.2.0.2.i
DISTFILES += libImath.so.2.0.2.s

SPKG_SOURCEURL = http://www.openexr.com

LICENSE = LICENSE

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

PATCHFILES = ImathMath.patch

LIBS += -lCstd -lCrun -lc -lm
export LIBS

TEST_TARGET = check

include gar/category.mk


post-install-isa-sparcv8:
	@cp $(FILEDIR)/libHalf.so.2.0.2.s $(INSTALLISADIR)/opt/csw/lib/libHalf.so.2.0.2
	@cp $(FILEDIR)/libIex.so.2.0.2.s $(INSTALLISADIR)/opt/csw/lib/libIex.so.2.0.2
	@cp $(FILEDIR)/libImath.so.2.0.2.s $(INSTALLISADIR)/opt/csw/lib/libImath.so.2.0.2
	@ln -s libHalf.so.2.0.2 $(INSTALLISADIR)/opt/csw/lib/libHalf.so.2
	@ln -s libIex.so.2.0.2 $(INSTALLISADIR)/opt/csw/lib/libIex.so.2
	@ln -s libImath.so.2.0.2 $(INSTALLISADIR)/opt/csw/lib/libImath.so.2

post-install-isa-i386:
	@cp $(FILEDIR)/libHalf.so.2.0.2.i $(INSTALLISADIR)/opt/csw/lib/libHalf.so.2.0.2
	@cp $(FILEDIR)/libIex.so.2.0.2.i $(INSTALLISADIR)/opt/csw/lib/libIex.so.2.0.2
	@cp $(FILEDIR)/libImath.so.2.0.2.i $(INSTALLISADIR)/opt/csw/lib/libImath.so.2.0.2
	@ln -s libHalf.so.2.0.2 $(INSTALLISADIR)/opt/csw/lib/libHalf.so.2
	@ln -s libIex.so.2.0.2 $(INSTALLISADIR)/opt/csw/lib/libIex.so.2
	@ln -s libImath.so.2.0.2 $(INSTALLISADIR)/opt/csw/lib/libImath.so.2
