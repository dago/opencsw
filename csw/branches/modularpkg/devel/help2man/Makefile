GARNAME = help2man
GARVERSION = 1.36.4
CATEGORIES = devel

DESCRIPTION = A tool for automatically generating simple manual pages from program output
define BLURB
  help2man is a tool for automatically generating simple manual pages from program output.
  It is intended to provide an easy way for software authors to include a manual page
  in their distribution without having to maintain that document.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWhelp2man,depend)

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PREREQUISITE_PKGS = CSWpmlocalegettext

CONFIGURE_ARGS = $(DIRPATHS)
# We need to disable NLS as we don't have preloadable_libintl.so
# (only installed on glibc systems)
CONFIGURE_ARGS += --disable-nls

TEST_SCRIPTS =

include ../category.mk

post-install:
	@echo " ==> Fixing install anomalies"
	@rm -f $(DESTDIR)$(prefix)/share/info/dir
