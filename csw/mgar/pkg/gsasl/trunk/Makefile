NAME = gsasl
VERSION = 1.6.2
CATEGORIES = apps

DESCRIPTION = GNU SASL binary
define BLURB
  GNU SASL is an implementation of the Simple Authentication and
  Security Layer framework and a few common SASL mechanisms.
  SASL is used by network servers (e.g., IMAP, SMTP) to request
  authentication from clients, and in clients to authenticate against servers.
endef

GNU_PROJ = gsasl
MASTER_SITES = $(GNU_MIRROR)
MASTER_SITES += http://daily.josefsson.org/gsasl/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

VENDOR_URL = http://www.gnu.org/software/$(GNU_PROJ)

BUILD_DEP_PKGS += CSWgnulinks
BUILD_DEP_PKGS += CSWlibkrb5-dev

PACKAGES += CSWlibgsasl7
SPKG_DESC_CSWlibgsasl7 = GNU SASL library, libgsasl.so.7
PKGFILES_CSWlibgsasl7 += $(call pkgfiles_lib,libgsasl.so.7)
PKGFILES_CSWlibgsasl7 += .*/libgsasl\.mo
RUNTIME_DEP_PKGS_CSWlibgsasl7 += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWlibgsasl7 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgsasl7 += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWlibgsasl7 += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWlibgsasl7 += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWlibgsasl7 += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWlibgsasl7 += CSWlibntlm0
RUNTIME_DEP_PKGS_CSWlibgsasl7 += CSWlibidn11
RUNTIME_DEP_PKGS_CSWlibgsasl7 += CSWlibk5crypto3
OBSOLETED_BY_CSWlibgsasl7 += CSWlibgsasl

PACKAGES += CSWlibgsasl-dev
SPKG_DESC_CSWlibgsasl-dev = Development files for GNU SASL library libgsasl.so.7
PKGFILES_CSWlibgsasl-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibgsasl-dev += CSWlibgsasl7
RUNTIME_DEP_PKGS_CSWlibgsasl-dev += CSWlibkrb5-dev
OBSOLETED_BY_CSWlibgsasl-dev += CSWlibgsasldevel
CATALOGNAME_CSWlibgsasldevel = libgsasl_devel_stub

PACKAGES += CSWgsasl
SPKG_DESC_CSWgsasl = GNU SASL
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWgsasl += CSWlibgsasl7
RUNTIME_DEP_PKGS_CSWgsasl += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgsasl += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWgsasl += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgsasl += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWgsasl += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWgsasl += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWgsasl += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWgsasl += CSWlibntlm0
RUNTIME_DEP_PKGS_CSWgsasl += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWgsasl += CSWlibidn11
RUNTIME_DEP_PKGS_CSWgsasl += CSWlibk5crypto3
RUNTIME_DEP_PKGS_CSWgsasl += CSWlibgnutls26

# We don't need it and if defined the test breaks
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

# Disable 64 bit until krb5 is available in 64 bit
BUILD64 = 1

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

include gar/category.mk

# Tests use 'grep -e'
PATH := /opt/csw/gnu:$(PATH)
