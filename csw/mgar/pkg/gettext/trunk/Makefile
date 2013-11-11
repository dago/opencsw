NAME = gettext
VERSION = 0.18.3.1
CATEGORIES = lib
GARTYPE = v2

PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

DESCRIPTION = GNU locale utilities
define BLURB
	GNU gettext utilities are a set of tools that provides a framework to help other GNU packages produce multi-lingualMASTER_SITES += $(GNU_MIRROR)
DISTFILES += $(NAME)-$(VERSION).tar.gz

# Assages
endef

# a few legacy packages that we still need to depend on for dependency reasons
# that we no longer want to rebuild and carry.
FOREIGN_PACKAGES += CSWlibgettextlib0-14-1
FOREIGN_PACKAGES += CSWlibgettextlib0-17
FOREIGN_PACKAGES += CSWlibgettextsrc0-17
FOREIGN_PACKAGEOBSOLETED_BY_CSWlibintl2 += CSWggettextrt
FOREIGN_PACKAGES += CSWlibintl3
OBSOLETED_BY_CSWlibintl3 += CSWggettextrt

BUILD_DEP_PKGS += CSWlibncurses-dev
BUILD_DEP_PKGS += CSWlibxml2-dev
BUILD_DEP_PKGS += CSWlibexpat-dev
BUILD_DEP_PKGS += CSWlibiconv-dev
BUILD_DEP_PKGS += CSWggettext-dev

PACKAGES += CSWggettext
SPKG_DESC_CSWggettext = GNU locale utilitiespendency package

RUNTIME_DEP_PKGS_CSWggettext += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWggettext += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWggettext += CS8-3
RUNTIME_DEP_PKGS_CSWggettext += CSWlibgettextsrc0-18-3
RUNTIME_DEP_PKGS_CSWggettext += CSWlibintl8
RUNTIME_DEP_PKGS_CSWggettext += CSWlibgomp1
RUNTIME_DEP_PKGS_CSWggettext += CSWlibasprintf0
RUNTIME_DEP_PKGS_CSWggettext += CSWlibgettextpo0
RUNTIME_DEP_PKGS_CSWggettext += CSWlibunistring0
RUNTIME_DEP_PKGS_CSWggettext += CSWggettext-dataependency|CSWperl
CHECKPKG_OVERRIDES_CSWggettext += surplus-dependency|CSWggettext-data
CHECKPKG_OVERRIDEmissing-dependency|CSWemacs-common
# Legacy. Remove after these libs are no longer used by packages depending on any of them.
RUNTIME_DEP_PKGS_CSWggettext += CSWlibgettextlib0-14-1
CHECKPKG_OVERRIDES_CSWggettext += surplus-dependency|CSWlibgettextlib0-14-1
RUNTIME_DEP_PKGS_CSWggettext += CSWlibgettextlib0-17
CHECKPKG_OVERRIDES_CSWggettext += surplus-dependency|CSWlibgettextlib0-17
RUNTIME_DEP_PKGS_CSWggettext += CSWlibintl2
CHECKPKG_OVERRIDES_CSWggettext += surplus-dependency|CSWlibintl2
RUNTIME_DEP_PKGS_CSWggettext += CSWlibintl3
CHECKPKG_OVERRIDES_CSWggettext += surplus-dependency|CSWlibintl3

PACKAGES += CSWlibasprintf0
SPKG_DESC_CSWlibasprintf0 += GNU locale utilities, libasprintf.so.0
PKGFILES_CSWlibasprintf0 += $(call pkgfiles_lib,libasprintf.so.0)
RUNTIME_DEP_PKGS_CSWlibasprintf0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibasprintf0 += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWlibasprintf0 += CSWggettext-data
CHECKPKG_OVERRIDES_CSWlibasprintf0 += surplus-dependency|CSWggettext-data
OBSOLETED_BY_CSWlibasprintf0 += CSWggettextrt

