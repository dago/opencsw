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

MASTER_SITES = http://jpilot.org/
DISTFILES  = $(DISTNAME).tar.gz

GARCOMPILER			=	GNU

BUILD_DEP_PKGS		+=	CSWpmxmlparser
BUILD_DEP_PKGS		+=	CSWpilotlink

CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--with-pilot-prefix=$(prefix)
CONFIGURE_ARGS	+=	--with-libintl-prefix=$(prefix)
CONFIGURE_ARGS	+=	--with-libiconv-prefix=$(prefix)

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)
