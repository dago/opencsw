GARNAME = drupal
GARVERSION = 6.12
CATEGORIES = apps

DESCRIPTION = An open source content management platform
define BLURB
	GD is an open source code library for the dynamic creation of 
	images by programmers. GD creates PNG, JPEG and GIF images, 
	among other formats. GD is commonly used to generate charts, 
	graphics, thumbnails, and most anything else, on the fly. 
	While not restricted to use on the web, the most common 
	applications of GD involve web site development.
endef

MASTER_SITES = http://ftp.drupal.org/files/projects/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWdrupal
CATALOGNAME_CSWdrupal = drupal
SPKG_SOURCEURL = http://drupal.org/
SPKG_DESC_CSWdrupal = $(DESCRIPTION)


# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

ARCHALL_CSWdrupal = 1

CONFIGURE_SCRIPTS = 
BUILD_SCRIPTS     = 
INSTALL_SCRIPTS   = custom

REQUIRED_PKGS_CSWdrupal = CSWapache2c CSWphp5 CSWphp5gd 

## There are no tests for this
TEST_SCRIPTS = skip

test-skip:
	@$(MAKECOOKIE)

install-custom:
	ginstall -d $(DESTDIR)$(prefix)/$(GARNAME)/$(GARVERSION)
	cd $(WORKSRC); /usr/bin/pax -rw -v * $(DESTDIR)$(prefix)/$(GARNAME)/$(GARVERSION)
	@$(MAKECOOKIE)

include gar/category.mk
