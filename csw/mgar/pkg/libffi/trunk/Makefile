GARNAME = libffi
GARVERSION = 3.0.8
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

PACKAGES = CSWlibffi
CATALOGNAME_CSWlibffi = libffi
SPKG_DESC_CSWlibffi = $(DESCRIPTION)


#REQUIRED_PKGS_CSWlibffi += 

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

GARCOMPILER = GNU

CONFIGURE_ARGS  = $(DIRPATHS)
TEST_TARGET = check
include gar/category.mk
