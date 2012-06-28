# $Id$

NAME = svn2cl
VERSION = 0.13
GARTYPE = v2
CATEGORIES = devel

DESCRIPTION = An xsl stylesheet for generating a classic GNU-style ChangeLog from a subversion repository log
define BLURB
  This is an xsl stylesheet for generating a classic GNU-style ChangeLog from
  a subversion repository log. It is made from several changelog-like scripts
  using common xslt constructs found in different places.
endef

MASTER_SITES		=	http://arthurdejong.org/svn2cl/
DISTFILES			=	$(DISTNAME).tar.gz
DISTFILES			+=	COPYING
PATCHFILES			=	0001-Author-self.patch
PATCHFILES			+=	0002-Static-search-library.patch

RUNTIME_DEP_PKGS	=	CSWlibxslt

ARCHALL_CSWsvn2cl				=	1
CHECKPKG_OVERRIDES_CSWsvn2cl	+=	surplus-dependency|CSWlibxslt

CONFIGURE_SCRIPTS	=
BUILD_SCRIPTS		=
TEST_SCRIPTS		=
INSTALL_SCRIPTS		=	custom

include gar/category.mk

install-custom: pkgmandir = $(mandir)/man1
install-custom: pkglibdir = $(sharedstatedir)/$(NAME)
install-custom:
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(bindir)
	ginstall --preserve-timestamps --mode=u=rwx,go=rx $(WORKSRC)/svn2cl.sh $(DESTDIR)/$(bindir)/svn2cl
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkgmandir)
	ginstall --preserve-timestamps --mode=u=rw,go=r $(WORKSRC)/svn2cl.1 $(DESTDIR)/$(pkgmandir)
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkglibdir)
	ginstall --preserve-timestamps --mode=u=rw,go=r $(WORKSRC)/authors.xml $(WORKSRC)/svn2cl.xsl $(WORKSRC)/svn2html.css $(WORKSRC)/svn2html.xsl  $(DESTDIR)/$(pkglibdir)
