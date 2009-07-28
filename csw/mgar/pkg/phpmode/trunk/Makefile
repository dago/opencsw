GARNAME = php-mode
GARVERSION = 1.5.0
CATEGORIES = utils

DESCRIPTION = An Emacs mode for editting PHP code
define BLURB
PHP mode is a major mode for editing PHP source code in Emacs. As an extension of Emacs's C mode, it inherits all C mode's navigation and editing functionality. Syntax elements of PHP source code is colored according to the grammar of PHP versions 3, 4 and 5. By default, the indent rules follow the PHP PEAR coding guidelines. Additional aids for developing in PHP include documentation search of the PHP manual, code completion and a class browser.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PREREQUISITE_PKGS = CSWemacs

PACKAGES = CSWphpmode

CATALOGNAME_CSWphpmode = php_mode

REQUIRED_PKGS_CSWphpmode = CSWemacscommon

ARCHALL = 1

SPKG_DESC_CSWphpmode = An Emacs mode for editting PHP code

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of
# MASTER_SITES, then uncomment the next line. Otherwise it is set by
# default to the value of MASTER_SITES

# UPSTREAM_MASTER_SITES = 

CONFIGURE_SCRIPTS =
BUILD_ARGS = php-mode.info
INSTALL_SCRIPTS = 
TEST_SCRIPTS =

include gar/category.mk

LISPDIR = $(datadir)/emacs/site-lisp
INFODIR = $(datadir)/info

post-extract-modulated:
	@echo "Adding GPLv3 file to source tree."
	@( cp $(FILEDIR)/gpl-3.0.txt $(WORKSRC)/COPYING )
	@$(MAKECOOKIE)

post-install-modulated:
	@echo "Installing required files..."
	( gmkdir -p $(DESTDIR)/$(LISPDIR) $(DESTDIR)/$(INFODIR); \
		emacs -batch -f batch-byte-compile $(WORKSRC)/php-mode.el; \
		cp $(WORKSRC)/php-mode.el* $(DESTDIR)$(LISPDIR); \
		cp $(WORKSRC)/*info $(DESTDIR)/$(INFODIR) )
	@$(MAKECOOKIE)