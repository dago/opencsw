NAME = bzr
VERSION = 1.17
#PATCHREV = .1
CATEGORIES = devel
GARTYPE = v2

DESCRIPTION = Bazaar is a distributed version control system.
define BLURB
  Bazaar is a slow distributed version control system that
  "Just Works". While other systems require you to adapt to
  their model of working, Bazaar adapts to the way you want
  to work, and you can try it out in five minutes. 
endef

MASTER_SITES = http://launchpad.net/bzr/$(VERSION)/$(VERSION)$(PATHREV)/+download/
DISTFILES  = $(NAME)-$(VERSION)$(PATHREV).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)$(PATHREV)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS += CSWcswclassutils

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS =
INSTALL_SCRIPTS = $(WORKSRC)/setup.py
INSTALL_ARGS = --root=$(DESTDIR)

include gar/category.mk
