GARNAME = libntlm
GARVERSION = 0.4.1
CATEGORIES = lib

DESCRIPTION = A library that implement Microsoft's NTLM authentication
define BLURB
  libntlm is a library that implement Microsoft's NTLM authentication.
  However, the packaging of libntlm lacked certain things, such as having
  build problems, lacking shared library support, lacking autoconf macro
  for use in other applications, lacking pkg-config support, and more.
  So this page distributes an improved version of the library; called Libntlm.
endef

MASTER_SITES = http://josefsson.org/libntlm/releases/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibntlm,depend)

# With Sun cc we get several errors, including preprocessor errors on
#   #if ! (-9223372036854775807LL < 0 && 0 < 9223372036854775807ll)
#      error in preprocessor;
#   #endif
# This yields in
#   checking for long long int... no
#   checking for unsigned long long int... yes
# which finally yields to
#   sizeof (intmax_t) != sizeof (uintmax_t)
# which aborts the compile.
# That's why we use gcc...
GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include ../category.mk
