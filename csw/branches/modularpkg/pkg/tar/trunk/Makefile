GARNAME = tar
GARVERSION = 1.13.25
CATEGORIES = utils

DESCRIPTION = GNU tar
define BLURB
  GNU 'tar' saves many files together into a single tape or disk archive,
  and can restore individual files from the archive. It includes multivolume
  support, the ability to archive sparse files, automatic archive
  compression/decompression, remote archives and special features that allow
  'tar' to be used for incremental and full backups. It also includes 'rmt',
  the remote tape server (the 'mt' tape drive control program is in GNU 'cpio').
endef

MASTER_SITES = ftp://alpha.gnu.org/gnu/tar/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

# tar is very poorly behaved!  It prepends prefix onto things
# like bindir!  This is not the way GNU packages should behave!
# -NickM
NODIRPATHS = --prefix

TEST_TARGET = check

include gar/category.mk
