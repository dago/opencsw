GARNAME = File-Fetch
GARVERSION = 0.10
CATEGORIES = cpan
AUTHOR = KANE

DESCRIPTION = A generic file fetching mechanism
define BLURB
  File::Fetch is a generic file fetching mechanism.  It allows you to fetch
  any file pointed to by a ftp, http, file, or rsync uri by a number of
  different means.
endef

DISTFILES += $(call admfiles,CSWpmfilefetch,depend prototype)

DEPENDS += cpan/IPC-Cmd
DEPENDS += cpan/Params-Check
DEPENDS += cpan/Module-Load-Conditional
DEPENDS += cpan/Locale-Maketext-Simple

include ../category.mk
