NAME = rrdtool
VERSION = 1.4.5
CATEGORIES = utils

DESCRIPTION = Time-series data logging and graphing
define BLURB
  RRDtool is basically the time-series graphing and data storage/management
  component of MRTG, broken out and `done right'. `done right' means that
  RRDtool is magnitudes faster than MRTG and extremely configurable.
endef

MASTER_SITES = http://oss.oetiker.ch/$(NAME)/pub/
DISTFILES = $(NAME)-$(VERSION).tar.gz

# Make sure to link against libperl.so to make shared libraries self-contained.
PATCHFILES += patch-bindings-perl-piped-Makefile.PL
PATCHFILES += patch-bindings-perl-shared-Makefile.PL

PACKAGES += CSWrrdtool
CATALOGNAME_CSWrrdtool = rrdtool
SPKG_DESC_CSWrrdtool = Time-series data logging and graphing
RUNTIME_DEP_PKGS_CSWrrdtool += CSWglib2
RUNTIME_DEP_PKGS_CSWrrdtool += CSWpango
RUNTIME_DEP_PKGS_CSWrrdtool += CSWlibxml2
RUNTIME_DEP_PKGS_CSWrrdtool += CSWlibcairo
RUNTIME_DEP_PKGS_CSWrrdtool += CSWlibintl8
RUNTIME_DEP_PKGS_CSWrrdtool += CSWtcpwrap
RUNTIME_DEP_PKGS_CSWrrdtool += CSWlibdbi1
RUNTIME_DEP_PKGS_CSWrrdtool += CSWlibrrd4
RUNTIME_DEP_PKGS_CSWrrdtool += CSWlibrrd-th4
OBSOLETES_CSWrrdtool = CSWrrd

PACKAGES += CSWrrdtool-dev
CATALOGNAME_CSWrrdtool-dev = rrdtool_dev
SPKG_DESC_CSWrrdtool-dev = Development files for librrd.so.4
PKGFILES_CSWrrdtool-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWrrdtool-dev += CSWlibrrd4
RUNTIME_DEP_PKGS_CSWrrdtool-dev += CSWlibrrd-th4

PACKAGES += CSWlibrrd4
CATALOGNAME_CSWlibrrd4 = librrd4
SPKG_DESC_CSWlibrrd4 = Runtime library for RRDtool, librrd.so.4
PKGFILES_CSWlibrrd4 += $(call pkgfiles_lib,librrd.so.4)
RUNTIME_DEP_PKGS_CSWlibrrd4 += CSWglib2
RUNTIME_DEP_PKGS_CSWlibrrd4 += CSWlibcairo
RUNTIME_DEP_PKGS_CSWlibrrd4 += CSWpango
RUNTIME_DEP_PKGS_CSWlibrrd4 += CSWlibxml2
RUNTIME_DEP_PKGS_CSWlibrrd4 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibrrd4 += CSWtcpwrap
RUNTIME_DEP_PKGS_CSWlibrrd4 += CSWlibdbi1

PACKAGES += CSWlibrrd-th4
CATALOGNAME_CSWlibrrd-th4 = librrd_th4
SPKG_DESC_CSWlibrrd-th4 = Runtime library for RRDtool, librrd_th.so.4
PKGFILES_CSWlibrrd-th4 += $(call pkgfiles_lib,librrd_th.so.4)
RUNTIME_DEP_PKGS_CSWlibrrd-th4 += CSWtcpwrap
RUNTIME_DEP_PKGS_CSWlibrrd-th4 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibrrd-th4 += CSWlibcairo
RUNTIME_DEP_PKGS_CSWlibrrd-th4 += CSWlibxml2
RUNTIME_DEP_PKGS_CSWlibrrd-th4 += CSWpango
RUNTIME_DEP_PKGS_CSWlibrrd-th4 += CSWglib2
RUNTIME_DEP_PKGS_CSWlibrrd-th4 += CSWlibdbi1

PACKAGES += CSWpm-rrdtool
CATALOGNAME_CSWpm-rrdtool = pm_rrdtool
SPKG_DESC_CSWpm-rrdtool = RRDs: Access RRDtool as a shared module (part of RRDtool)
PKGFILES_CSWpm-rrdtool += $(libdir)/perl/.*
PKGFILES_CSWpm-rrdtool += $(sharedstatedir)/perl/.*
PKGFILES_CSWpm-rrdtool += $(sharedstatedir)/rrdtool/examples/.*
PKGFILES_CSWpm-rrdtool += .*\.3perl
RUNTIME_DEP_PKGS_CSWpm-rrdtool += CSWperl
RUNTIME_DEP_PKGS_CSWpm-rrdtool += CSWlibrrd4
OBSOLETES_CSWpm-rrdtool = CSWrrd

