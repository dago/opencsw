GARNAME = pycairo
GARVERSION = 1.8.2
CATEGORIES = lang

DESCRIPTION = pycairo support for Python
define BLURB
  This is a Python language binding for cairo.
endef

MASTER_SITES = http://www.cairographics.org/releases/
SPKG_SOURCEURL = http://www.cairographics.org
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += fixme.sh

PACKAGES = CSWpycairo
REQUIRED_PKGS_CSWpycairo  = CSWpython CSWggettextrt CSWglib2

CATALOGNAME_CSWpycairo = pycairo
SPKG_DESC_CSWpycairo = $(DESCRIPTION)

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)

CONFIGURE_ARGS  = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

post-configure-$(MODULATION):
	@(echo "~~~ Fixing Libtool ~~~")
	@$(DOWNLOADDIR)/fixme.sh $(WORKSRC)
	$(DONADA)
