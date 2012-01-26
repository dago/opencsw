# $Id$
#
# TODO (release-critical prefixed with !, non release-critical with *)
# ! write install-custom, cf.
#   http://pkgs.fedoraproject.org/gitweb/?p=waf.git;a=blob_plain;f=waf.spec
#
NAME = waf
VERSION = 1.6.3
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Python-based build automation tool
define BLURB
  Waf is a Python-based framework for configuring, compiling and
  installing applications. It is a replacement for other tools such as
  Autotools, Scons, CMake or Ant.
endef

VENDOR_URL   = http://code.google.com/p/waf/
MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES    = $(DISTNAME).tar.bz2

UPSTREAM_MASTER_SITES = http://code.google.com/p/waf/downloads/list

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS     = custom
TEST_SCRIPTS      = 
INSTALL_SCRIPTS   = custom

include gar/category.mk

configure-custom:
	cd $(WORKSRC) && $(CONFIGURE_ENV) ./waf-light configure
	@$(MAKECOOKIE)	

build-custom:
	cd $(WORKSRC) && $(BUILD_ENV) ./waf-light build
	@$(MAKECOOKIE)	

install-custom:
	$(error "waf's install-custom not yet populated")
	@$(MAKECOOKIE)	
