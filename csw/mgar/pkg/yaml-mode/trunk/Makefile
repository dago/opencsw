GARNAME = yaml-mode
GARVERSION = 0.0.3
CATEGORIES = xtra

PACKAGES = CSWyamlmode

CATALOGNAME_CSWyamlmode = yaml_mode

REQUIRED_PKGS_CSWphpmode = CSWemacscommon

ARCHALL_CSWyamlmode = 1

DESCRIPTION = A YAML mode for Emacs
define BLURB
This is a major mode for editing files in the YAML data
serialization format.  It was initially developed by Yoshiki
Kurihara and many features were added by Marshall Vandegrift.  As
YAML and Python share the fact that indentation determines
structure, this mode provides indentation and indentation command
behavior very similar to that of python-mode.
endef

MASTER_SITES = http://tweedle-dee.org/svn/emacs.d/site-lisp/
DISTFILES  = $(GARNAME).el

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of
# MASTER_SITES, then uncomment the next line. Otherwise it is set by
# default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = 
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

COMPILE_ELISP = 1

include gar/category.mk

cp-extract-yaml-mode.el: $(WORKSRC)
	@echo " ===> Copying yaml-mode.el into work source directory."
	@cp $(DOWNLOADDIR)/yaml-mode.el $(WORKSRC)
	@cp $(FILEDIR)/gpl* $(WORKSRC)/COPYING
	@$(MAKECOOKIE)

install-custom:
	@( cd $(WORKSRC); \
		gmkdir -p $(DESTDIR)$(lispdir); \
		cp yaml-mode.el $(DESTDIR)$(lispdir) )
	@$(MAKECOOKIE)