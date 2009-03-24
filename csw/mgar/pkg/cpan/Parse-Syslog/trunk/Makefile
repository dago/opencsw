GARNAME = Parse-Syslog
GARVERSION = 1.10
CATEGORIES = cpan
AUTHOR = DSCHWEI

DESCRIPTION = parse Unix syslog files
define BLURB
  Unix syslogs are convenient to read for humans but because of small
  differences between operating systems and things like 'last message repeated
  xx times' not very easy to parse by a script.  Parse::Syslog presents a
  simple interface to parse syslog files: you create a parser on a file (with
  new) and call next to get one line at a time with Unix-timestamp, host,
  program, pid and text returned in a hash-reference.
endef

CATALOGNAME     = pm_parsesyslog
PACKAGES	= CSWpmparsesyslog

ARCHALL_CSWpmparsesyslog = 1

LICENSE = README

include gar/category.mk

post-extract:
	@chmod o+r $(WORKSRC)/README
	@$(MAKECOOKIE)
