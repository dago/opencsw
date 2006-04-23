GARNAME = pwsafe
GARVERSION = 0.1.6
CATEGORIES = utils

DESCRIPTION = command-line password database.
define BLURB
  pwsafe is a command line password database program for Unix. It is compatible
  with Counterpane's Win32 Password Safe software. It can also copy the
  passwords into the X selection and clipboard, but it doesn't open a visible
  window. The encrypted password database uses the same format as Password Safe
  1.9.x. The database is encrypted with blowfish, and a single passphrase
  decrypts it all.
endef

MASTER_SITES = http://nsd.dyndns.org/pwsafe/releases/
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += CSWpwsafe.gspec

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-openssl-dir=$(prefix)/ssl
CONFIGURE_ARGS += --with-x

TEST_TARGET = check

include ../category.mk
