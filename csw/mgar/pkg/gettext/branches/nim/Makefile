NAME = gettext
VERSION = 0.18.1.1
GARTYPE = bts lib
GARTYPE = v2

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

DESCRIPTION = GNU locale utilities
define BLURB
	GNU gettext utilities are a set of tools that provides a framework to help other GNU packages produce multi-lingual messages
endef

# a few legacy packages that we still need to depend on for dependency reasons
# that we no longer want to rebuild and carry.
FORNIMOSSlibgettextlib0-14-1
FOREIGN_PACKAGES += NIMOSSlibgettextlib0-17
FOREIGN_PACKAGES += NIMOSSlibgettextsrc0-17
FOREIGN_PACKAGES += NIMOSSlibintl2
FOREIGN_PACKAGES += NIMOSSlibintl3

BUILD_DEP_PKGS += NIMOSSlibncurses-dev NIMOSSlibxml2-dev NIMOSSlibexpat-dev
BUILD_DEP_PKGS += NIMOSSlibiconv-dev NIMOSSggettext-dev

PACKAGES += NIMOSSggettext
PACKAGES += NIMOSSggettextdoc
PACKAGES += NIMOSSlibasprintf0
PACKAGES += NIMOSSlibgettextlib0-18-1
PACKAGES += NIMOSSlibgettextpo0
PACKAGES += NIMOSSlibgettextsrc0-18-1
PACKAGES += NIMOSSlibintl8
PACKAGES += NIMOSSggettext-dev
PACKAGES += NIMOSSggettext-data
PACKAGES += NIMOSSggettextrt

CATALOGNAME_NIMOSSlibasprintf0 = libasprintf0
CATALOGNAME_NIMOSSggettext = ggettext
CATALOGNAME_NIMOSSggettextdoc = ggettextdoc
CATALOGNAME_NIMOSSlibgettextlib0-18-1 = libgettextlib0_18_1
CATALOGNAME_NIMOSSlibgettextpo0 = libgettextpo0
CATALOGNAME_NIMOSSlibgettextsrc0-18-1 = libgettextsrc0_18_1
CATALOGNAME_NIMOSSlibintl8 = libintl8
CATALOGNAME_NIMOSSlibgettextlib0-18-1 = libgettextlib0_18_1
CATALOGNAME_NIMOSSggettext-dev = ggettext_dev
CATALOGNAME_NIMOSSggettext-data = ggettext_data
CATALOGNAME_NIMOSSggettextrt = ggettextrt

SPKG_DESC_NIMOSSggettext = GNU locale utilities
SPKG_DESC_NIMOSSggettextdoc = GNU locale utility documentation
SPKG_DESC_NIMOSSlibasprintf0 += GNU locale utilities, libasprintf.so.0
SPKG_DESC_NIMOSSggettext-dev = GNU locale utilities, development files
SPKG_DESC_NIMOSSlibgettextlib0-18-1 += GNU locale utilities, libgettextlib-0.18.1.so
SPKG_DESC_NIMOSSlibgettextpo0 += GNU locale utilities, libgettextpo.so.0
SPKG_DESC_NIMOSSo.0
SPKG_DESC_CSWlibgettextsrc0-18-1 += GNU locale utilities, libgettextsrc-0.1NIMOSSlibintl8 += GNU locale utilities, libintl.so.8
SPKG_DESC_NIMOSSlibgettextlib0-18-1 += GNU locale utilities, libgettextlib-0.18.1.so
SPKG_DESC_NIMOSSggettext-data += GNU locale utilities, translation files
SPKG_DESC_NIMOSSggettextrt += GNU locale utilities, transitional dependency package

