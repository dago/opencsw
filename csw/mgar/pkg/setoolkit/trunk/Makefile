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
CHECKPKG_OVERRIDES_CSWsetoolkit += init-file-missing-cswinitsmf-class|/opt/csw/share/setoolkit/etc/init.d/mon_cm|class=none
CHECKPKG_OVERRIDES_CSWsetoolkit += init-file-missing-cswinitsmf-class|/opt/csw/share/setoolkit/etc/init.d/monlog|class=none
CHECKPKG_OVERRIDES_CSWsetoolkit += init-file-missing-cswinitsmf-class|/opt/csw/share/setoolkit/etc/init.d/percol|class=none
CHECKPKG_OVERRIDES_CSWsetoolkit += init-file-missing-cswinitsmf-class|/opt/csw/share/setoolkit/etc/init.d/va_monitor|class=none
CHECKPKG_OVERRIDES_CSWsetoolkit += init-file-missing-cswinitsmf-class|/opt/csw/share/setoolkit/etc/init.d/vader|class=none
CHECKPKG_OVERRIDES_CSWsetoolkit += soname-equals-filename|file=/opt/csw/lib/libsegui.so
CHECKPKG_OVERRIDES_CSWsetoolkit += soname-equals-filename|file=/opt/csw/lib/libsenet.so
CHECKPKG_OVERRIDES_CSWsetoolkit += soname-equals-filename|file=/opt/csw/lib/amd64/libsegui.so
CHECKPKG_OVERRIDES_CSWsetoolkit += soname-equals-filename|file=/opt/csw/lib/amd64/libsenet.so
CHECKPKG_OVERRIDES_CSWsetoolkit += soname-equals-filename|file=/opt/csw/lib/sparcv9/libsegui.so
CHECKPKG_OVERRIDES_CSWsetoolkit += soname-equals-filename|file=/opt/csw/lib/sparcv9/libsenet.so
CHECKPKG_OVERRIDES_CSWsetoolkit += file-with-bad-content|/usr/local|root/opt/csw/share/doc/setoolkit/INSTALL
CHECKPKG_OVERRIDES_CSWsetoolkit += file-with-bad-content|/usr/local|root/opt/csw/share/setoolkit/examples/limits.se
CHECKPKG_OVERRIDES_CSWsetoolkit += shared-lib-pkgname-mismatch|sonames=libsegui.so,libsenet.so|pkgname=CSWsetoolkit|expected=CSWlibse|

include gar/category.mk
