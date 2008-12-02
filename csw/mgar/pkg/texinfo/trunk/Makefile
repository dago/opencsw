GARNAME = texinfo
GARVERSION = 4.6
CATEGORIES = utils

DESCRIPTION = Create different types of documentation from a single source.
define BLURB
    Texinfo is a documentation system that uses a single source to produce both
    on-line information (info, HTML, XML, Docbook) and printed output (DVI, PDF).
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
