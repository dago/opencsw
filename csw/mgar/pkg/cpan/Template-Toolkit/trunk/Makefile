NAME = Template-Toolkit
VERSION = 2.24
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = ABW

DESCRIPTION = Comprehensive template processing system
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the perl license

PACKAGES += CSWpm-template
CATALOGNAME_CSWpm-template = pm_template
SPKG_DESC_CSWpm-template = Comprehensive template processing system
RUNTIME_DEP_PKGS_CSWpm-template += CSWpm-appconfig
OBSOLETED_BY_CSWpm-template += CSWpmtt2
CATALOGNAME_CSWpmtt2 = pm_tt2_stub
OBSOLETED_BY_CSWpm-template += CSWpmtt2-common
CATALOGNAME_CSWpmtt2-common = pm_tt2common_stub

# I checked some, all of them were examples, maybe take a closer look at some other time
CHECKPKG_OVERRIDES_CSWpm-template += file-with-bad-content|/usr/local|root/opt/csw/bin/ttree
CHECKPKG_OVERRIDES_CSWpm-template += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/ttree.1
CHECKPKG_OVERRIDES_CSWpm-template += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/Template::Manual::Intro.3perl
CHECKPKG_OVERRIDES_CSWpm-template += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/Template::Provider.3perl
CHECKPKG_OVERRIDES_CSWpm-template += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/Template::Tools::ttree.3perl
CHECKPKG_OVERRIDES_CSWpm-template += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/Template::Manual::Config.3perl
CHECKPKG_OVERRIDES_CSWpm-template += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/Template.3perl
CHECKPKG_OVERRIDES_CSWpm-template += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/Template::Config.3perl
CHECKPKG_OVERRIDES_CSWpm-template += file-with-bad-content|/usr/local|root/opt/csw/lib/perl/csw/Template.pm
CHECKPKG_OVERRIDES_CSWpm-template += file-with-bad-content|/usr/local|root/opt/csw/lib/perl/csw/Template/Config.pm
CHECKPKG_OVERRIDES_CSWpm-template += file-with-bad-content|/usr/local|root/opt/csw/lib/perl/csw/Template/Provider.pm
CHECKPKG_OVERRIDES_CSWpm-template += file-with-bad-content|/usr/local|root/opt/csw/lib/perl/csw/Template/Manual/Intro.pod
CHECKPKG_OVERRIDES_CSWpm-template += file-with-bad-content|/usr/local|root/opt/csw/lib/perl/csw/Template/Manual/Config.pod
CHECKPKG_OVERRIDES_CSWpm-template += file-with-bad-content|/usr/local|root/opt/csw/lib/perl/csw/Template/Tools/ttree.pod
CHECKPKG_OVERRIDES_CSWpm-template += file-with-bad-content|/usr/share|root/opt/csw/share/man/man3/Template::Manual::Config.3perl
CHECKPKG_OVERRIDES_CSWpm-template += file-with-bad-content|/usr/share|root/opt/csw/lib/perl/csw/Template/Manual/Config.pod

include gar/category.mk
