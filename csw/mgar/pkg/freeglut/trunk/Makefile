GARNAME = freeglut
GARVERSION = 2.6.0
CATEGORIES = lib

DESCRIPTION = OpenSourced alternative to the OpenGL Utility Toolkit
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PATCHFILES  = 0001-Add-support-for-Sun.patch
PATCHFILES += 0002-Fix-windows-line-ending-and-wrong-endif.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://freeglut.sourceforge.net/

DEP_PKGS = CSWmesa

# If we put the include into CPPFLAGS it is too early in the commandline
# and the installed headers take precedence over the newly built.
CPPFLAGS =
EXTRA_CFLAGS = -I/opt/csw/include -DSUN_OGL_NO_VERTEX_MACROS

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
