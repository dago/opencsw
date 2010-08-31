GARNAME = gettext
GARVERSION = 0.18.1.1
CATEGORIES = lib

DESCRIPTION = GNU locale utilities
define BLURB
	GNU gettext utilities are a set of tools that provides a framework to help other GNU packages produce multi-lingual messages
endef

PACKAGES = CSWggettextrt CSWggettextdoc CSWggettext

ARCHALL_CSWggettextel = 1

CATALOGNAME_CSWggettext = ggettext
CATALOGNAME_CSWggettextdoc = ggettextdoc
CATALOGNAME_CSWggettextrt = ggettextrt
SPKG_DESC_CSWggettext = GNU locale utilities and development headers
SPKG_DESC_CSWggettextdoc = GNU locale documentation
SPKG_DESC_CSWggettextrt = GNU locale runtime
ARCHALL_CSWggettextdoc = 1

COMPILE_ELISP = 1

MASTER_SITES = $(GNU_MIRROR)

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
#Include earlier library revisions for compatibility with existing packages
DISTFILES += libgettextlib-0.14.1.so.i
DISTFILES += libgettextlib-0.14.1.so.s
DISTFILES += libintl.so.2.i
DISTFILES += libintl.so.2.s
DISTFILES += libintl.so.3.i
DISTFILES += libintl.so.3.s

PATCHFILES += 0001-Use-the-auto-detected-SHELL-to-run-convert-archive.patch
PATCHFILES += 0002-Update-ltmain.sh-to-prevent-libtool-stripping-runpat.patch

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --program-prefix=g
#Dont' depend on packages that depend on me
CONFIGURE_ARGS += --with-included-glib
CONFIGURE_ARGS += --with-included-libcroco
#No glibc
CONFIGURE_ARGS += --with-included-gettext

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1
NOISAEXEC = 1
STRIP_LIBTOOL = 1

RUNTIME_DEP_PKGS_CSWggettextrt = CSWiconv
RUNTIME_DEP_PKGS_CSWggettext = CSWggettextrt CSWiconv CSWexpat CSWncurses
RUNTIME_DEP_PKGS_CSWggettext += CSWlibxml2
RUNTIME_DEP_PKGS_CSWggettextdoc = CSWggettext

#NOTE: gettext tests are sensitive to bash environment variables, make sure
#      custom paths are prefixed by $PATH, may be better to set aside
#      ~/.bashrc, etc. during build.
TEST_TARGET = check

#provided by iconv
MERGE_EXCLUDE_FILES  = .*/charset.alias
MERGE_EXCLUDE_FILES += .*/iconv.m4
MERGE_EXCLUDE_FILES += /opt/csw/bin/$(ISA)/.*

#This syntaxt skips 64-bit for some reason
#PKGFILES_CSWggettextrt  = $(call baseisadirs,$(libdir),libintl\..*)
#PKGFILES_CSWggettextrt += $(call baseisadirs,$(libdir),libasprintf\..*)
#PKGFILES_CSWggettextrt += $(call baseisadirs,$(libdir),libgettextpo\..*) 
#so use this for now
PKGFILES_CSWggettextrt  = .*/libintl\.so.* .*/libasprintf\.so.* .*/libgettextpo\.so.*
PKGFILES_CSWggettextrt += /opt/csw/bin/ggettext /opt/csw/bin/gngettext /opt/csw/bin/genvsubst
PKGFILES_CSWggettextrt += /opt/csw/bin/ggettext.sh /opt/csw/share/java/libintl.jar
PKGFILES_CSWggettextrt += /opt/csw/share/locale/.*
PKGFILES_CSWggettextdoc  = $(PKGFILES_DOC)

CHECKPKG_OVERRIDES_CSWggettextdoc += missing-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWggettextdoc += surplus-dependency|CSWggettext
CHECKPKG_OVERRIDES_CSWggettextel += surplus-dependency|CSWggettext
# This lib is legacy from the old versions and can't be updated (easily)
CHECKPKG_OVERRIDES_CSWggettext += bad-rpath-entry|/export/home/phil/build/gettext-0.14.1/gettext-tools/intl/.libs|opt/csw/lib/sparcv9/libgettextlib-0.14.1.so 
# just until checkpkg doesn't squawk about this.
CHECKPKG_OVERRIDES_CSWggettext += missing-dependency|CSWemacscommon

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

#Include old libraries for compatibility with existing packages
#  TODO: Convert to modulated builds
post-install-isa-sparcv8:
	@mkdir $(INSTALLISADIR)/opt/csw/share/java
	@mv $(INSTALLISADIR)/opt/csw/share/gettext/libintl.jar $(INSTALLISADIR)/opt/csw/share/java
	@cp $(FILEDIR)/libgettextlib-0.14.1.so.s $(INSTALLISADIR)/opt/csw/lib/libgettextlib-0.14.1.so
	@cp $(FILEDIR)/libintl.so.2.s $(INSTALLISADIR)/opt/csw/lib/libintl.so.2
	@cp $(FILEDIR)/libintl.so.3.s $(INSTALLISADIR)/opt/csw/lib/libintl.so.3
	$(DONADA)

post-install-isa-sparcv9:
	@rm $(INSTALLISADIR)/opt/csw/share/gettext/libintl.jar
	@cp $(FILEDIR)/libgettextlib-0.14.1.so.s9 $(INSTALLISADIR)/opt/csw/lib/64/libgettextlib-0.14.1.so
	@cp $(FILEDIR)/libintl.so.2.s9 $(INSTALLISADIR)/opt/csw/lib/64/libintl.so.2
	@cp $(FILEDIR)/libintl.so.3.s9 $(INSTALLISADIR)/opt/csw/lib/64/libintl.so.3
	$(DONADA)

post-install-isa-i386:
	@mkdir $(INSTALLISADIR)/opt/csw/share/java
	@mv $(INSTALLISADIR)/opt/csw/share/gettext/libintl.jar $(INSTALLISADIR)/opt/csw/share/java
	@cp $(FILEDIR)/libgettextlib-0.14.1.so.i $(INSTALLISADIR)/opt/csw/lib/libgettextlib-0.14.1.so
	@cp $(FILEDIR)/libintl.so.2.i $(INSTALLISADIR)/opt/csw/lib/libintl.so.2
	@cp $(FILEDIR)/libintl.so.3.i $(INSTALLISADIR)/opt/csw/lib/libintl.so.3
	$(DONADA)

post-install-isa-amd64:
	@rm $(INSTALLISADIR)/opt/csw/share/gettext/libintl.jar
	$(DONADA)
