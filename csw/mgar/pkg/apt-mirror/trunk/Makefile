# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = apt-mirror
VERSION = 0.4.8
GARTYPE = v2

DESCRIPTION = Debian and Ubuntu apt sources mirroring tool
define BLURB
  A small tool that provides ability to mirror any parts (or even all) of
  Debian and Ubuntu GNU/Linux distributions and/or any other apt sources
  which typically provided by open source developers.
endef

MASTER_SITES	=	$(SF_MIRRORS)
DISTFILES		=	$(NAME)_$(VERSION).orig.tar.gz
DISTFILES		+=	COPYING
PATCHFILES		+=	0001-From-private-recipe.patch
PATCHFILES		+=	0002-Adapt-to-OpenCSW-file-system-layout.patch

CONFIGURE_SCRIPTS	=
BUILD_SCRIPTS		=
TEST_SCRIPTS		=
INSTALL_SCRIPTS		=	custom

RUNTIME_DEP_PKGS					+=	CSWperl
CHECKPKG_OVERRIDES_CSWapt-mirror	+=	surplus-dependency|CSWperl
RUNTIME_DEP_PKGS					+=	CSWgzip
CHECKPKG_OVERRIDES_CSWapt-mirror	+=	surplus-dependency|CSWgzip
RUNTIME_DEP_PKGS					+=	CSWwget
CHECKPKG_OVERRIDES_CSWapt-mirror	+=	surplus-dependency|CSWwget

ARCHALL	=	1

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/libexec/flex-2.5.35/bin:$(PATH)

install-custom: pkgdocdir = $(docdir)/$(NAME)
install-custom: pkgsysconfdir = $(sysconfdir)/$(NAME)
install-custom: pkglocalstatedir = $(localstatedir)/$(NAME)
install-custom:
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(bindir)
	ginstall --mode=u=rwx,go=rx $(WORKSRC)/apt-mirror $(DESTDIR)/$(bindir)
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkgdocdir)
	ginstall --mode=u=rw,go=r $(WORKSRC)/CHANGELOG $(DESTDIR)/$(pkgdocdir)
	ginstall --mode=u=rw,go=r $(WORKSRC)/postmirror.sh $(DESTDIR)/$(pkgdocdir)
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkgsysconfdir)
	ginstall --mode=u=rw,go=r $(WORKSRC)/mirror.list $(DESTDIR)/$(pkgsysconfdir)
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkglocalstatedir)/mirror
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkglocalstatedir)/skel
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(pkglocalstatedir)/var
	$(MAKECOOKIE)
