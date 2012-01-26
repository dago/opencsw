NAME = Mail-Sendmail
VERSION = 0.79
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MIVKOVIC

DESCRIPTION = Simple platform independent mailer
define BLURB
  Mail::Sendmail contains mainly &sendmail, which takes a hash with the
  message to send and sends it. It is intended to be very easy to setup and
  use. See also "FEATURES" below.
endef

DISTFILES = COPYING

PACKAGES = CSWpmmailsendmail
CATALOGNAME = pm_mailsendmail

DEPS_PKGS = CSWpmmimebase64

ARCHALL = 1

# Skip sending test email
PATCHFILES = test.diff

include gar/category.mk
