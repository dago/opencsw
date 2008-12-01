GARNAME = cvs
GARVERSION = 1.11.23
CATEGORIES = utils

DESCRIPTION = Concurrent Versioning System
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

MASTER_SITES = http://ftp.gnu.org/non-gnu/cvs/source/stable/$(GARVERSION)/
UPSTREAM_MASTER_SITES = http://ftp.gnu.org/non-gnu/cvs/source/stable/
DISTFILES = $(DISTNAME).tar.bz2
DISTFILES += $(call admfiles,CSWcvs,)

CONFIGURE_ARGS = $(DIRPATHS)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)

TEST_TARGET = check

# Test suite won't run as root!
TEST_SCRIPTS =

include gar/category.mk

post-install:
	@rm -f $(DESTDIR)$(infodir)/dir
	@gln -sf ../share/cvs/contrib/rcs2log $(DESTDIR)$(bindir)/rcslog
	@$(MAKECOOKIE)
