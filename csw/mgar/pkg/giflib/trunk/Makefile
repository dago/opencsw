GARNAME = giflib
GARVERSION = 4.1.6
CATEGORIES = lib

DESCRIPTION = A library for reading and writing gif images
define BLURB
  giflib is a library for reading and writing gif images.
  It is API and ABI compatible with libungif which was in
  wide use while the LZW compression algorithm was patented.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

PACKAGES = CSWgiflib CSWgiflibrt CSWx11giflib CSWx11giflibrt CSWgiflibdoc CSWungif

CATALOGNAME_CSWgiflib = giflib
CATALOGNAME_CSWgiflibrt = giflib_rt
CATALOGNAME_CSWx11giflib = x11_giflib
CATALOGNAME_CSWx11giflibrt = x11_giflib_rt
CATALOGNAME_CSWgiflibdoc = giflib_doc
CATALOGNAME_CSWungif = libungif

SPKG_DESC_CSWgiflib = A library for reading and writing gif images
SPKG_DESC_CSWgiflibrt = Runtime library for giflib (Sun X11 binding)
SPKG_DESC_CSWx11giflib = Package for giflib bound against OpenCSW X11
SPKG_DESC_CSWx11giflibrt = Runtime libraries for giflib bound against OpenCSW X11
SPKG_DESC_CSWgiflibdoc = Documentation for giflib
SPKG_DESC_CSWungif = Stub which links to giflib now the patent is dropped

SPKG_SOURCEURL = http://giflib.sourceforge.net/

BUILD_DEP_PKGS = CSWlibicedevel CSWlibsmdevel CSWlibx11devel

RUNTIME_DEP_PKGS_CSWx11giflibrt = CSWlibice CSWlibsm CSWlibx11
RUNTIME_DEP_PKGS_CSWx11giflib = CSWlibice CSWlibsm CSWlibx11 CSWx11giflibrt
RUNTIME_DEP_PKGS_CSWgiflib = CSWgiflibrt
RUNTIME_DEP_PKGS_CSWungif = CSWgiflib


EXTRA_MODULATORS = X11
MODULATIONS_X11 = sunwx11 cswx11

# EXTRA_INC_cswx11 = $(prefix)/X11/include
# EXTRA_LIB_cswx11 = $(prefix)/X11/lib
# EXTRA_PKG_CONFIG_DIRS_cswx11 = $(prefix)/X11/lib

# EXTRA_INC = $(EXTRA_INC_$(X11))
# EXTRA_LIB = $(EXTRA_LIB_$(X11))
# EXTRA_PKG_CONFIG_DIRS = $(EXTRA_PKG_CONFIG_DIRS_$(X11))

STRIP_LIBTOOL = 1

BUILD64 = 1

prefix_cswx11 = $(BUILD_PREFIX)/X11
prefix = $(or $(prefix_$(X11)),$(BUILD_PREFIX))

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_ARGS_sunwx11  = --x-includes=/usr/openwin/include
CONFIGURE_ARGS_sunwx11 += --x-libraries=$(abspath /usr/openwin/lib/$(MM_LIBDIR))
CONFIGURE_ARGS_cswx11  = --x-include=$(prefix)/include
CONFIGURE_ARGS_cswx11 += --x-libraries=$(abspath $(prefix)/lib/$(MM_LIBDIR))
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(X11))

TEST_TARGET = check

# We don't want 64 bit executables as they gain no speed
NOISAEXEC = 1

MERGE_SCRIPTS_isa-default-x11-sunwx11 = copy-all
MERGE_SCRIPTS_isa-default64-x11-sunwx11 = copy-relocated-only
MERGE_DIRS_isa-default64-x11-sunwx11 = $(libdir)
MERGE_SCRIPTS_isa-default-x11-cswx11 = copy-only
MERGE_DIRS_isa-default-x11-cswx11 = $(libdir) $(bindir)
MERGE_SCRIPTS_isa-default64-x11-cswx11 = copy-relocated-only
MERGE_DIRS_isa-default64-x11-cswx11 = $(libdir)

ARCHALL_CSWgiflibdoc = 1
ARCHALL_CSWungif = 1

PKGFILES_CSWgiflibrt = $(call baseisadirs,$(libdir),libgif\.so.*)
PKGFILES_CSWx11giflibrt = $(call baseisadirs,$(prefix)/X11/lib,[^/]*\.so(\.\d+)*)
PKGFILES_CSWx11giflib = $(prefix)/X11/bin/.*
PKGFILES_CSWgiflibdoc = $(PKGFILES_DOC)
PKGFILES_CSWungif = .*/libungif\..*

CHECKPKG_OVERRIDES_CSWungif += surplus-dependency|CSWgiflib
CHECKPKG_OVERRIDES_CSWgiflibrt += bad-rpath-entry|/usr/openwin/lib/64|opt/csw/lib/sparcv9/libgif.so.4.1.6
CHECKPKG_OVERRIDES_CSWgiflibrt += linked-against-discouraged-library|libgif.so.4.1.6|libX11.so.4

include gar/category.mk

DOCFILES = AUTHORS BUGS COPYING ChangeLog DEVELOPERS INSTALL NEWS ONEWS README TODO

post-install-modulated:
	mkdir -p $(DESTDIR)$(docdir)/giflib
	cd $(WORKSRC) && cp $(DOCFILES) $(DESTDIR)$(docdir)/giflib
	cd $(WORKSRC)/doc && cp *.html *.png *.txt $(DESTDIR)$(docdir)/giflib
	@$(MAKECOOKIE)

post-merge:
	mkdir -p $(PKGROOT)$(libdir)
	gln -s libgif.so.4 $(PKGROOT)$(libdir)/libungif.so.4
	gln -s libgif.so $(PKGROOT)$(libdir)/libungif.so
	@$(MAKECOOKIE)
