NAME = cvs
VERSION = 1.12.13
CATEGORIES = utils
GARTYPE = v2

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

MASTER_SITES = http://ftp.gnu.org/non-gnu/cvs/source/feature/$(VERSION)/
UPSTREAM_MASTER_SITES = http://ftp.gnu.org/non-gnu/cvs/source/feature/

DISTFILES += $(DISTNAME).tar.bz2
DISTFILES += README.CSW

# Allow extssh as connection method by patch taken from
#   http://lists.gnu.org/archive/html/bug-cvs/2008-01/msg00007.html
PATCHFILES += cvs-1.12.13-extssh.diff

# The above is a functionality patch
VERSION_FLAG_PATCH = 1

PACKAGES += CSWcvs
CATALOGNAME_CSWcvs = cvs
SPKG_DESC_CSWcvs = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWcvs += CSWggettextrt
RUNTIME_DEP_PKGS_CSWcvs += CSWkrb5lib
RUNTIME_DEP_PKGS_CSWcvs += CSWosslrt
RUNTIME_DEP_PKGS_CSWcvs += CSWzlib

PACKAGES += CSWcvs-feature
CATALONGAME_CSWcvs-feature = cvs_feature
SPKG_DESC_CSWcvs-feature = Legacy package as CSWcvs now contains the feature CVS
PKGFILES_CSWcvs-feature = $(prefix)/cvs-feature
ARCHALL_CSWcvs-feature = 1
RUNTIME_DEP_PKGS_CSWcvs-feature = CSWcvs
CHECKPKG_OVERRIDES_CSWcvs-feature += surplus-dependency|CSWcvs

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-external-zlib=$(prefix)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)

# The testsuite runs for more than one hour!
# SKIPTEST ?= 1

# This is for GNATS. We don't have GNATS at OpenCSW
CHECKPKG_OVERRIDES_CSWcvs += file-with-bad-content|/usr/local|root/opt/csw/bin/cvsbug

# This is to find sccs and does no harm
CHECKPKG_OVERRIDES_CSWcvs += file-with-bad-content|/usr/local|root/opt/csw/share/cvs/contrib/sccs2rcs

# Here the pathes are for user-specific examples
CHECKPKG_OVERRIDES_CSWcvs += file-with-bad-content|/usr/local|root/opt/csw/share/info/cvs.info-1
CHECKPKG_OVERRIDES_CSWcvs += file-with-bad-content|/usr/local|root/opt/csw/share/info/cvs.info-2

include gar/category.mk

# Only GNU 'id' understands option '-u'
PATH := /opt/csw/gnu:$(PATH)

post-install-modulated:
	@gln -sf ../share/cvs/contrib/rcs2log $(DESTDIR)$(bindir)/rcslog
	@gln -s . $(DESTDIR)$(prefix)/cvs-feature
	@$(MAKECOOKIE)
