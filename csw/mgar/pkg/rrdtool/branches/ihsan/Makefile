NAME = rrdtool
VERSION = 1.4.3
CATEGORIES = utils

DESCRIPTION = Time-series data logging and graphing.
define BLURB
  RRDtool is basically the time-series graphing and data storage/management
  component of MRTG, broken out and `done right'. `done right' means that
  RRDtool is magnitudes faster than MRTG and extremely configurable.
endef

MASTER_SITES = http://oss.oetiker.ch/$(NAME)/pub/
DISTFILES = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWrrd
CATALOGNAME = rrdtool

PACKAGING_PLATFORMS =  solaris9-sparc solaris9-i386

RUNTIME_DEP_PKGS += CSWggettextrt
RUNTIME_DEP_PKGS += CSWglib2
RUNTIME_DEP_PKGS += CSWlibcairo
RUNTIME_DEP_PKGS += CSWpango
RUNTIME_DEP_PKGS += CSWperl
RUNTIME_DEP_PKGS += CSWruby
RUNTIME_DEP_PKGS += CSWpython
RUNTIME_DEP_PKGS += CSWlibxml2

BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS)
BUILD_DEP_PKGS += CSWlibpthreadstubs
BUILD_DEP_PKGS += CSWlibxaudevel
BUILD_DEP_PKGS += CSWlibxcbdevel
BUILD_DEP_PKGS += CSWpangodevel
BUILD_DEP_PKGS += CSWlibcairodevel
BUILD_DEP_PKGS += CSWglib2devel
BUILD_DEP_PKGS += CSWxproto
BUILD_DEP_PKGS += CSWlibxrenderdevel
BUILD_DEP_PKGS += CSWx11renderproto
BUILD_DEP_PKGS += CSWx11kbproto
BUILD_DEP_PKGS += CSWpython-devel
BUILD_DEP_PKGS += CSWrubydev

EXTRA_INC = $(prefix)/include/cairo
EXTRA_INC += $(prefix)/include/libxml2
EXTRA_INC += $(prefix)/X11/include

EXTRA_LIB = $(prefix)/X11/lib

EXTRA_PKG_CONFIG_DIRS = $(prefix)/X11/lib

EXTRA_SOS_LD_FLAGS = -L$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
EXTRA_SOS_LD_OPTIONS = -R$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --docdir=$(sharedstatedir)/doc/$(NAME)
CONFIGURE_ARGS += --disable-lua 
CONFIGURE_ARGS += --enable-python
CONFIGURE_ARGS += --enable-ruby
CONFIGURE_ARGS += --with-ruby-options=CFLAGS=
CONFIGURE_ARGS += --enable-perl
CONFIGURE_ARGS += --with-perl-options=INSTALLDIRS=vendor
CONFIGURE_ARGS += --x-includes=$(prefix)/X11/include
CONFIGURE_ARGS += --x-libraries=$(abspath $(prefix)/X11/lib/$(MM_LIBDIR))
CONFIGURE_ARGS += --with-libintl-prefix=$(libdir)

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

TEST_TARGET = check

PATCHFILES += patch-src-Makefile.in
PATCHFILES += patch-src-rrd_open.c
PATCHFILES += patch-bindings-Makefile.in
PATCHFILES += patch-bindings-ruby-extconf.rb
PATCHFILES += patch-bindings-perl-piped-Makefile.PL
PATCHFILES += patch-bindings-perl-shared-Makefile.PL

BUILD64 = 1
NOISAEXEC = 1
MERGE_DIRS_isa-sparcv9 = $(libdir)
MERGE_DIRS_isa-amd64 = $(libdir)

STRIP_LIBTOOL = 1

CHECKPKG_OVERRIDES_CSWrrd += bad-rpath-entry|/home/ihsan/mgar/pkg/rrdtool/branches/ihsan/work/solaris9-sparc/install-isa-sparcv8/opt/csw/lib

include gar/category.mk
# ugly fix to fix doc path
#post-install-modulated:
	#echo "  ==> Fixing doc path"
	#mv $(DESTDIR)$(prefix)/share/doc/rrdtool-$(VERSION) $(DESTDIR)$(prefix)/share/doc/rrdtool

pre-build-modulated:
	echo "  ==> Adding math function round()"
	cp $(FILEDIR)/s_round.c $(WORKSRC)/src
	cp $(FILEDIR)/s_round.h $(WORKSRC)/src
	@$(MAKECOOKIE)

post-patch-isa-amd64:
	@# since our perl/python is 32bit, we need to patch away the build
	echo "  ==> Removing perl/python module"
	gpatch -d$(WORKSRC) -p1 -F2 < $(FILEDIR)/patch-64-Makefile.in
	gpatch -d$(WORKSRC) -p1 -F2 < $(FILEDIR)/patch-64-bindings-Makefile.in
	@$(MAKECOOKIE)

post-patch-isa-sparcv9:
	@# since our perl/python is 32bit, we need to patch away the build
	echo "  ==> Removing perl/python module"
	gpatch -d$(WORKSRC) -p1 -F2 < $(FILEDIR)/patch-64-Makefile.in
	gpatch -d$(WORKSRC) -p1 -F2 < $(FILEDIR)/patch-64-bindings-Makefile.in
	@$(MAKECOOKIE)
