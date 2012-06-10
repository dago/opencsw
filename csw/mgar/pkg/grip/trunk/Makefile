# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = grip
VERSION = 3.3.1
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = CD-player and CD-ripper for the Gnome desktop
define BLURB
  Grip is a GTK-based CD-player and CD-ripper / MP3 encoder.
  It has the ripping capabilities of cdparanoia built in, but can also use
  external rippers (such as cdda2wav).
  Encoder presets are provided for lame, bladeenc, l3enc, xingmp3enc,
   mp3encode, gogo)
endef

MASTER_SITES	=	$(SF_MIRRORS)
DISTFILES		=	$(DISTNAME).tar.gz
DISTFILES		+=	README.CSW

PACKAGING_PLATFORMS	=	solaris10-sparc
PACKAGING_PLATFORMS	+=	solaris10-i386

BUILD_DEP_PKGS		+=	CSWfconfig-dev
BUILD_DEP_PKGS		+=	CSWggettext-dev
BUILD_DEP_PKGS		+=	CSWgnomekeyring-dev
BUILD_DEP_PKGS		+=	CSWgnomevfs2-dev
BUILD_DEP_PKGS		+=	CSWlibart
BUILD_DEP_PKGS		+=	CSWlibatk-dev
BUILD_DEP_PKGS		+=	CSWlibaudiofile-dev
BUILD_DEP_PKGS		+=	CSWlibbonobo2
BUILD_DEP_PKGS		+=	CSWlibbonoboui
BUILD_DEP_PKGS		+=	CSWlibcairo-dev
BUILD_DEP_PKGS		+=	CSWlibcurl-dev
BUILD_DEP_PKGS		+=	CSWlibdbus-glib-dev
BUILD_DEP_PKGS		+=	CSWlibesd-dev
BUILD_DEP_PKGS		+=	CSWlibexpat-dev
BUILD_DEP_PKGS		+=	CSWlibfreetype-dev
BUILD_DEP_PKGS		+=	CSWlibgconf-dev
BUILD_DEP_PKGS		+=	CSWlibgdk-pixbuf-dev
BUILD_DEP_PKGS		+=	CSWlibglib2-dev
BUILD_DEP_PKGS		+=	CSWlibgnomeui-devel
BUILD_DEP_PKGS		+=	CSWlibgtk2-dev
BUILD_DEP_PKGS		+=	CSWlibiconv-dev
BUILD_DEP_PKGS		+=	CSWlibid3-dev
BUILD_DEP_PKGS		+=	CSWlibidn-dev
BUILD_DEP_PKGS		+=	CSWlibpixman-dev
BUILD_DEP_PKGS		+=	CSWlibpng-dev
BUILD_DEP_PKGS		+=	CSWlibssl-dev
BUILD_DEP_PKGS		+=	CSWlibxft2devel
BUILD_DEP_PKGS		+=	CSWlibxml2-dev
BUILD_DEP_PKGS		+=	CSWlibz-dev
BUILD_DEP_PKGS		+=	CSWorbit2
BUILD_DEP_PKGS		+=	CSWpangodevel
BUILD_DEP_PKGS		+=	CSWvte

RUNTIME_DEP_PKGS	+=	CSWgnomevfs2
RUNTIME_DEP_PKGS	+=	CSWlibart
RUNTIME_DEP_PKGS	+=	CSWlibatk1-0-0
RUNTIME_DEP_PKGS	+=	CSWlibaudiofile0
RUNTIME_DEP_PKGS	+=	CSWlibbonobo2
RUNTIME_DEP_PKGS	+=	CSWlibbonoboui
RUNTIME_DEP_PKGS	+=	CSWlibbz2-1-0
RUNTIME_DEP_PKGS	+=	CSWlibcairo2
RUNTIME_DEP_PKGS	+=	CSWlibcurl4
RUNTIME_DEP_PKGS	+=	CSWlibdbus-glib1-2
RUNTIME_DEP_PKGS	+=	CSWlibdbus1-3
RUNTIME_DEP_PKGS	+=	CSWlibesd0
RUNTIME_DEP_PKGS	+=	CSWlibexpat1
RUNTIME_DEP_PKGS	+=	CSWlibfontconfig1
RUNTIME_DEP_PKGS	+=	CSWlibfreetype6
RUNTIME_DEP_PKGS	+=	CSWlibgailutil18
RUNTIME_DEP_PKGS	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS	+=	CSWlibgconf2-4
RUNTIME_DEP_PKGS	+=	CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibgio2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibglib2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibgnome
RUNTIME_DEP_PKGS	+=	CSWlibgnome-keyring0
RUNTIME_DEP_PKGS	+=	CSWlibgnomecanvas
RUNTIME_DEP_PKGS	+=	CSWlibgnomeui2-0
RUNTIME_DEP_PKGS	+=	CSWlibgobject2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibgthread2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS	+=	CSWlibiconv2
RUNTIME_DEP_PKGS	+=	CSWlibid3-3-8-3
RUNTIME_DEP_PKGS	+=	CSWlibidn11
RUNTIME_DEP_PKGS	+=	CSWlibintl3
RUNTIME_DEP_PKGS	+=	CSWlibintl8
RUNTIME_DEP_PKGS	+=	CSWlibpixman1-0
RUNTIME_DEP_PKGS	+=	CSWlibpng12-0
RUNTIME_DEP_PKGS	+=	CSWlibpopt0
RUNTIME_DEP_PKGS	+=	CSWlibssl0-9-8
RUNTIME_DEP_PKGS	+=	CSWlibssl1-0-0
RUNTIME_DEP_PKGS	+=	CSWlibstdc++6
RUNTIME_DEP_PKGS	+=	CSWlibxft2
RUNTIME_DEP_PKGS	+=	CSWlibxml2-2
RUNTIME_DEP_PKGS	+=	CSWlibxrender
RUNTIME_DEP_PKGS	+=	CSWlibz1
RUNTIME_DEP_PKGS	+=	CSWorbit2
RUNTIME_DEP_PKGS	+=	CSWpango
RUNTIME_DEP_PKGS	+=	CSWsunmath
RUNTIME_DEP_PKGS	+=	CSWvte

PATCHFILES			+=	0001-Fix-sendmail-path.patch
PATCHFILES			+=	0002-Fix-auto-tools-suggested-by-libtoolize.patch

CONFIGURE_ARGS = $(DIRPATHS)
GARCOMPILER			=	GNU
#GCC4_VERSION		=	4.7

STRIP_LIBTOOL		=	1

include gar/category.mk

pre-configure-modulated:
	@echo "executing $@"
	cd $(WORKSRC) && libtoolize
	cd $(WORKSRC) && aclocal
	cd $(WORKSRC) && automake -a
	cd $(WORKSRC) && autoconf
	$(MAKECOOKIE)

# this is private and not available publicly
mydependencies:
	$(HOME)/bin/ocswdeplist --package $(NAME)
