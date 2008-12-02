GARNAME = setoolkit
GARVERSION = 3.5.0
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
DISTFILES += $(call admfiles,CSWsetoolkit,depend)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

BUILD64 = 1

# Don't relocate $(bindir) as it contains a shell wrapper
ISAEXEC_DIRS = $(libexecdir)

MERGE_EXCLUDE_FILES = .*~ $(bindir)/.*\.sh .*\.la

# Don't add the shell wrapper for other ISAs
EXTRA_MERGE_EXCLUDE_FILES_amd64 = $(bindir)/se
EXTRA_MERGE_EXCLUDE_FILES_sparcv9 = $(bindir)/se

SKIPTEST = 1

include gar/category.mk
