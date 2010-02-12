GARNAME = setoolkit
GARVERSION = 3.5.1
DISTNAME = $(GARNAME)-$(GARVERSION)
CATEGORIES = utils

DESCRIPTION = A system performance monitoring tool
define BLURB
  The SE Toolkit is
  * An interpreter for a programming language that is both a subset of C and C++.
    Syntactically, it looks like C, but it contains a limited class mechanism.
  * Include files for use by toolkit scripts.
  * A bunch of example scripts.
  * A set of extensions for writing GUIs and "network aware" scripts.
endef

SF_PROJ = setoolkit
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=189279
UPSTREAM_USE_SF = 1
UFILES_REGEX = SE.Toolkit.(\d+(?:\.\d+)*)

BUILD_DEP_PKGS = CSWpydocutils

BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS)

# Don't relocate $(bindir) as it contains a shell wrapper
ISAEXEC_DIRS = $(libexecdir)

MERGE_EXCLUDE_FILES = .*~ $(bindir)/.*\.sh .*\.la

# Don't add the shell wrapper for other ISAs
EXTRA_MERGE_EXCLUDE_FILES_amd64 = $(bindir)/se
EXTRA_MERGE_EXCLUDE_FILES_sparcv9 = $(bindir)/se

# Testsuite must be run as root
SKIPTEST = 1

# This is intended behaviour as the missing symbols are provided by the "se" binary
# and the libs are to be used only by "se".
CHECKPKG_OVERRIDES  = CSWsetoolkit|symbol-not-found|libsegui.so
CHECKPKG_OVERRIDES += CSWsetoolkit|symbol-not-found|libsenet.so

include gar/category.mk
