NAME = gnome-desktop
VERSION = 2.28.2
CATEGORIES = gnome

DESCRIPTION = Evolution database backend server
define BLURB
	The data server, called "Evolution Data Server" is responsible for
	managing calendar and addressbook information.
endef

MASTER_SITES =  $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTNAME  = $(NAME)-$(VERSION)

PACKAGES = CSWgnomedesktop CSWgnomedesktop-devel CSWgnomedesktop-doc
CATALOGNAME_CSWgnomedesktop = gnomedesktop
CATALOGNAME_CSWgnomedesktop-devel = gnomedesktop_devel
CATALOGNAME_CSWgnomedesktop-doc = gnomedesktop_doc

SPKG_DESC_CSWgnomedesktop += Evolution database backend server
SPKG_DESC_CSWgnomedesktop-devel += Evolution database backend server - developer package
SPKG_DESC_CSWgnomedesktop-doc += Evolution database backend server - documentation

RUNTIME_DEP_PKGS_CSWgnomedesktop += 
RUNTIME_DEP_PKGS_CSWgnomedesktop += 
RUNTIME_DEP_PKGS_CSWgnomedesktop += 
RUNTIME_DEP_PKGS_CSWgnomedesktopdevel += CSWevolution
RUNTIME_DEP_PKGS_CSWgnomedesktopdoc += CSWevolution

BUILD_DEP_PKGS_CSWgnomedesktop += CSWlibxrandrdevel
BUILD_DEP_PKGS_CSWgnomedesktop += CSWx11randrproto

PKGFILES_CSWgnomedesktopdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWgnomedesktopdoc = $(sharedstatedir)/gtk-doc/.*

ARCHALL_CSWgnomedesktopdoc = 1

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://projects.gnome.org/evolution

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

# BUILD64_LIBS_ONLY = 1

STRIP_LIBTOOL = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

pre-build-modulated:
	gsed -i 's/^\(GNOME_DESKTOP_LIBS = .*\)$$/\1 -lm/' \
		$(WORKSRC)/libgnome-desktop/Makefile
	gsed -i 's,\tmsgfmt,\t$$(GMSGFMT),' \
		$(WORKSRC)/desktop-docs/fdl/Makefile
	gsed -i 's,\tmsgfmt,\t$$(GMSGFMT),' \
		$(WORKSRC)/desktop-docs/gpl/Makefile
	gsed -i 's,\tmsgfmt,\t$$(GMSGFMT),' \
		$(WORKSRC)/desktop-docs/lgpl/Makefile
