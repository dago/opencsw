NAME = Mail-DKIM
VERSION = 0.37
CATEGORIES = cpan
GARTYPE = v2
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
LICENSE = $(FILEDIR)/LICENSE
ARCHALL = 1

DEPENDS += cpan/Crypt-OpenSSL-RSA
DEPENDS += cpan/Error
DEPENDS += cpan/MailTools
DEPENDS += cpan/Net-DNS

RUNTIME_DEP_PKGS += CSWpmcryptosslrsa
RUNTIME_DEP_PKGS += CSWpmdigestsha1
RUNTIME_DEP_PKGS += CSWpmerror
RUNTIME_DEP_PKGS += CSWpmmailtools
RUNTIME_DEP_PKGS += CSWpmmimebase64
RUNTIME_DEP_PKGS += CSWpmnetdns

include gar/category.mk
