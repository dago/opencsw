NAME = CPANPLUS
VERSION = 0.9007
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = BINGOS

DESCRIPTION = API and CLI access to the CPAN mirrors
define BLURB
  The CPANPLUS library is an API to the CPAN mirrors and a collection of
  interactive shells, commandline programs, etc, that use this API.
endef

DISTFILES += COPYING

PACKAGES = CSWpmcpanplus
CATALOGNAME = pm_cpanplus

RUNTIME_DEP_PKGS += CSWpmarchiveextract CSWpmfilefetch CSWpmipccmd
RUNTIME_DEP_PKGS += CSWpmlclemktxtsimple CSWpmlogmessage CSWpmmodcorelist
RUNTIME_DEP_PKGS += CSWpmmodload CSWpmmodloadcond CSWpmmodloaded
RUNTIME_DEP_PKGS += CSWpmmoduleplug CSWpmobjaccessor CSWpmpkgconst
RUNTIME_DEP_PKGS += CSWpmprmscheck CSWpmtermui

ARCHALL = 1

SKIPTEST = 1

EXTRA_MERGE_EXCLUDE_FILES = .*\/man\/man3\/.* .*\/man\/man1\/.*

include gar/category.mk
