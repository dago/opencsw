NAME = htmldoc
VERSION = 1.8.27
GARTYPE = v2

DESCRIPTION = C2

DESCRIPTION = converts HTML files and web pages into indexed HTML PostScript and PDF
define BLURB
 HTMLDOC is a program for writing documentation in HTML and producing indexed
 HTML, PostScript, or PDF output (with tables of contents). It supports most
 HTML 3.2 and some HTML 4.0 syntax, as well as GIF, JPEG, and PMASTER_SITES += http://www.msweet.org/files/project1/
DISTFILES += $(DISTNAME)-source.tar.bz2

PATCHFILES += mainpatch
PATCHFILES += 0002-libpng15-compatibility-fix.patch

VENDOR_URL = http://www.htmldoc.org
LICENSE = COPYING.txt

PACKAGES += CSWhtmldoc-common
SPKG_DESC_CSWhtmldoc-common = This package contains the htmldoc files common to all architectures
# PKGFILES is catchall
ARCHALL_CSWhtmldoc-common = 1
CHECKPKG_OVERRIDES_CSWhtmldoc-common += file-with-bad-content|/usr/share|root/opt/csw/share/man/man1/htmldoc.1WhtACKAGES += CSWhtmldoc
SPKG_DESC_CSWhtmldoc = $(DESCRIPTION)
PKGFILES_CSWhtmldoc = $(bindir)/.*
RUNTIME_DEP_PKGS_CSWhtmldoc += CSWfltk
RUNTIME_DEP_PKGS_CSWhtmldoc += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWhtmldoc += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWhtmldoc += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWhtmldoc += CSWlibz1
RUNTIME_DEP_PKGS_CSWhtmldoc += CSWhtmldoc-common

CHECKPKG_OVERRIDES_CSWhtmldoc += surplus-dependency|CSWhtmldoc-common

# There is no testsuite
TEST_SCRIPTS =

#ENABLE_CHECK = 0
includ
post-configure:
	gsed -i -e 's/-xnorunpath//' $(WORKSRC)/Makedefs