PACKAGES += CSWpy-rrdtool
CATALOGNAME_CSWpy-rrdtool = py_rrdtool
SPKG_DESC_CSWrb-rrdtool = Ruby binding for RRD access (part of RRDtool)
PKGFILES_CSWpy-rrdtool = $(libdir)/python/.*
RUNTIME_DEP_PKGS_CSWpy-rrdtool += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-rrdtool += CSWlibrrd4
RUNTIME_DEP_PKGS_CSWpy-rrdtool += CSWlibintl8
OBSOLETES_CSWpy-rrdtool = CSWrrd

PACKAGES += CSWrb-rrdtool
CATALOGNAME_CSWrb-rrdtool = rb_rrdtool
SPKG_DESC_CSWpy-rrdtool = Python egg for RRD access (part of RRDtool)
PKGFILES_CSWrb-rrdtool = $(libdir)/ruby/.*
RUNTIME_DEP_PKGS_CSWrb-rrdtool += CSWlibruby1
RUNTIME_DEP_PKGS_CSWrb-rrdtool += CSWlibrrd4
OBSOLETES_CSWrb-rrdtool = CSWrrd
# This is crappy and needs fixing, unfortunately inside extconf.rb which is hard.
CHECKPKG_OVERRIDES_CSWrb-rrdtool += bad-rpath-entry

BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS_CSWlibrrd4)
BUILD_DEP_PKGS += CSWpangodevel
BUILD_DEP_PKGS += CSWlibcairodevel
BUILD_DEP_PKGS += CSWglib2devel
BUILD_DEP_PKGS += CSWperl
BUILD_DEP_PKGS += CSWpython-devel
BUILD_DEP_PKGS += CSWrubydev

EXTRA_INC = $(prefix)/include/cairo
EXTRA_INC += $(prefix)/include/libxml2

EXTRA_LINKER_FLAGS = -lintl

BUILD64 = 1
NOISAEXEC = 1
STRIP_LIBTOOL = 1

CONFIGURE_ARGS_32 += --enable-python
CONFIGURE_ARGS_32 += --enable-ruby
CONFIGURE_ARGS_32 += --with-ruby-options=RUBY_MAKE_OPTIONS=DESTDIR=$(DESTDIR)
CONFIGURE_ARGS_32 += --enable-perl
CONFIGURE_ARGS_32 += --with-perl-options=INSTALLDIRS=vendor
# We don't have any of these in 64 bit (yet!)
CONFIGURE_ARGS_64 += --disable-python
CONFIGURE_ARGS_64 += --disable-ruby
CONFIGURE_ARGS_64 += --disable-perl

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --docdir=$(sharedstatedir)/doc/$(NAME)
CONFIGURE_ARGS += --disable-lua
CONFIGURE_ARGS += --disable-tcl
CONFIGURE_ARGS += --with-libintl-prefix=$(libdir)
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(MEMORYMODEL))

TEST_TARGET = check

MERGE_DIRS_isa-extra = $(libdir)
MERGE_SCRIPTS_isa-extra = copy-relocated-only copy-config-only
EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod .*/\.packlist
EXTRA_PAX_ARGS += -s ',^\.$(docdir)/$(NAME)-$(VERSION),.$(BUILD_PREFIX)/share/doc/rrdtool,'

include gar/category.mk

post-install-modulated:
	perl -pi -e 's,/usr/local,$(prefix),g' \
		$(addprefix $(DESTDIR), \
		/opt/csw/share/perl/csw/RRDp.pm \
		/opt/csw/share/man/man3/RRDp.3perl \
		/opt/csw/share/man/man1/rrd-beginners.1 \
		/opt/csw/share/man/man1/rrdcgi.1 \
		/opt/csw/share/doc/rrdtool-1.4.5/txt/rrd-beginners.pod \
		/opt/csw/share/doc/rrdtool-1.4.5/txt/rrdcgi.pod \
		/opt/csw/share/doc/rrdtool-1.4.5/txt/rrd-beginners.txt \
		/opt/csw/share/doc/rrdtool-1.4.5/txt/rrdcgi.txt \
		/opt/csw/share/doc/rrdtool-1.4.5/html/rrd-beginners.html \
		/opt/csw/share/doc/rrdtool-1.4.5/html/RRDp.html \
		/opt/csw/share/doc/rrdtool-1.4.5/html/rrdcgi.html \
		)

	perl -pi -e 's,/usr/share,$(sharedstatedir),g' \
		$(addprefix $(DESTDIR), \
		/opt/csw/share/man/man1/rrdbuild.1 \
		/opt/csw/share/doc/rrdtool-1.4.5/txt/rrdbuild.txt \
		/opt/csw/share/doc/rrdtool-1.4.5/txt/rrdbuild.pod \
		/opt/csw/share/doc/rrdtool-1.4.5/html/rrdbuild.html \
		)

	@$(MAKECOOKIE)
