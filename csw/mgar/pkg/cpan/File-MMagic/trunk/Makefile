NAME = File-MMagic
VERSION = 1.28
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = KNOK

DESCRIPTION = Guess file type from contents
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = COPYING

PACKAGES += CSWpm-file-mmagic
CATALOGNAME_CSWpm-file-mmagic = pm_file_mmagic
SPKG_DESC_CSWpm-file-mmagic = Guess file type from contents
ARCHALL_CSWpm-file-mmagic = 1
OBSOLETED_BY_CSWpm-file-mmagic += CSWpmfilemmagic
CATALOGNAME_CSWpmfilemmagic = pm_filemmagic_stub

# These are just examples
CHECKPKG_OVERRIDES_CSWpm-file-mmagic += file-with-bad-content|/usr/share|root/opt/csw/share/man/man3/File::MMagic.3perl
CHECKPKG_OVERRIDES_CSWpm-file-mmagic += file-with-bad-content|/usr/share|root/opt/csw/share/perl/csw/File/MMagic.pm

include gar/category.mk
