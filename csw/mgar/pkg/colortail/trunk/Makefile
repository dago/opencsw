# $Id$
NAME = colortail
VERSION = 0.3.0
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Tail-variant with color support for easier log file reading
define BLURB
  colortail works like tail but can optionally read one or more config
  files where it's specified which patterns results in which colors.
  Colortail uses regular expressions (see regex(7)) to determine which
  lines and parts of lines to print in which colors. 
endef

VENDOR_URL   = http://joakimandersson.se/projects/colortail/
MASTER_SITES = http://joakimandersson.se/files/
DISTFILES    = $(DISTNAME).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
