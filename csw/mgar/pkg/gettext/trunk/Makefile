NAME = gettext
VERSION = 0.18.1.1
CATEGORIES = lib
GARTYPE = v2

DESCRIPTION = GNU locale utilities
define BLURB
	GNU gettext utilities are a set of tools that provides a framework to help other GNU packages produce multi-lingual messages
endef

# a few legacy packages that we still need to depend on for dependency reasons
# that we no longer want to rebuild and carry.
FOREIGN_PACKAGES += CSWlibgettextlib0-14-1
FOREIGN_PACKAGES += CSWlibgettextlib0-17
FOREIGN_PACKAGES += CSWlibgettextsrc0-17
FOREIGN_PACKAGES += CSWlibintl2
FOREIGN_PACKAGES += CSWlibintl3

BUILD_DEP_PKGS += CSWlibncurses-dev CSWlibxml2-dev CSWlibexpat-dev
BUILD_DEP_PKGS += CSWlibiconv-dev CSWggettext-dev

PACKAGES += CSWggettext
PACKAGES += CSWggettextdoc
PACKAGES += CSWlibasprintf0
PACKAGES += CSWlibgettextlib0-18-1
PACKAGES += CSWlibgettextpo0
PACKAGES += CSWlibgettextsrc0-18-1
PACKAGES += CSWlibintl8
PACKAGES += CSWggettext-dev
PACKAGES += CSWggettext-data
PACKAGES += CSWggettextrt

CATALOGNAME_CSWlibasprintf0 = libasprintf0
CATALOGNAME_CSWggettext = ggettext
CATALOGNAME_CSWggettextdoc = ggettextdoc
CATALOGNAME_CSWlibgettextlib0-18-1 = libgettextlib0_18_1
CATALOGNAME_CSWlibgettextpo0 = libgettextpo0
CATALOGNAME_CSWlibgettextsrc0-18-1 = libgettextsrc0_18_1
CATALOGNAME_CSWlibintl8 = libintl8
CATALOGNAME_CSWlibgettextlib0-18-1 = libgettextlib0_18_1
CATALOGNAME_CSWggettext-dev = ggettext_dev
CATALOGNAME_CSWggettext-data = ggettext_data
CATALOGNAME_CSWggettextrt = ggettextrt

SPKG_DESC_CSWggettext = GNU locale utilities
SPKG_DESC_CSWggettextdoc = GNU locale utility documentation
SPKG_DESC_CSWlibasprintf0 += GNU locale utilities, libasprintf.so.0
SPKG_DESC_CSWggettext-dev = GNU locale utilities, development files
SPKG_DESC_CSWlibgettextlib0-18-1 += GNU locale utilities, libgettextlib-0.18.1.so
SPKG_DESC_CSWlibgettextpo0 += GNU locale utilities, libgettextpo.so.0
SPKG_DESC_CSWlibgettextsrc0-18-1 += GNU locale utilities, libgettextsrc-0.18.1.so
SPKG_DESC_CSWlibintl8 += GNU locale utilities, libintl.so.8
SPKG_DESC_CSWlibgettextlib0-18-1 += GNU locale utilities, libgettextlib-0.18.1.so
SPKG_DESC_CSWggettext-data += GNU locale utilities, translation files
SPKG_DESC_CSWggettextrt += GNU locale utilities, transitional dependency package

