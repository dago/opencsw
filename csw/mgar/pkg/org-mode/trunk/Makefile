# $Id$

NAME_PREFIX	=	org
NAME		=	$(NAME_PREFIX)-mode
VERSION		=	8.2.1
GARTYPE		=	v2

DESCRIPTION = An Emacs Mode for Notes, Planning, and Authoring
define BLURB
  Org mode is for keeping notes, maintaining TODO lists, doing project
  planning, and authoring with a fast and effective plain-text system. 
endef

MASTER_SITES	=	http://orgmode.org/
WORKSRC			=	$(WORKDIR)/$(NAME_PREFIX)-$(VERSION)
PATCHDIR		=	$(WORKSRC)
DISTFILES		=	$(NAME_PREFIX)-$(VERSION).tar.gz
DISTFILES		+=	COPYING
DISTFILES		+=	local.mk

BUILD_DEP_PKGS		+=	CSWemacs
BUILD_DEP_PKGS		+=	CSWgsed
BUILD_DEP_PKGS		+=	CSWtexlive
BUILD_DEP_PKGS		+=	CSWtexinfo

CONFIGURE_SCRIPTS	=
# skiping the tests because the scripts are supplied only in
# repository snapshots but not in the distributed sources
TEST_SCRIPTS		=

ARCHALL							=	1
CATALOGNAME_CSWorg-mode			=	org_mode
RUNTIME_DEP_PKGS				+=	CSWemacs
CHECKPKG_OVERRIDES_CSWorg-mode	+=	surplus-dependency|CSWemacs
CHECKPKG_OVERRIDES_CSWorg-mode	+=	missing-dependency|CSWemacs-common
CHECKPKG_OVERRIDES_CSWorg-mode	+=	file-with-bad-content|/usr/local|root/opt/csw/share/org/lisp/htmlize.el

EXTRA_TEXINFO						=	$(infodir)/.*

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

# remove not supported contributions (this is the easiest way to do it)
post-extract:
	cd $(WORKSRC)/contrib/lisp && \
	rm -f \
		ob-oz.el \
		org-jira.el
	$(MAKECOOKIE)

pre-build-modulated:
	cp $(WORKDIR)/local.mk $(WORKSRC)
	$(MAKECOOKIE)

post-install-modulated: pkgdoc = $(docdir)/$(CATALOGNAME_CSWorg-mode)
post-install-modulated: source = $(WORKSRC)/doc
post-install-modulated: contrib = $(sharedstatedir)/$(NAME)
post-install-modulated:
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkgdoc)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/org.html $(DESTDIR)/$(pkgdoc)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/org.pdf $(DESTDIR)/$(pkgdoc)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/orgcard.pdf $(DESTDIR)/$(pkgdoc)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/orgcard_letter.pdf $(DESTDIR)/$(pkgdoc)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(source)/orgguide.pdf $(DESTDIR)/$(pkgdoc)
	mv $(DESTDIR)/$(infodir)/org $(DESTDIR)/$(infodir)/org-ocsw
	gsed --in-place --expression='s/^[*] Org Mode: (org)[.]      Outline-based notes management and organizer$$/* Org Mode (OCSW): (org-ocsw).      Outline-based notes management and organizer as supplied by Open CSW/' $(DESTDIR)/$(infodir)/org-ocsw
	$(MAKECOOKIE)
