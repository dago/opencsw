NAME = swaks
VERSION = 20120320.0
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Swiss Army Knife SMTP
define BLURB
  Command line SMTP testing, including TLS and AUTH
endef

MASTER_SITES = http://jetmore.net/john/code/swaks/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

LICENSE = LICENSE

PATCHFILES += 0001-use-csw-perl.patch

RUNTIME_DEP_PKGS += CSWperl

ARCHALL = 1

# Checkpkg does not know we forced CSW perl to be used
CHECKPKG_OVERRIDES_CSWswaks += surplus-dependency|CSWperl

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = custom
TEST_SCRIPTS =

include gar/category.mk

install-custom:
	@echo "==> Installing $(NAME) in $(WORKSRC)"
	@ginstall -d -m 755 $(DESTDIR)$(bindir)
	@cp $(WORKSRC)/$(NAME) $(DESTDIR)$(bindir)
	@ginstall -d -m 755 $(DESTDIR)$(docdir)/$(NAME)
	@cp $(WORKSRC)/doc/* $(DESTDIR)$(docdir)/$(NAME)
	@$(MAKECOOKIE)
