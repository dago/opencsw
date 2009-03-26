GARNAME = libgsasl
GARVERSION = 1.1
CATEGORIES = lib

DESCRIPTION = GNU SASL Library
define BLURB
  GNU SASL is an implementation of the Simple Authentication and
  Security Layer framework and a few common SASL mechanisms.
  SASL is used by network servers (e.g., IMAP, SMTP) to request
  authentication from clients, and in clients to authenticate against servers.
endef

GNU_PROJ = gsasl
MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PREREQUISITE_PKGS = CSWkrb5libdev
REQUIRED_PKGS = CSWggettextrt CSWiconv CSWkrb5lib CSWlibidn CSWlibntlm

SPKG_SOURCEURL = http://www.gnu.org/software/$(GNU_PROJ)

# We have to wait with 64 bit until Kerberos is updated to 64 bit
#BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

