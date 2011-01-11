NAME = gettext
VERSION = 0.18.1.1
CATEGORIES = lib

DESCRIPTION = GNU locale utilities
define BLURB
	GNU gettext utilities are a set of tools that provides a framework to help other GNU packages produce multi-lingual messages
endef

PACKAGES = CSWggettextrt CSWggettextdoc CSWggettext
PACKAGES += CSWlibasprintf0 CSWlibgettextlib0-14-1 CSWlibgettextlib0-17
PACKAGES += CSWlibgettextlib0-18-1 CSWlibgettextpo0 CSWlibgettextsrc0-17
PACKAGES += CSWlibgettextsrc0-18-1 CSWlibintl2 CSWlibintl3 CSWlibintl8

ARCHALL_CSWggettextel = 1

CATALOGNAME_CSWggettext = ggettext
CATALOGNAME_CSWggettextdoc = ggettextdoc
CATALOGNAME_CSWggettextrt = ggettextrt
CATALOGNAME_CSWlibasprintf0 = libasprintf0
CATALOGNAME_CSWlibgettextlib0-14-1 = libgettextlib0_14_1
CATALOGNAME_CSWlibgettextlib0-17 = libgettextlib0_17
CATALOGNAME_CSWlibgettextlib0-18-1 = libgettextlib0_18_1
CATALOGNAME_CSWlibgettextpo0 = libgettextpo0
CATALOGNAME_CSWlibgettextsrc0-17 = libgettextsrc0_17
CATALOGNAME_CSWlibgettextsrc0-18-1 = libgettextsrc0_18_1
CATALOGNAME_CSWlibintl2 = libintl2
CATALOGNAME_CSWlibintl3 = libintl3
CATALOGNAME_CSWlibintl8 = libintl8
SPKG_DESC_CSWggettext = GNU locale utilities and development headers
SPKG_DESC_CSWggettextdoc = GNU locale documentation
SPKG_DESC_CSWggettextrt = GNU locale runtime
SPKG_DESC_CSWlibasprintf0 = GNU locale runtime, libasprintf.so.0
SPKG_DESC_CSWlibgettextlib0-14-1 += GNU locale runtime, libgettextlib-0.14.1.so
SPKG_DESC_CSWlibgettextlib0-17 += GNU locale runtime, libgettextlib-0.17.so
SPKG_DESC_CSWlibgettextlib0-18 += GNU locale runtime, libgettextlib-0.1.1.so
SPKG_DESC_CSWlibgettextpo0 += GNU locale runtime, libgettextpo.so.0
SPKG_DESC_CSWlibgettextsrc0-17 += GNU locale runtime, libgettextsrc-0.17.so
SPKG_DESC_CSWlibgettextsrc0-18-1 += GNU locale runtime, libgettextsrc-0.18.1.so
SPKG_DESC_CSWlibintl2 += GNU locale runtime, libintl.so.2
SPKG_DESC_CSWlibintl3 += GNU locale runtime, libintl.so.3
SPKG_DESC_CSWlibintl8 += GNU locale runtime, libintl.so.8

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

RUNTIME_DEP_PKGS_CSWggettextrt = CSWiconv CSWlibxml2 CSWncurses
RUNTIME_DEP_PKGS_CSWggettext = CSWggettextrt CSWiconv CSWexpat CSWncurses
RUNTIME_DEP_PKGS_CSWggettext += CSWlibxml2
RUNTIME_DEP_PKGS_CSWggettextdoc = CSWggettext

#NOTE: gettext tests are sensitive to bash environment variables, make sure
#      custom paths are prefixed by $PATH, may be better to set aside
#      ~/.bashrc, etc. during build.
TEST_TARGET = check

#provided by iconv
MERGE_EXCLUDE_FILES  = .*/charset.alias
MERGE_EXCLUDE_FILES += .*/locale.alias
MERGE_EXCLUDE_FILES += .*/iconv.m4
MERGE_EXCLUDE_FILES += /opt/csw/bin/$(ISA)/.*

