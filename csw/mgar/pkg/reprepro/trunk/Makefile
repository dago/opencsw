# $Id$

NAME	=	reprepro
VERSION	=	4.16.0
GARTYPE	=	v2

DESCRIPTION	=	Debian package repository producer
define BLURB
 reprepro is a tool to manage a repository of Debian packages
 (.deb, .udeb, .dsc, ...). It stores files either being
 injected manually or downloaded from some other repository
 (partially) mirrored into one pool/ hierarchy.
 Managed packages and files are stored in a Berkeley DB,
 so no database server is needed.
 Checking signatures of mirrored repositories and creating
 signatures of the generated Package indices is supported.
 .
 This package also contains the changestool and rredtool helpers.
endef

MASTER_SITES	=	https://alioth.debian.org/frs/download.php/file/4109/
DISTFILES		=	$(DISTNAME).orig.tar.gz

GARCOMPILER		=	GNU
GARFLAVOR		=	DBG
EXTRA_INC		=	$(prefix)/bdb48/include
EXTRA_LIB		=	$(prefix)/bdb48/lib
CONFIGURE_ARGS	=	$(DIRPATHS)

BUILD_DEP_PKGS	+=	CSWbdb48devel
BUILD_DEP_PKGS	+=	CSWgpgme-dev
BUILD_DEP_PKGS	+=	CSWlibarchive-dev

# this is necessary to have vasprintf which is available only with
# libc from SUNW_1.22.7 up
LINKER_MAP_RELEASE	=	

PATCHFILES	+=	0001-fix-directory-entry-portability.patch
PATCHFILES	+=	0002-fix-make-temporary-file.patch
PATCHFILES	+=	0003-add-missing-prototypes.patch
PATCHFILES	+=	0004-implement-missing-getline-function.patch

INSTALL_SCRIPTS		=	nominal
INSTALL_SCRIPTS		+=	custom

RUNTIME_DEP_PKGS_CSWreprepro	+=	CSWlibgpgme11
include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

install-nominal:
	cd $(WORKSRC) && /usr/bin/env -i $(INSTALL_ENV) && $(MAKE) -C $(OBJDIR) $(INSTALL_ARGS) DESTDIR=$(DESTDIR) install

install-custom: pkgdocdir = $(docdir)/$(NAME)
install-custom:
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkgdocdir)
	ginstall --mode=u=rw,go=r $(WORKSRC)/docs/bzip.example $(DESTDIR)/$(pkgdocdir)
	ginstall --mode=u=rw,go=r $(WORKSRC)/docs/changelogs.example $(DESTDIR)/$(pkgdocdir)
	ginstall --mode=u=rw,go=r $(WORKSRC)/docs/copybyhand.example $(DESTDIR)/$(pkgdocdir)
	ginstall --mode=u=rw,go=r $(WORKSRC)/docs/pdiff.example $(DESTDIR)/$(pkgdocdir)
	ginstall --mode=u=rw,go=r $(WORKSRC)/docs/xz.example $(DESTDIR)/$(pkgdocdir)
	ginstall --mode=u=rw,go=r $(WORKSRC)/docs/FAQ $(DESTDIR)/$(pkgdocdir)
	ginstall --mode=u=rw,go=r $(WORKSRC)/docs/manual.html $(DESTDIR)/$(pkgdocdir)
	ginstall --mode=u=rw,go=r $(WORKSRC)/docs/*.py $(DESTDIR)/$(pkgdocdir)
	ginstall --mode=u=rw,go=r $(WORKSRC)/docs/recovery $(DESTDIR)/$(pkgdocdir)
	ginstall --mode=u=rw,go=r $(WORKSRC)/docs/short-howto $(DESTDIR)/$(pkgdocdir)
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkgdocdir)/di.example
	ginstall --mode=u=rw,go=r $(WORKSRC)/docs/di.example/* $(DESTDIR)/$(pkgdocdir)/di.example
	$(MAKECOOKIE)
