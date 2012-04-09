# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = tumbler
VERSION = 0.1.24
GARTYPE = v2
CATEGORIES = xfce4.10

DESCRIPTION = A D-Bus thumbnailing service based on the thumbnail management D-Bus specification.
define BLURB
  A D-Bus thumbnailing service based on the thumbnail management D-Bus specification.
endef

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PATCHFILES += 0001-Under-Solaris-try-to-find-first-the-binanries-with-t.patch

CONFIGURE_ARGS = $(DIRPATHS)

# Catalog description
PACKAGES = CSWtumbler 

# Package description
SPKG_DESC_CSWtumbler       = $(DESCRIPTION)

include gar/category.mk

pre-configure-modulated:
	( cd "${WORKSRC}" ; pwd ; autoconf )
	@$(MAKECOOKIE)
