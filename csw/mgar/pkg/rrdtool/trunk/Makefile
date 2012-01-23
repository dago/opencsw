NAME = rrdtool
VERSION = 1.4.6
CATEGORIES = utils

DESCRIPTION = Time-series data logging and graphing
define BLURB
  RRDtool is basically the time-series graphing and data storage/management
  component of MRTG, broken out and `done right'. `done right' means that
  RRDtool is magnitudes faster than MRTG and extremely configurable.
endef

MASTER_SITES = http://oss.oetiker.ch/$(NAME)/pub/
DISTFILES = $(DISTNAME).tar.gz

# Use patch until this is fixed:
#   http://oss.oetiker.ch/rrdtool-trac/ticket/330
PATCHFILES += 0001-Do-not-reference-tm.tm_gmtoff-on-Solaris.patch

PATCHFILES += 0002-Always-link-local-libs-first-during-Perl-module.patch

# Make sure to link against libperl.so to make shared libraries self-contained.
PATCHFILES += 0003-Always-link-against-libperl.so.patch

# Do not pass LDFLAGS during pysetup or -L/opt/csw/lib will appear too early during
# linking which results in the system installed librrd.so is linked against instead
# of the newly build one
PATCHFILES += 0004-Do-not-pass-LDFLAGS-to-pysetup-or-the-system-lib-is-.patch

# New glib2 is only available for Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

VENDOR_URL = http://oss.oetiker.ch/rrdtool/

BUILD_DEP_PKGS += $(RUNTIME_DEP_PKGS_CSWlibrrd4)
BUILD_DEP_PKGS += CSWpangodevel
BUILD_DEP_PKGS += CSWlibcairo-dev
BUILD_DEP_PKGS += CSWlibglib2-dev
BUILD_DEP_PKGS += CSWperl
BUILD_DEP_PKGS += CSWpython-dev
BUILD_DEP_PKGS += CSWruby18-dev
BUILD_DEP_PKGS += CSWlibdbi-devel

PACKAGES += CSWrrdtool
SPKG_DESC_CSWrrdtool = Time-series data logging and graphing
RUNTIME_DEP_PKGS_CSWrrdtool += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWrrdtool += CSWpango
RUNTIME_DEP_PKGS_CSWrrdtool += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWrrdtool += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWrrdtool += CSWlibintl8
RUNTIME_DEP_PKGS_CSWrrdtool += CSWlibwrap1
RUNTIME_DEP_PKGS_CSWrrdtool += CSWlibdbi1
RUNTIME_DEP_PKGS_CSWrrdtool += CSWlibrrd3
RUNTIME_DEP_PKGS_CSWrrdtool += CSWlibrrd-th3
OBSOLETED_BY_CSWrrdtool = CSWrrd
CATALOGNAME_CSWrrd = rrd_stub

PACKAGES += CSWrrdtool-dev
SPKG_DESC_CSWrrdtool-dev = Development files for librrd.so.3
# Explicitly do not include *.3perl
PKGFILES_DEVEL_MAN3_MANPAGE = $(mandir)/man3/.*\.3
PKGFILES_CSWrrdtool-dev = $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWrrdtool-dev += CSWlibrrd3
RUNTIME_DEP_PKGS_CSWrrdtool-dev += CSWlibrrd-th3

PACKAGES += CSWlibrrd3
SPKG_DESC_CSWlibrrd3 = Runtime library for RRDtool, librrd.so.3
PKGFILES_CSWlibrrd3 += $(call pkgfiles_lib,librrd.so.3)
RUNTIME_DEP_PKGS_CSWlibrrd3 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibrrd3 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibrrd3 += CSWpango
RUNTIME_DEP_PKGS_CSWlibrrd3 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibrrd3 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibrrd3 += CSWlibwrap1
RUNTIME_DEP_PKGS_CSWlibrrd3 += CSWlibdbi1

PACKAGES += CSWlibrrd-th3
SPKG_DESC_CSWlibrrd-th3 = Runtime library for RRDtool, librrd_th.so.3
PKGFILES_CSWlibrrd-th3 += $(call pkgfiles_lib,librrd_th.so.3)
RUNTIME_DEP_PKGS_CSWlibrrd-th3 += CSWlibwrap1
RUNTIME_DEP_PKGS_CSWlibrrd-th3 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibrrd-th3 += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWlibrrd-th3 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibrrd-th3 += CSWpango
RUNTIME_DEP_PKGS_CSWlibrrd-th3 += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWlibrrd-th3 += CSWlibdbi1

