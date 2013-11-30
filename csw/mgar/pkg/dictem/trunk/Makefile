# $Id$

NAME = dictem
VERSION = 1.0.4
GARTYPE = v2

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = http://www.mova.org/~cheusov/pub/dictem/
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES		+=	COPYING.GPL2
LICENSE			=	COPYING.GPL2

BUILD_DEP_PKGS		+=	CSWemacs

CONFIGURE_SCRIPTS	=
BUILD_SCRIPTS		=	custom
TEST_SCRIPTS		=
INSTALL_SCRIPTS		=	custom

ARCHALL = 1

RUNTIME_DEP_PKGS += CSWemacs-common
RUNTIME_DEP_PKGS += CSWdict
CHECKPKG_OVERRIDES_CSWdictem += surplus-dependency|CSWdict

include gar/category.mk

build-custom:
	cd $(WORKSRC) && emacs --batch --funcall batch-byte-compile dictem.el
	$(MAKECOOKIE)

install-custom: pkgdest		=	$(DESTDIR)/$(datadir)/emacs/site-lisp
install-custom: pkgdocdir	=	$(DESTDIR)/$(docdir)/$(NAME)
install-custom:
	ginstall --directory --mode=u=rwx,go=rx $(pkgdest)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/dictem.el $(pkgdest)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/dictem.elc $(pkgdest)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/dictem-lingvo-dsl.el $(pkgdest)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/dictem-elisp.el $(pkgdest)
	ginstall --directory --mode=u=rwx,go=rx $(pkgdocdir)
	ginstall --preserve-timestamps --mode=u=rw,go=r $(WORKSRC)/AUTHORS $(pkgdocdir)
	ginstall --preserve-timestamps --mode=u=rw,go=r $(WORKSRC)/NEWS $(pkgdocdir)
	ginstall --preserve-timestamps --mode=u=rw,go=r $(WORKSRC)/README $(pkgdocdir)
	ginstall --preserve-timestamps --mode=u=rw,go=r $(WORKSRC)/TODO	$(pkgdocdir)
	$(MAKECOOKIE)
