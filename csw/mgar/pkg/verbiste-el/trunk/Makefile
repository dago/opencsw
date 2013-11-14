# $Id$

NAME	=	verbiste-el
# taken from the constant verbiste-version
VERSION	=	head
GARTYPE	=	v2

DESCRIPTION	=	Emacs extension for the verbiste French conjugation system
define BLURB
  Emacs extension for the verbiste French conjugation system
endef

VENDOR_URL		=	http://gaffer.ptitcanardnoir.org/verbiste-el/
GIT_REPOS		=	git://gaffer.ptitcanardnoir.org/verbiste-el.git
ifeq ($(TZ),Europe/Berlin)
GIT_USE_PROXY	=	1
endif
DISTFILES		+=	COPYING.GPL2
LICENSE			=	COPYING.GPL2

BUILD_DEP_PKGS		+=	CSWemacs

CONFIGURE_SCRIPTS	=
BUILD_SCRIPTS		=	custom
TEST_SCRIPTS		=
INSTALL_SCRIPTS		=	custom

ARCHALL = 1

RUNTIME_DEP_PKGS += CSWemacs-common
RUNTIME_DEP_PKGS += CSWverbiste
CHECKPKG_OVERRIDES_CSWverbiste-el += surplus-dependency|CSWverbiste

include gar/category.mk

build-custom:	\
				$(WORKSRC)/verbiste.elc
	$(MAKECOOKIE)

$(WORKSRC)/verbiste.elc:	$(WORKSRC)/verbiste.el
	cd $(WORKSRC) && emacs --batch --funcall batch-byte-compile verbiste.el

install-custom: pkgdest	=	$(DESTDIR)/$(datadir)/emacs/site-lisp
install-custom:
	ginstall --directory --mode=u=rwx,go=rx $(pkgdest)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/verbiste.el $(pkgdest)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/verbiste.elc $(pkgdest)
	$(MAKECOOKIE)
