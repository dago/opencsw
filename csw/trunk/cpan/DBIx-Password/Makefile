GARNAME = DBIx-Password
GARVERSION = 1.8
CATEGORIES = cpan
AUTHOR = KROW

DESCRIPTION = create a global password file for DB passwords
define BLURB
  Don't you hate keeping track of database passwords and such throughout your
  scripts? How about the problem of changing those passwords on a mass scale?
  This module is one possible solution. When you go to build this module it
  will ask you to create virtual users. For each user you need to specify the
  database module to use, the database connect string, the username and the
  password. You will be prompted to give a name to this virtual user. You can
  add as many as you like.
endef

DISTFILES += CSWpmdbixpassword.gspec CSWpmdbixpassword.depend

# Disable interactive install
PATCHFILES = interact.diff

DEPENDS += cpan/DBI

include ../category.mk

# Supply a sample cached entry for the mysql 'test' db
pre-configure:
	@cp $(FILEDIR)/test.cache $(WORKSRC)/.cache

