NAME = File-Fetch
VERSION = 0.24
CATEGORIES = cpan
AUTHOR = BINGOS

DESCRIPTION = A generic file fetching mechanism
define BLURB
  File::Fetch is a generic file fetching mechanism.  It allows you to fetch
  any file pointed to by a ftp, http, file, or rsync uri by a number of
  different means.
endef

DISTFILES += COPYING

PACKAGES = CSWpmfilefetch
CATALOGNAME = pm_filefetch

ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpmipccmd CSWpmlclemktxtsimple CSWpmmodloadcond CSWpmprmscheck

SKIPTEST = 1

EXTRA_MERGE_EXCLUDE_FILES = .*\/man\/man3.* .*\/man\/man1.*

include gar/category.mk
