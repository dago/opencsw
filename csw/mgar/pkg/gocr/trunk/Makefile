# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gocr
VERSION = 0.49
GARTYPE = v2

DESCRIPTION = GOCR is Optical Character Recognition
define BLURB
 GOCR is an OCR (Optical Character Recognition) program, developed under the GNU Public License. It converts scanned images of text back to text files. Joerg Schulenburg started the program, and now leads a team of developers.
GOCR can be used with different front-ends, which makes it very easy to port to different OSes and architectures. It can open many different image formats, and its quality have been improving in a daily basis. 
endef

MASTER_SITES = http://www-e.uni-magdeburg.de/jschulen/ocr/
DISTFILES  = $(DISTNAME).tar.gz
LICENSE = CREDITS

GARCOMPILER = GCC4
# no target 
SKIPTEST = 1

RUNTIME_DEP_PKGS_CSWgocr += CSWlibnetpbm10
CHECKPKG_OVERRIDES_CSWgocr += file-with-bad-content|/usr/share|root/opt/csw/share/man/man1/gocr.1


CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

