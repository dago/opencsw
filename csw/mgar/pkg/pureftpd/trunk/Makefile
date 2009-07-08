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
CONFIGURE_ARGS += --with-everything
CONFIGURE_ARGS += --with-paranoidmsg
CONFIGURE_ARGS += --with-virtualchroot
CONFIGURE_ARGS += --with-tls
CONFIGURE_ARGS += --with-pam
CONFIGURE_ARGS += --with-altlog
CONFIGURE_ARGS += --with-brokenrealpath
CONFIGURE_ARGS += --enable-largefile
CONFIGURE_ARGS += --sysconfdir=$(prefix)/etc/$(SRCNAME)

# use X/Open CAE specifications
EXTRA_CFLAGS = -D_XOPEN_SOURCE=1 -D_XOPEN_SOURCE_EXTENDED=1

# No test suite available
TEST_SCRIPTS =

include gar/category.mk

# make sure, the linker uses libcrypt before libssl
post-configure-modulated:
	@perl -pi -e 's@-lssl -lcrypto -lcrypt@-lcrypt -lssl -lcrypto@' \
           ${WORKSRC}/Makefile
	@perl -pi -e 's@-lssl -lcrypto -lcrypt@-lcrypt -lssl -lcrypto@' \
           ${WORKSRC}/src/Makefile

# strange archive...
post-build-modulated:
	@chmod 751 $(WORKSRC)/x

# create config directory
pre-install-modulated:
	ginstall -d $(DESTDIR)$(sysconfdir)/$(SRCNAME)
