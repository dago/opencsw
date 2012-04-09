# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = xfce-dtlogin
VERSION = 4.10
GARTYPE = v2
CATEGORIES = xfce4.10

DESCRIPTION = Xfce lightweight desktop environment, dtlogin
define BLURB
  Xfce lightweight desktop environment, dtlogin
endef

# Catalog description
PACKAGES = CSWxfcedtlogin

# Package description
SPKG_DESC_CSWxfcedtlogin       = $(DESCRIPTION)

ARCHALL_CSWxfcedtlogin         = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = 
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@gcp -fr $(WORKSRC) $(DESTDIR)
	@rm  -fr $(DESTDIR)/.git
