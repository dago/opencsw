GARNAME = authz-tools
GARVERSION = 0.6.1
CATEGORIES = utils

DESCRIPTION = tools to manipulate authz files
define BLURB
	This is a package that contains several tools to manipulate authz files (as
	used by mod_auth_svn module for Subversion. The main reason for this package
	to exist -- big authz files and authz files located on remote computers.
endef

# Project URL
SPKG_SOURCEURL = http://only.mawhrin.net/~mss/thingies/authz/

# Source files
MASTER_SITES = http://only.mawhrin.net/~mss/thingies/authz/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
#DISTFILES += $(call admfiles,CSWauthztools,depend,prototype)
DISTFILES += $(call admfiles,CSWauthztools,)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include ../category.mk

install-custom:
	@( cd $(WORKSRC) ; python ./setup.py install --root=$(DESTDIR) )
	@$(MAKECOOKIE)

