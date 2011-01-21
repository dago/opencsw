NAME = tar
VERSION = 1.25
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
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# These two patches are from
#   http://cvs.opensolaris.org/source/xref/sfw/usr/src/cmd/gtar/Patches/
PATCHFILES += verify.diff
PATCHFILES += xgetcwd.diff

PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

PACKAGES = CSWgtar
CATALOGNAME_CSWgtar = gtar

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://www.gnu.org/software/tar/

BUILD_DEP_PKGS = CSWgcpio
RUNTIME_DEP_PKGS_CSWgtar += CSWggettextrt
RUNTIME_DEP_PKGS_CSWgtar += CSWiconv
RUNTIME_DEP_PKGS_CSWgtar += CSWgcpio

NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS) --program-prefix=g
CONFIGURE_ARGS += --with-rmt=/opt/csw/libexec/grmt
# As suggested in http://lists.gnu.org/archive/html/bug-tar/2010-11/msg00073.html
CONFIGURE_ARGS-sol5.9 += gl_cv_func_futimesat_works=yes
CONFIGURE_ARGS += $(CONFIGURE_ARGS-sol$(GAROSREL))
TEST_TARGET = check

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

CHECKPKG_OVERRIDES_CSWgtar += file-with-bad-content|/usr/local|root/opt/csw/share/info/tar.info-1

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(prefix)/gnu
	$(foreach G,$(notdir $(wildcard $(DESTDIR)$(bindir)/*)),ln -s ../bin/$G $(DESTDIR)$(prefix)/gnu/$(patsubst g%,%,$G);)
	@$(MAKECOOKIE)

