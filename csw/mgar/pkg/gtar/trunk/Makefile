NAME = tar
VERSION = 1.27
CATEGORIES = utils
GARTYPE = v2

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
DISTFILES  = $(NAME)Solaris-9-an.patch

VENDOR_URL = http://www.gnu.org/software/tar/

PACKAGES = CSWgtar

BUILD_DEP_PKGS = CSWgcpio
RUNTIME_DEP_PKGS_CSWgtar += CSWlibintl8
RUNTIME_DEP_libiconv2CSWgtar += CSWiconv
RUNTIME_DEP_PKGS_CSWgtar += CSWgcpio

NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS) --program-prefix=g
CONFIGURE_ARGS += --with-rmt=/opt/csw/libexec/grmt

EXTRA_MERGE_EXCLUDE_FILES = $(libdeam
SKIPTEST ?= 1

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(prefix)/gnu
	$(foreach G,$(notdir $(wildcard $(DESTDIR)$(bindir)/*)),ln -s ../bin/$G $(DESTDIR)$(prefix)/gnu/$(patsubst g%,%,$G);