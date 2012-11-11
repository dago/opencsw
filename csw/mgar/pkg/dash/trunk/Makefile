# $Id$
#
NAME = dash
VERSION = 0.5.7
GARTYPE = v2

DESCRIPTION = POSIX-compliant implementation of /bin/sh that aims to be as small as possible
define BLURB
endef

VENDOR_URL = http://gondor.apana.org.au/~herbert/dash/
MASTER_SITES = http://gondor.apana.org.au/~herbert/dash/files/
DISTFILES  = $(DISTNAME).tar.gz

# I'm too lazy to remove gcc-isms such as -Wall and -include.
GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)

CHECKPKG_OVERRIDES_CSWdash += file-with-bad-content|/usr/share|root/opt/csw/share/doc/dash/license
CHECKPKG_OVERRIDES_CSWdash += file-with-bad-content|/usr/local|root/opt/csw/bin/dash

include gar/category.mk

# There are "sh foo" bits in the Makefile. Need to use a POSIX shell for that.
PATH := /usr/xpg4/bin:$(PATH)
