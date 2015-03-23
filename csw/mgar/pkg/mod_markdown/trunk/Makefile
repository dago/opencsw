NAME = apache-mod-markdown
VERSION = 1.0.2
GARTYPE = v2

DESCRIPTION = Apache markdown rendering module

MASTER_SITES = https://github.com/hamano/apache-mod-markdown/releases/download/$(VERSION)/
DISTFILES += $(DISTNAME).tar.bz2
DISTFILES += CSWap2-mod-markdown.postinstall CSWap2-mod-markdown.preremove

# Use patch until this is fixed:
#   https://github.com/hamano/apache-mod-markdown/pull/6
PATCHFILES += 0001-Do-not-unconditionally-use-Wall.patch

# Use patch until this is fixed:
#   https://github.com/hamano/apache-mod-markdown/pull/7
PATCHFILES += 0002-Honour-DESTDIR.patch

VENDOR_URL = https://github.com/hamano/apache-mod-markdown

BUILD_DEP_PKGS += CSWlibmarkdown-dev

PACKAGES = CSWap2-mod-markdown
SPKG_DESC_CSWap2-mod-markdown = Apache markdown rendering module
RUNTIME_DEP_PKGS_CSWap2-mod-markdown += CSWapache2
RUNTIME_DEP_PKGS_CSWap2-mod-markdown += CSWlibmarkdown2
CHECKPKG_OVERRIDES_CSWap2-mod-markdown += soname-not-part-of-filename|soname=libmodmarkdown.so.0|filename=mod_markdown.so

# Apache paths
AP2_ROOT      = $(prefix)/apache2
AP2_LIBEXEC   = $(DESTDIR)$(AP2_ROOT)/libexec
AP2_EXTRACONF = $(DESTDIR)$(AP2_ROOT)/etc/extra
AP2_SBIN      = $(AP2_ROOT)/sbin
APXS          = $(AP2_SBIN)/apxs

# Unconditional use of -Wall
# GARCOMPILER = GNU

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-apxs=$(APXS)
CONFIGURE_ARGS += --with-discount=$(prefix)

# We need ginstall as install
INSTALL_ENV_PATH = /opt/csw/gnu:$(PATH)

include gar/category.mk
