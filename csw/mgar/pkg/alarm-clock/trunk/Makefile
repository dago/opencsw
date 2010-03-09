GARNAME = alarm-clock
GARVERSION = 1.3
CATEGORIES = gnome

DESCRIPTION = A simple interface for reminding about birthdays, appointments and important dates
define BLURB
  Alarm Clock is designed to provide user with simple interface for creating alarms,
  reminding him about birthdays, appointments, important dates. Alarm Clock can be configured
  very easily even by a non-power user and fits perfectly into the GNOME Desktop.
endef

MASTER_SITES = http://alarm-clock.pl/media/distfiles/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

# AM_CFLAGS contains -Wall which only works with GCC
BUILD_OVERRIDE_VARS = AM_CFLAGS
BUILD_OVERRIDE_VAR_AM_CFLAGS =

include gar/category.mk

#For GNU xgettext
PATH := /opt/csw/gnu:$(PATH)
