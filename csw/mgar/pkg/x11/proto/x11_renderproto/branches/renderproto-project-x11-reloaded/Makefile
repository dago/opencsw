VERSION = 0.11
CATEGORIES = devel
PROTONAME = renderproto
NAME = $(PROTONAME)
DISTNAME = $(PROTONAME)-$(VERSION)

DESCRIPTION = Render extension headers from modular X.org
define BLURB
  This provides the Render extension headers from modular X.org X11 project.
endef
	
X11_RELEASE_VERSION = X11R7.5
MASTER_SITES = http://xorg.freedesktop.org/releases/$(X11_RELEASE_VERSION)/src/proto/
DISTFILES = $(PROTONAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(PROTONAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSW$(PROTONAME)
CATALOGNAME_CSW$(PROTONAME) = $(PROTONAME)

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

