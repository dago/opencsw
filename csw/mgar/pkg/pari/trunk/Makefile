NAME = pari
VERSION = 2.3.5
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Efficient computations in number theory
define BLURB
  PARI/GP is a widely used computer algebra system designed for fast computations
  in number theory (factorizations, algebraic number theory, elliptic curves...),
  but also contains a large number of other useful functions to compute with mathematical
  entities such as matrices, polynomials, power series, algebraic numbers, etc., and
  a lot of transcendental functions.
endef

MASTER_SITES = http://pari.math.u-bordeaux.fr/pub/pari/unix/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# TODO: The galdata is missing in the package, where does it come from?

PACKAGES = CSWparigp
CATALOGNAME = parigp

VENDOR_URL = http://pari.math.u-bordeaux.fr

CONFIGURE_SCRIPTS = custom
CONFIGURE_ARGS  = --prefix=$(prefix)
CONFIGURE_ARGS += --bindir=$(bindir)
CONFIGURE_ARGS += --includedir=$(includedir)
CONFIGURE_ARGS += --libdir=$(libdir)
CONFIGURE_ARGS += --mandir=$(mandir)

BUILD_ARGS        = gp

# There are lots of tests, TBD: pick one
TEST_SCRIPTS =

include gar/category.mk

configure-custom:
	@echo " ==> Running Configure"
	( cd $(WORKSRC) ; $(CONFIGURE_ENV) ./Configure $(CONFIGURE_ARGS) )
	@$(MAKECOOKIE)
