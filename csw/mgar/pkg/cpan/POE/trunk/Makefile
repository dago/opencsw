NAME = POE
VERSION = 1.287
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = RCAPUTO

DESCRIPTION = Portable multitasking and networking framework for Perl
define BLURB
  POE is a framework for cooperative, event driven multitasking in Perl. Other
  languages have similar frameworks. Python has Twisted. TCL has "the event
  loop".

  POE originally was developed as the core of a persistent object server and
  runtime environment. It has evolved into a general purpose multitasking and
  networking framework, encompassing and providing a consistent interface to
  other event loops such as Event and the Tk and Gtk toolkits.
endef

DISTFILES = COPYING

PACKAGES = CSWpmpoe
CATALOGNAME = pm_poe

RUNTIME_DEP_PKGS = CSWpmiotty
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS) CSWpoetestloops

ARCHALL = 1

CONFIGURE_ARGS = --default

include gar/category.mk
