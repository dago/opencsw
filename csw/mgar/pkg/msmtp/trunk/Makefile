NAME = msmtp
VERSION = 1.4.26
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
SPKG_DESC_CSWmsmtp = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWmsmtp += CSWlibgsasl7
RUNTIME_DEP_PKGS_CSWmsmtp += CSWlibintl8
RUNTIME_DEP_PKGS_CSWmsmtp += CSWlibidn11
RUNTIME_DEP_PKGS_CSWmsmtp += CSWlibgnome-keyring0
RUNTIME_DEP_PKGS_CSWmsmtp += CSWlibgnutls26
RUNTIME_DEP_PKGS_CSWmsmtp += CSWglib2

RUNTIME_DEP_PKGS_5.9 = CSWlibgnugetopt0
RUNTIME_DEP_PKGS_CSWmsmtp += $(RUNTIME_DEP_PKGS_$(GAROSREL))

EXTRA_LINKER_FLAGS_5.9 = -lgnugetopt
EXTRA_LINKER_FLAGS = $(EXTRA_LINKER_FLAGS_$(GAROSREL))

VENDOR_URL = http://msmtp.sourceforge.net/

BUILD_DEP_PKGS += CSWlibgnutls-dev
BUILD_DEP_PKGS += CSWlibgsasl-dev
BUILD_DEP_PKGS += CSWggettext-dev
BUILD_DEP_PKGS += CSWgnomekeyring-dev

PRESERVECONF = $(sysconfdir)/msmtprc

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
