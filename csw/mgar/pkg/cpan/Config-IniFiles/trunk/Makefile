NAME = Config-IniFiles
VERSION = 2.66
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SHLOMIF

DESCRIPTION = A module for reading .ini-style configuration files.
define BLURB
  Config::IniFiles provides a way to have readable configuration files outside
  your Perl script. Configurations can be imported (inherited, stacked,...),
  sections can be grouped, and settings can be accessed from a tied hash.
endef

DISTFILES += COPYING
DISTFILES += CSWpm-config-inifiles.cswreleasenotes

PACKAGES = CSWpm-config-inifiles
CATALOGNAME_CSWpm-config-inifiles = pm_config_inifiles
SPKG_DESC_CSWpm-config-inifiles = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-config-inifiles = CSWpmcfginifls
CATALOGNAME_CSWpmcfginifls = pm_configinifiles

ARCHALL = 1

CHECKPKG_OVERRIDES_CSWpm-config-inifiles += file-with-bad-content|/usr/share|root/opt/csw/share/perl/csw/Config/IniFiles.pm
CHECKPKG_OVERRIDES_CSWpm-config-inifiles += file-with-bad-content|/usr/share|root/opt/csw/share/man/man3/Config::IniFiles.3perl

include gar/category.mk
