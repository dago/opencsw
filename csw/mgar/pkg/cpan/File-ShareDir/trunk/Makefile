NAME = File-ShareDir
VERSION = 1.03
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = ADAMK

DESCRIPTION = Locate per-dist and per-module shared files
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

PACKAGES += CSWpm-file-sharedir
CATALOGNAME_CSWpm-file-sharedir = pm_file_sharedir
SPKG_DESC_CSWpm-file-sharedir = Locate per-dist and per-module shared files
ARCHALL_CSWpm-file-sharedir = 1
RUNTIME_DEP_PKGS_CSWpm-file-sharedir += CSWpm-class-inspector

CHECKPKG_OVERRIDES_CSWpm-file-sharedir += file-with-bad-content|/usr/share|root/opt/csw/share/man/man3/File::ShareDir.3perl
CHECKPKG_OVERRIDES_CSWpm-file-sharedir += file-with-bad-content|/usr/share|root/opt/csw/share/perl/csw/File/ShareDir.pm

include gar/category.mk
