NAME    = pidgin-sipe
VERSION = 1.15.1
GARTYPE = v2

DESCRIPTION = The SIPE Project - A third-party Pidgin plugin for Microsoft LCS/OCS
define BLURB
  The SIPE Project - A third-party Pidgin plugin for Microsoft LCS/OCS
endef

GARCOMPILER = GNU

SF_PROJECT = sipe
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.bz2

PACKAGES                   = CSWpidgin-sipe
CATALOGNAME_CSWpidgin-sipe = pidgin_sipe
SPKG_DESC_CSWpidgin-sipe   = A third-party Pidgin plugin for Microsoft LCS/OCS

# For msgfmt, msgmerge, xgettext and gettext to be used from GNU
CONFIGURE_ENV_PATH = $(prefix)/gnu:$(PATH)

CONFIGURE_ARGS = $(DIRPATHS)

RUNTIME_DEP_PKGS_CSWpidgin-sipe += CSWpidgin
RUNTIME_DEP_PKGS_CSWpidgin-sipe += CSWlibsmime3
RUNTIME_DEP_PKGS_CSWpidgin-sipe += CSWlibintl8
RUNTIME_DEP_PKGS_CSWpidgin-sipe += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWpidgin-sipe += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWpidgin-sipe += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWpidgin-sipe += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWpidgin-sipe += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpidgin-sipe += CSWlibnss3
RUNTIME_DEP_PKGS_CSWpidgin-sipe += CSWlibnspr4

CHECKPKG_OVERRIDES_CSWpidgin-sipe += surplus-dependency|CSWpidgin

BUILD_DEP_PKGS += CSWintltool
BUILD_DEP_PKGS += CSWpkgconfig
BUILD_DEP_PKGS += CSWlibgtk2-dev
BUILD_DEP_PKGS += CSWlibpcre-dev
BUILD_DEP_PKGS += CSWfontconfig-dev
BUILD_DEP_PKGS += CSWlibfreetype-dev
BUILD_DEP_PKGS += CSWlibpng-dev
BUILD_DEP_PKGS += CSWsunx11devel
BUILD_DEP_PKGS += CSWlibid3-dev
BUILD_DEP_PKGS += CSWlibiconv-dev
BUILD_DEP_PKGS += CSWggettext-dev
BUILD_DEP_PKGS += CSWpidgin

include gar/category.mk
