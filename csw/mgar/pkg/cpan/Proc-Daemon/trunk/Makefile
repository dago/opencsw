# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = Proc-Daemon
VERSION = 0.14
GARTYPE = v2
CATEGORIES = cpan
AUTHOR = DETI

DESCRIPTION = Run Perl program(s) as a daemon process
define BLURB
  Run Perl program(s) as a daemon process
endef

# Weird subdir (proc) makes auto-fetch not work
MASTER_SITES = http://mirrors.kernel.org/cpan/authors/id/D/DE/DETI/Proc/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

DISTFILES += COPYING

PACKAGES = CSWpm-proc-daemon
CATALOGNAME = pm_proc_daemon
ARCHALL = 1

include gar/category.mk
