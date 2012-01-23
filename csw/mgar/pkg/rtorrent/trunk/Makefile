NAME = rtorrent
VERSION = 0.8.6
CATEGORIES = apps

DESCRIPTION = Client for Unix, based on libtorrent 
define BLURB
endef

MASTER_SITES = http://libtorrent.rakshasa.no/downloads/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# Patches mostly from http://cr.opensolaris.org/~alz/bittorrent/raw_files/new/usr/src/cmd/rtorrent/
PATCHFILES = rtorrent-01-solaris.diff 0001-curl_get.patch rtorrent-04-sunpro.diff 
PATCHFILES += 0001-scgi_task.cc.patch rtorrent-05-sunpro-crash.diff work-around-UNUSED.patch 0001-build-fixes.patch
PATCHFILES += 0001-more-build-fixes.patch 0001-more-build-fixes2.patch

EXTRA_CXXFLAGS = -D_RWSTD_ALLOCATOR -mt
EXTRA_LDFLAGS  = -Wl,-zignore -Wl,-zcombreloc -Wl,-Bdirect

CONFIGURE_ARGS = $(DIRPATHS) --disable-debug
include gar/category.mk

pre-configure-modulated:
	cd $(WORKSRC) && aclocal-1.10 -I scripts && \
  automake-1.10 --gnu && autoconf

	$(MAKECOOKIE)


#post-configure-modulated:
#	perl -pi -e 's,\|-xarch=,|-norunpath|-xarch=,' $(WORKSRC)/libtool
#	@$(MAKECOOKIE)
