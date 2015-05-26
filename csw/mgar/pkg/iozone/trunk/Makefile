NAME = iozone
VERSION = 3.430
DISTVERSION = $(subst .,_,$(VERSION))
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = I/O benchmarking tool
define BLURB
  IOzone is a filesystem benchmark tool. The benchmark
  generates and measures a variety of file operations.
  The benchmark tests file I/O performance for the
  following operations: Read, write, re-read, re-write,
  read backwards, read strided, fread, fwrite, random
  read, pread ,mmap, aio_read, aio_write
endef

VENDOR_URL   = http://www.iozone.org/
LICENSE_TEXT = This is freeware

MASTER_SITES = http://www.iozone.org/src/current/
DISTNAME     = $(NAME)$(DISTVERSION)

DISTFILES    = $(DISTNAME).tar
DISTFILES   += vx_ioctl.h

DOCSRC       = $(WORKDIR)/$(DISTNAME)/docs
DOCS         = IOzone_msword_98.pdf
DOCS        += IOzone_msword_98.doc
DOCS        += Iozone_ps.gz
DOCS        += Run_rules.doc

# Solaris10cc: Always use LDFLAGS during linkage, Solaris8-64-VXFS: Use correct arch option
PATCHFILES   = patch_makefile.diff
# Move from man1 to man8
PATCHFILES  += patch_manfile.diff
# Use vx_ioctl.h in BUILDSRC instead of /opt/VRTSvxfs/include/sys/fs/
PATCHFILES  += patch_vxioctl.diff

# Dependency for contributed script_CSWiozone += CSWperl_PKGS = CSWgnuplot

PACKAGING_PLATFORMS += solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

BUILD64 = 1
ISAEXEC = 1

CONFIGURE_SCRIPTS =

BUILD_ARGS_5.9_i386_32   = Solaris
BUILD_ARGS_5.9_sparc_32  = Solaris
BUILD_ARGS_5.9_sparc_64  = Solaris8-64-VXFS
BUILD_ARGS_5.10_sparc_32 = Solaris10cc
BUILD_ARGS_5.10_sparc_64 = Solaris10cc
BUILD_ARGS_5.10_i386_32  = Solaris10cc
BUILD_ARGS_5.10_i386_64  = Solaris10cc
BUILD_TARGET = $(BUILD_ARGS_$(GAROSREL)_$(GARCH)_$(MEMORYMODEL))

BUILD_ARGS += $(BUILD_TARGET)

BUILD_OVERRIDE_VARS += CFLAGS
BUILD_OVERRIDE_VAR_CFLAGS = $(CFLAGS)

BUILD_OVERRIDE_VARS += S10CCFLAGS
BUILD_OVERRIDE_VAR_S10CCFLAGS = 

BUILD_OVERRIDE_VARS += LDFLAGS
BUILD_OVERRIDE_VAR_LDFLAGS = $(LDFLAGS)

BUILD_SCRIPTS = $(WORKSRC)/src/pendency|CSWperl

# There is no test suite
TEST_SCRIPTS =

INSTALL_SCRIPTS = custom

include gar/category.mk

# Copy the VxFS header file into the build directory
post-extract-modulated:
	mkdir -p $(WORKSRC)/src/current
	cp $(WORKDIR)/vx_ioctl.h $(WORKSRC)/src/current
	@$(MAKECOOKIE)

install-custom:
	@echo " ==> Installing $(NAME)"
	# Original Iozone files
	ginstall -D $(WORKSRC)/src/current/iozone $(DESTDIR)$(bindir)/iozone
	ginstall -D $(DOCSRC)/iozone.1 $(DESTDIR)$(mandir)/man8/iozone.8
	ginstall -D $(DOCSRC)/IOzone_msword_98.pdf $(DESTDIR)$(docdir)/iozone/IOzone_msword_98.pdf
	ginstall $(DOCSRC)/IOzone_msword_98.doc $(DESTDIR)$(docdir)/iozone/IOzone_msword_98.doc
	ginstall $(DOCSRC)/Iozone_ps.gz $(DESTDIR)$(docdir)/iozone/Iozone_ps.gz
	ginstall $(DOCSRC)/Run_rules.doc $(DESTDIR)$(docdir)/iozone/Run_rules.doc
	# Contributed files
	ginstall -D $(WORKSRC)/src/current/Generate_Graphs $(DESTDIR)$(datadir)/iozone/contrib/Generate_Graphs
	ginstall $(WORKSRC)/src/current/gengnuplot.sh $(DESTDIR)$(datadir)/iozone/contrib/gengnuplot.sh
	ginstall $(WORKSRC)/src/current/gnu3d.dem $(DESTDIR)$(datadir)/iozone/contrib/gnu3d.dem
	ginstall $(WORKSRC)/src/current/gnuplot.dem $(DESTDIR)$(datadir)/iozone/contrib/gnuplot.dem
	ginstall $(WORKSRC)/src/current/gnuplotps.dem $(DESTDIR)$(datadir)/iozone/contrib/gnuplotps.dem
	ginstall $(WORKSRC)/src/current/iozone_visualizer.pl $(DESTDIR)$(datadir)/iozone/contrib/iozone_visualizer.pl
	ginstall $(WORKSRC)/src/current/report.pl $(DESTDIR)$(datadir)/iozone/contrib/report.pl
	ginstall $(WORKSRC)/src/current/Gnuplot.txt $(DESTDIR)$(datadir)/iozone/contrib/Gnuplot.txt
	chmod 444 $(DESTDIR)$(datadir)/iozone/contrib/Gnuplot.tx