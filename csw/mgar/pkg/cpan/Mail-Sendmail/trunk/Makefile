GARNAME = Mail-Sendmail
GARVERSION = 0.79
CATEGORIES = cpan
AUTHOR = MIVKOVIC

DESCRIPTION = simple platform independent mailer
define BLURB
  Mail::Sendmail contains mainly &sendmail, which takes a hash with the
  message to send and sends it. It is intended to be very easy to setup and
  use. See also "FEATURES" below.
endef

DISTFILES += CSWpmmailsendmail.gspec

# Skip sending test email
PATCHFILES = test.diff

include gar/category.mk
