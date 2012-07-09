# $Id$

NAME = kakasi
VERSION = 2.3.4
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = KAnji KAna Simple Inverter
define BLURB
  KAnji KAna Simple Inverter
endef

MASTER_SITES = http://kakasi.namazu.org/stable/
DISTFILES  = $(DISTNAME).tar.gz

GARCOMPILER		=	GNU
CONFIGURE_ARGS	=	$(DIRPATHS)

PACKAGES							+=	CSWkakasi
CATALOGNAME_CSWkakasi				=	kakasi
SPKG_DESC_CSWkakasi					+=	$(DESCRIPTION)

PACKAGES							+=	CSWlibkakasi2
CATALOGNAME_CSWlibkakasi2			=	libkakasi2
PKGFILES_CSWlibkakasi2				+=	$(call baseisadirs,$(libdir),libkakasi\.so\.2\.1\.0)
PKGFILES_CSWlibkakasi2				+=	$(call baseisadirs,$(libdir),libkakasi\.so\.2(\.\d+)*)
PKGFILES_CSWlibkakasi2				+=	/opt/csw/share/kakasi/.*

SPKG_DESC_CSWlibkakasi2				+=	$(DESCRIPTION), libkakasi.so.2

PACKAGES							+=	CSWkakasi-dev
CATALOGNAME_CSWkakasi-dev			=	kakasi_dev
SPKG_DESC_CSWkakasi-dev				+=	$(DESCRIPTION), development files
PKGFILES_CSWkakasi-dev				+=	/opt/csw/lib/libkakasi.so
PKGFILES_CSWkakasi-dev				+=	$(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWkakasi-dev		+=	CSWlibkakasi2
CHECKPKG_OVERRIDES_CSWkakasi-dev	+=	surplus-dependency|CSWlibkakasi2
CHECKPKG_OVERRIDES_CSWkakasi-dev	+=	archall-devel-package
ARCHALL_CSWkakasi-dev				=	1

include gar/category.mk

post-install-modulated:
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(mandir)/man1
	ginstall --preserve-timestamps --mode=u=rwx,go=r $(WORKSRC)/doc/kakasi.1 $(DESTDIR)/$(mandir)/man1
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)
