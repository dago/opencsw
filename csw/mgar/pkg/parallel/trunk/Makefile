# $Id$
NAME = parallel
VERSION = 20100424
CATEGORIES = utils

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
DISTFILES += gpl-3.0.txt

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

LICENSE = gpl-3.0.txt

VENDOR_URL = http://www.gnu.org/software/parallel/

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

ARCHALL = 1

include gar/category.mk
