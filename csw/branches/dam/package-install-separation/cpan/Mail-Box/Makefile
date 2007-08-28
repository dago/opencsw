GARNAME = Mail-Box
GARVERSION = 2.069
CATEGORIES = cpan
AUTHOR = MARKOV

DESCRIPTION = manage a mailbox, a folder with messages
define BLURB
  Mail::Box is the base class for accessing various types of mailboxes
  (folders) in a uniform manner. The various folder types vary on how they
  store their messages, but when some effort those differences could be hidden
  behind a general API. For example, some folders store many messages in one
  single file, where other store each message in a separate file withing the
  same directory.
endef

DEPENDS += cpan/Scalar-List-Utils cpan/File-Remove cpan/Object-Realize-Later
DEPENDS += cpan/MailTools cpan/MIME-Types cpan/URI cpan/IO-stringy
DEPENDS += cpan/Digest-HMAC cpan/User-Identity cpan/TimeDate
DEPENDS += cpan/MIME-tools cpan/HTML-Format cpan/Time-HiRes

DISTFILES += CSWpmmailbox.gspec

include ../category.mk
