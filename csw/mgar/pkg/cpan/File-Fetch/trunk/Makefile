NAME = File-Fetch
VERSION = 0.32
CATEGORIES = cpan
AUTHOR = BINGOS

DESCRIPTION = A generic file fetching mechanism
define BLURB
  File::Fetch is a generic file fetching mechanism.  It allows you to fetch
  any file pointed to by a ftp, http, file, or rsync uri by a number of
  different means.
endef

DISTFILES += COPYING

PACKAGES = CSWpm-file-fetch
CATALOGNAME = pm_file_fetch
SPKG_DESC_CSWpm-file-fetch = $(DESCRIPTION)
OBSOLETES_CSWpm-file-fetch = CSWpmfilefetch
CATALOGNAME_CSWpmfilefetch = pm_filefetch

ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpmipccmd CSWpmlclemktxtsimple CSWpmmodloadcond CSWpmprmscheck

SKIPTEST = 1

EXTRA_MERGE_EXCLUDE_FILES = .*\/man\/man3.* .*\/man\/man1.*

include gar/category.mk
