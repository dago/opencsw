GARNAME = pil
GARVERSION = 1.1.6
CATEGORIES = lib
DISTNAME = Imaging-$(GARVERSION)


DESCRIPTION = Python Imaging Library
define BLURB
  Long description
endef

MASTER_SITES = http://effbot.org/downloads/
DISTFILES  = $(DISTNAME).tar.gz

REQUIRED_PKGS_CSWpil = CSWftype2 CSWjpeg CSWpython 


# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = Imaging-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom
INSTALL_ARGS = --root=$(DESTDIR)

include gar/category.mk

install-custom:
	        @echo " ==> Installing $(GARNAME)"
			            @( cd $(WORKSRC) ; $(INSTALL_ENV) python ./setup.py install $(INSTALL_ARGS) )
						                $(DONADA)

post-install: copy-docs
	        $(DONADA)


