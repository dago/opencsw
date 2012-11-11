# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = crosstool-ng
VERSION = 1.13.2
GARTYPE = v2

DESCRIPTION = Toolchain generator
define BLURB
endef

MASTER_SITES = http://crosstool-ng.org/download/crosstool-ng/
# http://crosstool-ng.org/download/crosstool-ng/crosstool-ng-1.13.2.tar.bz2	
DISTFILES  = $(DISTNAME).tar.bz2

CONFIGURE_ARGS = --prefix=$(prefix)
TEST_SCRIPTS =

PATCHFILES += 0001-If-you-use-bash-declare-that.patch

CHECKPKG_OVERRIDES_CSWcrosstool-ng += file-with-bad-content

include gar/category.mk

post-merge:
	$(FILEDIR)/sanitize_filenames.sh $(PKGROOT)
	if [ -f $(PKGROOT)/opt/csw/share/man/man1/ct-ng.1.gz ]; then \
		gunzip $(PKGROOT)/opt/csw/share/man/man1/ct-ng.1.gz; \
	fi

PATH := /opt/csw/gnu:$(PATH)
