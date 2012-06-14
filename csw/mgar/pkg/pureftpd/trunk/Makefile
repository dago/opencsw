# known build facts
#
# no linkage against
# - ldap
# - mysql 
# - pgsql
NAME = pureftpd
VERSION = 1.0.36
CATEGORIES = net
GARTYPE = v2
SRCNAME = pure-ftpd

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

DESCRIPTION = A secure FTP daemon
define BLURB
  Pure-FTPd is a free (BSD), secure, production-quality and
  standard-conformant FTP server. It doesn't provide useless bells and
  whistles, but focuses on efficiency and ease of use. It provides simple
  answers to common needs, plus unique useful features for personal users
  as well as hosting providers.
endef

MASTER_SITES = http://download.pureftpd.org/pub/pure-ftpd/releases/
DISTFILES  = $(SRCNAME)-$(VERSION).tar.gz
WORKSRC = $(WORKDIR)/$(SRCNAME)-$(VERSION)

BUILD_DEP_PKGS += CSWlibssl-dev

# we require openssl for tls
RUNTIME_DEP_PKGS = CSWlibssl1-0-0

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

sysconfdir = /etc/opt/csw
SAMPLECONF = $(sysconfdir)/$(SRCNAME)/*.conf

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
	ginstall -d $(DESTDIR)$(docdir)/$(SRCNAME)
	ginstall -d $(DESTDIR)/var/opt/csw/run
	perl -pi -e 's@/var/run@/var/opt/csw/run@' ${WORKSRC}/src/ftpd.h
	perl -pi -e 's@/var/run@/var/opt/csw/run@' ${WORKSRC}/src/ftpwho-update.h
	perl -pi -e 's@/var/run@/var/opt/csw/run@' ${WORKSRC}/src/upload-pipe.h
	@$(MAKECOOKIE)

conf-list  = $(WORKSRC)/pureftpd-ldap.conf
conf-list += $(WORKSRC)/pureftpd-mysql.conf
conf-list += $(WORKSRC)/pureftpd-pgsql.conf
post-install-modulated:
	( for file in $(conf-list) ; do \
		ginstall -m 644 $$file $(DESTDIR)$(sysconfdir)/$(SRCNAME) ; \
		done )
	ginstall -m 644 $(WORKSRC)/pureftpd.schema $(DESTDIR)$(docdir)/$(SRCNAME)
	@$(MAKECOOKIE)
