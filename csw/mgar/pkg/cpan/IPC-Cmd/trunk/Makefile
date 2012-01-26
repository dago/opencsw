NAME = IPC-Cmd
VERSION = 0.70
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = BINGOS

DESCRIPTION = Finding and running system commands made easy
define BLURB
  IPC::Cmd allows you to run commands, interactively if desired, platform
  independent but have them still work.
endef

DISTFILES += COPYING

PACKAGES = CSWpm-ipc-cmd
CATALOGNAME = pm_ipc_cmd 
SPKG_DESC_CSWpm-ipc-cmd = $(DESCRIPTION)
ARCHALL = 1
OBSOLETED_BY_CSWpm-ipc-cmd = CSWpmipccmd
CATALOGNAME_CSWpmipccmd = pm_ipccmd

RUNTIME_DEP_PKGS = CSWpmlclemktxtsimple CSWpmmodloadcond CSWpmprmscheck

EXTRA_MERGE_EXCLUDE_FILES = .*\/man\/man3.* .*\/man\/man1.*

include gar/category.mk
