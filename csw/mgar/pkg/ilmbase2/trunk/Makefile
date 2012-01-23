NAME = ilmbase
VERSION = 1.0.1
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
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += libHalf.so.2.0.2.i
DISTFILES += libHalf.so.2.0.2.s
DISTFILES += libIex.so.2.0.2.i
DISTFILES += libIex.so.2.0.2.s
DISTFILES += libImath.so.2.0.2.i
DISTFILES += libImath.so.2.0.2.s

PACKAGES = CSWilmbase CSWilmbasedevel
CATALOGNAME_CSWilmbase = ilmbase
CATALOGNAME_CSWilmbasedevel = ilmbase_devel

SPKG_DESC_CSWilmbase += Base libraries used by OpenEXR
SPKG_DESC_CSWilmbasedevel += Base libraries used by OpenEXR - developer package

PKGFILES_CSWilmbasedevel = $(PKGFILES_DEVEL)

RUNTIME_DEP_PKGS_CSWilmbase += 
RUNTIME_DEP_PKGS_CSWilmbasedevel += CSWilmbase


CHECKPKG_OVERRIDES_CSWilmbase += symbol-not-found|libIex.so.2.0.2
CHECKPKG_OVERRIDES_CSWilmbase += symbol-not-found|libHalf.so.2.0.2
CHECKPKG_OVERRIDES_CSWilmbase += symbol-not-found|libImath.so.2.0.2
CHECKPKG_OVERRIDES_CSWilmbase += symbol-not-found|libIlmThread.so.6.0.0
CHECKPKG_OVERRIDES_CSWilmbase += symbol-not-found|libImath.so.6.0.0

SPKG_SOURCEURL = http://www.openexr.com

LICENSE = LICENSE

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
UPSTREAM_MASTER_SITES = http://download.savannah.nongnu.org/releases/openexr/

CONFIGURE_ARGS = $(DIRPATHS)

PATCHFILES = ImathMath.patch
PATCHFILES += ltmain.sh.patch

EXTRA_LD_FLAGS += -lCstd -lCrun -lc -lm
EXTRA_CXX_FLAGS_isa-i386    = 
EXTRA_CXX_FLAGS_isa-sparcv8 = 
EXTRA_CXX_FLAGS_isa-amd64   = -KPIC
EXTRA_CXX_FLAGS_isa-sparcv9 = -KPIC
EXTRA_CXX_FLAGS += $(EXTRA_LD_FLAGS_$(MODULATION))

BUILD64_LIBS_ONLY = 1

# Check fails if library isn't installed /opt/csw/lib and until a 64-bit
# lib is installed test has to be disabled
#TEST_TARGET = check
TEST_TARGET = 

STRIP_LIBTOOL = 1

include gar/category.mk

#
# Test to see if rebuilding libtool would fix 64-bit problem...
#
#pre-configure-modulated:
#	@echo " ==> Regenerating build tools..."
#	@(cd $(WORKSRC) ; \
#		aclocal                       && \
#		autoconf                      && \
#		libtoolize --automake --force && \
#		aclocal                       && \
#		automake -a )
#	@$(MAKECOOKIE)

post-install-isa-sparcv8:
	@cp $(FILEDIR)/libHalf.so.2.0.2.s $(INSTALLISADIR)/opt/csw/lib/libHalf.so.2.0.2
	@cp $(FILEDIR)/libIex.so.2.0.2.s $(INSTALLISADIR)/opt/csw/lib/libIex.so.2.0.2
	@cp $(FILEDIR)/libImath.so.2.0.2.s $(INSTALLISADIR)/opt/csw/lib/libImath.so.2.0.2
	@( if [ ! -r $(INSTALLISADIR)$(libdir)/libHalf.so.2 ] ; then ln -s libHalf.so.2.0.2 $(INSTALLISADIR)/opt/csw/lib/libHalf.so.2 ; fi )
	@( if [ ! -r $(INSTALLISADIR)$(libdir)/libIex.so.2 ] ; then ln -s libIex.so.2.0.2 $(INSTALLISADIR)/opt/csw/lib/libIex.so.2 ; fi )
	@( if [ ! -r $(INSTALLISADIR)$(libdir)/libImath.so.2 ] ; then ln -s libImath.so.2.0.2 $(INSTALLISADIR)/opt/csw/lib/libImath.so.2 ; fi )

post-install-isa-i386:
	@cp $(FILEDIR)/libHalf.so.2.0.2.i $(INSTALLISADIR)/opt/csw/lib/libHalf.so.2.0.2
	@cp $(FILEDIR)/libIex.so.2.0.2.i $(INSTALLISADIR)/opt/csw/lib/libIex.so.2.0.2
	@cp $(FILEDIR)/libImath.so.2.0.2.i $(INSTALLISADIR)/opt/csw/lib/libImath.so.2.0.2
	@( if [ ! -r $(INSTALLISADIR)$(libdir)/libHalf.so.2 ] ; then ln -s libHalf.so.2.0.2 $(INSTALLISADIR)/opt/csw/lib/libHalf.so.2 ; fi )
	@( if [ ! -r $(INSTALLISADIR)$(libdir)/libIex.so.2 ] ; then ln -s libIex.so.2.0.2 $(INSTALLISADIR)/opt/csw/lib/libIex.so.2 ; fi )
	@( if [ ! -r $(INSTALLISADIR)$(libdir)/libImath.so.2 ] ; then ln -s libImath.so.2.0.2 $(INSTALLISADIR)/opt/csw/lib/libImath.so.2 ; fi )
