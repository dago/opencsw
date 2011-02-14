NAME = msmtp
VERSION = 1.4.23
CATEGORIES = net

DESCRIPTION = SMTP client
define BLURB
  In the default mode, it transmits a mail to an SMTP server
  (for example at a free mail provider) which does the delivery.
  To use this program with your mail user agent (MUA), create a
  configuration file with your mail account(s) and tell your MUA
  to call msmtp instead of /usr/sbin/sendmail.
  Features include:
    * Sendmail compatible interface (command line options and exit codes).
    * Authentication methods PLAIN, LOGIN, CRAM-MD5, DIGEST-MD5, GSSAPI, and NTLM.
    * TLS/SSL both in SMTP-over-SSL mode and in STARTTLS mode.
      Full certificate trust checks can be performed. A client certificate can be sent.
    * Fast SMTP implementation using command pipelining.
    * Support for Internationalized Domain Names (IDN).
    * DSN (Delivery Status Notification) support.
    * RMQS (Remote Message Queue Starting) support (ETRN keyword).
    * IPv6 support.
    * Support for multiple accounts.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES = $(NAME)-$(VERSION).tar.bz2

PACKAGES += CSWmsmtp
CATALOGNAME_CSWmsmtp = msmtp
SPKG_DESC_CSWmsmtp = $(DESCRIPTION)

VENDOR_URL = http://msmtp.sourceforge.net/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

BUILD_DEP_PKGS += CSWgnutlsdevel
BUILD_DEP_PKGS += CSWlibgsasldevel
BUILD_DEP_PKGS += CSWggettext

RUNTIME_DEP_PKGS_CSWmsmtp += CSWlibidn
RUNTIME_DEP_PKGS_CSWmsmtp += CSWgnutls
RUNTIME_DEP_PKGS_CSWmsmtp += CSWlibgsasl7
RUNTIME_DEP_PKGS_CSWmsmtp += CSWggettextrt

sysconfdir = /etc/opt/csw
CONFIGURE_ARGS = $(DIRPATHS)

PRESERVECONF = $(sysconfdir)/msmtprc

TEST_TARGET = check

include gar/category.mk

# The path in CA_CERTIFICATES is taken from CSWcacertificates
post-install-modulated: DOCDIR=$(docdir)/msmtp
post-install-modulated: CA_CERTIFICATES=/opt/csw/etc/ca-certificates.conf
post-install-modulated:
	ginstall -d $(DESTDIR)$(DOCDIR)
	ginstall $(WORKSRC)/doc/Mutt+msmtp.txt $(DESTDIR)$(DOCDIR)
	# ginstall $(WORKSRC)/doc/msmtp.html $(DESTDIR)$(DOCDIR)
	# ginstall $(WORKSRC)/doc/msmtp.pdf $(DESTDIR)$(DOCDIR)
	ginstall -d $(DESTDIR)$(sysconfdir)
	cat $(WORKSRC)/doc/msmtprc-system.example | \
		perl -np -e 's/^/#/ if( /^[^#]+/ );' \
			-e 's,(tls_trust_file\s+).*,\1$(CA_CERTIFICATES),;' \
			> $(DESTDIR)/etc/opt/csw/msmtprc
	ginstall $(WORKSRC)/doc/msmtprc-user.example	\
		$(DESTDIR)$(DOCDIR)/msmtprc-user.example
	perl -pi -e 's,/usr/local/etc,$(sysconfdir),;' \
		-e 's,/usr/local/bin,$(bindir),;' \
		$(DESTDIR)$(infodir)/msmtp.info \
		$(DESTDIR)$(DOCDIR)/Mutt+msmtp.txt
	@$(MAKECOOKIE)
