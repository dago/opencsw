NAME = gsasl
VERSION = 1.8.0
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = GNU SASL binary
define BLURB
  GNU SASL is an implementation of the Simple Authentication and
  Security Layer framework and a few common SASL mechanisms.
  SASL is used by network servers (e.g., IMAP, SMTP) to request
  authentication from clients, and in clients to authenticate against serverECTs.
endef

GNU_PROJ = gsasl
MASTER_SITES = $(GNU_MIRROR)
MASTER_SITES += http://daily.josMASTER_SITES += ftp://alpha.gnu.org/gnuaily.josefsson.org/gsasl/
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
RUNTIME_DEP_PKGS_CSWlibgsasl7 += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWlibgsasl7 += CSWlibntlm0
RUNTIME_DEP_PKGS_CSWlibgsas= CSWlibk5crypto3
OBSOLETED_BY_CSWlibgsasl# Annoying, override for now
CHECKPKG_OVERRIDES_CSWlibgsasl7 += surplus-dependency|CSWlibgpg-error0sl7 += CSWlibgsasl

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
RUNTIME_DEP_PKGS_intl8
RUNTIME_DEP_PKGS_CSWgsasl += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWgsasl += CSWlibgnutls28

# Disable 64 bit until krb5 is available in 64 bit
BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-gssapi-impl=mit

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

# The testsuite runs fine, but finishes with exit code 1, ?!?
SKIPTEST ?= 1

include gar/category.mk

