NAME = iozone
VERSION = 3.398
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
MASTER_SITES = http://www.iozone.org/src/current/

DISTNAME     = $(NAME)$(DISTVERSION)
WORKSRC      = $(WORKDIR)/$(DISTNAME)/src/current
DOCSRC       = $(WORKDIR)$(DISTNAME)/docs

DISTFILES    = $(DISTNAME).tar
DISTFILES   += vx_ioctl.h

PATCHFILES   = patch_makefile.diff
PATCHFILES  += patch_manfile.diff
PATCHFILES  += patch_vxioctl.diff

DOCS         = IOzone_msword_98.pdf
DOCS        += IOzone_msword_98.doc
DOCS        += Iozone_ps.gz
DOCS        += Run_rules.doc

CONFIGURE_SCRIPTS =
TEST_SCRIPTS =

BUILD_ARGS = Solaris8-64-VXFS
BUILD_SCRIPTS = $(WORKSRC)/makefile

INSTALL_SCRIPTS = custom

include gar/category.mk

post-extract-modulated:
	mkdir -p work/solaris9-sparc/build-isa-sparcv8/$(DISTNAME)/src/current
	cp $(FILEDIR)/vx_ioctl.h work/solaris9-sparc/build-isa-sparcv8/$(DISTNAME)/src/current
	@$(MAKECOOKIE)

install-custom:
	@echo " ==> Installing $(NAME)"
	ginstall -D $(WORKSRC)/iozone $(DESTDIR)$(bindir)/iozone
	ginstall -D $(DOCSRC)/iozone.1 $(DESTDIR)$(mandir)/man8/iozone.8
	ginstall -D $(DOCSRC)/IOzone_msword_98.pdf $(DESTDIR)$(docdir)/iozone/IOzone_msword_98.pdf
	ginstall $(DOCSRC)/IOzone_msword_98.doc $(DESTDIR)$(docdir)/iozone/IOzone_msword_98.doc
	ginstall $(DOCSRC)/Iozone_ps.gz $(DESTDIR)$(docdir)/iozone/Iozone_ps.gz
	ginstall $(DOCSRC)/Run_rules.doc $(DESTDIR)$(docdir)/iozone/Run_rules.doc
	@$(MAKECOOKIE)
