GARNAME = Mail-DKIM
GARVERSION = 0.32
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

DISTFILES += $(call admfiles,CSWpmmaildkim,depend,)

DEPENDS += cpan/Crypt-OpenSSL-RSA
DEPENDS += cpan/Digest-SHA1
DEPENDS += cpan/Error
DEPENDS += cpan/MailTools
DEPENDS += cpan/Net-DNS

include gar/category.mk
