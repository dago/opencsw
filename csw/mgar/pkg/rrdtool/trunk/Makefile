NAME = rrdtool
VERSION = 1.4.4
CATEGORIES = utils

DESCRIPTION = Time-series data logging and graphing
define BLURB
  RRDtool is basically the time-series graphing and data storage/management
  component of MRTG, broken out and `done right'. `done right' means that
  RRDtool is magnitudes faster than MRTG and extremely configurable.
endef

MASTER_SITES = http://oss.oetiker.ch/$(NAME)/pub/
DISTFILES = $(NAME)-$(VERSION).tar.gz

# Use patch until this is fixed:
#   http://oss.oetiker.ch/rrdtool-trac/ticket/284
PATCHFILES += patch-bindings-ruby-extconf.rb

# Make sure to link against libperl.so to make shared libraries self-contained.
PATCHFILES += patch-bindings-perl-piped-Makefile.PL
PATCHFILES += patch-bindings-perl-shared-Makefile.PL

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWrrd CSWrrdtool CSWrrdtool-devel CSWlibrrd4 CSWpm-rrdtool CSWpy-rrdtool CSWrb-rrdtool

CATALOGNAME_CSWrrd = rrd
CATALOGNAME_CSWrrdtool = rrdtool
CATALOGNAME_CSWrrdtool-devel = rrdtool_devel
CATALOGNAME_CSWlibrrd4 = librrd4
CATALOGNAME_CSWpm-rrdtool = pm_rrdtool
CATALOGNAME_CSWpy-rrdtool = py_rrdtool
CATALOGNAME_CSWrb-rrdtool = rb_rrdtool

SPKG_DESC_CSWrrd = Stub package as contents now moved to CSWrrdtool
SPKG_DESC_CSWrrdtool = $(DESCRIPTION)
SPKG_DESC_CSWrrdtool-devel = Development Files for RRDTool
SPKG_DESC_CSWlibrrd4 = Runtime libraries for RRDtool providing librrd_th.so.4
SPKG_DESC_CSWpm-rrdtool = RRDs: Access RRDtool as a shared module (part of RRDtool)
SPKG_DESC_CSWpy-rrdtool = Python egg for RRD access (part of RRDtool)
SPKG_DESC_CSWrb-rrdtool = Ruby binding for RRD access (part of RRDtool)

RUNTIME_DEP_PKGS_CSWrrd = CSWrrdtool CSWpm-rrdtool CSWpy-rrdtool CSWrb-rrdtool
RUNTIME_DEP_PKGS_CSWrrdtool = CSWglib2 CSWpango CSWggettextrt CSWlibxml2 CSWlibcairo
RUNTIME_DEP_PKGS_CSWrrdtool += CSWlibrrd4
RUNTIME_DEP_PKGS_CSWrrdtool-devel = CSWlibrrd4
RUNTIME_DEP_PKGS_CSWlibrrd4 += CSWggettextrt CSWglib2 CSWlibcairo CSWpango CSWlibxml2
RUNTIME_DEP_PKGS_CSWpm-rrdtool += CSWperl
RUNTIME_DEP_PKGS_CSWpm-rrdtool += CSWlibrrd4
RUNTIME_DEP_PKGS_CSWpy-rrdtool += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-rrdtool += CSWlibrrd4
RUNTIME_DEP_PKGS_CSWpy-rrdtool += CSWggettextrt
RUNTIME_DEP_PKGS_CSWrb-rrdtool += CSWlibruby1
RUNTIME_DEP_PKGS_CSWrb-rrdtool += CSWlibrrd4

BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS_CSWlibrrd4)
BUILD_DEP_PKGS += CSWpangodevel CSWlibcairodevel CSWglib2devel
BUILD_DEP_PKGS += CSWperl
BUILD_DEP_PKGS += CSWpython-devel
BUILD_DEP_PKGS += CSWrubydev

EXTRA_INC = $(prefix)/include/cairo
EXTRA_INC += $(prefix)/include/libxml2

EXTRA_LINKER_FLAGS = -lintl

BUILD64 = 1
NOISAEXEC = 1
STRIP_LIBTOOL = 1

CONFIGURE_ARGS_32 = --enable-python --enable-ruby --with-ruby-options=CFLAGS= --enable-perl --with-perl-options=INSTALLDIRS=vendor
CONFIGURE_ARGS_64 = --disable-python --disable-ruby --disable-perl

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --docdir=$(sharedstatedir)/doc/$(NAME)
CONFIGURE_ARGS += --disable-lua --disable-tcl
CONFIGURE_ARGS += --with-libintl-prefix=$(libdir)
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(MEMORYMODEL))

TEST_TARGET = check

MERGE_DIRS_isa-extra = $(libdir)
MERGE_SCRIPTS_isa-extra = copy-relocated-only copy-config-only
EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod .*/\.packlist
EXTRA_PAX_ARGS += -s ',^\.$(docdir)/$(NAME)-$(VERSION),.$(BUILD_PREFIX)/share/doc/$(CATALOGNAME),'

ARCHALL_CSWrrd = 1

PKGFILES_CSWrrd = NOFILES
PKGFILES_CSWrrdtool-devel = $(PKGFILES_DEVEL)
PKGFILES_CSWlibrrd4 = $(PKGFILES_RT)
PKGFILES_CSWpm-rrdtool += $(libdir)/perl/.*
PKGFILES_CSWpm-rrdtool += $(sharedstatedir)/perl/.*
PKGFILES_CSWpm-rrdtool += $(sharedstatedir)/rrdtool/examples/.*
PKGFILES_CSWpm-rrdtool += .*\.3perl
PKGFILES_CSWpy-rrdtool = $(libdir)/python/.*
PKGFILES_CSWrb-rrdtool = $(libdir)/ruby/.*

# Make legacy package depend on all new ones
CHECKPKG_OVERRIDES_CSWrrd += surplus-dependency|CSWpm-rrdtool
CHECKPKG_OVERRIDES_CSWrrd += surplus-dependency|CSWpy-rrdtool
CHECKPKG_OVERRIDES_CSWrrd += surplus-dependency|CSWrb-rrdtool
CHECKPKG_OVERRIDES_CSWrrd += surplus-dependency|CSWrrdtool

# These libraries always come in pairs, bundle them also
CHECKPKG_OVERRIDES_CSWlibrrd4 += shared-lib-pkgname-mismatch|file=opt/csw/lib/librrd_th.so.4.1.4|soname=librrd_th.so.4|pkgname=CSWlibrrd4|expected=CSWlibrrd-th4
CHECKPKG_OVERRIDES_CSWlibrrd4 += shared-lib-pkgname-mismatch|file=opt/csw/lib/sparcv9/librrd_th.so.4.1.4|soname=librrd_th.so.4|pkgname=CSWlibrrd4|expected=CSWlibrrd-th4

include gar/category.mk

