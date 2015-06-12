NAME = perl
VERSION = 5.22.0
VERSION_MAJOR = $(shell echo $(VERSION) | cut -f1-2 -d.)
#CATEGORIES = lang
GARTYPE = v2

DESCRIPTION = A high-level, general-purpose programming language
define BLURB
  Perl is a high-level, general-purpose programming language that makes easy
  things easy and hard things possible. It is optimized for scanning arbitrary
  text files and system administration. It has built-in extended regular
  expression matching and replacement, a dataflow mechanism to improve security
  with setuid scripts and is extendable via modules that can interface to C
  libraries.
  This package is built with gcc.
endef

#MASTER_SITES = manual://
MASTER_SITES = http://www.cpan.org/src/5.0/
VENDOR_URL = http://www.perl.org
DISTFILES  = $(NAME)-$(VERSION).tar.bz2
PACKAGING_PLATFORMS += solaris10-i386 solaris10-sparc
PACKAGES               = CSWperl
PKG_DESC_CSWperl    = $(DESCRIPTION)
SPKG_DESC_CSWperl   = $(DESCRIPTION)
LICENSE = Copying

# GCC build (Sun Studio build has been fixed)
GARCOMPILER = GCC4
MAKE_OPT_unstable10s = -j 24
MAKE_OPT_unstable10x = -j 4
MAKE_OPT = $(MAKE_OPT_$(shell hostname))
BUILD64 = 1
ISAEXEC = 1
IGNORE_DESTDIR = 1

# a .git directory will cause failing upstream author tests (the source will be considered blead)
NOGITPATCH = 1

EXTRA_RUNPATH_DIRS = $(libdir)/perl/5.22/CORE
EXTRA_RUNPATH_ISALIST = $(EXTRA_RUNPATH_DIRS)
#EXTRA_LIB = $(prefix)/$(libdir)/perl/5.20/CORE
#EXTRA_RUNPATH_LINKER_FLAGS += $(prefix)/$(libdir)/perl/5.20/CORE/libperl.so

# Depends
RUNTIME_DEP_PKGS_CSWperl += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWperl += CSWlibssp0
RUNTIME_DEP_PKGS_CSWperl += CSWlibgdbm4
CHECKPKG_OVERRIDES_CSWperl += missing-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWperl += 64-bit-binaries-missing
CHECKPKG_OVERRIDES_CSWperl += file-with-bad-content
CHECKPKG_OVERRIDES_CSWperl += bad-rpath-entry

# Overridden because "/usr/ccs/bin/elfdump -y <file>" returns output
#CHECKPKG_OVERRIDES_CSWperl += no-direct-binding|/opt/csw/lib/perl/5.18/CORE/libperl.so|is|not|directly|bound|to|soname|libgcc_s.so.1
#CHECKPKG_OVERRIDES_CSWperl += no-direct-binding|/opt/csw/lib/perl/5.18/CORE/libperl.so|is|not|directly|bound|to|soname|libssp.so.0

# Custom configure
CONFIGURE_SCRIPTS = perl
CONFIGURE_ARGS += -Darchlib=$(libdir)/perl/$(VERSION_MAJOR)
CONFIGURE_ARGS += -Dcc=$(CC)
CONFIGURE_ARGS += -Dcf_email=$(SPKG_EMAIL)
CONFIGURE_ARGS += -Dman1dir=$(mandir)/man1
CONFIGURE_ARGS += -Dman1ext=1
CONFIGURE_ARGS += -Dman3dir=$(mandir)/man3
CONFIGURE_ARGS += -Dman3ext=3perl
CONFIGURE_ARGS += -Dperladmin="root@localhost"
CONFIGURE_ARGS += -Dprefix=$(prefix)
CONFIGURE_ARGS += -Dbin=$(bindir)
CONFIGURE_ARGS += -Dscriptdir=$(bindir)
# CSW provided modules should install in the privlib directory (/opt/csw/share/perl/5.<MAJOR>)
CONFIGURE_ARGS += -Dprivlib=$(datadir)/perl/$(VERSION_MAJOR)
CONFIGURE_ARGS += -Dsitearch=/opt/csw/local/lib/perl/$(VERSION_MAJOR)
CONFIGURE_ARGS += -Dsitelib=/opt/csw/local/share/perl/$(VERSION)
CONFIGURE_ARGS += -Dsiteman1dir=/opt/csw/local/share/man/man1
CONFIGURE_ARGS += -Dsiteman3dir==/opt/csw/local/share/man/man3
CONFIGURE_ARGS += -Dsiteprefix=/opt/csw/local
CONFIGURE_ARGS += -Duseshrplib
CONFIGURE_ARGS += -Dusesitecustomize
CONFIGURE_ARGS += -Dusethreads
CONFIGURE_ARGS += -Dusedtrace
CONFIGURE_ARGS += -Duselargefiles 
CONFIGURE_ARGS += -Dvendorarch=$(libdir)/perl5
CONFIGURE_ARGS += -Dvendorlib=$(datadir)/perl5
CONFIGURE_ARGS += -Dvendorprefix=$(prefix)
CONFIGURE_ARGS += -Dlibsdirs=" $(abspath /usr/lib/$(MEMORYMODEL)) $(libdir)"
CONFIGURE_ARGS += -Dsed=/opt/csw/bin/gsed
CONFIGURE_ARGS-64 += -Duse64bitint
CONFIGURE_ARGS-64 += -Duse64bitall
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL)) 
CONFIGURE_ARGS += -Dlddlflags=-shared

# We want 64 bit binaries
MERGE_DIRS_isa-extra = $(bindir) $(sbindir) $(libdir) $(libexecdir)

BUILD_SCRIPTS = perl
TEST_SCRIPTS = perl

include gar/category.mk

# Configure

PATH:=/opt/csw/gnu:$(PATH)
configure-perl: CONFIGURE_EXPORTS = PATH LD_OPTIONS
configure-perl:
	(cd $(WORKSRC) ; $(CONFIGURE_ENV) ./Configure $(CONFIGURE_ARGS) -ders)
	@$(MAKECOOKIE)

# Build
build-perl: BUILD_EXPORTS = LD_OPTIONS
build-perl:
	@echo " ==> Running make in $*"
	cd $(WORKSRC) && $(BUILD_ENV) $(MAKE) $(MAKE_OPT)
	@$(MAKECOOKIE)

# Test
# Beware, test may fail when run in paralled. We leave it like this because it's a lot faster and the failure not very common. Just rerun mgar test.
# You can always run the test single threaded if needed.
test-perl:
	@echo " ==> Running make $(TEST_TARGET) in $*"
	# workaround gar pwd bug (PWD is not changed with cd from Makefile:
	# http://sourceforge.net/apps/trac/gar/ticket/78	
	cd $(WORKSRC) && PWD=`pwd` $(MAKE) $(MAKE_OPT) test
	@$(MAKECOOKIE)
