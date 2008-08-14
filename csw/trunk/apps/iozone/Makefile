GARNAME = iozone
GARVERSION = 3.291
VERSION = $(shell echo $(GARVERSION) | sed -e 's/\./_/g')
CATEGORIES = apps

DESCRIPTION = IO benchmarking tool
define BLURB
  IOzone is a filesystem benchmark tool. The benchmark
  generates and measures a variety of file operations.
  Iozone has been ported to many machines and runs under
  many operating systems.
endef

MASTER_SITES  = http://www.iozone.org/src/current/
MASTER_SITES += http://www.iozone.org/docs/
DISTFILES  = $(GARNAME)$(VERSION).tar
DISTFILES += vx_ioctl.h
DISTFILES += $(call admfiles,CSWiozone)

DISTNAME = $(GARNAME)$(VERSION)

PATCHFILES = patch-vx_ioctl.diff

DOCS = IOzone_msword_98.pdf
DOCS += Iozone_ps.gz
DOCS += IOzone_msword_98.doc
DOCS += Run_rules.doc

WORKSRC = $(WORKDIR)/$(DISTNAME)/src/current
DOCSRC = $(WORKDIR)$(DISTNAME)/docs

# Make sure the VxFS header is in place
EXTRA_INC = $(WORKSRC)/include/sys/fs
post-extract:
	@mkdir -p $(WORKSRC)/include/sys/fs
	@cp $(WORKDIR)/vx_ioctl.h $(WORKSRC)
	@$(MAKECOOKIE)

# We don't have this modern autoconfig-doodle-crap
CONFIGURE_SCRIPTS =
TEST_SCRIPTS =

BUILD_ARGS = Solaris8-64-VXFS
BUILD_SCRIPTS = $(WORKSRC)/makefile

INSTALL_SCRIPTS = custom

include ../category.mk

# The install part from the Makefile is completely unrelocatable :-(
install-custom:
	@echo " ==> Installing $(GARNAME)"
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(mandir)/man6
	@$(MAKECOOKIE)
