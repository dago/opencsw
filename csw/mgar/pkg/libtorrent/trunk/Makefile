GARNAME = libtorrent
GARVERSION = 0.12.6
CATEGORIES = lib

DESCRIPTION = BitTorrent library written in C++ for *nix.
define BLURB
  BitTorrent library written in C++ for *nix, with a focus on high performance and good code.
  The library differentiates itself from other implementations by transfering directly from
  file pages to the network stack. On high-bandwidth connections it is able to seed at 3 times
  the speed of the official client. 
endef

MASTER_SITES = http://libtorrent.rakshasa.no/downloads/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

#Patches mostly from http://cr.opensolaris.org/~alz/bittorrent/raw_files/new/usr/src/lib/libtorrent/

PATCHFILES = rlibtorrent-04-sunpro.diff rlibtorrent-01-madvise.diff rlibtorrent-03-dh-generate.diff
PATCHFILES += rlibtorrent-05-tracker-usable.diff work-around-UNUSED.patch more-UNUSED.patch


RUNTIME_DEP_PKGS_CSWlibtorrent += CSWosslrt
RUNTIME_DEP_PKGS_CSWlibtorrent += CSWlibsigc++rt

PACKAGES  = CSWlibtorrent
PACKAGES += CSWlibtorrentdevel
SPKG_DESC_CSWlibtorrent = BitTorrent library written in C++ for *nix
SPKG_DESC_CSWlibtorrentdevel = Header files for libtorrent

CATALOGNAME_CSWlibtorrent= libtorrent
CATALOGNAME_CSWlibtorrentdevel = libtorrent_devel

PKGFILES_CSWlibtorrentdevel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibtorrentdevel += $(docdir)/.*
PKGFILES_CSWlibtorrentdevel += .*\.h
PKGFILES_CSWlibtorrentdevel += $(sharedstatedir)/.*

#No 64bit build until libsigc++ is 64bit too
#BUILD64 = 1
CONFIGURE_ARGS = $(DIRPATHS) --enable-shared --disable-static --disable-libtool-lock --disable-debug
TEST_TARGET = check

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
