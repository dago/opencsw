GARNAME = cvs
GARVERSION = 1.12.13
CATEGORIES = utils

DESCRIPTION = The Concurrent Versioning System.
define BLURB
  CVS is a version control system, which allows you to keep old
  versions of files (usually source code), keep a log of who, when,
  and why changes occurred, etc., like RCS or SCCS. Unlike the
  simpler systems, CVS does not just operate on one file at a time
  or one directory at a time, but operates on hierarchical collections
  of directories consisting of version controlled files. CVS helps
  to manage releases and to control the concurrent editing of source
  files among multiple authors. CVS allows triggers to enable/log/control
  various operations and works well over a wide area network.
endef

# Master site won't work for cvs, as the download mechanism is a
# CGI script that uses a database ID to select the file rather than
# the file name.  Download a copy manually.

DISTFILES = $(DISTNAME).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

# Test suite won't run as root!
TEST_SCRIPTS =

include ../category.mk
