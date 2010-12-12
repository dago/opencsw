NAME = setoolkit
VERSION = 3.5.1
DISTNAME = $(NAME)-$(VERSION)
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
EXTRA_MERGE_EXCLUDE_FILES_isa-amd64 = $(bindir)/se
EXTRA_MERGE_EXCLUDE_FILES_isa-sparcv9 = $(bindir)/se

# Testsuite must be run as root
SKIPTEST = 1

CHECKPKG_OVERRIDES_CSWsetoolkit += missing-dependency|CSWemacscommon
CHECKPKG_OVERRIDES_CSWsetoolkit += linked-against-discouraged-library|libsegui.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWsetoolkit += linked-against-discouraged-library|libsegui.so|libX11.so.4
CHECKPKG_OVERRIDES_CSWsetoolkit += init-file-missing-cswinitsmf-class|/opt/csw/share/setoolkit/etc/init.d/mon_cm|class=none
CHECKPKG_OVERRIDES_CSWsetoolkit += init-file-missing-cswinitsmf-class|/opt/csw/share/setoolkit/etc/init.d/monlog|class=none
CHECKPKG_OVERRIDES_CSWsetoolkit += init-file-missing-cswinitsmf-class|/opt/csw/share/setoolkit/etc/init.d/percol|class=none
CHECKPKG_OVERRIDES_CSWsetoolkit += init-file-missing-cswinitsmf-class|/opt/csw/share/setoolkit/etc/init.d/va_monitor|class=none
CHECKPKG_OVERRIDES_CSWsetoolkit += init-file-missing-cswinitsmf-class|/opt/csw/share/setoolkit/etc/init.d/vader|class=none
CHECKPKG_OVERRIDES_CSWsetoolkit += soname-not-found|libm.so.2

include gar/category.mk
