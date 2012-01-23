NAME = libtorrent
VERSION = 0.12.6
CATEGORIES = lib

DESCRIPTION = BitTorrent library written in C++ for *nix.
define BLURB
  BitTorrent library written in C++ for *nix, with a focus on high performance and good code.
  The library differentiates itself from other implementations by transfering directly from
  file pages to the network stack. On high-bandwidth connections it is able to seed at 3 times
  the speed of the official client. 
endef

MASTER_SITES = http://libtorrent.rakshasa.no/downloads/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# Patches from http://cr.opensolaris.org/~alz/bittorrent/raw_files/new/usr/src/lib/libtorrent/
PATCHFILES = rlibtorrent-04-sunpro.diff rlibtorrent-01-madvise.diff rlibtorrent-03-dh-generate.diff
PATCHFILES += rlibtorrent-05-tracker-usable.diff

PATCHFILES += 0001-Ignore-__UNUSED.patch

BUILD_DEP_pkgs = CSWossldevel CSWlibsigc++devel

PACKAGES  = CSWlibtorrent CSWlibtorrentdevel

CATALOGNAME_CSWlibtorrent      = libtorrent
CATALOGNAME_CSWlibtorrentdevel = libtorrent_devel

SPKG_DESC_CSWlibtorrent      = BitTorrent library written in C++ for *nix
SPKG_DESC_CSWlibtorrentdevel = Development files for libtorrent

RUNTIME_DEP_PKGS_CSWlibtorrent      = CSWosslrt CSWlibsigc++
RUNTIME_DEP_PKGS_CSWlibtorrentdevel = CSWlibtorrent

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS) --enable-shared --disable-static --disable-libtool-lock --disable-debug

PKGFILES_CSWlibtorrentdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibtorrentdevel += $(docdir)/.*
PKGFILES_CSWlibtorrentdevel += .*\.h
PKGFILES_CSWlibtorrentdevel += $(sharedstatedir)/.*

CHECKPKG_OVERRIDES_CSWlibtorrentdevel += surplus-dependency|CSWlibtorrent

include gar/category.mk

pre-configure-modulated:
#	cd $(WORKSRC) && aclocal-1.10 -I./scripts -I. && autoheader \
# && libtoolize --automake --copy --force && automake-1.10 && autoconf
	cd $(WORKSRC) && aclocal-1.10 -I scripts && \
  automake-1.10 --gnu && autoconf

	$(MAKECOOKIE)


post-configure-modulated:
	perl -pi -e 's,\|-xarch=,|-norunpath|-xarch=,' $(WORKSRC)/libtool
	@$(MAKECOOKIE)
