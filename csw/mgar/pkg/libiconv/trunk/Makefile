GARNAME = libiconv
GARVERSION = 1.13
CATEGORIES = lib

DESCRIPTION = GNU iconv library
define BLURB
  Some programs, like mailers and web browsers, must be able to convert
  between a given text encoding and the user's encoding. Other programs
  internally store strings in Unicode, to facilitate internal processing,
  and need to convert between internal string representation (Unicode) and
  external string representation (a traditional encoding) when they are
  doing I/O. GNU libiconv is a conversion library for both kinds of
  applications. 
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# Package naming is a bit unfortunate CSWiconv vs. libiconv :/ but
# that's not something i want to change right now. CSWiconv has
# heaps of dependents.
PACKAGES = CSWiconv CSWiconvdevel

CATALOGNAME_CSWiconv = libiconv
CATALOGNAME_CSWiconvdevel = libiconv_devel

SPKG_DESC_CSWiconv = GNU iconv library
SPKG_DESC_CSWiconvdevel = GNU iconv library development pacakge

PKGFILES_CSWiconvdevel = $(PKGFILES_DEVEL) .*.3.html
# All other unspecified files go into CSWlibiconv

# Dependencies:
#  Some of the utility programs 'depend' on ggettext.
#  But DO NOT put CSWggettext in depend, or it will break things!!!
#  Read: Circular dependency between ggettextrt and libiconv

REQUIRED_PKGS_CSWiconvdevel = CSWiconv

# Work around Sun Studio Preprocessor bug #6655406
#   http://sunsolve.sun.com/search/document.do?assetkey=1-1-6655406-1
#PATCHFILES = patch-workaround-cc-bug-6655406.diff

# The current 1.12 only has a 32-Bit iconv binary, leave it that way
EXTRA_MERGE_EXCLUDE_FILES = /opt/csw/bin/.*/iconv
NO_ISAEXEC = 1
BUILD64 = 1

# 'gmake test' shows three errors of coredumping printf's
#
#   ./check-translitfailure . TranslitFail1 ISO-8859-1 ASCII
#   ./check-subst
#   Segmentation Fault - core dumped
#   Segmentation Fault - core dumped
#   Segmentation Fault - core dumped
#   ./test-shiftseq
#
# This is due to bug #6550204
#   http://sunsolve.sun.com/search/document.do?assetkey=1-1-6550204-1
# and can safely be ignored as it is a failure in the testsuite.
TEST_TARGET = check

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-rpath

include gar/category.mk

post-install-modulated:
	ginstall -D $(WORKSRC)/srcm4/iconv.m4 \
		$(DESTDIR)$(datadir)/aclocal/iconv.m4
	@$(MAKECOOKIE)
