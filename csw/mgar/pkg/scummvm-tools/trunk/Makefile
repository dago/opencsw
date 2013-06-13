# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME    = scummvm-tools
VERSION = 1.6.0
GARTYPE = v2

DESCRIPTION = ScummVM tools -- unsupported tools for ScummVM
define BLURB
  ScummVM tools are additional programs to manipulate game files, extract da
ta, recompress audio.
endef

MASTER_SITES = $(SF_MIRRORS)
SF_PROJECT   = scummvm
DISTFILES    = $(DISTNAME).zip

GARCOMPILER = SOS12U3

RUNTIME_DEP_PKGS_CSWscummvm-tools += CSWwxwidgets
RUNTIME_DEP_PKGS_CSWscummvm-tools += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWscummvm-tools += CSWlibpng15-15
RUNTIME_DEP_PKGS_CSWscummvm-tools += CSWlibz1
RUNTIME_DEP_PKGS_CSWscummvm-tools += CSWlibogg0
RUNTIME_DEP_PKGS_CSWscummvm-tools += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWscummvm-tools += CSWlibvorbis0
RUNTIME_DEP_PKGS_CSWscummvm-tools += CSWlibvorbisenc2
RUNTIME_DEP_PKGS_CSWscummvm-tools += CSWlibflac8
RUNTIME_DEP_PKGS_CSWscummvm-tools += CSWwxwidgetsgtk2

TEST_SCRIPTS =

PATCHFILES += 0001-teach-configure-about-studio.patch
PATCHFILES += 0002-avoid-deque-constructor-for-studio.patch
PATCHFILES += 0003-fix-wxT-macro-on-split-lines.patch
PATCHFILES += 0004-install-should-create-path.patch

CONFIGURE_ARGS = --prefix=$(prefix)
CONFIGURE_ARGS += --bindir=$(bindir)
CONFIGURE_ARGS += --mandir=$(mandir)
CONFIGURE_ARGS += --datadir=$(datadir)
CONFIGURE_ARGS += --libdir=$(libdir)

EXTRA_CXXFLAGS   += -norunpath
EXTRA_LDFLAGS    += -norunpath
EXTRA_LD_OPTIONS += -z nolazyload -B direct

# To make sure make install does not try to use Solaris' install
EXTRA_INSTALL_EXPORTS = INSTALL 
INSTALL = ginstall

include gar/category.mk

