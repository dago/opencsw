NAME = gettext
VERSION = 1.05
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = PVANDRY

DESCRIPTION = Multilanguage messages
define BLURB
endef

DISTFILES += COPYING

# Compatibility patches for Perl 5.10.1 from
#   https://rt.cpan.org/Public/Bug/Display.html?id=35680
PATCHFILES += compatibility-with-POSIX-module.diff
PATCHFILES += doc-update.diff

CATALOG_RELEASE = unstable

PACKAGES += CSWpm-locale-gettext
CATALOGNAME_CSWpm-locale-gettext = pm_locale_gettext
SPKG_DESC_CSWpm-locale-gettext = Multilanguage messages
RUNTIME_DEP_PKGS_CSWpm-locale-gettext += CSWlibintl8
OBSOLETED_BY_CSWpm-locale-gettext += CSWpmlocalegettext
CATALOGNAME_CSWpmlocalegettext = pm_localegettext_stub

BUILD_ARGS += OTHERLDFLAGS="-lintl -R$(libdir)"

include gar/category.mk
