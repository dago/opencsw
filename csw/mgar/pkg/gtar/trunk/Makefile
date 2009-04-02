GARNAME = tar
GARVERSION = 1.22
CATEGORIES = utils

DESCRIPTION = GNU tape archiver
define BLURB
	GNU 'tar' saves many files together into a single tape or disk archive,
	and can restore individual files from the archive. It includes 
	multivolume support, the ability to archive sparse files, automatic 
	archive compression/decompression, remote archives and special features
	that allow 'tar' to be used for incremental and full backups. This 
	distribution also includes 'rmt', the remote tape server. The 'mt' tape 
	drive control program is in the GNU 'cpio' distribution. GNU 'tar' is 
	derived from John Gilmore's public domain 'tar'.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

PACKAGES = CSWgtar

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.gnu.org/software/tar/

REQUIRED_PKGS = CSWggettextrt CSWiconv

NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS) --program-prefix=g
TEST_SCRIPTS =

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

include gar/category.mk
