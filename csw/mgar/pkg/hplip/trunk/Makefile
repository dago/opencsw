NAME = hplip
VERSION = 3.12.2
GARTYPE = v2
CATEGORIES = utils

MASTER_SITES = http://prdownloads.sourceforge.net/hplip
DISTFILES = $(NAME)-$(VERSION).tar.gz


DESCRIPTION = HP Cups Printing and Imaging
define BLURB
	Cups printer drivers for HP non postsript printers
endef

# GARCOMPILER = GNU
GARCOMPILER = SOS12U3

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

PACKAGES = CSWhplip
OBSOLETED_BY_CSWhplip = CSWhpijs
SPKG_DESC_CSWhplip = $(DESCRIPTION) foomatic
RUNTIME_DEP_PKGS_CSWhplip += CSWlibjpeg7

PATCHFILES += 0001-add-strnlen.patch
PATCHFILES += 0002-set-csw-path-hpijs.cpp.patch
PATCHFILES += 0004-set-csw-path-foomatic-rip-hplip.patch

EXTRA_LINKER_FLAGS += -norunpath -xnorunpath

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-hpijs-only-build
CONFIGURE_ARGS += --enable-hpijs-install
# CONFIGURE_ARGS += --enable-hpcups-only-build

CHECKPKG_OVERRIDES_CSWhplip += file-with-bad-content|/usr/share|root/opt/csw/share/doc/hplip-3.12.2/upgrading.html
CHECKPKG_OVERRIDES_CSWhplip += file-with-bad-content|/usr/share|root/opt/csw/share/doc/hplip-3.12.2/uninstalling.html

include gar/category.mk

