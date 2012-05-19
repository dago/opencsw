NAME = giflib
VERSION = 4.2.0
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = A library for reading and writing gif images
define BLURB
  giflib is a library for reading and writing gif images.
  It is API and ABI compatible with libungif which was in
  wide use while the LZW compression algorithm was patented.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
UPSTREAM_MASTER_SITES = http://sourceforge.net/projects/giflib/files/giflib-4.x/

VENDOR_URL = http://giflib.sourceforge.net/

# giflib no longer supported on Solaris 9 because of C99 compliance
# requirement.
# https://sourceforge.net/tracker/?func=detail&atid=631304&aid=3527787&group_id=102202
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

EXTRA_CFLAGS += -xc99

PACKAGES = CSWgiflib
SPKG_DESC_CSWgiflib = A library for reading and writing gif images
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWgiflib += CSWlibgif4
OBSOLETED_BY_CSWgiflib += CSWgiflibdoc
CATALOGNAME_CSWgiflibdoc = giflib_doc_stub

# Just docs, override for now
CHECKPKG_OVERRIDES_CSWgiflib += file-with-bad-content|/usr/local|root/opt/csw/share/doc/giflib/INSTALL

PACKAGES += CSWlibgif4
SPKG_DESC_CSWlibgif4 = A library for reading and writing GIF images, libgif.so.4
PKGFILES_CSWlibgif4 += $(call pkgfiles_lib,libgif.so.4)
OBSOLETED_BY_CSWlibgif4 += CSWgiflibrt
CATALOGNAME_CSWgiflibrt = giflib_rt_stub

PACKAGES += CSWlibungif4
SPKG_DESC_CSWlibungif4 = GIF access library, previously without compression, now a link to libgif.so.4, libungif.so.4
PKGFILES_CSWlibungif4 += $(call pkgfiles_lib,libungif.so.4)
ARCHALL_CSWlibungif4 = 1
RUNTIME_DEP_PKGS_CSWlibungif4 += CSWlibgif4
OBSOLETED_BY_CSWlibungif4 += CSWungif
CATALOGNAME_CSWungif = libungif_stub

PACKAGES += CSWlibgif-dev
SPKG_DESC_CSWlibgif-dev = Development files for libgif.so.4 and legacy libungif.so.4
PKGFILES_CSWlibgif-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibgif-dev += CSWlibgif4
RUNTIME_DEP_PKGS_CSWlibgif-dev += CSWlibungif4

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --x-includes=/usr/openwin/include
CONFIGURE_ARGS += --x-libraries=$(abspath /usr/openwin/lib/$(MM_LIBDIR))

include gar/category.mk

DOCFILES = AUTHORS BUGS COPYING ChangeLog INSTALL NEWS README TODO

post-install-modulated:
	mkdir -p $(DESTDIR)$(docdir)/giflib
	cd $(WORKSRC) && cp $(DOCFILES) $(DESTDIR)$(docdir)/giflib
	cd $(WORKSRC)/doc && cp *.html *.txt $(DESTDIR)$(docdir)/giflib
	@$(MAKECOOKIE)

post-merge:
	mkdir -p $(PKGROOT)$(libdir)
	gln -s libgif.so.4 $(PKGROOT)$(libdir)/libungif.so.4
	gln -s libgif.so $(PKGROOT)$(libdir)/libungif.so
	@$(MAKECOOKIE)
