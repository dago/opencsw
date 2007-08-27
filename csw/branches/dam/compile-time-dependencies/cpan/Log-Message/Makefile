GARNAME = Log-Message
GARVERSION = 0.01
CATEGORIES = cpan
AUTHOR = KANE

DESCRIPTION = Generic message storage mechanism.
define BLURB
  Log::Message is a generic message storage mechanism. It allows you to store
  messages on a stack -- either shared or private -- and assign meta-data to
  it.  Some meta-data will automatically be added for you, like a timestamp
  and a stack trace, but some can be filled in by the user, like a tag by
  which to identify it or group it, and a level at which to handle the message
  (for example, log it, or die with it)
endef

DISTFILES += $(call admfiles,CSWpmlogmessage,depend prototype)

DEPENDS += cpan/Params-Check
DEPENDS += cpan/Locale-Maketext-Simple

include ../category.mk
