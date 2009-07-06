GARNAME = pureftpd
GARVERSION = 1.0.22
CATEGORIES = net
SRCNAME = pure-ftpd

DESCRIPTION = A secure FTP daemon
define BLURB
  Pure-FTPd is a free (BSD), secure, production-quality and 
  standard-conformant FTP server. It doesn't provide useless bells and 
  whistles, but focuses on efficiency and ease of use. It provides simple 
  answers to common needs, plus unique useful features for personal users 
  as well as hosting providers.
endef

MASTER_SITES = http://download.pureftpd.org/pub/pure-ftpd/releases/
DISTFILES  = $(SRCNAME)-$(GARVERSION).tar.gz
WORKSRC = $(WORKDIR)/$(SRCNAME)-$(GARVERSION)

# we require openssl for tls
REQUIRED_PKGS = CSWosslrt

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# configure args
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-tls
CONFIGURE_ARGS += --with-pam
CONFIGURE_ARGS += --enable-largefile

# No test suite available
TEST_SCRIPTS =

include gar/category.mk

# strange archive...
post-build-modulated:
	@chmod 751 $(WORKSRC)/x
