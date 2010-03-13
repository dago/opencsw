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

PACKAGES = CSWgiflib CSWgiflibrt CSWgiflibrtx11 CSWgiflibdoc CSWungif

CATALOGNAME_CSWgiflib = giflib
CATALOGNAME_CSWgiflibrt = giflib_rt
CATALOGNAME_CSWgiflibrtx11 = giflib_rt_x11
CATALOGNAME_CSWgiflibdoc = giflib_doc
CATALOGNAME_CSWungif = libungif

SPKG_DESC_CSWgiflib = A library for reading and writing gif images
SPKG_DESC_CSWgiflibrt = giflib runtime libraries (minimal alternative without X11 support)
SPKG_DESC_CSWgiflibrtx11 = giflib runtime libraries (full alternative with support for CSW X11)
SPKG_DESC_CSWgiflibdoc = giflib documentation
SPKG_DESC_CSWungif = Stub which links to giflib now the patent is dropped

SPKG_SOURCEURL = http://giflib.sourceforge.net/

BUILD_DEP_PKGS = CSWlibicedevel CSWlibsmdevel CSWlibx11devel

RUNTIME_DEP_PKGS_CSWgiflibrt =
RUNTIME_DEP_PKGS_CSWgiflibrtx11 = CSWlibice CSWlibsm CSWlibx11
RUNTIME_DEP_PKGS_CSWgiflib = CSWgiflibrt
RUNTIME_DEP_PKGS_CSWungif = CSWgiflib

EXTRA_MODULATORS = FEATURES
MODULATIONS_FEATURES = nox11 cswx11

EXTRA_INC = $(prefix)/X11/include
EXTRA_LIB = $(prefix)/X11/lib
EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_ARGS_nox11   = --disable-x11
CONFIGURE_ARGS_cswx11  = --x-include=$(prefix)/X11/include
CONFIGURE_ARGS_cswx11 += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(FEATURES))

TEST_TARGET = check

EXTRA_PAX_ARGS-32 = -s ",\(\.$(libdir)/libgif\)\(\.so\.4\.1\.6\),\1-$(FEATURES)\2,p"
EXTRA_PAX_ARGS-64 = -s ",\.$(libdir)/libgif\(\.so\.4\.1\.6\),.$(libdir_install)/$(ISA)/libgif-$(FEATURES)\1,p"
EXTRA_PAX_ARGS += $(EXTRA_PAX_ARGS-$(MEMORYMODEL))

# We don't want 64 bit executables as they gain no speed
NOISAEXEC = 1

MERGE_SCRIPTS_isa-default-features-nox11 = copy-all
MERGE_SCRIPTS_isa-default64-features-nox11 = copy-relocated-only
MERGE_DIRS_isa-default64-features-nox11 = $(libdir)
MERGE_SCRIPTS_isa-default-features-cswx11 = copy-only
MERGE_DIRS_isa-default-features-cswx11 = $(libdir)
MERGE_SCRIPTS_isa-default64-features-cswx11 = copy-relocated-only
MERGE_DIRS_isa-default64-features-cswx11 = $(libdir)

ARCHALL_CSWgiflibdoc = 1
ARCHALL_CSWungif = 1

PKGFILES_CSWgiflibrt = .*/libgif-nox11\..*
PKGFILES_CSWgiflibrtx11 = .*/libgif-cswx11\..*
PKGFILES_CSWgiflibdoc = $(PKGFILES_DOC)
PKGFILES_CSWungif = .*/libungif\..*

ALTERNATIVES_CSWgiflibrt = nox11
ALTERNATIVES_CSWgiflibrtx11 = cswx11

ALTERNATIVE_nox11  = $(libdir)/libgif.so.4.1.6 giflib $(libdir)/libgif-nox11.so.4.1.6 100
ALTERNATIVE_nox11 += $(libdir)/$(ISA_DEFAULT64)/libgif.so.4.1.6 giflib64 $(libdir)/$(ISA_DEFAULT64)/libneon-nox11.so.4.1.6

ALTERNATIVE_cswx11  = $(libdir)/libgif.so.4.1.6 giflib $(libdir)/libgif-cswx11.so.4.1.6 100
ALTERNATIVE_cswx11 += $(libdir)/$(ISA_DEFAULT64)/libgif.so.4.1.6 giflib64 $(libdir)/$(ISA_DEFAULT64)/libneon-cswx11.so.4.1.6

include gar/category.mk

DOCFILES = AUTHORS BUGS COPYING ChangeLog DEVELOPERS INSTALL NEWS ONEWS README TODO

post-install-modulated:
	@mkdir -p $(DESTDIR)$(docdir)/giflib
	cd $(WORKSRC) && cp $(DOCFILES) $(DESTDIR)$(docdir)/giflib
	cd $(WORKSRC)/doc && cp *.html *.png *.txt $(DESTDIR)$(docdir)/giflib
	@$(MAKECOOKIE)

post-merge:
	gln -s libgif.so.4 $(PKGROOT)$(libdir)/libungif.so.4
	gln -s libgif.so $(PKGROOT)$(libdir)/libungif.so
	@$(MAKECOOKIE)
