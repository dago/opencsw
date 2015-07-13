NAME = jdk7
SPKG_VERSION = 1.7.0_80
VERSION = 7u80
GARTYPE = v2

DESCRIPTION = Java Development Kit 7 Development Kit 6
define BLURB
endef

# There is no MASTER_SITES because the software must be downloaded
# manually and put into /home/src before packaging.
MASTER_SITES = manual://

SUFF sparcv9
SUFFIXES_i386  = i586FIXES_i386  = i586 x64
SUFFIXES = $(SUFFIXES_sparc) $(SUFFIXES_i386)

DISTNAME = jdk$(SPKG_VERSION)
DISTFILES  = $(foreach S,$(SUFFIXES),jdk-$(VEtar.gz)
NOEXTRACT  = $(foreach S,$(filter-out $(SUFFIXES_$(GARCH)),$(SUFFIXES)),jdk-$(VERSION)-solaris-$S.tar.gz)

NOGITPATCH = 1

VENDOR_URL = http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html
LICENSE = COPYRIGHT

FILES_JDK += javadoc
FILES_JDK += javap
FILES_JDK += jconsole
FILES_JDK += jdb
FILES_JDK += jhat
FILES_JDK += jinfo
FILES_JDK += jmap
FILES_JDK += jsadebugd
FILES_JDK += jstack
FILES_JDK += jstat
FILES_JDK += jstatd
FILES_JDK += jvisualvm
FILES_JDK += serialver

PACKAGES += CSWjdk7
SPKG_DESC_CSWjdk7 = Java Development Kit 7
# PKGFILES is catchall
PKGFILES_CSWjdk7 += $(foreach F,$(FILES_JDK),$(prefix)/java/$(DISTNAME)/bin/$F)
PKGFILES_CSWjdk7 += $(foreach F,$(FILES_JDK),$(prefix)/java/$(DISTNAME)/bin/$(ISA_DEFAULT64_$(GARCH))/$F)
PKGFILES_CSWjdk7 += $(foreach F,$(FILES_JDK),$(prefix)/java/$(DISTNAME)/man/man1/$F.1)
PKGFILES_CSWjdk7 += $(foreach F,$(FILES_JDK),$(prefix)/java/$(DISTNAME)/man/ja/man1/$F.1)
PKGFILES_CSWjdk7 += $(foreach F,$(FILES_JDK),$(prefix)/java/$(DISTNAME)/man/ja_JP.PCK/man1/$F.1)
PKGFILES_CSWjdk7 += $(foreach F,$(FILES_JDK),$(prefix)/java/$(DISTNAME)/man/ja_JP.UTF-8/man1/$F.1)
PKGFILES_CSWjdk7 += $(prefix)/java/$(DISTNAME)/src.zip
PKGFILES_CSWjdk7 += $(prefix)/java/$(DISTNAME)/lib/visualvm(/.*)?
PKGFILES_CSWjdk7 += $(prefix)/java/jdk/jdk7
# This is a logical dependency, so no way for checkpkg to detect it
RUNTIME_DEP_PKGS_CSWjdk7 += CSWjre7
CHECKPKG_OVERRIDES_CSWjdk7 += surplus-dependency|CSWjre7
# We package upstream as is, no chance to change anything.
CHECKPKG_OVERRIDES_CSWjdk7 += binary-architecture-does-not-match-placement
CHECKPKG_OVERRIDES_CSWjdk7 += binary-disallowed-placement
CHECKPKG_OVERRIDES_CSWjdk7 += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWjdk7 += soname-not-found
CHECKPKG_OVERRIDES_CSWjdk7 += no-direct-binding
CHECKPKG_OVERRIDES_CSWjdk7 += file-with-bad-content

PACKAGES += CSWjre7
SPKG_DESC_CSWjre7 = Java Server Runtime Environment 8
# PKGFILES is catchall
# We package upstream as is, no chance to change anything.
CHECKPKG_OVERRIDES_CSWjre7 += binary-architecture-does-not-match-placement
CHECKPKG_OVERRIDES_CSWjre7 += binary-disallowed-placement
CHECKPKG_OVERRIDES_CSWjre7 += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWjre7 += soname-not-found
CHECKPKG_OVERRIDES_CSWjre7 += no-direct-binding
CHECKPKG_OVERRIDES_CSWjre7 += file-with-bad-content

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk gets all the rest

# Tell the user to download the file manually
manual//%:
	@echo
	@echo "Please download the file"
	@echo "  $*"
	@echo "manually VENDOR_URL)"
	@echo "and copy it to"
	@echo "  $(GARCHIVEDIR)"
	@echo

install-custom:
	@echo " ==> Installing $(NAME)"
	rm -rf $(DESTDIR)$(prefix)/java
	ginstall -d -m 0755 $(DESTDIR)$(prefix)/java
	cp -rp $(WORKSRC) $(DESTDIR)$(prefix)/java/$(DISTNAME)
	rm -rf $(DESTDIR)$(prefix)/java/jre
	ginstall -d -m 0755 $(DESTDIR)$(prefix)/java/jdk
	gln -sf ../$(DISTNAME) $(DESTDIR)$(prefix)/java/jdk/jdk7
	ginstall -d -m 0755 $(DESTDIR)$(prefix)/java/jre
	gln -sf ../$(DISTNAME)/jre $(DESTDIR)$(prefix)/java/jre/jre7
	@$(MAKECOOKIE)