RUNTIME_DEP_PKGS_NIMOSSggettext += NIMOSSlibexpat1
RUNTIME_DEP_PKGS_NIMOSSggettext += NIMOSSlibiconv2
RUNTIME_DEP_PKGS_NIMOSSggettext += NIMOSSlibgettextlib0-14-1
RUNTIME_DEP_PKGS_NIMOSSggettext += NIMOSSlibgettextlib0-17
RUNTIME_DEP_PKGS_NIMOSSggettext += NIMOSSlibgettextlib0-18-1
RUNTIME_DEP_PKGS_NIMOSSggettext += NIMOSSlibgettextsrc0-18-1
RUNTIME_DEP_PKGS_NIMOSSggettext += NIMOSSlibintl2
RUNTIME_DEP_PKGS_NIMOSSggettext += NIMOSSlibintl3
RUNTIME_DEP_PKGS_NIMOSSggettext += NIMOSSlibintl8
RUNTIME_DEP_PKGS_NIMOSSggettext += NIMOSSlibxml2-2
RUNTIME_DEP_PKGS_NIMOSSggettext += NIMOSSlibncurses5
RUNTIME_DEP_PKGS_NIMOSSggettext += NIMOSSggettext-data
RUNTIME_DEP_PKGS_NIMOSSggettext-dev += NIMOSSlibasprintf0
RUNTIME_DEP_PKGS_NIMOSSggettext-dev += NIMOSSlibgettextlib0-18-1
RUNTIME_DEP_PKGS_NIMOSSggettext-dev += NIMOSSlibgettextpo0
RUNTIME_DEP_PKGS_NIMOSSggettext-dev += NIMOSSlibgettextsrc0-17
RUNTIME_DEP_PKGS_NIMOSSggettext-dev += NIMOSSlibgettextsrc0-18-1
RUNTIME_DEP_PKGS_NIMOSSggettext-dev += NIMOSSlibintl8
RUNTIME_DEP_PKGS_NIMOSSggettextrt += NIMOSSlibasprintf0
RUNTIME_DEP_PKGS_NIMOSSggettextrt += NIMOSSlibgettextpo0
RUNTIME_DEP_PKGS_NIMOSSggettextrt += NIMOSSlibintl2
RUNTIME_DEP_PKGS_NIMOSSggettextrt += NIMOSSlibintl3
RUNTIME_DEP_PKGS_NIMOSSggettextrt += NIMOSSlibintl8
RUNTIME_DEP_PKGS_NIMOSSggettextrt += NIMOSSggettext-data
RUNTIME_DEP_PKGS_NIMOSSlibasprintf0 += NIMOSSggettext-data
RUNTIME_DEP_PKGS_NIMOSSlibgettextlib0-18-1 += NIMOSSlibiconv2
RUNTIME_DEP_PKGS_NIMOSSlibgettextlib0-18-1 += NIMOSSlibintl8
RUNTIME_DEP_PKGS_NIMOSSlibgettextlib0-18-1 += NIMOSSlibxml2-2
RUNTIME_DEP_PKGS_NIMOSSlibgettextlib0-18-1 += NIMOSSlibncurses5
RUNTIME_DEP_PKGS_NIMOSSlibgettextlib0-18-1 += NIMOSSggettext-data
RUNTIME_DEP_PKGS_NIMOSSlibgettextpo0 += NIMOSSlibiconv2
RUNTIME_DEP_PKGS_NIMOSSlibgettextpo0 += NIMOSSlibintl8
RUNTIME_DEP_PKGS_NIMOSSlibgettextpo0 += NIMOSSggettext-data
RUNTIME_DEP_PKGS_NIMOSSlibgettextsrc0-18-1 += NIMOSSlibiconv2
RUNTIME_DEP_PKGS_NIMOSSlibgettextsrc0-18-1 += NIMOSSlibgettextlib0-18-1
RUNTIME_DEP_PKGS_NIMOSSlibgettextsrc0-18-1 += NIMOSSlibintl8
RUNTIME_DEP_PKGS_NIMOSSlibgettextsrc0-18-1 += NIMOSSlibxml2-2
RUNTIME_DEP_PKGS_NIMOSSlibgettextsrc0-18-1 += NIMOSSlibncurses5
RUNTIME_DEP_PKGS_NIMOSSlibgettextsrc0-18-1 += NIMOSSggettext-data
RUNTIME_DEP_PKGS_NIMOSSlibintl8 += NIMOSSlibiconv2
RUNTIME_DEP_PKGS_NIMOSSlibintl8 += NIMOSSggettext-data

