GARNAME = jdk6
SPKG_VERSION = 1.6.0_13
GARVERSION = 6u13
CATEGORIES = lang

DESCRIPTION = Java Development Kit 6
define BLURB
endef

# There is no MASTER_SITES because the software must be downloaded
# manually and put into /home/src before packaging.
MASTER_SITES = manual://

SUFFIXES_sparc = sparc sparcv9
SUFFIXES_i386  = i586 x64
SUFFIXES = $(SUFFIXES_sparc) $(SUFFIXES_i386)

DISTNAME = jdk$(SPKG_VERSION)
DISTFILES  = $(foreach S,$(SUFFIXES),jdk-$(GARVERSION)-solaris-$S.sh)
NOEXTRACT  = $(foreach S,$(filter-out $(SUFFIXES_$(GARCH)),$(SUFFIXES)),jdk-$(GARVERSION)-solaris-$S.sh)
DISTFILES += $(call admfiles,CSWjdk6)
DISTFILES += $(call admfiles,CSWjre6)
DISTFILES += $(call admfiles,CSWjdk)
DISTFILES += $(call admfiles,CSWjre)

SPKG_SOURCEURL = http://java.sun.com/javase/downloads/index.jsp

SPKG_DESC_CSWjdk6 = Java Development Kit 6
SPKG_DESC_CSWjre6 = Java Runtime Environment 6
SPKG_DESC_CSWjdk = Java Delopment Kit - Latest Version (now CSWjdk6)
SPKG_DESC_CSWjre = Java Runtime Environment - Latest Version (now CSWjre6)

REQUIRED_PKGS_CSWjdk6 = CSWjre6
REQUIRED_PKGS_CSWjdk = CSWjdk6
REQUIRED_PKGS_CSWjre = CSWjre6

MANPAGES_JRE  = java.1 javaws.1 keytool.1 orbd.1 pack200.1 policytool.1 rmid.1 rmiregistry.1
MANPAGES_JRE += servertool.1 tnameserv.1 unpack200.1

MANPAGE_REGEX = ($(shell echo $(MANPAGES_JRE) | perl -lne 's/\./\\./g;print join("|",split)'))

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

PKGFILES_CSWjdk = $(prefix)/java/jdk/latest

PKGFILES_CSWjre  = $(prefix)/java/jre/latest
PKGFILES_CSWjre += $(prefix)/java/man

PKGFILES_CSWjre6  = $(prefix)/java/jdk/$(DISTNAME)/jre/.*
PKGFILES_CSWjre6 += $(prefix)/java/jdk/$(DISTNAME)/man/.*/$(MANPAGE_REGEX)
PKGFILES_CSWjre6 += $(prefix)/java/jre/jre$(SPKG_VERSION)
PKGFILES_CSWjre6 += $(prefix)/java/jre/jre6

# CSWjdk6 gets all the rest

# Tell the user to download the file manually
manual//%:
	@echo
	@echo "Please download the file"
	@echo "  $*"
	@echo "manually from"
	@echo "  $(SPKG_SOURCEURL)"
	@echo "and copy it to"
	@echo "  $(GARCHIVEDIR)"
	@echo

# rule to extract files with shell
# Clear DISPLAY or the installer will bring up advertisement
shell-extract-archive-%:
	@echo " ==> Extracting $(DOWNLOADDIR)/$*"
	@echo "yes" | (D=$(abspath $(DOWNLOADDIR)/$*); cd $(EXTRACTDIR); DISPLAY= MORE="-10000" sh $$D -noregister)
	@$(MAKECOOKIE)

extract-archive-%.sh: shell-extract-archive-%.sh
	@$(MAKECOOKIE)

include gar/category.mk

install-custom:
	@echo " ==> Installing $(GARNAME)"

	@rm -rf $(DESTDIR)$(prefix)/java
	@ginstall -d $(DESTDIR)$(prefix)/java/jdk
	@(cd $(WORKDIR); pax -r -w $(DISTNAME) $(DESTDIR)$(prefix)/java/jdk)
	@rm -f $(DESTDIR)$(prefix)/java/jdk/latest
	@gln -sf jdk6 $(DESTDIR)$(prefix)/java/jdk/latest
	@rm -f $(DESTDIR)$(prefix)/java/jdk/jdk6
	@gln -sf $(DISTNAME) $(DESTDIR)$(prefix)/java/jdk/jdk6

	@ginstall -d $(DESTDIR)$(prefix)/java/jre
	@rm -f $(DESTDIR)$(prefix)/java/jre/jre$(SPKG_VERSION)
	@gln -sf ../jdk/$(DISTNAME)/jre $(DESTDIR)$(prefix)/java/jre/jre$(SPKG_VERSION)
	@rm -f $(DESTDIR)$(prefix)/java/jre/latest
	@gln -sf jre6 $(DESTDIR)$(prefix)/java/jre/latest
	@rm -f $(DESTDIR)$(prefix)/java/jre/jre6
	@gln -sf jre$(SPKG_VERSION) $(DESTDIR)$(prefix)/java/jre/jre6

	@gln -sf ../man $(DESTDIR)$(prefix)/java/jdk/$(DISTNAME)/jre/man
	@$(MAKECOOKIE)
