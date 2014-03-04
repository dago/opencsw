NAME = xjobs
VERSION = 20140125
CATEGORIES = utils
GARTYPE = v2

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
DISTFILES  = $(DISTNAME).tgz

VENDOR_URL = http://www.maier-komolibumem.so.1 has only symbols which are not directly bindable
# dam@unstable10s [unstable10s]:/home/dam/mgar/pkg/xjobs/trunk > $(mgar show-buildsys | cut -f1)/bin/check_db_symbols work/solaris10-sparc/pkgroot/opt/csw/bin/xjobs
# Library                 Directly bound    Not directly bound    Not directly bindable
# libumem.so.1                    0                  0            3
# libc.so.1                      74                  0            2
# libm.so.2                       2                  0            0
CHECKPKG_OVERRIDES_CSWxjobs += no-direct-binding|/opt/csw/bin/xjobs|is|not|directly|bound|to|soname|libumem.so.1

# No tests available
TEST_SCRIPTS =

include gar/category.mk
