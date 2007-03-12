GARNAME = Event-Lib
GARVERSION = 1.01
CATEGORIES = cpan
AUTHOR = VPARSEVAL

DESCRIPTION = Perl extentions for event-based programming
define BLURB
  This module is a Perl wrapper around libevent(3) as available from
  http://www.monkey.org/~provos/libevent/. It allows to execute a function
  whenever a given event on a filehandle happens, a timeout occurs or a signal
  is received.
endef

DISTFILES  += $(call admfiles,CSWpmeventlib,depend prototype)

# Sun cc inline function patch
PATCHFILES += inline.diff

CONFIGURE_ARGS += LIBS="-L$(libdir) -levent"
CONFIGURE_ARGS += INC="-I$(includedir)"

include ../category.mk
