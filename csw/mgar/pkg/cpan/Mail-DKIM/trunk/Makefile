GARNAME = Mail-DKIM
GARVERSION = 0.36
CATEGORIES = cpan
AUTHOR = JASLONG

DESCRIPTION = Signs/verifies Internet mail with DKIM/DomainKey signatures
define BLURB
  This module implements the various components of the DKIM and DomainKeys
  message-signing and verifying standards for Internet mail. It currently
  tries to implement these Internet Drafts:
   * draft-ietf-dkim-base-10
   * draft-delany-domainkeys-base
endef

PACKAGES = CSWpmmaildkim
CATALOGNAME = pm_maildkim
ARCHALL = 1

DEPENDS += cpan/Crypt-OpenSSL-RSA
DEPENDS += cpan/Digest-SHA1
DEPENDS += cpan/Error
DEPENDS += cpan/MailTools
DEPENDS += cpan/Net-DNS

REQUIRED_PKGS += CSWpmcryptosslrsa
REQUIRED_PKGS += CSWpmdigestsha
REQUIRED_PKGS += CSWpmdigestsha1
REQUIRED_PKGS += CSWpmerror
REQUIRED_PKGS += CSWpmmailtools
REQUIRED_PKGS += CSWpmmimebase64
REQUIRED_PKGS += CSWpmnetdns

include gar/category.mk
