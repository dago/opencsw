NAME = php-mode
VERSION = 1.5.0
CATEGORIES = utils

DESCRIPTION = An Emacs mode for editting PHP code
define BLURB
PHP mode is a major mode for editing PHP source code in Emacs. As an extension of Emacs's C mode, it inherits all C mode's navigation and editing functionality. Syntax elements of PHP source code is colored according to the grammar of PHP versions 3, 4 and 5. By default, the indent rules follow the PHP PEAR coding guidelines. Additional aids for developing in PHP include documentation search of the PHP manual, code completion and a class browser.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += php-mode.el

BUILD_DEP_PKGS = CSWemacs

PACKAGES = CSWphp-mode

SPKG_DESC_CSWphp-mode = $(DESCRIPTION)
CATALOGNAME_CSWphp-mode = php_mode
RUNTIME_DEP_PKGS_CSWphp-mode = CSWemacscommon CSWemacssitestart
CHECKPKG_OVERRIDES_CSWphp-mode += surplus-dependency|CSWemacssitestart
OBSOLETES_CSWphp-mode = CSWphpmode

ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_ARGS = php-mode.info
INSTALL_SCRIPTS = 
TEST_SCRIPTS =

COMPILE_ELISP = 1

include gar/category.mk

LISPDIR = $(datadir)/emacs/site-lisp
INFODIR = $(datadir)/info

post-extract-modulated: $(WORKSRC)
	@echo "Adding GPLv3 file to source tree."
	@( cp $(FILEDIR)/gpl-3.0.txt $(WORKSRC)/COPYING )
	@$(MAKECOOKIE)

post-install-modulated:
	@echo "Installing required files..."
	@( gmkdir -p $(DESTDIR)/$(LISPDIR) $(DESTDIR)/$(INFODIR); \
		cp $(WORKSRC)/php-mode.el $(DESTDIR)$(LISPDIR); \
		chmod -x $(DESTDIR)$(LISPDIR)/*; \
		cp $(WORKSRC)/*info $(DESTDIR)/$(INFODIR) )
	@echo Installing emacs site-start file.
	@( gmkdir -p $(DESTDIR)/$(LISPDIR)/site-start.d; \
		cp $(FILEDIR)/php-mode.el $(DESTDIR)/$(LISPDIR)/site-start.d )
	@$(MAKECOOKIE)
