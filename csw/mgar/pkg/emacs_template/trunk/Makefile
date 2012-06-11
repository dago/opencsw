# $Id$

NAME = emacs_template
VERSION = 3.1c
GARTYPE = v2
CATEGORIES = xtra

DESCRIPTION = Templates for Emacs
define BLURB
  Template Package for Emacs
endef

DISTNAME		=	template
MASTER_SITES	=	http://downloads.sourceforge.net/emacs-template/$(DISTNAME)/$(VERSION)/
DISTFILES  		=	$(DISTNAME)-$(VERSION).tar.gz
DISTFILES		+=	README.CSW
VENDOR_URL		=	http://emacs-template.sourceforge.net/

BUILD_DEP_PKGS		+=	CSWemacs

RUNTIME_DEP_PKGS	+=	CSWemacs

PACKAGES						=	CSWemacs-template
SPKG_DESC_CSWemacs-template		=	$(DESCRIPTION)
CATALOGNAME_CSWemacs-template	=	emacs_template
OBSOLETED_BY_CSWemacs-template	=	CSWemacstemplate
CATALOGNAME_CSWemacstemplate	=	emacs_template_stub
ARCHALL_CSWemacs-template		=	1

# this is by desing overriden because I wish to depend on a common
# named package in both Solaris 9 and Solaris 10 when 23.1 is the
# current version for the former and 23.4 is the current version for
# the later. Note that when packaging 23.4, the CSWemacscommon became
# CSWemacs-common.
CHECKPKG_OVERRIDES_CSWemacs-template += missing-dependency|CSWemacscommon
CHECKPKG_OVERRIDES_CSWemacs-template += surplus-dependency|CSWemacs

CONFIGURE_SCRIPTS	=
BUILD_SCRIPTS		=	custom
TEST_SCRIPTS		=
INSTALL_SCRIPTS		=	custom

include gar/category.mk

prefix		=	/opt/csw
sharedir	=	$(prefix)/share
lispdir		=	$(sharedir)/emacs/site-lisp
docdir		=	$(sharedir)/doc/$(NAME)
tpldir		=	$(docdir)/templates

build-custom:	\
				$(WORKSRC)/lisp/template.elc
	$(MAKECOOKIE)

$(WORKSRC)/lisp/template.elc:	$(WORKSRC)/lisp/template.el
	cd $(WORKSRC) && emacs --batch --funcall batch-byte-compile lisp/template.el

install-custom:
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(lispdir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/lisp/template.el $(DESTDIR)/$(lispdir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/lisp/template.elc $(DESTDIR)/$(lispdir)
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(docdir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/lisp/ChangeLog $(DESTDIR)/$(docdir)
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(tpldir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/templates/DEFAULT.tpl $(DESTDIR)/$(tpldir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/templates/Makefile.tpl $(DESTDIR)/$(tpldir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/templates/README.tpl $(DESTDIR)/$(tpldir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/templates/TEMPLATE.c.tpl $(DESTDIR)/$(tpldir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/templates/TEMPLATE.cls.tpl $(DESTDIR)/$(tpldir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/templates/TEMPLATE.el.tpl $(DESTDIR)/$(tpldir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/templates/TEMPLATE.h.tpl $(DESTDIR)/$(tpldir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/templates/TEMPLATE.html.tpl $(DESTDIR)/$(tpldir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/templates/TEMPLATE.java.tpl $(DESTDIR)/$(tpldir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/templates/TEMPLATE.sty.tpl $(DESTDIR)/$(tpldir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/templates/TEMPLATE.tex.tpl $(DESTDIR)/$(tpldir)
	$(MAKECOOKIE)
