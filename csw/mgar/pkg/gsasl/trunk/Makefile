NAME = gsasl
VERSION = 1.6.0
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
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWlibgsasl CSWlibgsasl7 CSWlibgsasldevel CSWgsasl

CATALOGNAME_CSWlibgsasl = libgsasl
CATALOGNAME_CSWlibgsasl7 = libgsasl7
CATALOGNAME_CSWlibgsasldevel = libgsasl_devel
CATALOGNAME_CSWgsasl = gsasl

BUILD_DEP_PKGS = CSWkrb5libdev CSWgnulinks
RUNTIME_DEP_PKGS_CSWlibgsasl7 = CSWggettextrt CSWkrb5lib CSWlibidn CSWlibntlm
RUNTIME_DEP_PKGS_CSWlibgsasl7 += CSWgcrypt CSWgpgerr
RUNTIME_DEP_PKGS_CSWlibgsasl = CSWlibgsasl7
RUNTIME_DEP_PKGS_CSWgsasl = CSWlibgsasl7 CSWgnutls CSWggettextrt CSWiconv CSWkrb5lib CSWlibidn CSWlibntlm CSWreadline
RUNTIME_DEP_PKGS_CSWgsasl += CSWgcrypt CSWgpgerr
RUNTIME_DEP_PKGS_CSWlibgsasldevel = CSWlibgsasl7 CSWkrb5libdev

SPKG_DESC_CSWlibgsasl = Stub for legacy dependencies to CSWlibgsasl7
SPKG_DESC_CSWlibgsasl7 = GNU SASL Library providing libgsasl.so.7
SPKG_DESC_CSWlibgsasldevel = GNU SASL Development Files
SPKG_DESC_CSWgsasl = GNU SASL

SPKG_SOURCEURL = http://www.gnu.org/software/$(GNU_PROJ)

# We don't need it and if defined the test breaks
LD_OPTIONS =
EXTRA_LINKER_FLAGS = $(RUNPATH_LINKER_FLAGS)

# Disable 64 bit until krb5 is available in 64 bit
# BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

# One test inside GNULib fails, reported upstream. This is most
# probably harmless.
SKIPTEST ?= 1

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

ARCHALL_CSWlibgsasl = 1

# Make sure we do NOT add here /opt/csw/include/gsasl.h
PKGFILES_CSWgsasl = $(bindir)/.*
PKGFILES_CSWgsasl += $(infodir)/gsasl\..*
PKGFILES_CSWgsasl += $(sharedstatedir)/.*/gsasl\..*
PKGFILES_CSWgsasl += $(mandir)/.*/gsasl\..*

PKGFILES_CSWlibgsasl = NOFILES

PKGFILES_CSWlibgsasldevel = $(PKGFILES_DEVEL)

CHECKPKG_OVERRIDES_CSWlibgsasl += surplus-dependency|CSWlibgsasl7

include gar/category.mk

# Tests use 'grep -e'
PATH := /opt/csw/gnu:$(PATH)
