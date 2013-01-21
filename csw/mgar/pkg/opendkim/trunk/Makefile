NAME = opendkim
VERSION = 2.7.4

DESCRIPTION = DKIM library and milter

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz

PACKAGES += CSWopendkim
SPKG_DESC_CSWopendkim = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWopendkim += CSWlibopendkim8
RUNTIME_DEP_PKGS_CSWopendkim += CSWlibssl1-0-0

PACKAGES += CSWlibopendkim8
PKGFILES_CSWlibopendkim8 += $(call baseisadirs,$(libdir),libopendkim\.so\.8\.0\.2)
PKGFILES_CSWlibopendkim8 += $(call baseisadirs,$(libdir),libopendkim\.so\.8(\.\d+)*)
SPKG_DESC_CSWlibopendkim8 += $(DESCRIPTION), libopendkim.so.8
RUNTIME_DEP_PKGS_CSWlibopendkim8 += CSWlibssl1-0-0

PACKAGES += CSWopendkim-dev
SPKG_DESC_CSWopendkim-dev += $(DESCRIPTION), development files
PKGFILES_CSWopendkim-dev += /opt/csw/lib/libopendkim.so
PKGFILES_CSWopendkim-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWopendkim-dev += CSWlibopendkim8

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-milter=/opt/csw

# Only in docs
CHECKPKG_OVERRIDES_CSWopendkim += file-with-bad-content
# Don't want to pull in Perl just because a script in docs uses it
CHECKPKG_OVERRIDES_CSWopendkim += missing-dependency|CSWperl

include gar/category.mk
