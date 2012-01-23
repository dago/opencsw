NAME = freeglut
VERSION = 2.6.0
CATEGORIES = lib

DESCRIPTION = OpenSourced alternative to the OpenGL Utility Toolkit
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# Use these patches until this is fixed:
#   http://sourceforge.net/tracker/index.php?func=detail&aid=3077828&group_id=1032&atid=101032
PATCHFILES  = 0001-Add-support-for-Sun.patch
PATCHFILES += 0002-Fix-windows-line-ending-and-wrong-endif.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://freeglut.sourceforge.net/

DEP_PKGS = CSWmesa

# If we put the include into CPPFLAGS it is too early in the commandline
# and the installed headers take precedence over the newly built.
CPPFLAGS =
EXTRA_CFLAGS = -I/opt/csw/include -DSUN_OGL_NO_VERTEX_MACROS

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)

# No 64 bit libs on Solaris 9 x86
CHECKPKG_OVERRIDES_CSWfreeglut += soname-not-found|libXxf86vm.so.1|is|needed|by|opt/csw/lib/amd64/libglut.so.3.9.0

include gar/category.mk
