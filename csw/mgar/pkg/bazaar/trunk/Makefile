GARNAME = bzr
GARVERSION = 1.17
#PATCHREV = .1
CATEGORIES = devel

DESCRIPTION = Bazaar is a distributed version control system.
define BLURB
  Bazaar is a slow distributed version control system that
  "Just Works". While other systems require you to adapt to
  their model of working, Bazaar adapts to the way you want
  to work, and you can try it out in five minutes. 
endef

MASTER_SITES = http://launchpad.net/bzr/$(GARVERSION)/$(GARVERSION)$(PATHREV)/+download/
DISTFILES  = $(GARNAME)-$(GARVERSION)$(PATHREV).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)$(PATHREV)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS += CSWcswclassutils

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS =
INSTALL_SCRIPTS = $(WORKSRC)/setup.py
INSTALL_ARGS = --root=$(DESTDIR)

include gar/category.mk
