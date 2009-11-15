GARNAME = geda
GARVERSION = 1.6.0
CATEGORIES = devel

DESCRIPTION = The gEDA suite with gschem, gattrib, gnetlist, gsch2pcb, gsymcheck and libgeda
define BLURB
endef

MASTER_SITES = http://geda.seul.org/release/v1.6/1.6.0/
DISTFILES  = geda-gaf-$(GARVERSION).tar.gz

WORKSRC = $(WORKDIR)/geda-gaf-$(GARVERSION)

# We define upstream file regex so we can be notifed of new upstream software release
# UFILES_REGEX = geda-gaf-(\d+(?:\.\d+)*).tar.gz
# That pattern won't work, geda has a funny major.minor/major.minor.micro 
# layout, see MASTER_SITES - trygve

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
