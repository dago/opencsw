NAME = Nagios-Plugin
VERSION = 0.36
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = TONVOON

DESCRIPTION = A family of perl modules to streamline writing Nagios
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE_TEXT = This module is licensed under the unknown license

PACKAGES += CSWpm-nagios-plugin
CATALOGNAME_CSWpm-nagios-plugin = pm_nagios_plugin
SPKG_DESC_CSWpm-nagios-plugin = A family of perl modules to streamline writing Nagios
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-nagios-plugin = 1
RUNTIME_DEP_PKGS_CSWpm-nagios-plugin += CSWpm-params-validate
RUNTIME_DEP_PKGS_CSWpm-nagios-plugin += CSWpm-config-tiny
RUNTIME_DEP_PKGS_CSWpm-nagios-plugin += CSWpm-math-calc-units
RUNTIME_DEP_PKGS_CSWpm-nagios-plugin += CSWpm-class-accessor

# These are just docs now
CHECKPKG_OVERRIDES_CSWpm-nagios-plugin += file-with-bad-content|/usr/local|root/opt/csw/share/perl/csw/Nagios/Plugin/Config.pm
CHECKPKG_OVERRIDES_CSWpm-nagios-plugin += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/Nagios::Plugin::Config.3perl

# Configuration pathes:
#   /etc/nagios /usr/local/nagios/etc /usr/local/etc/nagios /etc/opt/nagios
#   /etc /usr/local/etc /etc/opt
# my @NAGIOS_CONFIG_PATH = qw(/etc/nagios /usr/local/nagios/etc /usr/local/etc/nagios /etc/opt/nagios);
# Config paths not ending in nagios (search for $FILENAME2)
# my @CONFIG_PATH = qw(/etc /usr/local/etc /etc/opt);

REINPLACEMENTS += nagios_config_path
REINPLACE_MATCH_nagios_config_path = /etc/nagios /usr/local/nagios/etc /usr/local/etc/nagios /etc/opt/nagios
REINPLACE_WITH_nagios_config_path = $(sysconfdir)/nagios
REINPLACE_FILES_nagios_config_path += lib/Nagios/Plugin/Config.pm

REINPLACEMENTS += config_path
REINPLACE_MATCH_config_path = /etc /usr/local/etc /etc/opt
REINPLACE_WITH_config_path = $(sysconfdir)
REINPLACE_FILES_config_path += lib/Nagios/Plugin/Config.pm

include gar/category.mk
