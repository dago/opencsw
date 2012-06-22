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

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

# The above is a functionality patch
VERSION_FLAG_PATCH = 1

PACKAGES += CSWcvs
CATALOGNAME_CSWcvs = cvs
SPKG_DESC_CSWcvs = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWcvs += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWcvs += CSWlibz1
RUNTIME_DEP_PKGS_CSWcvs += CSWlibintl8
RUNTIME_DEP_PKGS_CSWcvs += CSWlibcom-err3
RUNTIME_DEP_PKGS_CSWcvs += CSWlibkrb5-3
RUNTIME_DEP_PKGS_CSWcvs += CSWlibgssapi-krb5-2
RUNTIME_DEP_PKGS_CSWcvs += CSWlibk5crypto3
OBSOLETED_BY_CSWcvs += CSWcvs-feature

# This is just the legacy link
PKGFILES_CSWcvs-feature += $(prefix)/cvs-feature

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-external-zlib=$(prefix)

# The testsuite runs for more than one hour!
SKIPTEST ?= 1

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
	gln -sf ../share/cvs/contrib/rcs2log $(DESTDIR)$(bindir)/rcslog
	gln -s . $(DESTDIR)$(prefix)/cvs-feature
	@$(MAKECOOKIE)
