# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = fluxbox
VERSION = 1.3.5
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = Brief description
define BLURB
  Long description
endef

VENDOR_URL = http://fluxbox.org/
MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DEXTRA_CPPFLAGS = -features=extensions -D__FUNCTION__=__func__
EXTRA_LINKER_FLAGS = -norunpath

PATCHFILES += 0001-Solaris-userland-OpenCSW-bash.patch
PATCHFILES += 0002-Workaround-the-double-EXEEXT-substitution.patch
PATCHFILES += 0003-The-italian-NLS-part-is-broken.patch
PATCHFILES += 0004-Use-the-fluxbox-command-that-was-just-built.patch
PATCHFILES += 0006-fluxbox-generate_menu-Use-CSWbash.patch

CONFIGURE_ARGS = $(DIRPATHS)

RUNTIME_DEP_PKGS_CSWfluxbox += CSWbash
RUNTIME_DEP_PKGS_CSWfluxbox += CSWlibxpm4
RUNTIME_DEP_PKGS_CSWfluxbox += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWfluxbox += CSWlibxrender
RUNTIME_DEP_PKGS_CSWfluxbox += CSWlibimlib2-1
RUNTIME_DEP_PKGS_CSWfluxbox += CSWlibfribidi0
CHECKPKG_OVERRIDES_CSWfluxbox += file-with-bad-content

# checkpkg doesn't detect this dependency
CHECKPKG_OVERRIDES_CSWfluxbox += surplus-dependency|CSWbash

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