RUNTIME_DEP_PKGS_CSWggettext += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWggettext += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWggettext += CSWlibgettextlib0-14-1
RUNTIME_DEP_PKGS_CSWggettext += CSWlibgettextlib0-17
RUNTIME_DEP_PKGS_CSWggettext += CSWlibgettextlib0-18-1
RUNTIME_DEP_PKGS_CSWggettext += CSWlibgettextsrc0-18-1
RUNTIME_DEP_PKGS_CSWggettext += CSWlibintl2
RUNTIME_DEP_PKGS_CSWggettext += CSWlibintl3
RUNTIME_DEP_PKGS_CSWggettext += CSWlibintl8
RUNTIME_DEP_PKGS_CSWggettext += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWggettext += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWggettext += CSWggettext-data
RUNTIME_DEP_PKGS_CSWggettext-dev += CSWlibasprintf0
RUNTIME_DEP_PKGS_CSWggettext-dev += CSWlibgettextlib0-18-1
RUNTIME_DEP_PKGS_CSWggettext-dev += CSWlibgettextpo0
RUNTIME_DEP_PKGS_CSWggettext-dev += CSWlibgettextsrc0-17
RUNTIME_DEP_PKGS_CSWggettext-dev += CSWlibgettextsrc0-18-1
RUNTIME_DEP_PKGS_CSWggettext-dev += CSWlibintl8
RUNTIME_DEP_PKGS_CSWggettextrt += CSWlibasprintf0
RUNTIME_DEP_PKGS_CSWggettextrt += CSWlibgettextpo0
RUNTIME_DEP_PKGS_CSWggettextrt += CSWlibintl2
RUNTIME_DEP_PKGS_CSWggettextrt += CSWlibintl3
RUNTIME_DEP_PKGS_CSWggettextrt += CSWlibintl8
RUNTIME_DEP_PKGS_CSWggettextrt += CSWggettext-data
RUNTIME_DEP_PKGS_CSWlibasprintf0 += CSWggettext-data
RUNTIME_DEP_PKGS_CSWlibgettextlib0-18-1 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgettextlib0-18-1 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgettextlib0-18-1 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibgettextlib0-18-1 += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWlibgettextlib0-18-1 += CSWggettext-data
RUNTIME_DEP_PKGS_CSWlibgettextpo0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgettextpo0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgettextpo0 += CSWggettext-data
RUNTIME_DEP_PKGS_CSWlibgettextsrc0-18-1 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgettextsrc0-18-1 += CSWlibgettextlib0-18-1
RUNTIME_DEP_PKGS_CSWlibgettextsrc0-18-1 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgettextsrc0-18-1 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibgettextsrc0-18-1 += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWlibgettextsrc0-18-1 += CSWggettext-data
RUNTIME_DEP_PKGS_CSWlibintl8 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibintl8 += CSWggettext-data

PKGFILES_CSWlibgettextlib0-18-1 += $(call baseisadirs,$(libdir),libgettextlib-0\.18\.1\.so)
PKGFILES_CSWlibgettextlib0-18-1 += $(call baseisadirs,$(libdir),libgettextlib-0\.18\.1\.so(\.\d+)*)
PKGFILES_CSWlibgettextpo0 += $(call baseisadirs,$(libdir),libgettextpo\.so\.0\.4\.0)
PKGFILES_CSWlibgettextpo0 += $(call baseisadirs,$(libdir),libgettextpo\.so\.0(\.\d+)*)
PKGFILES_CSWlibgettextpo0 += $(call baseisadirs,$(libdir),libgettextpo\.so\.0\.5\.1)
PKGFILES_CSWlibgettextsrc0-18-1 += $(call baseisadirs,$(libdir),libgettextsrc-0\.18\.1\.so)
PKGFILES_CSWlibgettextsrc0-18-1 += $(call baseisadirs,$(libdir),libgettextsrc-0\.18\.1\.so(\.\d+)*)
PKGFILES_CSWlibintl8 += $(call baseisadirs,$(libdir),libintl\.so\.8\.0\.2)
PKGFILES_CSWlibintl8 += $(call baseisadirs,$(libdir),libintl\.so\.8\.1\.1)
PKGFILES_CSWlibintl8 += $(call baseisadirs,$(libdir),libintl\.so\.8(\.\d+)*)
PKGFILES_CSWlibgettextlib0-18-1 += $(call baseisadirs,$(libdir),libgettextlib-0\.18\.1\.so)
PKGFILES_CSWlibgettextlib0-18-1 += $(call baseisadirs,$(libdir),libgettextlib-0\.18\.1\.so(\.\d+)*)
PKGFILES_CSWlibasprintf0 += $(call baseisadirs,$(libdir),libasprintf\.so\.0\.0\.0)
PKGFILES_CSWlibasprintf0 += $(call baseisadirs,$(libdir),libasprintf\.so\.0(\.\d+)*)
PKGFILES_CSWggettext-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWggettext-data += /opt/csw/share/locale/.*mo
PKGFILES_CSWggettextrt += /opt/csw/share/.*ggettextrt.*
PKGFILES_CSWggettextdoc = $(PKGFILES_DOC)

