NAME = lutefisk
VERSION = 0.1
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = provides statistics about 
define BLURB
  Lutefisk is a reporting tool used to send upstream information about the usage of packages. Lutefisk is made of two scripts, smor and tilbehor, each script is a hook called by the package management tools, like pkgutil.
  Smor is the package statistics tool. The following informations are sent upstream when a package is downloaded. Package name, arch, OS version both for package and machine running the package tool and source used (current, stable, etc.). 
  Tilbehor is the mirror statistics tool. The following informations are sent upstream when a package is downloaded. Base URL of the mirror used, arch, OS version of the machine running the package tool and source used (current, stable, etc.). 
  The use of this tools is completly anonymous. Only the day of the installation taken in account. Especially no time are recorded, and no personal information (such as IP adress) are stored. 
endef

MASTER_SITES = 

DISTFILES  = lutefisk_med_tilbehor lutefisk_med_smor license

# We define upstream file regex so we can be notifed of new upstream software release
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PACKAGES = CSWlutefisktilbehor CSWlutefisksmor
ARCHALL  = 1
LICENSE  = license

CATALOGNAME_CSWlutefisktilbehor = lutefisktilbehor
CATALOGNAME_CSWlutefisksmor     = lutefisksmor

# Defines package description
SPKG_DESC_CSWlutefisksmor     = Lutefisk med smor $(DESCRIPTION) OpenCSW packages use
SPKG_DESC_CSWlutefisktilbehor = Lutefisk med tilbehor $(DESCRIPTION) OpenCSW mirrors use

# Defines dependencies
RUNTIME_DEP_PKGS_CSWlutefisktilbehor = CSWwget CSWgawk 
RUNTIME_DEP_PKGS_CSWlutefisksmor     = CSWwget CSWgawk CSWgsed

# Defines package content
PKGFILES_CSWlutefisktilbehor = .*/lutefisk_med_tilbehor
# PKGFILES_CSWlutefisksmor     = .*/lutefisk_med_smor

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS = 
BUILD_SCRIPTS = 
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@ginstall -d $(DESTDIR)/etc/opt/csw/pkg-hooks/postfetch.d/
	@gcp $(FILEDIR)/lutefisk_med_tilbehor $(DESTDIR)/etc/opt/csw/pkg-hooks/postfetch.d/
	@gcp $(FILEDIR)/lutefisk_med_smor $(DESTDIR)/etc/opt/csw/pkg-hooks/postfetch.d/
