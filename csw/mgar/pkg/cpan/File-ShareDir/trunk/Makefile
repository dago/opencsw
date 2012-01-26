NAME = File-ShareDir
VERSION = 1.03
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = ADAMK

DESCRIPTION = Locate per-dist and per-module shared files
define BLURB
endef

LICENSE = LICENSE

PACKAGES += CSWpm-file-sharedir
CATALOGNAME_CSWpm-file-sharedir = pm_file_sharedir
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-file-sharedir = 1
RUNTIME_DEP_PKGS_CSWpm-file-sharedir = CSWpmclassinspector

# These are examples
CHECKPKG_OVERRIDES_CSWpm-file-sharedir += file-with-bad-content|/usr/share|root/opt/csw/share/perl/csw/File/ShareDir.pm
CHECKPKG_OVERRIDES_CSWpm-file-sharedir += file-with-bad-content|/usr/share|root/opt/csw/share/man/man3/File::ShareDir.3perl

include gar/category.mk
