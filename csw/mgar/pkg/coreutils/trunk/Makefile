GARNAME = coreutils
GARVERSION = 7.6
CATEGORIES = utils

DESCRIPTION = Basic file, shell and text manipulation utilities
define BLURB
The GNU Core Utilities are the basic file, shell and text manipulation
utilities of the GNU operating system. These are the core utilities which
are expected to exist on every operating system.

Previously these utilities were offered as three individual sets of GNU
utilities, fileutils, shellutils, and textutils. Those three have been
combined into a single set of utilities called the coreutils. 
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --program-prefix=g
CONFIGURE_ARGS += --enable-silent-rules
CONFIGURE_ARGS += --disable-libcap
CONFIGURE_ARGS += --with-packager="$(SPKG_PACKAGER) <$(SPKG_EMAIL)>"

TEST_ARGS = check

GARCOMPILER = GNU

include gar/category.mk
