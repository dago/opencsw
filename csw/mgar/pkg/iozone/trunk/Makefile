NAME = iozone
VERSION = 3.291
DISTVERSION = $(shell echo $(VERSION) | sed -e 's/\./_/g')
GARTYPE = v1
CATEGORIES = apps

DESCRIPTION = IO benchmarking tool
define BLURB
  IOzone is a filesystem benchmark tool. The benchmark
  generates and measures a variety of file operations.
  Iozone has been ported to many machines and runs under
  many operating systems.
endef

VENDOR_URL    = http://www.iozone.org/
MASTER_SITES  = http://www.iozone.org/src/current/
MASTER_SITES += http://www.iozone.org/docs/
UFILES_REGEX  = $(NAME)(\d+(?:\.\d+)*).tar
DISTFILES     = $(NAME)$(DISTVERSION).tar
DISTFILES    += vx_ioctl.h
DISTFILES    += $(call admfiles,CSWiozone)

DISTNAME      = $(NAME)$(DISTVERSION)

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

include gar/category.mk

# The install part from the Makefile is completely unrelocatable :-(
install-custom:
	@echo " ==> Installing $(NAME)"
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(mandir)/man6
	@$(MAKECOOKIE)