PACKAGES += CSWpm-rrdtool
SPKG_DESC_CSWpm-rrdtool = RRDs: Access RRDtool as a shared module (part of RRDtool)
PKGFILES_CSWpm-rrdtool += $(libdir)/perl/.*
PKGFILES_CSWpm-rrdtool += $(sharedstatedir)/perl/.*
PKGFILES_CSWpm-rrdtool += $(sharedstatedir)/rrdtool/examples/.*
PKGFILES_CSWpm-rrdtool += .*\.3perl

RUNTIME_DEP_PKGS_CSWpm-rrdtool += CSWperl
RUNTIME_DEP_PKGS_CSWpm-rrdtool += CSWlibrrd3
OBSOLETED_BY_CSWpm-rrdtool = CSWrrd

PACKAGES += CSWpy-rrdtool
SPKG_DESC_CSWrb-rrdtool = Ruby binding for RRD access (part of RRDtool)
PKGFILES_CSWpy-rrdtool = $(libdir)/python/.*
RUNTIME_DEP_PKGS_CSWpy-rrdtool += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWpy-rrdtool += CSWlibrrd3
OBSOLETED_BY_CSWpy-rrdtool = CSWrrd

PACKAGES += CSWrb-rrdtool
SPKG_DESC_CSWpy-rrdtool = Python egg for RRD access (part of RRDtool)
PKGFILES_CSWrb-rrdtool = $(libdir)/ruby/.*
RUNTIME_DEP_PKGS_CSWrb-rrdtool += CSWlibruby18-1
RUNTIME_DEP_PKGS_CSWrb-rrdtool += CSWlibrrd3
OBSOLETED_BY_CSWrb-rrdtool = CSWrrd
# This is crappy and needs fixing, unfortunately inside extconf.rb which is hard.
CHECKPKG_OVERRIDES_CSWrb-rrdtool += bad-rpath-entry

#CHECKPKG_OVERRIDES_CSWpm-rrdtool += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/RRDp.3perl
#CHECKPKG_OVERRIDES_CSWpm-rrdtool += file-with-bad-content|/usr/local|root/opt/csw/share/perl/csw/RRDp.pm
#CHECKPKG_OVERRIDES_CSWpm-rrdtool += pkginfo-opencsw-repository-uncommitted
#CHECKPKG_OVERRIDES_CSWrrdtool += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/rrd-beginners.1
#CHECKPKG_OVERRIDES_CSWrrdtool += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/rrdcgi.1
#CHECKPKG_OVERRIDES_CSWrrdtool += file-with-bad-content|/usr/local|root/opt/csw/share/doc/rrdtool/html/rrdcgi.html
#CHECKPKG_OVERRIDES_CSWrrdtool += file-with-bad-content|/usr/local|root/opt/csw/share/doc/rrdtool/html/rrd-beginners.html
#CHECKPKG_OVERRIDES_CSWrrdtool += file-with-bad-content|/usr/local|root/opt/csw/share/doc/rrdtool/html/RRDp.html
#CHECKPKG_OVERRIDES_CSWrrdtool += file-with-bad-content|/usr/local|root/opt/csw/share/doc/rrdtool/txt/rrdcgi.txt
#CHECKPKG_OVERRIDES_CSWrrdtool += file-with-bad-content|/usr/local|root/opt/csw/share/doc/rrdtool/txt/rrd-beginners.pod
#CHECKPKG_OVERRIDES_CSWrrdtool += file-with-bad-content|/usr/local|root/opt/csw/share/doc/rrdtool/txt/rrd-beginners.txt
#CHECKPKG_OVERRIDES_CSWrrdtool += file-with-bad-content|/usr/local|root/opt/csw/share/doc/rrdtool/txt/rrdcgi.pod
#CHECKPKG_OVERRIDES_CSWrrdtool += file-with-bad-content|/usr/share|root/opt/csw/share/man/man1/rrdbuild.1
#CHECKPKG_OVERRIDES_CSWrrdtool += file-with-bad-content|/usr/share|root/opt/csw/share/doc/rrdtool/html/rrdbuild.html
#CHECKPKG_OVERRIDES_CSWrrdtool += file-with-bad-content|/usr/share|root/opt/csw/share/doc/rrdtool/txt/rrdbuild.pod
#CHECKPKG_OVERRIDES_CSWrrdtool += file-with-bad-content|/usr/share|root/opt/csw/share/doc/rrdtool/txt/rrdbuild.txt

