GARNAME = libgsasl
GARVERSION = 0.2.29
CATEGORIES = lib

DESCRIPTION = GNU SASL Library
define BLURB
  GNU SASL is an implementation of the Simple Authentication and
  Security Layer framework and a few common SASL mechanisms.
  SASL is used by network servers (e.g., IMAP, SMTP) to request
  authentication from clients, and in clients to authenticate against servers.
endef

MASTER_SITES = ftp://alpha.gnu.org/pub/gnu/gsasl/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibgsasl)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PREREQUISITE_PKGS = CSWkrb5libdev
REQUIRED_PKGS = CSWggettext CSWiconv CSWkrb5lib CSWlibidn CSWlibntlm

CONFIGURE_ARGS = $(DIRPATHS)

# Test has compile errors
TEST_TARGET =
#TEST_TARGET = check

include gar/category.mk

