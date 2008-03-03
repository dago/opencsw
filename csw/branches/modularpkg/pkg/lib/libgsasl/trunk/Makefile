GARNAME = libgsasl
GARVERSION = 0.2.24
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
DISTFILES += $(call admfiles,CSWlibgsasl,depend)

PREREQUISITE_PKGS = CSWkrb5libdev CSWlibntlm

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

