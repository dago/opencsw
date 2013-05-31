NAME = groff
VERSION = 1.22.2

DESCRIPTION = Front end for the groff document formatting system(jg@axis.se).
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(VENDOR_URL = http://www.gnu.org/software/groff/groff.html

PACKAGES += CSWgroff
SPKG_DESC_CSWgroff = GNU roff/troff/nroff
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWgroff += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgroff += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWgroff += CSWperl

# I am not sure if we really need this
RUNTIME_DEP_PKGS_CSWgroff += CSWpsutils
CHECKPKG_OVERRIDES_CSWgroff += surplus-dependency|CSWpsutils

# Mostly harmless
CHECKPKG_OVERRIDES_CSWgroff += file-with-bad-content

EXTRA_MERGE_EXCLUDE_FILES += $(libdir)/charset\.alias

GARCOMPILER = GNU

BUILD64 = 1
ISAEXEC = 1

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-appresdir=$(libdir)/X11/app-defaults

include gar/category.mk
