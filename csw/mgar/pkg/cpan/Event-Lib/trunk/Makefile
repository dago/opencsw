NAME = Event-Lib
VERSION = 1.03
CATEGORIES = cpan
GARTYPE = v2
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

LICENSE = README

BUILD_DEP_PKGS = CSWlibevent-devel
RUNTIME_DEP_PKGS = CSWlibevent2-0-5

# Sun cc inline function patch
PATCHFILES = inline.diff

CONFIGURE_ARGS += LIBS="-L$(libdir) -levent"
CONFIGURE_ARGS += INC="-I$(includedir)"

# Skip tests as some of them are failing. Remove after the
# issues have been resolved:
#   https://rt.cpan.org/Ticket/Display.html?id=51129
SKIPTEST = 1

# These can be removed after release of libevent2_0_5
CHECKPKG_OVERRIDES_CSWpmeventlib += unidentified-dependency|CSWlibevent2-0-5
CHECKPKG_OVERRIDES_CSWpmeventlib += soname-not-found|libevent-2.0.so.5|is|needed|by|opt/csw/lib/perl/csw/auto/Event/Lib/Lib.so

include gar/category.mk