REINPLACE_USRLOCAL += /opt/csw/share/perl/csw/RRDp.pm
REINPLACE_USRLOCAL += /opt/csw/share/man/man3/RRDp.3perl
REINPLACE_USRLOCAL += /opt/csw/share/man/man1/rrd-beginners.1
REINPLACE_USRLOCAL += /opt/csw/share/man/man1/rrdcgi.1
REINPLACE_USRLOCAL += /opt/csw/share/doc/rrdtool-$(VERSION)/txt/rrd-beginners.pod
REINPLACE_USRLOCAL += /opt/csw/share/doc/rrdtool-$(VERSION)/txt/rrdcgi.pod
REINPLACE_USRLOCAL += /opt/csw/share/doc/rrdtool-$(VERSION)/txt/rrd-beginners.txt
REINPLACE_USRLOCAL += /opt/csw/share/doc/rrdtool-$(VERSION)/txt/rrdcgi.txt
REINPLACE_USRLOCAL += /opt/csw/share/doc/rrdtool-$(VERSION)/html/rrd-beginners.html
REINPLACE_USRLOCAL += /opt/csw/share/doc/rrdtool-$(VERSION)/html/RRDp.html
REINPLACE_USRLOCAL += /opt/csw/share/doc/rrdtool-$(VERSION)/html/rrdcgi.html
REINPLACE_WHEN_USRLOCAL = postinstall

REINPLACE_USRSHARE += /opt/csw/share/man/man1/rrdbuild.1
REINPLACE_USRSHARE += /opt/csw/share/doc/rrdtool-$(VERSION)/txt/rrdbuild.txt
REINPLACE_USRSHARE += /opt/csw/share/doc/rrdtool-$(VERSION)/txt/rrdbuild.pod
REINPLACE_USRSHARE += /opt/csw/share/doc/rrdtool-$(VERSION)/html/rrdbuild.html
REINPLACE_WHEN_USRSHARE = postinstall

EXTRA_INC += $(includedir)/pango-1.0
EXTRA_INC += $(includedir)/cairo
EXTRA_INC += $(includedir)/libxml2
EXTRA_INC += $(includedir)/glib-2.0
EXTRA_INC += $(libdir)/glib-2.0/include

EXTRA_LINKER_FLAGS = -lintl

BUILD64_LIBS_ONLY = 1

# Verbose build output
# BUILD_ARGS += V=1

CONFIGURE_ARGS_32 += --enable-python
CONFIGURE_ARGS_32 += --enable-ruby
CONFIGURE_ARGS_32 += --with-ruby-options=RUBY_MAKE_OPTIONS=DESTDIR=$(DESTDIR)
CONFIGURE_ARGS_32 += --enable-perl
# Reenable when new lua package with pkgconfig is there
CONFIGURE_ARGS_32 += --disable-lua
CONFIGURE_ARGS_32 += --with-perl-options=INSTALLDIRS=vendor
# We don't have any of these in 64 bit (yet!)
CONFIGURE_ARGS_64 += --disable-python
CONFIGURE_ARGS_64 += --disable-ruby
CONFIGURE_ARGS_64 += --disable-perl
CONFIGURE_ARGS_64 += --disable-lua

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --docdir=$(sharedstatedir)/doc/$(NAME)
CONFIGURE_ARGS += --disable-tcl
CONFIGURE_ARGS += --with-libintl-prefix=$(libdir)
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(MEMORYMODEL))

# TEST_TARGET = check

# MERGE_SCRIPTS_isa-extra = copy-relocated-only copy-config-only
EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod .*/\.packlist
EXTRA_PAX_ARGS += -s ',^\.$(docdir)/$(NAME)-$(VERSION),.$(BUILD_PREFIX)/share/doc/rrdtool,'

include gar/category.mk
