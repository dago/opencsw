GARNAME = Email-Valid
GARVERSION = 0.15
CATEGORIES = cpan
AUTHOR = MAURICE

DESCRIPTION = check validity of Internet email addresses
define BLURB
  This module determines whether an email address is well-formed, and
  optionally, whether a mail host exists for the domain.  Please note that
  there is no way to determine whether an address is deliverable without
  attempting delivery (for details, see perlfaq 9).
endef

DISTFILES += CSWpmemailvalid.gspec CSWpmemailvalid.depend

# Disable MX check test
PATCHFILES = mxcheck.diff

DEPENDS += cpan/MailTools

include ../category.mk
