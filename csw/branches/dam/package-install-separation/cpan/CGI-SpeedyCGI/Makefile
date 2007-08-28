GARNAME = CGI-SpeedyCGI
GARVERSION = 2.22
CATEGORIES = cpan
AUTHOR = HORROCKS

DESCRIPTION = Speed up perl scripts by running them persistently
define BLURB
  SpeedyCGI is a way to run perl scripts persistently, which can make them run
  much more quickly.
endef

DISTFILES += CSWpmspeedycgi.gspec

# Don't build the apache/apache2 modules
PATCHFILES += build.diff

include ../category.mk
