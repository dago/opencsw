# $Id$

NAME = gnusnamazu
# there is no realy a version version as we fetch from a git repository
VERSION = 0.3
GARTYPE = v2
CATEGORIES = xtra

DESCRIPTION = Gnus interface to Namazu
define BLURB
  Gnus interface to Namazu
endef

MASTER_SITES	=	http://git.gnus.org/cgit/gnus.git/plain/contrib/
DISTFILES		=	gnus-namazu.el
DISTFILES		+=	COPYING

CONFIGURE_SCRIPTS	=
BUILD_DEP_PKGS		+=	CSWemacs
BUILD_SCRIPTS		=	custom
TEST_SCRIPTS		=
INSTALL_SCRIPTS		=	custom

PACKAGES						=	CSWgnus-namazu
SPKG_DESC_CSWgnus-namazu		=	$(DESCRIPTION)
CATALOGNAME_CSWgnus_namazu		=	gnus_namazu
OBSOLETED_BY_CSWgnus-namazu		=	CSWgnusnamazu
CATALOGNAME_CSWgnusnamazu		=	gnusnamazu_stub
RUNTIME_DEP_PKGS_CSWgnus-namazu	+=	CSWemacs
RUNTIME_DEP_PKGS_CSWgnus-namazu	+=	CSWnamazu
# this is by desing overriden because I wish to depend on a common
# named package in both Solaris 9 and Solaris 10 when 23.1 is the
# current version for the former and 23.4 is the current version for
# the later. Note that when packaging 23.4, the CSWemacscommon became
# CSWemacs-common.
CHECKPKG_OVERRIDES_CSWgnus-namazu	+=	missing-dependency|CSWemacscommon
# these cannot be detected by checkpkg:
CHECKPKG_OVERRIDES_CSWgnus-namazu	+=	surplus-dependency|CSWnamazu
CHECKPKG_OVERRIDES_CSWgnus-namazu	+=	surplus-dependency|CSWemacs
ARCHALL_CSWgnus-namazu			=	1

include gar/category.mk

build-custom:
	cd $(WORKDIR) && emacs --batch --funcall batch-byte-compile gnus-namazu.el
	$(MAKECOOKIE)

install-custom: pkgdocdir = $(DESTDIR)/$(docdir)/$(CATALOGNAME_CSWgnus_namazu)
install-custom:
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(lispdir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKDIR)/gnus-namazu.el* $(DESTDIR)/$(lispdir)
	ginstall --directory --mode=u=rwx,go=rx $(pkgdocdir)
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(FILEDIR)/README.CSW $(pkgdocdir)
	$(MAKECOOKIE)