PKGFILES_NIMOSSlibgettextlib0-18-1 += $(call baseisadirs,$(libdir),libgettextlib-0\.18\.1\.so)
PKGFILES_NIMOSSlibgettextlib0-18-1 += $(call baseisadirs,$(libdir),libgettextlib-0\.18\.1\.so(\.\d+)*)
PKGFILES_NIMOSSlibgettextpo0 += $(call baseisadirs,$(libdir),libgettextpo\.so\.0\.4\.0)
PKGFILES_NIMOSSlibgettextpo0 += $(call baseisadirs,$(libdir),libgettextpo\.so\.0(\.\d+)*)
PKGFILES_NIMOSS+)*)
PKGFILES_CSWlibgettextpo0 += $(call baseisadirs,$(libdir),libgettextpo\.so\.0NIMOSSlibgettextsrc0-18-1 += $(call baseisadirs,$(libdir),libgettextsrc-0\.18\.1\.so)
PKGFILES_NIMOSS.so)
PKGFILES_CSWlibgettextsrc0-18-1 += $(call baseisadirs,$(libdir),libgettextsrc-0\.18\.1\.so(\NIMOSSlibintl8 += $(call baseisadirs,$(libdir),libintl\.so\.8\.0\.2)
PKGFILES_NIMOSSlibintl8 += $(call baseisadirs,$(libdir),libintl\.so\.8\.1\.1)
PKGFILES_NIMOSSlibintl8 += $(call baseisadirs,$(libdir),libintl\.so\.8(\.\d+)*)
PKGFILES_NIMOSSlibgettextlib0-18-1 += $(call baseisadirs,$(libdir),libgettextlib-0\.18\.1\.so)
PKGFILES_NIMOSSlibgettextlib0-18-1 += $(call baseisadirs,$(libdir),libgettextlib-0\.18\.1\.so(\.\d+)*)
PKGFILES_NIMOSSlibasprintf0 += $(call baseisadirs,$(libdir),libasprintf\.so\.0\.0\.0)
PKGFILES_NIMOSS\.0)
PKGFILES_CSWlibasprintf0 += $(call baseisadirs,$(libdir),libasprintf\.so\.0(\NIMOSSggettext-dev += $(PKGFILES_DEVEL_CONFIG)
PKGFILES_NIMOSSggettext-dev += $(PKGFILES_DEVEL_STATICLIB)
PKGFILES_NIMOSSggettext-dev += $(PKGFILES_DEVEL_LIBTOOL)
PKGFILES_NIMOSSggettext-dev += $(PKGFILES_DEVEL_PKGCONFIG)
PKGFILES_NIMOSSggettext-dev += $(PKGFILES_DEVEL_INCLUDEDIR)
PKGFILES_NIMOSSggettext-dev += $(PKGFILES_DEVEL_ACLOCAL)
PKGFILES_NIMOSSggettext-dev += $(PKGFILES_DEVEL_CONFIG_MANPAGE)
PKGFILES_NIMOSSggettext-dev += $(PKGFILES_DEVEL_MAN3_MANPAGE)
PKGFILES_NIMOSSggettest-dev += $(libdir)/libgettextlib.so
PKGFILES_NIMOSSggettest-dev += $(libdir)/libgettextpo.so
PKGFILES_NIMOSSggettest-dev += $(libdir)/libgettextsrc.so
PKGFILES_NIMOSSggettest-dev += $(libdir)/libintl.so
PKGFILES_NIMOSSggettext-data += /opt/csw/share/locale/.*mo
PKGFILES_NIMOSSggettextrt += /opt/csw/share/.*ggettextrt.*
PKGFILES_NIMOSSggettextdoc = $(PKGFILES_DOC)

CHECKPKG_OVERRIDES_NIMOSSggettextdoc += missing-dependency|NIMOSSperl
CHECKPKG_OVERRIDES_NIMOSSggettext += surplus-dependency|NIMOSSggettext-data
CHECKPKG_OVERRIDES_NIMOSSggettext += discouraged-path-in-pkgmap|/opt/csw/share/gettext/archive.git.tar.gz
CHECKPKG_OVERRIDES_NIMOSSggettext += missing-dependency|NIMOSSemacscommon
CHECKPKG_OVERRIDES_NIMOSSggettextrt += surplus-dependency|NIMOSSlibintl8
CHECKPKG_OVERRIDES_NIMOSSggettextrt += surplus-dependency|NIMOSSlibgettextpo0
CHECKPKG_OVERRIDES_NIMOSSggettextrt += surplus-dependency|NIMOSSggettext-data
CHECKPKG_OVERRIDES_NIMOSSggettextrt += surplus-dependency|NIMOSSlibasprintf0
CHECKPKG_OVERRIDES_NIMOSSlibgettextpo0 += bad-rpath-entry|/opt/csw/lib/|opt/csw/lib/libgettextpo.so.0.4.0
CHECKPKG_OVERRIDES_NIMOSSlibgettextpo0 += surplus-dependency|NIMOSSggettext-data
CHECKPKG_OVERRIDES_NIMOSSlibgettextsrc0-18-1 += surplus-dependency|NIMOSSggettext-data
CHECKPKG_OVERRIDES_NIMOSSlibgettextsrc0-18-1 += soname-equals-filename
CHECKPKG_OVERRIDES_NIMOSSlibgettextlib0-18-1 += surplus-dependency|NIMOSSggettext-data
CHECKPKG_OVERRIDES_NIMOSSlibgettextlib0-18-1 += soname-equals-filename
CHECKPKG_OVERRIDES_NIMOSSlibintl8 += surplus-dependency|NIMOSSggettext-data
CHECKPKG_OVERRIDES_NIMOSSlibasprintf0 += surplus-dependency|NIMOSSggettext-data

CHECKPKG_OVERRIDES_NIMOSSggettext += file-with-bad-content|/usr/local|root/opt/csw/share/aclocal/lib-prefix.m4
CHECKPKG_OVERRIDES_NIMOSSPKG_OVERRIDES_CSWggettext += file-with-bad-content|/usr/local|root/opt/csw/share/aclocal/lib-link.m4

CHNIMOSSggettextdoc += file-with-bad-content

ARCHALL_NIMOSSggettextrt = 1
ARCHALL_NIMOSSggettext-data = 1
ARCHALL_NIMOSSggettextdoc = 1

COMPILE_ELISP = 1

MASTER_SITES = $(GNU_MIRROR)

DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += NIMOSSggettextdoc.cswreleasenotes
DISTFILES += NIMOSS
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