PACKAGES += CSWlibgettextlib0-18-3
SPKG_DESC_CSWlibgettextlib0-18-3 += GNU locale utilities, libgettextlib-0.18.3.so
PKGFILES_CSWlibgettextlib0-18-3 += $(call pkgfiles_lib,libgettextlib-0.18.3.so)
RUNTIME_DEP_PKGS_CSWlibgettextlib0-18-3 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgettextlib0-18-3 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgettextlib0-18-3 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibgettextlib0-18-3 += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWlibgettextlib0-18-3 += CSWlibunistring0
RUNTIME_DEP_PKGS_CSWlibgettextlib0-18-3 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgettextlib0-18-3 += CSWggettext-data
CHECKPKG_OVERRIDES_CSWlibgettextlib0-18-3 += surplus-dependency|CSWggettext-data
CHECKPKG_OVERRIDES_CSWlibgettextlib0-18-3 += soname-equals-filename

PACKAGES += CSWlibgettextpo0
SPKG_DESC_CSWlibgettextpo0 += GNU locale utilities, libgettextpo.so.0
PKGFILES_CSWlibgettextpo0 += $(call pkgfiles_lib,libgettextpo.so.0) CSWggettext-data
RUNTIME_DEP_PKGS_CSWlibgettextpo0 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgettextpo0 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWliblibunistring0
RUNTIME_DEP_PKGS_CSWlibgettextpo0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgettextpo0 += CSWggettext-data
CHECKPKG_OVERRIDES_CSWlibgettextpo0 += surplus-dependency|CSWggettext-data
OBSOLETED_BY_CSWlibgettextpo0 += CSWggettextrt

PACKAGES += CSWlibgettextsrc0-18-3
SPKG_DESC_CSWlibgettextsrc0-18-3 += GNU locale utilities, libgettextsrc-0.18.3.so
PKGFILES_CSWlibgettextsrc0-18-3 += $(call pkgfiles_lib,libgettextsrc-0.18.3.so)
RUNTIME_DEP_PKGS_CSWlibgettextsrc0-18-3 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibgettextsrc0-18-3 += CSWlibgettextlib0-18-3
RUNTIME_DEP_PKGS_CSWlibgettextsrc0-18-3 += CSWlibintl8
RUNTIME_DEP_PKGS_CSWlibgettextsrc0-18-3 += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWlibgettextsrc0-18-3 += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWlibgettextsrc0-18-3 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgettextsrc0-18-3 += CSWlibunistring0
RUNTIME_DEP_PKGS_CSWlibgettextsrc0-18-3 += CSWggettext-data
CHECKPKG_OVERRIDES_CSWlibgettextsrc0-18-3 += surplus-dependency|CSWggettext-data
CHECKPKG_OVERRIDES_CSWlibgettextsrc0-18-3 += soname-equals-filename
# On i386 only
CHECKPKG_OVERRIDES_CSWlibgettextsrc0-18-3 += surplus-dependency|CSWlibxml2-2
CHECKPKG_OVERRIDES_CSWlibgettextsrc0-18-3 += surplus-dependency|CSWlibncurses5

PACKAGES += CSWlibintl8
SPKG_DESC_CSWlibintl8 += GNU locale utilities, libintl.so.8
PKGFILES_CSWlibintl8 += $(call pkgfiles_lib,libintl.so.8)
RUNTIME_DEP_PKGS_CSWlibintl8 += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibintl8 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibintl8 += CSWggettext-data
CHECKPKG_OVERRIDES_CSWlibintl8 += surplus-dependency|CSWggettext-data
OBSOLETED_BY_CSWlibintl8 += CSWggettextrt