#This syntaxt skips 64-bit for some reason
#PKGFILES_CSWggettextrt  = $(call baseisadirs,$(libdir),libintl\..*)
#PKGFILES_CSWggettextrt += $(call baseisadirs,$(libdir),libasprintf\..*)
#PKGFILES_CSWggettextrt += $(call baseisadirs,$(libdir),libgettextpo\..*) 
PKGFILES_CSWlibasprintf0 += $(call baseisadirs,$(libdir),libasprintf\.so\.0(\.\d+)*)
PKGFILES_CSWlibgettextlib0-14-1 += $(call baseisadirs,$(libdir),libgettextlib-0.14\.1\.so)
PKGFILES_CSWlibgettextlib0-14-1 += $(call baseisadirs,$(libdir),libgettextlib-0\.14\.1\.so(\.\d+)*)
PKGFILES_CSWlibgettextlib0-18-1 += $(call baseisadirs,$(libdir),libgettextlib-0\.18\.1\.so)
PKGFILES_CSWlibgettextlib0-18-1 += $(call baseisadirs,$(libdir),libgettextlib-0\.18\.1\.so(\.\d+)*)
PKGFILES_CSWlibgettextpo0 += $(call baseisadirs,$(libdir),libgettextpo\.so\.0\.4\.0)
PKGFILES_CSWlibgettextpo0 += $(call baseisadirs,$(libdir),libgettextpo\.so\.0(\.\d+)*)
PKGFILES_CSWlibgettextsrc0-17 += $(call baseisadirs,$(libdir),libgettextsrc-0\.17\.so)
PKGFILES_CSWlibgettextsrc0-17 += $(call baseisadirs,$(libdir),libgettextsrc-0\.17\.so(\.\d+)*)
PKGFILES_CSWlibgettextsrc0-18-1 += $(call baseisadirs,$(libdir),libgettextsrc-0\.18\.1\.so)
PKGFILES_CSWlibgettextsrc0-18-1 += $(call baseisadirs,$(libdir),libgettextsrc-0\.18\.1\.so(\.\d+)*)
PKGFILES_CSWlibintl2 += $(call baseisadirs,$(libdir),libintl\.so\.2)
PKGFILES_CSWlibintl2 += $(call baseisadirs,$(libdir),libintl\.so\.2(\.\d+)*)
PKGFILES_CSWlibintl3 += $(call baseisadirs,$(libdir),libintl\.so\.3)
PKGFILES_CSWlibintl3 += $(call baseisadirs,$(libdir),libintl\.so\.3(\.\d+)*)
PKGFILES_CSWlibintl8 += $(call baseisadirs,$(libdir),libintl\.so\.8\.0\.2)
PKGFILES_CSWlibintl8 += $(call baseisadirs,$(libdir),libintl\.so\.8(\.\d+)*)
PKGFILES_CSWlibintl8 += $(call baseisadirs,$(libdir),libintl\.so\.8\.1\.1)
PKGFILES_CSWlibintl8 += $(call baseisadirs,$(libdir),libintl\.so\.8(\.\d+)*)

#so use this for now
PKGFILES_CSWggettextrt  = .*/libintl\.so.* .*/libasprintf\.so.* .*/libgettextpo\.so.*
PKGFILES_CSWggettextrt += .*/libgettext.*\.so.*
PKGFILES_CSWggettextrt += /opt/csw/bin/ggettext /opt/csw/bin/gngettext /opt/csw/bin/genvsubst
PKGFILES_CSWggettextrt += /opt/csw/bin/ggettext.sh /opt/csw/share/java/libintl.jar
PKGFILES_CSWggettextrt += /opt/csw/share/locale/.*
PKGFILES_CSWggettextdoc  = $(PKGFILES_DOC)

CHECKPKG_OVERRIDES_CSWggettextdoc += missing-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWggettextdoc += surplus-dependency|CSWggettext
CHECKPKG_OVERRIDES_CSWggettextel += surplus-dependency|CSWggettext
# This lib is legacy from the old versions and can't be updated (easily)
CHECKPKG_OVERRIDES_CSWggettext += bad-rpath-entry|/export/home/phil/build/gettext-0.14.1/gettext-tools/intl/.libs|opt/csw/lib/sparcv9/libgettextlib-0.14.1.so 
# A few more legacy libs that we can't update.
CHECKPKG_OVERRIDES_CSWggettextrt += bad-rpath-entry|/opt/csw/lib/|opt/csw/lib/libgettextlib-0.17.so
CHECKPKG_OVERRIDES_CSWggettextrt += bad-rpath-entry|/opt/csw/lib/|opt/csw/lib/libgettextsrc-0.17.so
CHECKPKG_OVERRIDES_CSWggettextrt += bad-rpath-entry|/opt/csw/lib/|opt/csw/lib/libgettextpo.so.0.4.0
# just until checkpkg doesn't squawk about this.
CHECKPKG_OVERRIDES_CSWggettext += missing-dependency|CSWemacscommon

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
