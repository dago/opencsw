NAME = gettext
VERSION = 0.18.1.1
CATEGORIES = lib

DESCRIPTION = GNU locale utilities
define BLURB
	GNU gettext utilities are a set of tools that provides a framework to help other GNU packages produce multi-lingual messages
endef

PACKAGES += CSWggettext CSWggettextdoc

CATALOGNAME_CSWggettext = ggettext
CATALOGNAME_CSWggettext = ggettextdoc
SPKG_DESC_CSWggettext = GNU locale utilities
SPKG_DESC_CSWggettextdoc = GNU locale utility documentation

ARCHALL_CSWggettextdoc = 1

COMPILE_ELISP = 1

MASTER_SITES = $(GNU_MIRROR)

DISTFILES  = $(NAME)-$(VERSION).tar.gz

PATCHFILES += 0001-Use-the-auto-detected-SHELL-to-run-convert-archive.patch
PATCHFILES += 0002-Update-ltmain.sh-to-prevent-libtool-stripping-runpat.patch

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --program-prefix=g
#Dont' depend on packages that depend on me
CONFIGURE_ARGS += --with-included-glib
CONFIGURE_ARGS += --with-included-libcroco
#No glibc
CONFIGURE_ARGS += --with-included-gettext

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
NOISAEXEC = 1
STRIP_LIBTOOL = 1

RUNTIME_DEP_PKGS_CSWggettextdoc = CSWggettext

PKGFILES_CSWggettextdoc = $(PKGFILES_DOC)

#NOTE: gettext tests are sensitive to bash environment variables, make sure
#      custom paths are prefixed by $PATH, may be better to set aside
#      ~/.bashrc, etc. during build.
TEST_TARGET = check

#provided by iconv
MERGE_EXCLUDE_FILES  = .*/charset.alias
MERGE_EXCLUDE_FILES += .*/locale.alias
MERGE_EXCLUDE_FILES += .*/iconv.m4
MERGE_EXCLUDE_FILES += /opt/csw/bin/$(ISA)/.*

SHELL = /bin/bash

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

#Include old libraries for compatibility with existing packages
#  TODO: Convert to modulated builds
post-install-isa-sparcv8:
	@mkdir $(INSTALLISADIR)/opt/csw/share/java
	@mv $(INSTALLISADIR)/opt/csw/share/gettext/libintl.jar $(INSTALLISADIR)/opt/csw/share/java
	@( for f in $(FILEDIR)/*.s; do gcp $$f $(INSTALLISADIR)/opt/csw/lib/$$(gbasename $$f .s); done )
	$(MAKECOOKIE)

post-install-isa-sparcv9:
	@rm $(INSTALLISADIR)/opt/csw/share/gettext/libintl.jar
	@( for f in $(FILEDIR)/*.s9; do gcp $$f $(INSTALLISADIR)/opt/csw/lib/$$(gbasename $$f .s9); done )
	$(MAKECOOKIE)

post-install-isa-i386:
	@mkdir $(INSTALLISADIR)/opt/csw/share/java
	@mv $(INSTALLISADIR)/opt/csw/share/gettext/libintl.jar $(INSTALLISADIR)/opt/csw/share/java
	@( for f in $(FILEDIR)/*.i; do gcp $$f $(INSTALLISADIR)/opt/csw/lib/$$(gbasename $$f .i); done )
	$(MAKECOOKIE)

post-install-isa-amd64:
	@rm $(INSTALLISADIR)/opt/csw/share/gettext/libintl.jar
	@( for f in $(FILEDIR)/*.amd64; do gcp $$f $(INSTALLISADIR)/opt/csw/lib/$$(gbasename $$f .amd64); done )
	$(MAKECOOKIE)
