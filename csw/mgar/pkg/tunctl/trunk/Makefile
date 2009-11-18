GARNAME = tunctl
GARVERSION = 1.5
CATEGORIES = net

DESCRIPTION = Used to set up and maintain persistent TUN/TAP network interface
define BLURB
  tunctl is used to set up and maintain persistent TUN/TAP network interfaces,
  enabling user applications to simulate network traffic. Such interfaces
  is useful for VPN software, virtualization, emulation, simulation, and a
  number of other applications.
endef

MASTER_SITES = http://garr.dl.sourceforge.net/sourceforge/tunctl/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# since there is no configure script, this is intentionally left empty
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_SCRIPTS =

# no tests
TEST_SCRIPTS = custom

include gar/category.mk

test-custom:
	@true

pre-build-modulated:
	@perl -pi -e 's#^CFLAGS.*#$(CFLAGS)#' $(WORKSRC)/Makefile
