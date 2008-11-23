GARNAME = swaks
GARVERSION = 20061116.0
CATEGORIES = utils

DESCRIPTION = Swiss Army Knife SMTP
define BLURB
Command line SMTP testing, including TLS and AUTH
endef

#http://jetmore.net/john/code/swaks.20061116.0

MASTER_SITES = http://jetmore.net/john/code/swaks
DISTFILES  = $(GARNAME)-$(GARVERSION)
DISTFILES += $(call admfiles,CSW$(GARNAME), depend)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = custom
TEST_SCRIPTS =

include gar/category.mk

install-custom:
	@echo "==> Installing $(GARNAME) in $(WORKSRC)"
	@mkdir $(DESTDIR)/opt/csw/bin
	@cp $(DOWNLOADDIR)/$(GARNAME)-$(GARVERSION) $(DESTDIR)/opt/csw/bin/swaks
	@$(MAKECOOKIE)
