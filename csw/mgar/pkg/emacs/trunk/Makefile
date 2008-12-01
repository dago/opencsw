GARNAME = emacs
GARVERSION = 21.4
PATCHLEVEL = a
CATEGORIES = utils

DESCRIPTION = Emacs editor
define BLURB
  Emacs is the extensible, customizable, self-documenting real-time display
  editor. Emacs has special code editing modes, a scripting language (elisp),
  and comes with many packages for doing mail, news and more, all in your
  editor.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION)$(PATCHLEVEL).tar.gz
#DISTFILES += CSWemacs.gspec
#DISTFILES += CSWemacsrt.gspec CSWemacs.gspec CSWxemacs.gspec
#DISTFILES += CSWemacsrt.prototype CSWemacs.prototype CSWxemacs.prototype

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)([a-z]).tar.gz

# Force make to acknowledge DESTDIR
#PATCHFILES += destdir.diff

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-kerberos5

# Test requires controlling terminal
TEST_SCRIPTS =

include gar/category.mk

pre-configure:
	@touch $(WORKSRC)/configure
	@$(MAKECOOKIE)

