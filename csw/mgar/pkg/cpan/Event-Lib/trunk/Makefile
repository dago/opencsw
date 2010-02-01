GARNAME = Event-Lib
GARVERSION = 1.03
CATEGORIES = cpan
AUTHOR = VPARSEVAL

DESCRIPTION = Perl extentions for event-based programming
define BLURB
  This module is a Perl wrapper around libevent(3) as available from
  http://www.monkey.org/~provos/libevent/. It allows to execute a function
  whenever a given event on a filehandle happens, a timeout occurs or a signal
  is received.
endef

PACKAGES = CSWpmeventlib
CATALOGNAME = pm_eventlib

PREREQUISITE_PKGS = CSWlibevent-devel
REQUIRED_PKGS = CSWlibevent

# Sun cc inline function patch
PATCHFILES = inline.diff

CONFIGURE_ARGS += LIBS="-L$(libdir) -levent"
CONFIGURE_ARGS += INC="-I$(includedir)"

# Skip tests as some of them are failing. Remove after the
# issues have been resolved:
#   https://rt.cpan.org/Ticket/Display.html?id=51129
SKIPTEST = 1

include gar/category.mk
