# $Id$

NAME			=	leocad
VERSION			=	0.79.3
PIECES_VERSION	=	7114
GARTYPE			=	v2

DESCRIPTION = Virtual Lego brick CAD software
define BLURB
  CAD program that allows people to build virtual models using bricks similar
  to those found in LEGO toys
endef

MASTER_SITES	=	$(GOOGLE_MIRROR)
DISTNAME		=	$(NAME)
DISTFILES		=	$(NAME)-$(VERSION)-src.tgz
DISTFILES		+=	pieces-$(PIECES_VERSION).zip
# this raises "warning: 1 line adds whitespace errors"; choosed to ignore
PATCHFILES		+=	0001-Use-POSIX-to-determine-the-file-type.patch

GARCOMPILER			=	GNU

CONFIGURE_ARGS		=	$(DIRPATHS)
CONFIGURE_SCRIPTS	=	custom

BUILD_DEP_PKGS		+=	CSWlibglib2-dev
BUILD_DEP_PKGS		+=	CSWlibgtk2-dev
BUILD_DEP_PKGS		+=	CSWlibz-dev
BUILD_DEP_PKGS		+=	CSWlibjpeg-dev
BUILD_DEP_PKGS		+=	CSWlibpng-dev
BUILD_DEP_PKGS		+=	CSWmesa

TEST_SCRIPTS		=

RUNTIME_DEP_PKGS_CSWleocad	+=	CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWleocad	+=	CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWleocad	+=	CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWleocad	+=	CSWlibz1
RUNTIME_DEP_PKGS_CSWleocad	+=	CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWleocad	+=	CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWleocad	+=	CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWleocad	+=	CSWpango
RUNTIME_DEP_PKGS_CSWleocad	+=	CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWleocad	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWleocad	+=	CSWlibjpeg7

REINPLACE_WHEN_USRSHARE	=	postinstall
REINPLACE_USRSHARE		+=	/opt/csw/share/man/man1/leocad.1

PACKAGES						+=	CSWleocad
CATALOGNAME_CSWleocad			=	leocad
SPKG_DESC_CSWleocad				+=	$(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWleocad		+=	CSWleocad-pieces
CHECKPKG_OVERRIDES_CSWleocad	+=	surplus-dependency|CSWleocad-pieces

leocadDatadir	=	$(datadir)/$(NAME)

PACKAGES							+=	CSWleocad-pieces
CATALOGNAME_CSWleocad-pieces		=	leocad_pieces
SPKG_DESC_CSWleocad-pieces			+=	$(DESCRIPTION), pieces
PKGFILES_CSWleocad-pieces			=	$(leocadDatadir)/library.bin
ARCHALL_CSWleocad-pieces			=	1

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/libexec/flex-2.5.35/bin:$(PATH)

configure-custom:
	cd $(WORKSRC) && $(MAKE) config PREFIX=$(prefix)
	$(MAKECOOKIE)

post-install-modulated:
	@echo "executing $@"
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)/$(leocadDatadir)
	ginstall --preserve-timestamps --mode=u=rwx,go=rx $(WORKDIR)/library.bin $(DESTDIR)/$(leocadDatadir)
	$(MAKECOOKIE)
