NAME = Apache-Test
VERSION = 1.38
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = PHRED

DESCRIPTION = Test.pm wrapper with helpers for testing Apache
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

PACKAGES += CSWpm-apache-test
CATALOGNAME_CSWpm-apache-test = pm_apache_test
SPKG_DESC_CSWpm-apache-test = Test.pm wrapper with helpers for testing Apache
ARCHALL_CSWpm-apache-test = 1
OBSOLETED_BY_CSWpm-apache-test += CSWap2modperl
CATALOGNAME_CSWap2modperl = ap2_modperl_stub

# These are probably ok
CHECKPKG_OVERRIDES_CSWpm-apache-test += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/Apache::TestMB.3perl
CHECKPKG_OVERRIDES_CSWpm-apache-test += file-with-bad-content|/usr/local|root/opt/csw/share/perl/csw/Apache/TestBuild.pm
CHECKPKG_OVERRIDES_CSWpm-apache-test += file-with-bad-content|/usr/local|root/opt/csw/share/perl/csw/Apache/TestMB.pm

include gar/category.mk
