NAME = Path-Class
VERSION = 0.25
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = KWILLIAMS

DESCRIPTION = Cross-platform path specification manipulation
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

PACKAGES += CSWpm-path-class
CATALOGNAME_CSWpm-path-class = pm_path_class
SPKG_DESC_CSWpm-path-class = Cross-platform path specification manipulation
ARCHALL_CSWpm-path-class = 1
OBSOLETED_BY_CSWpm-path-class += CSWpmpathclass
CATALOGNAME_CSWpmpathclass = pm_pathclass_stub

# These are just docs
CHECKPKG_OVERRIDES_CSWpm-path-class += file-with-bad-content|/usr/local|root/opt/csw/share/perl/csw/Path/Class/Dir.pm
CHECKPKG_OVERRIDES_CSWpm-path-class += file-with-bad-content|/usr/local|root/opt/csw/share/perl/csw/Path/Class/File.pm
CHECKPKG_OVERRIDES_CSWpm-path-class += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/Path::Class::File.3perl
CHECKPKG_OVERRIDES_CSWpm-path-class += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/Path::Class::Dir.3perl

include gar/category.mk
