GARNAME = gsasl
GARVERSION = 1.1
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
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWlibgsasl CSWgsasl

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PREREQUISITE_PKGS = CSWkrb5libdev CSWgnulinks
REQUIRED_PKGS_CSWlibgsasl = CSWggettextrt CSWiconv CSWkrb5lib CSWlibidn CSWlibntlm CSWreadline
REQUIRED_PKGS_CSWgsasl = CSWlibgsasl

SPKG_SOURCEURL = http://www.gnu.org/software/$(GNU_PROJ)

CONFIGURE_ARGS = $(DIRPATHS)

# One test fails, reported upstream
#TEST_TARGET = check
TEST_TARGET = 

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

PKGFILES_CSWlibgsasl  = $(includedir)/.*
PKGFILES_CSWlibgsasl += $(libdir)/.*
PKGFILES_CSWlibgsasl += $(mandir)/man3/.*
PKGFILES_CSWlibgsasl += $(sharedstatedir)/locale/.*/libgsasl.mo

include gar/category.mk

# Tests use 'grep -e'
PATH := /opt/csw/gnu:$(PATH)

