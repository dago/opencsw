NAME = libsexy
VERSION = 0.1.11
CATEGORIES = lib

DESCRIPTION = Sexy URLs
define BLURB
  libsexy is a collection of GTK+ widgets that extend the functionality of
  such standard widgets as GtkEntry and GtkLabel by subclassing them and
  working around the limitations of the widgets.
endef

MASTER_SITES = http://releases.chipx86.com/libsexy/libsexy/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibsexy CSWlibsexydevel

CATALOGNAME_CSWlibsexy      = libsexy
CATALOGNAME_CSWlibsexydevel = libsexy_devel

SPKG_DESC_CSWlibsexy      = $(DESCRIPTION)
SPKG_DESC_CSWlibsexydevel = Development files for libsexy

BUILD_DEP_PKGS = CSWglib2devel CSWgtk2devel

RUNTIME_DEP_PKGS_CSWlibsexy = CSWfconfig CSWftype2 CSWggettextrt CSWglib2 CSWgtk2 CSWlibatk CSWlibcairo CSWlibxml2 CSWpango
RUNTIME_DEP_PKGS_CSWlibsexydevel = CSWlibsexy

VENDOR_URL = http://www.chipx86.com/blog/tag/libsexy/

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)

PKGFILES_CSWlibsexydevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWlibsexydevel += $(sharedstatedir)/gtk-doc/.*

CHECKPKG_OVERRIDES_CSWlibsexydevel += surplus-dependency|CSWlibsexy

include gar/category.mk
