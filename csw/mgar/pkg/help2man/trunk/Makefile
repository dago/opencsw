NAME = help2man
VERSION = 1.39.2
CATEGORIES = devel

DESCRIPTION = A tool for automatically generating simple manual pages from program output
define BLURB
  help2man is a tool for automatically generating simple manual pages from program output.
  It is intended to provide an easy way for software authors to include a manual page
  in their distribution without having to maintain that document.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.gz

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

DEP_PKGS = CSWpmlocalegettext

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

CHECKPKG_OVERRIDES_CSWhelp2man += surplus-dependency|CSWpmlocalegettext

include gar/category.mk

post-install-modulated:
	-perl -pi -e 's,/usr/lib,$(libdir),g;' \
		-e 's,/usr/share,$(sharedstatedir),g;' \
		$(DESTDIR)$(infodir)/help2man.info
