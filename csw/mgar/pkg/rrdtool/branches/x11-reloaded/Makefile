GARNAME = rrdtool
GARVERSION = 1.4.3
CATEGORIES = utils

DESCRIPTION = Time-series data logging and graphing
define BLURB
  RRDtool is basically the time-series graphing and data storage/management
  component of MRTG, broken out and `done right'. `done right' means that
  RRDtool is magnitudes faster than MRTG and extremely configurable.
endef

MASTER_SITES = http://oss.oetiker.ch/$(GARNAME)/pub/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

PATCHFILES += patch-src-Makefile.in
PATCHFILES += patch-src-rrd_open.c
PATCHFILES += patch-bindings-Makefile.in
PATCHFILES += patch-bindings-ruby-extconf.rb
PATCHFILES += patch-bindings-perl-piped-Makefile.PL
PATCHFILES += patch-bindings-perl-shared-Makefile.PL

PATCHFILES += 0001-Fix-isinf.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWrrd CSWrrdrt CSWpmrrd CSWpy-rrdtool CSWrbrrd

CATALOGNAME_CSWrrd = rrdtool
CATALOGNAME_CSWrrdrt = rrdtool_rt
CATALOGNAME_CSWpmrrd = pm_rrd
CATALOGNAME_CSWpy-rrdtool = py_rrdtool
CATALOGNAME_CSWrbrrd = rb_rrd

SPKG_DESC_CSWrrd = $(DESCRIPTION)
SPKG_DESC_CSWrrdrt = Runtime libraries for RRDtool
SPKG_DESC_CSWpmrrd = RRDs: Access RRDtool as a shared module (part of RRDtool)
SPKG_DESC_CSWpy-rrdtool = Python egg for RRD access (part of RRDtool)
SPKG_DESC_CSWrbrrd = Ruby binding for RRD access (part of RRDtool)

RUNTIME_DEP_PKGS_CSWrrd = CSWrrdrt CSWglib2 CSWpango CSWggettextrt CSWlibxml2 CSWlibcairo
RUNTIME_DEP_PKGS_CSWrrdrt += CSWggettextrt CSWglib2 CSWlibcairo CSWpango CSWlibxml2
RUNTIME_DEP_PKGS_CSWpmrrd = CSWperl CSWrrdrt
RUNTIME_DEP_PKGS_CSWpy-rrdtool = CSWpython CSWrrdrt
RUNTIME_DEP_PKGS_CSWrbrrd = CSWruby CSWrrdrt

BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS_CSWrrdrt)
BUILD_DEP_PKGS += CSWpangodevel CSWlibcairodevel CSWglib2devel
BUILD_DEP_PKGS += CSWperl
BUILD_DEP_PKGS += CSWpython-devel
BUILD_DEP_PKGS += CSWrubydev

EXTRA_INC = $(prefix)/include/cairo
EXTRA_INC += $(prefix)/include/libxml2

BUILD64 = 1
NOISAEXEC = 1
STRIP_LIBTOOL = 1

CONFIGURE_ARGS_32 = --enable-python --enable-ruby --with-ruby-options=CFLAGS= --enable-perl --with-perl-options=INSTALLDIRS=vendor
CONFIGURE_ARGS_64 = --disable-python --disable-ruby --disable-perl

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --docdir=$(sharedstatedir)/doc/$(GARNAME)
CONFIGURE_ARGS += --disable-lua --disable-tcl
CONFIGURE_ARGS += --with-libintl-prefix=$(libdir)
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(MEMORYMODEL))

TEST_TARGET = check

MERGE_DIRS_isa-extra = $(bindir)
MERGE_SCRIPTS_isa-extra = copy-relocated-only copy-config-only
EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod .*/\.packlist
EXTRA_PAX_ARGS += -s ',^\.$(docdir)/$(GARNAME)-$(GARVERSION),.$(BUILD_PREFIX)/share/doc/$(CATALOGNAME),'

PKGFILES_CSWrrdrt = $(PKGFILES_RT)
PKGFILES_CSWpmrrd = $(libdir)/perl/.* $(sharedstatedir)/perl/.* .*\.3perl
PKGFILES_CSWpy-rrdtool = $(libdir)/python/.*
PKGFILES_CSWrbrrd = $(libdir)/ruby/.*

CHECKPKG_OVERRIDES_CSWrrd += soname-not-found|libm.so.2|is|needed|by|opt/csw/bin/amd64/rrdcached
CHECKPKG_OVERRIDES_CSWrrd += soname-not-found|libm.so.2|is|needed|by|opt/csw/bin/amd64/rrdcgi
CHECKPKG_OVERRIDES_CSWrrd += soname-not-found|libm.so.2|is|needed|by|opt/csw/bin/amd64/rrdtool
CHECKPKG_OVERRIDES_CSWrrd += soname-not-found|libm.so.2|is|needed|by|opt/csw/bin/amd64/rrdupdate

CHECKPKG_OVERRIDES_CSWrrd += missing-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWrrd += surplus-dependency|CSWrrdrt

CHECKPKG_OVERRIDES_CSWpy-rrdtool += missing-dependency|CSWrrd
CHECKPKG_OVERRIDES_CSWpy-rrdtool += surplus-dependency|CSWrrdrt

CHECKPKG_OVERRIDES_CSWpmrrd += missing-dependency|CSWrrd
CHECKPKG_OVERRIDES_CSWpmrrd += surplus-dependency|CSWrrdrt

CHECKPKG_OVERRIDES_CSWrbrrd += missing-dependency|CSWrrd
CHECKPKG_OVERRIDES_CSWrbrrd += surplus-dependency|CSWrrdrt
CHECKPKG_OVERRIDES_CSWrbrrd += bad-rpath-entry|/home/dam/mgar/pkg/rrdtool/branches/x11-reloaded/work/solaris9-sparc/install-isa-sparcv8/opt/csw/lib|opt/csw/lib/ruby/site_ruby/1.8/sparc-solaris2.8/RRD.so
CHECKPKG_OVERRIDES_CSWrbrrd += bad-rpath-entry|/home/dam/mgar/pkg/rrdtool/branches/x11-reloaded/work/solaris9-i386/install-isa-i386/opt/csw/lib|opt/csw/lib/ruby/site_ruby/1.8/i386-solaris2.8/RRD.so

include gar/category.mk

pre-build-modulated:
	echo "  ==> Adding math function round()"
	cp $(FILEDIR)/s_round.c $(WORKSRC)/src
	cp $(FILEDIR)/s_round.h $(WORKSRC)/src
	@$(MAKECOOKIE)
