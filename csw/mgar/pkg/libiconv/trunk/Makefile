GARNAME = libiconv
GARVERSION = 1.13.1
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

# We have to take care of the package naming. We once had CSWiconv
# (pkgname) as libiconv (software name). Now we have a consistent
# naming but still need to provide CSWiconv as a depencies-only
# package.
PACKAGES = CSWlibiconv CSWlibiconvdevel CSWiconv

CATALOGNAME_CSWlibiconv = libiconv
CATALOGNAME_CSWlibiconvdevel = libiconv_devel
CATALOGNAME_CSWiconv = iconv

SPKG_DESC_CSWlibiconv = GNU iconv library
SPKG_DESC_CSWlibiconvdevel = GNU iconv library development package
SPKG_DESC_CSWiconv = GNU iconv library - meta package (deprecated)

# CSWiconv is a dependencies-only pkg
PKGFILES_CSWiconv = $(docdir)/CSWiconv/README.CSW

# Devel files in _devel pkg, remaining files go into CSWlibiconv
PKGFILES_CSWlibiconvdevel = $(PKGFILES_DEVEL) .*.3.html

# Dependencies:
#  Some of the utility programs 'depend' on ggettext.
#  But DO NOT put CSWggettext in depend, or it will break things!!!
#  Read: Circular dependency between ggettextrt and libiconv

REQUIRED_PKGS_CSWlibiconvdevel = CSWlibiconv
REQUIRED_PKGS_CSWiconv = CSWlibiconv CSWlibiconvdevel

# CSWiconv depends on CSWlibiconv which we don't have yet
ENABLE_CHECK = 0

# The current 1.12 only has a 32-Bit iconv binary, leave it that way
EXTRA_MERGE_EXCLUDE_FILES = /opt/csw/bin/.*/iconv
NO_ISAEXEC = 1
BUILD64 = 1

# Optimize. -fast causes ./configure on Sparc to hang on the stdbool.h test.
# Patch the stdbool test away, stdbool is only available in C99 anyway.
#
# See the following posts for details
# - http://lists.opencsw.org/pipermail/maintainers/2009-July/003152.html
# - http://forums.sun.com/thread.jspa?threadID=5397065&tstart=0
OPT_FLAGS_SOS = -fast -xnolibmopt
PATCHFILES += patch-configure-stdbool.diff

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
	ginstall -D $(FILEDIR)/CSWiconv.README \
		$(DESTDIR)$(docdir)/CSWiconv/README.CSW
	@$(MAKECOOKIE)
