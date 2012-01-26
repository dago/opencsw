NAME = emacs_sitestart
VERSION = 1.0
CATEGORIES = xtra
GARTYPE = v2

PACKAGES = CSWemacssitestart
CATALOGNAME = $(NAME)

DESCRIPTION = Emacs support for autoloading functionality at startup

VENDOR_URL = "http://www.opencsw.org"

MASTER_SITES =
DISTFILES  = COPYING site-start.el

# We define upstream file regex so we can be notifed of new upstream
# software r elease
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of
# MASTER_SITES, then uncomment the next line. Otherwise it is set by
# default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

ARCHALL = 1

COMPILE_ELISP = 1

RUNTIME_DEP_PKGS = CSWemacscommon

CONFIGURE_SCRIPTS  =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

pre-build-modulated:
	@(cd $(WORKSRC); cp ../COPYING ../site-start.el .; )

install-custom: LISPDIR=opt/csw/share/emacs/site-lisp
install-custom: $(INSTALLISADIR)
	@( cd $(WORKSRC); \
		mkdir -p $(DESTDIR)/$(LISPDIR)/site-start.d; \
		cp site-start.el $(DESTDIR)/$(LISPDIR); )
