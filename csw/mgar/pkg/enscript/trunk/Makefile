GARNAME = enscript
GARVERSION = 1.6.4
CATEGORIES = utils

DESCRIPTION = GNU enscript converts ASCII files to PostScript
define BLURB
  GNU enscript is a free replacement for the Adobe's enscript program.
  Enscript converts ASCII files to PostScript and spools generated PostScript
  output to the specified printer or leaves it to file. Enscript can be easily
  extended to handle different output media and it has many options that can
  be used to customize printouts.
endef

MASTER_SITES = http://www.iki.fi/mtr/genscript/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.codento.com/people/mtr/genscript/

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
