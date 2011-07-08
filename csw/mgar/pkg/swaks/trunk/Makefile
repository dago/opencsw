NAME = swaks
VERSION = 20061116.0
GARTYPE = v1
CATEGORIES = utils

DESCRIPTION = Swiss Army Knife SMTP
define BLURB
Command line SMTP testing, including TLS and AUTH
endef

#http://jetmore.net/john/code/swaks.20061116.0

MASTER_SITES = http://jetmore.net/john/code/swaks
DISTFILES  = $(NAME)-$(VERSION)
DISTFILES += $(call admfiles,CSW$(NAME), depend)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = custom
TEST_SCRIPTS =

include gar/category.mk

install-custom:
	@echo "==> Installing $(NAME) in $(WORKSRC)"
	@mkdir $(DESTDIR)/opt/csw/bin
	@cp $(DOWNLOADDIR)/$(NAME)-$(VERSION) $(DESTDIR)/opt/csw/bin/swaks
	@$(MAKECOOKIE)
