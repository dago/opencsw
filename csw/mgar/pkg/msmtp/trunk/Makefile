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

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

post-install:
	@rm -f $(DESTDIR)$(infodir)/dir
	@ginstall -d $(DESTDIR)$(docdir)
	@ginstall $(WORKSRC)/doc/Mutt+msmtp.txt	\
		$(WORKSRC)/doc/msmtp.html 		\
		$(WORKSRC)/doc/msmtp.pdf		\
		$(DESTDIR)$(docdir)
	@ginstall -d $(DESTDIR)$(sysconfdir)
	@ginstall $(WORKSRC)/doc/msmtprc-system.example \
		$(WORKSRC)/doc/msmtprc-user.example	\
		$(DESTDIR)$(sysconfdir)