CHECKPKG_OVERRIDES_CSWggettextdoc += missing-dependency|CSWperl
CHECKPKG_OVERRIDES_CSWggettext += surplus-dependency|CSWggettext-data
CHECKPKG_OVERRIDES_CSWggettext += discouraged-path-in-pkgmap|/opt/csw/share/gettext/archive.git.tar.gz
CHECKPKG_OVERRIDES_CSWggettext += missing-dependency|CSWemacscommon
CHECKPKG_OVERRIDES_CSWggettextrt += surplus-dependency|CSWlibintl8
CHECKPKG_OVERRIDES_CSWggettextrt += surplus-dependency|CSWlibgettextpo0
CHECKPKG_OVERRIDES_CSWggettextrt += surplus-dependency|CSWggettext-data
CHECKPKG_OVERRIDES_CSWggettextrt += surplus-dependency|CSWlibasprintf0
CHECKPKG_OVERRIDES_CSWlibgettextpo0 += bad-rpath-entry|/opt/csw/lib/|opt/csw/lib/libgettextpo.so.0.4.0
CHECKPKG_OVERRIDES_CSWlibgettextpo0 += surplus-dependency|CSWggettext-data
CHECKPKG_OVERRIDES_CSWlibgettextsrc0-18-1 += surplus-dependency|CSWggettext-data
CHECKPKG_OVERRIDES_CSWlibgettextsrc0-18-1 += soname-equals-filename
CHECKPKG_OVERRIDES_CSWlibgettextlib0-18-1 += surplus-dependency|CSWggettext-data
CHECKPKG_OVERRIDES_CSWlibgettextlib0-18-1 += soname-equals-filename
CHECKPKG_OVERRIDES_CSWlibintl8 += surplus-dependency|CSWggettext-data
CHECKPKG_OVERRIDES_CSWlibasprintf0 += surplus-dependency|CSWggettext-data

CHECKPKG_OVERRIDES_CSWggettext += file-with-bad-content|/usr/local|root/opt/csw/share/aclocal/lib-prefix.m4
CHECKPKG_OVERRIDES_CSWggettext += file-with-bad-content|/usr/local|root/opt/csw/share/aclocal/lib-link.m4

CHECKPKG_OVERRIDES_CSWggettextdoc += file-with-bad-content

ARCHALL_CSWggettextrt = 1
ARCHALL_CSWggettext-data = 1
ARCHALL_CSWggettextdoc = 1

COMPILE_ELISP = 1

MASTER_SITES = $(GNU_MIRROR)

DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += CSWggettextdoc.cswreleasenotes
DISTFILES += CSWggettext.cswreleasenotes

PATCHFILES += 0001-Use-the-auto-detected-SHELL-to-run-convert-archive.patch
PATCHFILES += 0002-Update-ltmain.sh-to-prevent-libtool-stripping-runpat.patch

#This patch is not a simple 'make it compile' so we flag the feature
#patch below
PATCHFILES += 0003-Patch-around-thread-handling-differences-between-9-a.patch
VERSION_FLAG_PATCH = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --program-prefix=g
#Dont' depend on packages that depend on me
CONFIGURE_ARGS += --with-included-glib
CONFIGURE_ARGS += --with-included-libcroco
#No glibc
CONFIGURE_ARGS += --with-included-gettext

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64_LIBS_ONLY = 1
STRIP_LIBTOOL = 1
EXTRA_LINKER_FLAGS = -xnorunpath

#NOTE: gettext tests are sensitive to bash environment variables, make sure
#      custom paths are prefixed by $PATH, may be better to set aside
#      ~/.bashrc, etc. during build.
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
	$(MAKECOOKIE)

post-install-isa-sparcv9:
	@rm $(INSTALLISADIR)/opt/csw/share/gettext/libintl.jar
	$(MAKECOOKIE)

post-install-isa-i386:
	@mkdir $(INSTALLISADIR)/opt/csw/share/java
	@mv $(INSTALLISADIR)/opt/csw/share/gettext/libintl.jar $(INSTALLISADIR)/opt/csw/share/java
	$(MAKECOOKIE)

post-install-isa-amd64:
	@rm $(INSTALLISADIR)/opt/csw/share/gettext/libintl.jar
	$(MAKECOOKIE)

post-merge:
	@echo "Setting up gnu links..."
	@(cd $(PKGROOT)$(prefix); \
		mkdir gnu; cd gnu; \
		for f in ../bin/g*; do \
			echo Linking $$f; \
			base=$$(basename $$f); \
			gln -s $$f ./$${base/g/}; \
		done )
	@echo "Fixing usr/local and usr/share references..."
	@(cd $(PKGROOT); \
		find .$(docdir) .$(datadir)/aclocal -type f -print0 | \
		xargs -0 perl -pi \
			-e "s#/usr/share#/opt/csw/share#g;" \
			-e "s#/usr/local#/opt/csw#g;"; \
		perl -pi \
			-e "s#/usr/share#/opt/csw/share#g;" \
			-e "s#/usr/local#/opt/csw#g;" \
				.$(bindir)/ggettextize \
				.$(infodir)/gettext.info; )
