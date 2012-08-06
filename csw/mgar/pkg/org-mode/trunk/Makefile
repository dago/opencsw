# $Id$

NAME_PREFIX	=	org
NAME		=	$(NAME_PREFIX)-mode
VERSION		=	7.8.11
GARTYPE		=	v2
CATEGORIES	=	apps

DESCRIPTION = An Emacs Mode for Notes, Planning, and Authoring
define BLURB
  Org mode is for keeping notes, maintaining TODO lists, doing project
  planning, and authoring with a fast and effective plain-text system. 
endef

MASTER_SITES	=	http://orgmode.org/
WORKSRC			=	$(WORKDIR)/$(NAME_PREFIX)-$(VERSION)
PATCHDIR		=	$(WORKSRC)
DISTFILES		=	$(NAME_PREFIX)-$(VERSION).tar.gz
DISTFILES		+=	README.CSW
DISTFILES		+=	COPYING
PATCHFILES		+=	0001-Use-Open-CSW-prefix.patch
PATCHFILES		+=	0002-Fix-documentation-build-target.patch

BUILD_DEP_PKGS		+=	CSWemacs
BUILD_DEP_PKGS		+=	CSWgsed
BUILD_DEP_PKGS		+=	CSWtetex

CONFIGURE_SCRIPTS	=
BUILD_SCRIPTS		=	nominal
BUILD_SCRIPTS		+=	doc
TEST_SCRIPTS		=
INSTALL_SCRIPTS		=	nominal
INSTALL_SCRIPTS		+=	info

ARCHALL							=	1
RUNTIME_DEP_PKGS				+=	CSWemacs
CHECKPKG_OVERRIDES_CSWorg-mode	+=	surplus-dependency|CSWemacs
CHECKPKG_OVERRIDES_CSWorg-mode	+=	missing-dependency|CSWemacscommon
CHECKPKG_OVERRIDES_CSWorg-mode	+=	file-with-bad-content|/usr/local|root/opt/csw/share/org-mode/lisp/htmlize.el

EXTRA_TEXINFO						=	$(infodir)/.*

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/libexec/flex-2.5.35/bin:$(PATH)

build-nominal:
	cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) && $(MAKE) -C $(OBJDIR)
	$(MAKECOOKIE)

build-doc:
	cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) && $(MAKE) -C $(OBJDIR) doc
	$(MAKECOOKIE)

install-nominal:
	cd $(WORKSRC) && /usr/bin/env -i $(INSTALL_ENV) && $(MAKE) -C $(OBJDIR) $(INSTALL_ARGS) DESTDIR=$(DESTDIR) install
	$(MAKECOOKIE)

install-info:
	cd $(WORKSRC) && /usr/bin/env -i $(INSTALL_ENV) && $(MAKE) -C $(OBJDIR) $(INSTALL_ARGS) DESTDIR=$(DESTDIR) install-info
	$(MAKECOOKIE)

post-install-modulated: pkgdoc = $(docdir)/$(NAME)
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
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(contrib)
	gtar --directory=$(WORKSRC)/contrib --create --exclude-vcs --file=- . | gtar --directory $(DESTDIR)/$(contrib) --extract --file=-
	$(MAKECOOKIE)
