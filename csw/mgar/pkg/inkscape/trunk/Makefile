# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = inkscape
VERSION = 0.48.4
GARTYPE = v2

DESCRIPTION = Open source scalable vector graphics editor

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.bz2

GARCOMPILER = GNU

PATCHFILES += 0000-color-profile.cpp-Add-required-headers.patch
PATCHFILES += 0000-desktop-widget.h-Remove-stray-comma.patch
PATCHFILES += 0000-sp-ellipse.cpp-resolve-overload-ambiguity.patch
PATCHFILES += 0000-fixed_point.h-Resolved-ambiguity.patch
PATCHFILES += 0000-lpe-lattice.cpp-resolve-overload-ambiguity.patch
PATCHFILES += 0000-round.cpp-resolve-overload-ambiguity.patch
PATCHFILES += 0000-svg-length.cpp-resolve-overload-ambiguity.patch
PATCHFILES += 0000-desktop-widget.cpp-resolve-overload-ambiguity.patch
PATCHFILES += 0000-ruler.cpp-resolved-overload-ambiguity.patch
PATCHFILES += 0000-tile.cpp-resolved-overload-ambiguity.patch

# I want pango-querymodules be called
RUNTIME_DEP_PKGS_CSWinkscape += CSWpango
CHECKPKG_OVERRIDES_CSWinkscape += surplus-dependency|CSWpango
# I want gdk-pixbuf-query-loaders be called
RUNTIME_DEP_PKGS_CSWinkscape += CSWgdkpixbuf
CHECKPKG_OVERRIDES_CSWinkscape += surplus-dependency|CSWgdkpixbuf
# I want gtk-query-immodules-2.0 to be called
RUNTIME_DEP_PKGS_CSWinkscape += CSWgtk2
CHECKPKG_OVERRIDES_CSWinkscape += surplus-dependency|CSWgtk2
 
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibpango1-0-0
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibwpg0-2-2
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibruby1-9-1-1
RUNTIME_DEP_PKGS_CSWinkscape += CSWruby191
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibgsl0
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibgdkmm2-4-1
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibgomp1
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibatkmm1-6-1
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibintl8
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibz1
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibwpd0-9-9
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibgtkspell0
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibpangoft2-1-0-0
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibmagick++6q16hdri3
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibgc1
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibglibmm2-4-1
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibcairomm1-0-1
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibsigc2-0-0
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibaspell15
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibpoppler43
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibwpd-stream0-9-9
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibgtkmm2-4-1
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibpangomm1-4-1
RUNTIME_DEP_PKGS_CSWinkscape += CSWperl
RUNTIME_DEP_PKGS_CSWinkscape += CSWgnomevfs2
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibpoppler-glib8
RUNTIME_DEP_PKGS_CSWinkscape += CSWliblcms2-2
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibpangocairo1-0-0

# They stem from src/bind/javabind.cpp. It's a list of paths to search for javavm. Nothing to worry.
CHECKPKG_OVERRIDES_CSWinkscape += file-with-bad-content|/usr/local|root/opt/csw/bin/inkview
CHECKPKG_OVERRIDES_CSWinkscape += file-with-bad-content|/usr/local|root/opt/csw/bin/inkscape

# This is due to `ld -z ignore' issue on sparc. Remove once resolved.
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibgslcblas0
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWinkscape += CSWlibgio2-0-0
CHECKPKG_OVERRIDES_CSWinkscape += surplus-dependency|CSWlibgthread2-0-0
CHECKPKG_OVERRIDES_CSWinkscape += surplus-dependency|CSWlibgslcblas0
CHECKPKG_OVERRIDES_CSWinkscape += surplus-dependency|CSWlibgmodule2-0-0
CHECKPKG_OVERRIDES_CSWinkscape += surplus-dependency|CSWlibgio2-0-0


BUILD_DEP_PKGS += CSWlibwpg-dev
BUILD_DEP_PKGS += CSWpm-xml-parser
BUILD_DEP_PKGS += CSWlibgc-dev
BUILD_DEP_PKGS += CSWlibgtkmm-dev
BUILD_DEP_PKGS += CSWliblcms2-dev
BUILD_DEP_PKGS += CSWlibpangomm-dev
BUILD_DEP_PKGS += CSWlibcairomm-dev
BUILD_DEP_PKGS += CSWlibgtk2-dev
BUILD_DEP_PKGS += CSWlibatk-dev
BUILD_DEP_PKGS += CSWlibatkmm-dev
BUILD_DEP_PKGS += CSWgsl-dev
BUILD_DEP_PKGS += CSWimagemagick-dev
BUILD_DEP_PKGS += CSWlibiconv-dev


CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-silent-rules

EXTRA_CONFIGURE_EXPORTS += XGETTEXT MSGMERGE MSGFMT
CONFIGURE_ENV_XGETTEXT = $(bindir)/gxgettext
CONFIGURE_ENV_MSGMERGE = $(bindir)/gmsgmerge
CONFIGURE_ENV_MSGFMT = $(bindir)/gmsgfmt

#EXTRA_CONFIGURE_EXPORTS += PROTOC
#CONFIGURE_ENV_PROTOC = $(prefix)/gxx/bin/protoc

REINPLACE_MATCH = -Wl,--export-dynamic
REINPLACE_WITH = 
REINPLACE_FILES = src/Makefile.in

# Use this until GCC boost is moved to /opt/csw
EXTRA_INC += $(prefix)/gxx/include
EXTRA_LIB += $(prefix)/gxx/lib

include gar/category.mk

