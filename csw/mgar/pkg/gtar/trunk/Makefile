GARNAME = tar
GARVERSION = 1.25
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

BUILD_DEP_PKGS = CSWgcpio
RUNTIME_DEP_PKGS = CSWggettextrt CSWiconv CSWgcpio

NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS) --program-prefix=g
CONFIGURE_ARGS += --with-rmt=/opt/csw/libexec/grmt
TEST_SCRIPTS =

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

CHECKPKG_OVERRIDES_CSWgtar += surplus-dependency|CSWgcpio

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(prefix)/gnu
	$(foreach G,$(notdir $(wildcard $(DESTDIR)$(bindir)/*)),ln -s ../bin/$G $(DESTDIR)$(prefix)/gnu/$(patsubst g%,%,$G);)
	@$(MAKECOOKIE)

