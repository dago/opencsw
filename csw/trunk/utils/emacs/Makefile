GARNAME = emacs
GARVERSION = 21.3
CATEGORIES = utils

DESCRIPTION = Emacs editor
define BLURB
  Emacs is the extensible, customizable, self-documenting real-time display
  editor. Emacs has special code editing modes, a scripting language (elisp),
  and comes with many packages for doing mail, news and more, all in your
  editor.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWemacs.gspec
#DISTFILES += CSWemacsrt.gspec CSWemacs.gspec CSWxemacs.gspec
#DISTFILES += CSWemacsrt.prototype CSWemacs.prototype CSWxemacs.prototype

CONFIGURE_ARGS  = $(DIRPATHS)
#CONFIGURE_ARGS += 

# Test requires controlling terminal
ENABLE_TEST = 0

include ../category.mk

