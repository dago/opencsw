GARNAME = jdk5
SPKG_VERSION = 1.5.0_17
GARVERSION = $(shell echo $(SPKG_VERSION) | sed -e 's/\./_/g')
CATEGORIES = lang

DESCRIPTION = Java Development Kit 5.0
define BLURB
endef

# There is no MASTER_SITES because the software must be downloaded
# manually and put into /home/src before packaging.
MASTER_SITES = manual://

SUFFIXES_sparc = sparc sparcv9
SUFFIXES_i386  = i586 amd64
SUFFIXES = $(SUFFIXES_sparc) $(SUFFIXES_i386)

DISTNAME = jdk$(SPKG_VERSION)
DISTFILES  = $(foreach S,$(SUFFIXES),jdk-$(GARVERSION)-solaris-$S.sh)
NOEXTRACT  = $(foreach S,$(filter-out $(SUFFIXES_$(GARCH)),$(SUFFIXES)),jdk-$(GARVERSION)-solaris-$S.sh)
DISTFILES += $(call admfiles,CSWjdk5)
DISTFILES += $(call admfiles,CSWjre5)

SPKG_SOURCEURL = http://java.sun.com/javase/downloads/index_jdk5.jsp

SPKG_DESC_CSWjdk5 = Java Development Kit 6
SPKG_DESC_CSWjre5 = Java Runtime Environment 6

REQUIRED_PKGS_CSWjdk6 = CSWjre6

MANPAGES_JRE  = java.1 javaws.1 keytool.1 orbd.1 pack200.1 policytool.1 rmid.1 rmiregistry.1
MANPAGES_JRE += servertool.1 tnameserv.1 unpack200.1

MANPAGE_REGEX = ($(shell echo $(MANPAGES_JRE) | perl -lne 's/\./\\./g;print join("|",split)'))

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

PKGFILES_CSWjre5  = $(prefix)/java/jdk/$(DISTNAME)/jre/.*
PKGFILES_CSWjre5 += $(prefix)/java/jdk/$(DISTNAME)/man/.*/$(MANPAGE_REGEX)
PKGFILES_CSWjre5 += $(prefix)/java/jre/jre$(SPKG_VERSION)
PKGFILES_CSWjre5 += $(prefix)/java/jre/jre5

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
shell-extract-%:
	@echo " ==> Extracting $(DOWNLOADDIR)/$*"
	@echo "yes" | (D=$(abspath $(DOWNLOADDIR)/$*); cd $(EXTRACTDIR); DISPLAY= MORE="-10000" sh $$D -noregister)
	@$(MAKECOOKIE)

extract-%.sh: shell-extract-%.sh
	@$(MAKECOOKIE)

include gar/category.mk

install-custom:
	@echo " ==> Installing $(GARNAME)"

	rm -rf $(DESTDIR)$(prefix)/java
	ginstall -d $(DESTDIR)$(prefix)/java/jdk
	(cd $(WORKDIR); pax -r -w $(DISTNAME) $(DESTDIR)$(prefix)/java/jdk)
	rm -f $(DESTDIR)$(prefix)/java/jdk/jdk5
	gln -sf $(DISTNAME) $(DESTDIR)$(prefix)/java/jdk/jdk5
	
	ginstall -d $(DESTDIR)$(prefix)/java/jre
	rm -f $(DESTDIR)$(prefix)/java/jre/jre$(SPKG_VERSION)
	gln -sf ../jdk/$(DISTNAME)/jre $(DESTDIR)$(prefix)/java/jre/jre$(SPKG_VERSION)
	rm -f $(DESTDIR)$(prefix)/java/jre/jre5
	gln -sf jre$(SPKG_VERSION) $(DESTDIR)$(prefix)/java/jre/jre5
	
	gln -s ../man $(DESTDIR)$(prefix)/java/jdk/$(DISTNAME)/jre/man
	@$(MAKECOOKIE)
