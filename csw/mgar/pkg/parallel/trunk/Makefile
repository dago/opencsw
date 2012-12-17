# $Id$
NAME = parallel
VERSION = 20121122
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Shell tool for executing jobs in parallel
define BLURB
  GNU parallel is a shell tool for executing jobs in parallel. A job is
  typically a single command or a small script that has to be run for each
  of the lines in the input. The typical input is a list of files, a list
  of hosts, a list of users, or a list of tables.
  If you use xargs today you will find GNU parallel very easy to use. If you
  write loops in shell, you will find GNU parallel may be able to replace most
  of the loops and make them run faster by running jobs in parallel. If you use
  ppss or pexec you will find GNU parallel will often make the command easier to read.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

VENDOR_URL = http://www.gnu.org/software/parallel/

ARCHALL = 1

REINPLACE_MATCH = \#!/usr/bin/perl
REINPLACE_WITH = \#!/opt/csw/bin/perl
REINPLACE_FILES += src/niceload
REINPLACE_FILES += src/parallel
REINPLACE_FILES += src/sem
REINPLACE_FILES += src/sql

EXTRA_COMMON_EXPORTS = HOME

# Some idioms are used that the system Perl doesn't have
# (good that they show up during the testsuite run)
RUNTIME_DEP_PKGS = CSWperl
CHECKPKG_OVERRIDES_CSWparallel += surplus-dependency|CSWperl

# This references a special ssh like /usr/local/bin/myssh
CHECKPKG_OVERRIDES_CSWparallel += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/parallel.1
CHECKPKG_OVERRIDES_CSWparallel += file-with-bad-content|/usr/local|root/opt/csw/share/doc/parasr/local/bin/myssh
CHECKPKG_OVERRIDES_CSWparallel += file-with-bad-content|/usr/local|doc/parallel/parallel.texi

include gar/category.mk
