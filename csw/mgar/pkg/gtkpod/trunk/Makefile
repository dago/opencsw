NAME = gtkpod
VERSION = 0.99.14
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = gtk2 application for Apple iPods
define BLURB
  gtkpod is a platform independent Graphical User
  Interface for Apple's iPod using GTK2.  It supports
  the first to fifth Generation including the iPod
  mini, iPod Photo, iPod Shuffle, iPod nano, and iPod
  Video.
endef

VENDOR_URL = http://www.gtkpod.org
SF_PROJ = gtkpod
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
#PATCHFILES  = file_convert.diff
PATCHFILES = configure.in.diff

RUNTIME_DEP_PKGS_CSWgtkpod += CSWcurlrt
RUNTIME_DEP_PKGS_CSWgtkpod += CSWfconfig
RUNTIME_DEP_PKGS_CSWgtkpod += CSWflac
RUNTIME_DEP_PKGS_CSWgtkpod += CSWftype2
RUNTIME_DEP_PKGS_CSWgtkpod += CSWgconf2
RUNTIME_DEP_PKGS_CSWgtkpod += CSWggettextrt
RUNTIME_DEP_PKGS_CSWgtkpod += CSWglib2
RUNTIME_DEP_PKGS_CSWgtkpod += CSWgnomevfs2
RUNTIME_DEP_PKGS_CSWgtkpod += CSWgtk2
RUNTIME_DEP_PKGS_CSWgtkpod += CSWlibatk
RUNTIME_DEP_PKGS_CSWgtkpod += CSWlibcairo
RUNTIME_DEP_PKGS_CSWgtkpod += CSWlibglade2
RUNTIME_DEP_PKGS_CSWgtkpod += CSWlibgpod
RUNTIME_DEP_PKGS_CSWgtkpod += CSWlibid3tag
RUNTIME_DEP_PKGS_CSWgtkpod += CSWlibxml2
RUNTIME_DEP_PKGS_CSWgtkpod += CSWpango
RUNTIME_DEP_PKGS_CSWgtkpod += CSWpython
RUNTIME_DEP_PKGS_CSWgtkpod += CSWvorbis

UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=67873
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)

#GARCOMPILER = GNU

#libgpod uses a non-standard include path
#EXTRA_INC=$(DESTDIR)/opt/csw/include/gpod-1.0

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib
EXTRA_LDFLAGS = -lm

CONFIGURE_SCRIPTS = $(WORKSRC)/autogen.sh $(WORKSRC)/configure

CONFIGURE_ARGS = $(DIRPATHS)

MSGFMT= /opt/csw/bin/gmsgfmt
MSGMERGE= /opt/csw/bin/gmsgmerge
XGETTEXT = /opt/csw/bin/gxgettext
GETTEXT = /opt/csw/bin/ggettext
export MSGMERGE
export MSGFMT
export XGETTEXT
export GETTEXT

include gar/category.mk