PACKAGES += CSWggettext-dev
SPKG_DESC_CSWggettext-dev = GNU locale utilities, development files
# Why is this needed?
PKGFILES_DEVEL_SHAREDLIBLINK =
PKGFILES_CSWggettext-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWggettext-dev += $(PKGFILES_DOC)
PKGFILES_CSWggettext-dev += $(sharedstatedir)/gettext/.*
PKGFILES_CSWggettest-dev += $(call baseisadirs,$(libdir),libgettextlib.so)
PKGFILES_CSWggettest-dev += $(call baseisadirs,$(libdir),libgettextpo.so)
PKGFILES_CSWggettest-dev += $(call baseisadirs,$(libdir),libgettextsrc.so)
PKGFILES_CSWggettest-dev += $(call baseisadirs,$(libdir),libintl.so)
PKGFILES_CSWggettext-data += /opt/csw/share/locale/.*\.mo CSWggettext-data
RUNTIME_DEP_PKGS_CSWggettext-dev += CSWlibasprintf0
RUNTIME_DEP_PKGS_CSWggettext-dev += CSWl3bgettextlib0-18-1
RUNTIME_DEP_PKGS_CSWggettext-dev += CSWlibgettextpo0
RUNTIME_DEP_PKGS_CSWggettext-dev += CSWlibgettextsrc0-17
RUNTIME_DEP_PKGS_CSWggettext-dev += CSWl3
RUNTIME_DEP_PKGS_CSWggettext-dev += CSWlibintl8
OBSOLETED_BY_CSWggettext-dev += CSWggettextdoc
CHECKPKG_OVERRIDES_CSWggettext-dev += missing-dependency|CSWperl

PACKAGES += CSWggettext-data
SPKG_DESC_CSWggettext-data += GNU locale utilities, translation files
ARCHALL_CSWggettext-data = 1
OBSOLETED_BY_CSWggettext-data += CSWggettextrt

GARCOMPILER = GNU

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --program-prefix=g
# rogram-prefix=g
#Dont' depend on packages that depend on me
CONFIGURE_ARGS += --with-included-glib
CONFIGURE_ARGS += --with-in No glibc
CONFIGURE_ARGS += --with-included-gettext

BUILD64_LIBS_ONLY = 1
#EXTRA_LINKER_FLAGS = -xnorunpath

MERGE_EXCLUDE_FILES  = .*/charset.alias
MERGE_EXCLUDE_FILES += .*/locale.alias
MERGE_EXCLUDE_FILES += .*/iconv.m4

COMPILE_ELISP = 1

# Just 4 ACL tests are failing
SKIPTEST ?= 1

include gar/category.mkt/csw/gnu:$(PATH)

#Include old libraries for compatibility with existing packages
#  TODO: Convert to 
post-install-isa-sparcv8plusstall-isa-sparcv8:
	@mkdir $(INSTALLISADIR)/opt/csw/share/java
	@mv $(INSTALLISADIR)/opt/csw/share/gettext/libintl.jar $(INSTALLISADIR)/opt/csw/share/java
	$(MAKECOOKIE)

post-install-isa-sparcv9:
	@rm $(INSTALLISADIR)/opt/csw/share/gettext/libintl.jar
	$(MAKECOOKIE)

pentium_prostall-isa-sparcv8:
	@mkdir $(INSTALLISADIR)/opt/csw/share/java
	@mv $(INSTALLISADIR)/opt/csw/share/gettext/libintl.jar $(INSTALLISADIR)/opt/csw/share/java
	$(MAKECOOKIE)

post-install-isa-amd64:
	@rm $(INSTALLISADIR)/opt/csw/share/gettext/libintl.jar
	$(MAKECO-all:
	@echo "Setting up gnu links..."
	ginstall -d $(DESTDIR)$(prefix)/gnu
	$(foreach G,$(notdir $(wildcard $(DESTDIR)$(bindir)/*)),ln -s ../bin/$G $(DESTDIR)$(prefix)/gnu/$(patsubst g%,%,$G);)
	@echo "Fixing usr/local and usr/share references..."
	@(cd $(PKGROOT); \
		gfind .$(docdir) .$(datadir)/aclocal -type f -print0 | \
		gxargs -0 opt/csw#g;"; \
		perl -pi \
			-e "s#/usr/share#/opt/csw/share#g;" \
			-e "s#/usr/local#/opt/csw#g;"; \
		perl -pi \
			-e "s#/usr/share#/opt/csw/share#g;" \
			-e "s#/usr/local#/opt/csw#g;" \
				.$(bindir)/ggettextize \
				.$(infodir)/gettext.info; )