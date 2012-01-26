# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! csync2 uses a GNU-extension which isn't available on Solaris
#   "action.c", line 47: undefined symbol: FNM_LEADING_DIR
#   Might be possible to use the gnulib fnmatch-gnu module as a replacement
#   http://bugs.opensolaris.org/bugdatabase/view_bug.do;jsessionid=9fb51afbd594902d6b0fe775834d?bug_id=6721185
# ! csync2 uses scandir, not available on Solaris, but available via gnulib
#
NAME = csync2
VERSION = 1.34
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Keeps files across multiple (cluster) hosts in sync
define BLURB
  Csync2 is a cluster synchronization tool. It can be used to keep files on
  multiple hosts in a cluster in sync. Csync2 can handle complex setups with
  much more than just 2 hosts, handle file deletions and can detect conflicts.
   
  It is expedient for HA-clusters, HPC-clusters, COWs and server farms. If
  you are looking for a tool to sync your laptop with your workstation, you
  better have a look at Unison (http://www.cis.upenn.edu/~bcpierce/unison/)
  too.
endef

MASTER_SITES = http://oss.linbit.com/csync2/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
