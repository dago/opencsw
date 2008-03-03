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
DISTFILES += $(call admfiles,CSWlibntlm,)

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
#
# Reported as Bug 6655406:
#   <http://sunsolve.sun.com/search/document.do?assetkey=1-1-6655406-1>
# Broken Preprocessor and Workaround discussed at
#   <http://www.mail-archive.com/autoconf-patches@gnu.org/msg02949.html>

PATCHFILES = patch-workaround-cc-bug-6655406.diff

# libntlm is somewhat dependend on endianess
#   https://savannah.nongnu.org/bugs/?21288
# Patch submitted upstream.
PATCHFILES += patch-byteorder-bigendian.diff

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
