GARNAME = siege
GARVERSION = 2.66
CATEGORIES = xtra

DESCRIPTION = A http regression testing and benchmarking utility
define BLURB
  Siege is an http regression testing and benchmarking utility. It was
  designed to let web developers measure the performance of their code
  under duress, to see how it will stand up to load on the internet. It
  lets the user hit a web server with a configurable number of
  concurrent simulated users.
endef

MASTER_SITES = ftp://sid.joedog.org/pub/siege/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# we require
REQUIRED_PKGS = CSWosslrt

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl=$(prefix)

TEST_SCRIPTS =

include gar/category.mk

# fix sysconfdir, to honor $(DESTDIR)
pre-build-modulated:
	@perl -pi -e 's@sysconfdir = /opt/csw/etc@sysconfdir = \$(DESTDIR)/opt/csw/etc@' ${WORKSRC}/doc/Makefile
