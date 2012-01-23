NAME = alarm-clock
VERSION = 1.4.1
CATEGORIES = gnome

DESCRIPTION = A simple interface for reminding about birthdays, appointments and important dates
define BLURB
  Alarm Clock is designed to provide user with simple interface for creating alarms,
  reminding him about birthdays, appointments, important dates. Alarm Clock can be configured
  very easily even by a non-power user and fits perfectly into the GNOME Desktop.
endef

MASTER_SITES = http://alarm-clock.pl/downloads/
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

PACKAGES = CSWalarmclock
CATALOGNAME = alarmclock

RUNTIME_DEP_PKGS  = CSWdbusglib CSWfconfig CSWftype2 CSWggettextrt CSWglib2 CSWgstreamer CSWgtk2
RUNTIME_DEP_PKGS += CSWlibatk CSWlibcairo CSWlibdbus CSWlibnotify CSWlibxml2 CSWpango CSWlibunique

CONFIGURE_ARGS = $(DIRPATHS)

# AM_CFLAGS contains -Wall which only works with GCC
BUILD_OVERRIDE_VARS = AM_CFLAGS
BUILD_OVERRIDE_VAR_AM_CFLAGS =

# Remove when move towards csw x11 has been finished
EXTRA_LINKER_FLAGS = /usr/openwin/lib/libXext.so

STRIP_LIBTOOL = 1

INSTALL_OVERRIDE_VARS = alarmclockdocdir
INSTALL_OVERRIDE_VAR_alarmclockdocdir = $(docdir)/$(CATALOGNAME)

include gar/category.mk

#For GNU xgettext
PATH := /opt/csw/gnu:$(PATH)
