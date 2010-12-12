NAME = IPC-Cmd
VERSION = 0.64
CATEGORIES = cpan
AUTHOR = BINGOS

DESCRIPTION = Finding and running system commands made easy
define BLURB
  IPC::Cmd allows you to run commands, interactively if desired, platform
  independent but have them still work.
endef

DISTFILES += COPYING

PACKAGES = CSWpmipccmd
CATALOGNAME = pm_ipccmd 
ARCHALL = 1

RUNTIME_DEP_PKGS = CSWpmlclemktxtsimple CSWpmmodloadcond CSWpmprmscheck

EXTRA_MERGE_EXCLUDE_FILES = .*\/man\/man3.* .*\/man\/man1.*

include gar/category.mk
