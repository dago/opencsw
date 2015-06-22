NAME = jre8
SPKG_VERSION = 1.8.0_45
VERSION = 8u45
GARTYPE = v2

DESCRIPTION = Java Development Kit 8 Development Kit 6
define BLURB
endef

# There is no MASTER_SITES because the software must be downloaded
# manually and put into /home/src before packaging.
MASTER_SITES = manual://

SUFFv9
SUFFIXES_i386  =FIXES_i386  = i586 x64
SUFFIXES = $(SUFFIXES_sparc) $(SUFFIXES_i386)

DISTNAME = jdk$(SPKG_VERSION)
DISTFILES  = $(foreach S,$(SUFFIXES),jdk-$(VEtar.gz)
NOEXTRACT  = $(foreach S,$(filter-out $(SUFFIXES_$(GARCH)),$(SUFFIXES)),jdk-$(VERSION)-solaris-$S.tar.gz)

NOGITPATCH = 1

VENDOR_URL = http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
LICENSE = COPYRIGHT

PACKAGES += CSWjdk
SPKG_DESC_CSWjdk = Java Delopment Kit - Latest Version (now CSWjdk8)
PKGFILES_CSWjdk += $(prefix)/java/jdk/latest
ARCHALL_CSWjdk = 1
RUNTIME_DEP_PKGS_CSWjdk += CSWjdk8
CHECKPKG_OVERRIDES_CSWjdk += surplus-dependency|CSWjdk8

PACKAGES += CSWjre
SPKG_DESC_CSWjre = Java Runtime Environment - Latest Version (now CSWjre8)
PKGFILES_CSWjre += $(prefix)/java/jre/latest
PKGFILES_CSWjre += $(prefix)/java/man
ARCHALL_CSWjre = 1
RUNTIME_DEP_PKGS_CSWjre += CSWjre8
# False positive:
#   http://lists.opencsw.org/pipermail/maintainers/2015-January/019614.html
# Override until it is fixed
CHECKPKG_OVERRIDES_CSWjre += file-needed-but-no-package-satisfies-it|/opt/csw/java/jdk/latest/man|CSWjre|contains|symlink|/opt/csw/java/man|which|needs|the|target|file:|/opt/csw/java/jdk/latest/man

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

PACKAGES += CSWjdk8
SPKG_DESC_CSWjdk8 = Java Development Kit 8
# PKGFILES is catchall
PKGFILES_CSWjdk8 += $(foreach F,$(FILES_JDK),$(prefix)/java/$(DISTNAME)/bin/$F)
PKGFILES_CSWjdk8 += $(foreach F,$(FILES_JDK),$(prefix)/java/$(DISTNAME)/bin/$(ISA_DEFAULT64_$(GARCH))/$F)
PKGFILES_CSWjdk8 += $(foreach F,$(FILES_JDK),$(prefix)/java/$(DISTNAME)/man/man1/$F.1)
PKGFILES_CSWjdk8 += $(foreach F,$(FILES_JDK),$(prefix)/java/$(DISTNAME)/man/ja/man1/$F.1)
PKGFILES_CSWjdk8 += $(foreach F,$(FILES_JDK),$(prefix)/java/$(DISTNAME)/man/ja_JP.PCK/man1/$F.1)
PKGFILES_CSWjdk8 += $(foreach F,$(FILES_JDK),$(prefix)/java/$(DISTNAME)/man/ja_JP.UTF-8/man1/$F.1)
PKGFILES_CSWjdk8 += $(prefix)/java/$(DISTNAME)/src.zip
PKGFILES_CSWjdk8 += $(prefix)/java/$(DISTNAME)/lib/visualvm(/.*)?
PKGFILES_CSWjdk8 += $(prefix)/java/jdk/jdk8
# This is a logical dependency, so no way for checkpkg to detect it
RUNTIME_DEP_PKGS_CSWjdk8 += CSWjre8
CHECKPKG_OVERRIDES_CSWjdk8 += surplus-dependency|CSWjre8
# We package upstream as is, no chance to change anything.
CHECKPKG_OVERRIDES_CSWjdk8_OVERRIDES_CSWjdk6 += binary-architecture-does-not-match-placement
CHECKPK8 += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWjdk8 += soname-not-found
CHECKPKG_OVERRIDES_CSWjdk8 += no-direct-binding
CHECKPKG_OVERRIDES_CSWjdk8 += file-with-bad-content

PACKAGES += CSWjre8
SPKG_DESC_CSWjre8 = Java Server Runtime Environment 8
# PKGFILES is catchall
# We package upstream as is, no chance to change anything.
CHECKPKG_OVERRIDES_CSWjre8 += binary-architecture-does-not-match-placement
CHECKPKG_OVERRIDES_CSWjre8 += bad-rpath-entry
CHECKPKG_OVERRIDES_CSWjre8 += soname-not-found
CHECKPKG_OVERRIDES_CSWjre8 += no-direct-binding
CHECKPKG_OVERRIDES_CSWjre8 += file-with-bad-content

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
	gln -sf ../$(DISTNAME) $(DESTDIR)$(prefix)/java/jdk/jdk8
	gln -sf jdk8 $(DESTDIR)$(prefix)/java/jdk/latest
	ginstall -d -m 0755 $(DESTDIR)$(prefix)/java/jre
	gln -sf ../$(DISTNAME)/jre $(DESTDIR)$(prefix)/java/jre/jre8
	gln -sf jre8 $(DESTDIR)$(prefix)/java/jre/latest
	gln -sf jdk/latest/man $(DESTDIR)$(prefix)/java/man
	@$(MAKECOOKIE)
