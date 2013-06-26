# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME    = bonnie++
VERSION = 1.97.1
FILEVERSION = 1.97
GARTYPE = v2

GARCOMPILER = GNU

DESCRIPTION = A hard drive benchmark suite
define BLURB
  Bonnie++ is a benchmark suite that is aimed at performing a number of simple tests of hard drive and file system performance.
endef

MASTER_SITES = http://www.coker.com.au/bonnie++/experimental/
DISTFILES  = $(NAME)-$(FILEVERSION).tgz

PACKAGES = CSWbonnie++
CATALOGNAME_CSWbonnie++ = bonnie++
SPKG_DESC_CSWbonnie++ = A benchmark suite aimed at performing a number of simple tests of hard drive and file system performance
RUNTIME_DEP_PKGS_CSWbonnie++ += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWbonnie++ += CSWlibstdc++6

LICENSE = copyright.txt

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET =
INSTALL_SCRIPTS = custom

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

SBINFILES = bonnie++ zcav getc_putc getc_putc_helper
BINFILES  = bon_csv2html generate_randfile bon_csv2txt
MAN1FILES = bon_csv2html.1 bon_csv2txt.1 generate_randfile.1
MAN8FILES = bonnie++.8 zcav.8 getc_putc.8

install-custom:
	@echo " => Installing $(CATALOGNAME)"
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(sbindir)
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall -d $(DESTDIR)$(mandir)/man8
	cd $(WORKSRC) && \
		ginstall -m 755 $(BINFILES) $(DESTDIR)$(bindir)/ && \
		ginstall -m 755 $(SBINFILES) $(DESTDIR)$(sbindir)/ && \
		ginstall -m 644 $(MAN1FILES) $(DESTDIR)$(mandir)/man1/ && \
		ginstall -m 644 $(MAN8FILES) $(DESTDIR)$(mandir)/man8/
	@$(MAKECOOKIE)

