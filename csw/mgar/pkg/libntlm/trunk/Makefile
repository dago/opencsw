GARNAME = libntlm
GARVERSION = 1.1
CATEGORIES = lib

DESCRIPTION = Microsoft WinNT domain authentication library
define BLURB
  libntlm is a library that implement Microsoft's NTLM authentication.
  However, the packaging of libntlm lacked certain things, such as having
  build problems, lacking shared library support, lacking autoconf macro
  for use in other applications, lacking pkg-config support, and more.
  So this page distributes an improved version of the library; called Libntlm.
endef

MASTER_SITES = http://josefsson.org/libntlm/releases/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

SPKG_SOURCEURL = http://josefsson.org/libntlm/

include gar/category.mk
