NAME = bzr
MAJORVERSION = 2.6
PATCHREV = b2
VERSION = $(MAJORVERSION)$(PATCHREV)
GARTYPE = v2

DESCRIPTION = Bazaar is a distributed version control system.
define BLURB
  Bazaar is a slow distributed version control system that
  "Just Works". While other systems require you to adapt to
  their model of working, Bazaar adapts to the way you want
  to work, and you can try it out in five minutes. 
endef

MASTER_SITES = https://launchpad.net/bzr/$(MAJORVERSION)/$(VERSION)/+download/
# MASTER_SITES = https://launchpad.net/bzr/2.6/2.6b2/+download/bzr-2.6b2.tar.gz
DISTFILES  = $(NAME)-$(VERSION).tar.gz
LICENSE = COPYING.txt

GARCOMPILER = SOS12U3

REINPLACE_USRLOCAL += bzrlib/transport/http/_urllib2_wrappers.py
REINPLACE_MATCH = man/man1
REINPLACE_WITH = share/man/man1
REINPLACE_FILES += setup.py
EXTRA_MERGE_EXCLUDE_FILES += .*\.py[oc]

PACKAGES += CSWpy-bzr
RUNTIME_DEP_PKGS += CSWpython
RUNTIME_DEP_PKGS += CSWlibpython2-6-1-0

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py
TEST_SCRIPTS =
INSTALL_SCRIPTS = $(WORKSRC)/setup.py
INSTALL_ARGS = --root=$(DESTDIR)

include gar/category.mk
