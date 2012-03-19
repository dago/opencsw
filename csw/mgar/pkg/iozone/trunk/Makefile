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

MASTER_SITES += http://www.iozone.org/src/current/
DISTNAME = $(NAME)$(DISTVERSION)
DISTFILES += $(DISTNAME).tar
#PATCHFILES = patch-vx_ioctl.diff

VENDOR_URL    = http://www.iozone.org/

DOCS  = IOzone_msword_98.pdf
DOCS += IOzone_msword_98.doc
DOCS += Iozone_ps.gz
DOCS += Run_rules.doc

WORKSRC = $(WORKDIR)$(DISTNAME)/src/current
DOCSRC  = $(WORKDIR)$(DISTNAME)/docs

CONFIGURE_SCRIPTS =
TEST_SCRIPTS =

BUILD_ARGS = Solaris10
BUILD_SCRIPTS = $(WORKSRC)/makefile

INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@echo " ==> Installing $(NAME)"
	ginstall -D $(WORKSRC)/iozone $(DESTDIR)$(bindir)/iozone
	ginstall -D $(DOCSRC)/iozone.1 $(DESTDIR)$(mandir)/man6/iozone.1
	@$(MAKECOOKIE)
