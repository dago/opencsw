#
# Long-term TODO:
# See branches/sync-pkgname for an attempt to sync the CSW pkg name to
# the upstream name and split off a devel pkg.
#
NAME = libiconv
VERSION = 1.13.1
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
DISTFILES = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES += CSWlibiconv2
CATALOGNAME_CSWlibiconv2 = libiconv2
SPKG_DESC_CSWlibiconv2 = GNU iconv library, libiconv.so.2
PKGFILES_CSWlibiconv2 += $(call pkgfiles_lib,libiconv.so.2)
OBSOLETES_CSWlibiconv2 += CSWiconv

PACKAGES += CSWlibcharset1
CATALOGNAME_CSWlibcharset1 = libcharset1
SPKG_DESC_CSWlibcharset1 = GNU iconv charset library, libcharset.so.1
PKGFILES_CSWlibcharset1 += $(call pkgfiles_lib,libcharset.so.1)
# Now *this* time it is ok, iconv is the only package that is allowed to ship this!
CHECKPKG_OVERRIDES_CSWlibcharset1 += disallowed-path|opt/csw/lib/charset.alias
PKGFILES_CSWlibcharset1 += $(call baseisadirs,$(libdir),charset\.alias)
OBSOLETES_CSWlibcharset1 += CSWiconv

PACKAGES += CSWlibiconv-dev
CATALOGNAME_CSWlibiconv-dev = libiconv_dev
SPKG_DESC_CSWlibiconv-dev = Development files for libiconv.so.2
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibiconv-dev += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibiconv-dev += CSWlibcharset1
# This is from an example in a comment
CHECKPKG_OVERRIDES_CSWlibiconv-dev += file-with-bad-content|/usr/local|root/opt/csw/include/iconv.h

PACKAGES += CSWlibiconv-utils
CATALOGNAME_CSWlibiconv-utils = libiconv_utils
SPKG_DESC_CSWlibiconv-utils = GNU iconv utility programs
PKGFILES_CSWlibiconv-utils += $(bindir)/.*
PKGFILES_CSWlibiconv-utils += .*iconv\.1.*
PKGFILES_CSWlibiconv-utils += .*/libiconv\.mo
PKGFILES_CSWlibiconv-utils += $(call baseisadirs,$(libdir),preloadable_libiconv\.so)
# The SONAME of preloadable_libiconv.so is set to libiconv.so.0, although it doesn't
# matter in any way as this library is only used for LD_PRELOAD and is never being
# linked against during compile time.
CHECKPKG_OVERRIDES_CSWlibiconv-utils += soname-not-part-of-filename|soname=libiconv.so.0|filename=preloadable_libiconv.so
CHECKPKG_OVERRIDES_CSWlibiconv-utils += shared-lib-pkgname-mismatch|sonames=libiconv.so.0|pkgname=CSWlibiconv-utils|expected=CSWlibiconv0
RUNTIME_DEP_PKGS_CSWlibiconv-utils += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibiconv-utils += CSWlibintl8
OBSOLETES_CSWlibiconv-utils += CSWiconv

NOISAEXEC = 1
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

EXTRA_CPPFLAGS = -D_REENTRANT

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-rpath

MERGE_DIRS_isa-extra = $(libdir)

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
post-install-modulated:
	ginstall -d $(DOCDEST)
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	ginstall -D $(WORKSRC)/srcm4/iconv.m4 \
		$(DESTDIR)$(datadir)/aclocal/iconv.m4
	@$(MAKECOOKIE)

post-merge:
	@# Make the 64 bit charset-alias the same as the one for 32 bit
	rm -f $(PKGROOT)$(libdir)/$(ISA_DEFAULT64)/charset.alias
	gln -s ../charset.alias $(PKGROOT)$(libdir)/$(ISA_DEFAULT64)/charset.alias
	@$(MAKECOOKIE)
