# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = svnmailer
VERSION = 1.0.8
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = A tool to post subversion repository information.
define BLURB
  Svnmailer is a tool to post subversion repository commit information by
  mail, news or XML (to a CIA tracker).
endef

MASTER_SITES = http://storage.perlig.de/$(NAME)/
DISTFILES = $(DISTNAME).tar.bz2

ARCHALL = 1

# No test suite/scripts available, cf. README
# A (still incomplete) test suite is available as an extra package
# (svnmailer_test). This test package needs to be downloaded seperatly.
TEST_SCRIPTS = 

include gar/category.mk
