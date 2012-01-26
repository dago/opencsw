# $Id$
# 
# TODO (release-critical prefixed with !, non release-critical with *)
# ! doesn't compile yet
#  CC     yad-about.o
#  "yad.h", line 176: syntax error before or at: &
#  "yad.h", line 176: warning: syntax requires ";" after last struct/union member
#  "about.c", line 62: cannot recover from previous errors
#  cc: acomp failed for about.c

NAME = yad
VERSION = 0.10.1
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Display GTK dialog boxes from shell scripts (zenity fork)
define BLURB
  Yad (yet another dialog) is a fork of Zenity with many improvements,
  such as custom buttons, additional dialogs, pop-up menu in notification
  icon and more.
endef

VENDOR_URL   = http://code.google.com/p/yad/
MASTER_SITES = http://yad.googlecode.com/files/
DISTFILES    = $(DISTNAME).tar.xz

UPSTREAM_MASTER_SITES = http://code.google.com/p/yad/downloads/list

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

PATH := $(prefix)/gnu:$(PATH)
