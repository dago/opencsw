GARNAME = tar
GARVERSION = 1.20
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
DISTFILES += $(call admfiles,CSWgtar,depend)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS) --program-prefix=g
TEST_SCRIPTS =

include gar/category.mk

post-install:
	@rm -f $(DESTDIR)$(libdir)/charset.alias
	@rm -f $(DESTDIR)$(sharedstatedir)/info/dir
	@$(MAKECOOKIE)

