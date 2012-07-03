# $Id$

NAME = jpilot
VERSION = 1.8.1
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = GNOME Desktop Organizer Software for the Palm Pilot
define BLURB
  J-Pilot is a desktop organizer application for PalmOS devices.
  It is meant to be an alternative to the Palm Desktop for those
   who run the most popular Operating Systems in the World, Linux and Unix.
endef

MASTER_SITES	=	http://jpilot.org/
DISTFILES		=	$(DISTNAME).tar.gz
DISTFILES		+=	CSWjpilot.postinstall
DISTFILES		+=	CSWjpilot.preremove

GARCOMPILER			=	GNU

BUILD_DEP_PKGS		+=	CSWfconfig-dev
BUILD_DEP_PKGS		+=	CSWggettext-dev
BUILD_DEP_PKGS		+=	CSWlibatk-dev
BUILD_DEP_PKGS		+=	CSWlibbz2-dev
BUILD_DEP_PKGS		+=	CSWlibcairo-dev
BUILD_DEP_PKGS		+=	CSWlibexpat-dev
BUILD_DEP_PKGS		+=	CSWlibfreetype-dev
BUILD_DEP_PKGS		+=	CSWlibgcrypt-dev
BUILD_DEP_PKGS		+=	CSWlibgdk-pixbuf-dev
BUILD_DEP_PKGS		+=	CSWlibglib2-dev
BUILD_DEP_PKGS		+=	CSWlibgpg-error-dev
BUILD_DEP_PKGS		+=	CSWlibgtk2-dev
BUILD_DEP_PKGS		+=	CSWlibiconv-dev
BUILD_DEP_PKGS		+=	CSWlibpixman-dev
BUILD_DEP_PKGS		+=	CSWlibpng-dev
BUILD_DEP_PKGS		+=	CSWlibz-dev
BUILD_DEP_PKGS		+=	CSWpangodevel
BUILD_DEP_PKGS		+=	CSWpilot-link-dev
BUILD_DEP_PKGS		+=	CSWpmxmlparser

RUNTIME_DEP_PKGS	+=	CSWlibatk1-0-0
RUNTIME_DEP_PKGS	+=	CSWlibcairo2
RUNTIME_DEP_PKGS	+=	CSWlibfontconfig1
RUNTIME_DEP_PKGS	+=	CSWlibfreetype6
RUNTIME_DEP_PKGS	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS	+=	CSWlibgcrypt11
RUNTIME_DEP_PKGS	+=	CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibgio2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibglib2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibgobject2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibgpg-error0
RUNTIME_DEP_PKGS	+=	CSWlibgthread2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibintl8
RUNTIME_DEP_PKGS	+=	CSWlibpisock9
RUNTIME_DEP_PKGS	+=	CSWpango

CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--with-pilot-prefix=$(prefix)
CONFIGURE_ARGS	+=	--with-libintl-prefix=$(prefix)
CONFIGURE_ARGS	+=	--with-libiconv-prefix=$(prefix)

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

CHECKPKG_OVERRIDES_CSWjpilot += file-with-bad-content|/usr/share|root/opt/csw/bin/jpilot
CHECKPKG_OVERRIDES_CSWjpilot += file-with-bad-content|/usr/share|root/opt/csw/bin/jpilot-sync
CHECKPKG_OVERRIDES_CSWjpilot += file-with-bad-content|/usr/share|root/opt/csw/bin/jpilot-merge
CHECKPKG_OVERRIDES_CSWjpilot += file-with-bad-content|/usr/share|root/opt/csw/bin/jpilot-dump
CHECKPKG_OVERRIDES_CSWjpilot += file-with-bad-content|/usr/share|root/opt/csw/share/doc/jpilot/INSTALL
CHECKPKG_OVERRIDES_CSWjpilot += file-with-bad-content|/usr/local|root/opt/csw/share/doc/jpilot/README
CHECKPKG_OVERRIDES_CSWjpilot += file-with-bad-content|/usr/local|root/opt/csw/share/doc/jpilot/manual/plugin.html
CHECKPKG_OVERRIDES_CSWjpilot += file-with-bad-content|/usr/local|root/opt/csw/share/doc/jpilot/manual/manual.html

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

post-install-modulated:
	mv $(DESTDIR)/$(sharedstatedir)/$(NAME)/MañanaDB.pdb $(DESTDIR)/$(sharedstatedir)/$(NAME)/MananaDB.pdb
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)

# Local Variables:
# coding: latin-1
# End:
