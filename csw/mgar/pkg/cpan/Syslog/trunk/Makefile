GARNAME = Unix-Syslog
GARVERSION = 0.97
CATEGORIES = cpan
AUTHOR = MHARNISCH

DESCRIPTION = interface to the UNIX syslog(3) calls
define BLURB
  This module provides an interface to the system logger syslogd(8) via Perl's
  XSUBs. The implementation attempts to resemble the native libc-functions of
  your system, so that anyone being familiar with syslog.h should be able to
  use this module right away.  In contrary to Sys::Syslog(3), this modules
  does not open a network connection to send the messages. This can help you
  to avoid opening security holes in your computer (see "FAQ").
endef

DISTFILES += CSWpmunixsyslog.gspec

include gar/category.mk
