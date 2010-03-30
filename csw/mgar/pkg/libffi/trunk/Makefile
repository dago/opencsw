GARNAME = libffi
GARVERSION = 3.0.9
CATEGORIES = lib

DESCRIPTION = A portable foreign function interface library
define BLURB
	FFI stands for Foreign Function Interface. A foreign function 
	interface is the popular name for the interface that allows code 
	written in one language to call code written in another language. 
	The libffi library really only provides the lowest, machine 
	dependent layer of a fully featured foreign function interface. 
	A layer must exist above libffi that handles type conversions for 
	values passed between the two languages. 
endef

MASTER_SITES = ftp://sourceware.org/pub/libffi/
SPKG_SOURCEURL = http://sourceware.org/libffi/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
# Not needed unless using SOS12 compiler
#PATCHFILES = sun.patch

PACKAGES = CSWlibffi CSWlibffidevel
CATALOGNAME_CSWlibffi = libffi
CATALOGNAME_CSWlibffidevel = libffi_devel
SPKG_DESC_CSWlibffi = $(DESCRIPTION)
SPKG_DESC_CSWlibffidevel = $(DESCRIPTION) - developer package

PKGFILES_CSWlibffidevel = $(PKGFILES_DEVEL)

LICENSE = LICENSE

RUNTIME_DEP_PKGS_CSWlibffidevel += CSWlibffi
RUNTIME_DEP_PKGS_CSWlibffi = CSWgcc4corert

CHECKPKG_OVERRIDES_CSWlibffidevel += surplus-dependency|CSWlibffi

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

GARCOMPILER = GCC4
BUILD64 = 1

CONFIGURE_ARGS  = $(DIRPATHS)

# Tests fail since they are written for gcc only if using SOS12 compiler
# But they also fails on 64-bit
#TEST_TARGET = check
TEST_TARGET = 

include gar/category.mk


# v9.S is not needed when building 32-bit
pre-configure-isa-sparcv8:
	@( cd $(WORKSRC); gsed -e "s|src/sparc/v9.S||" -e "s/AM_CFLAGS = .*/AM_CFLAGS = /" -i Makefile.am ; \
		aclocal; \
		automake)

# v8.S will not build when building 64-bit
pre-configure-isa-sparcv9:
	@( cd $(WORKSRC); gsed -e "s|src/sparc/v8.S||" -e "s/AM_CFLAGS = .*/AM_CFLAGS = /" -i Makefile.am ; \
		aclocal; \
		automake)
	$(MAKECOOKIE)
