NAME = htmldoc
VERSION = 1.8.27
GARTYPE = v2

DESCRIPTION = C2

DESCRIPTION = converts HTML files and web pages into indexed HTML PostScript and PDF
define BLURB
 HTMLDOC is a program for writing documentation in HTML and producing indexed
 HTML, PostScript, or PDF output (with tables of contents). It supports most
 HTML 3.2 and some HTML 4.0 syntax, as well as GIF, JPEG, and PNG images.
endef

PACKAGES = CSWhtmldoc-common CSWhtmldoc
CATALOGNAME_CSWhtmldoc = $(NAME)
CATALOGNAME_CSWhtmldoc-common = $(NAME)_common
SPKG_DESC_CSWhtmldoc = $(DESCRIPTION)
SPKG_DESC_CSWhtmldoc-common = This package contains the htmldoc files common to all architectures.
ARCHALL_CSWhtmldoc-common = 1

RUNTIME_DEP_PKGS_CSWhtmllibjpeg7 CSWlibssl1-0-0 CSWlibpng15-15 CSWlibz1
RUNTIME_DEP_PKGS_CSWhtmldoc += CSWhtmldoc-common
#RUNTIME_DEP_PKGS_CSWhtmldoc-common = 

CHECKPKG_OVERRIDES_CSWhtmldoc += surplus-dependency|CSWhtmldoc-common
CHECKPKG_OVERRIDES_CSWhtmldoc-common += file-with-bad-content|/usr/share|root/opt/csw/share/man/man1/htmldoc.1Whtmldoc-common = 

PKGFILES_CSWhtmldoc = $(bindir)/.*
PKGFILES_CSWhtmldoc-commonn = $(datadir)/.*

MASTER_SITES = http://ftp.easysw.com/pub/htmldoc/$(VERSION)/
DISTFILES  = $(NAME)-$(VERSION)-source.tar.bz2
#DISTFILES    += $(call admfiles,CSWhtmldoc, )
#DISTFILES    += $(call admfiles,CSWhtmldoc-common, )

LICENSE = COPYING.txt

SPKG_SOURCEURL = http://www.htmldoc.org

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)-source.tar.bz2

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PATCHFPATCHFILES += 0002-libpng15-compatibility-fix.
PATCHFILES = mainpatch

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

# Disable check until package is released
#ENABLE_CHECK = 0
includ
post-configure:
	gsed -i -e 's/-xnorunpath//' $(WORKSRC)/Makedefs
