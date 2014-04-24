NAME = cscope
VERSION = 15.8a
GARTYPE = v2

DESCRIPTION = A text screen-based source browser
define BLURB
  cscope is a developer's tool for browsing source code. It has an impeccable
  Unix pedigree, having been originally developed at Bell Labs back in the days
  of the PDP-11. Cscope was part of the official AT&T Unix distribution for many
  years, and has been used to manage projects involving 20 million lines of code! 
endef

MASTER_SITES = $(SF_MIRRORS)
SF_PROJECT = cscope

PACKAGING_PLATFORMS = solaris9-i386 solaris9-sparc

DISTFILES = $(DISTNAME).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

# Test suite won't run as root!
TEST_SCRIPTS =

CHECKPKG_OVERRIDES_CSWcscope += file-with-bad-content|/usr/local|root/opt/csw/bin/ocs

include gar/category.mk
