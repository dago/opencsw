NAME = libgpod
VERSION = 0.7.2
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = Interface to Apple iPods
define BLURB
  libgpod is a shared library to access the contents of
  an iPod.  This library is based on code used in the
  gtkpod project.  libgpod supports playlists, smart
  playlists, playcounts, ratings, podcasts and cover art.
endef

SF_PROJ = gtkpod
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

RUNTIME_DEP_PKGS_CSWlibgpod += CSWggettextrt
RUNTIME_DEP_PKGS_CSWlibgpod += CSWglib2
RUNTIME_DEP_PKGS_CSWlibgpod += CSWgtk2
RUNTIME_DEP_PKGS_CSWlibgpod += CSWlibxml2

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=67873
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(NAME).(\d+(?:\.\d+)*)

GARCOMPILER = SOS12
#GARCOMPILER = GNU
#GCC4 won't work. There are too many libtool deps using GCC3
#GNU_CC_HOME = /opt/csw/gcc3

CONFIGURE_ARGS = $(DIRPATHS) --includedir=/opt/csw/include

TEST_SCRIPTS =

STRIP_LIBTOOL=1

MSGFMT= /opt/csw/bin/gmsgfmt
MSGMERGE= /opt/csw/bin/gmsgmerge
XGETTEXT = /opt/csw/bin/gxgettext
GETTEXT = /opt/csw/bin/ggettext
export MSGMERGE
export MSGFMT
export XGETTEXT
export GETTEXT

include gar/category.mk
