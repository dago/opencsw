GARNAME = xjobs
GARVERSION = 20091012
CATEGORIES = utils

DESCRIPTION = Executes jobs in parallel similar to xargs
define BLURB
  xjobs reads job descriptions line by line and executes them in parallel.
  It limits the number of parallel executing jobs and starts new jobs when
  jobs finish. Therefore, it combines the arguments from every input line
  with the utility and arguments given on the command line. If no utility
  is given as an argument to xjobs, then the first argument on every job
  line will be used as utility. To execute utility xjobs searches the
  directories given in the PATH environment variable and uses the first
  file found in these directories.
endef

MASTER_SITES = http://www.maier-komor.de/xjobs/
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tgz

CONFIGURE_ARGS = $(DIRPATHS)

# No tests available
TEST_SCRIPTS =

include gar/category.mk
