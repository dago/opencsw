NAME = openjdk
SPKG_VERSION = 7.ea.b118.11
VERSION = 7.b118.11
CATEGORIES = lang
GARTYPE = v2

DESCRIPTION = OpenJDK 7
define BLURB
endef

MASTER_SITES = http://www.java.net/download/openjdk/jdk7/promoted/b118/

SUFFIXES_sparc = sparc sparcv9
SUFFIXES_i386  = i586 x64
SUFFIXES = $(SUFFIXES_sparc) $(SUFFIXES_i386)

DISTNAME = jdk$(SPKG_VERSION)
DISTFILES  = $(foreach S,$(SUFFIXES),jdk-$(VERSION)-solaris-$S.sh)

DISTFILES  = openjdk-7-ea-src-b118-11_nov_2010.zip
DISTFILES += $(foreach S,$(SUFFIXES),jdk-7-ea-plug-b118-solaris-$S-11_nov_2010.jar)
NOEXTRACT  = $(foreach S,$(filter-out $(SUFFIXES_$(GARCH)),$(SUFFIXES)),jdk-7-ea-plug-b118-solaris-$S-11_nov_2010.jar)

SPKG_SOURCEURL = http://download.java.net/openjdk/jdk7/

PACKAGES = CSWopenjdk7

CATALOGNAME_CSWopenjdk7 = openjdk7

LICENSE = COPYRIGHT

SPKG_DESC_CSWopenjdk7 = Open Java Development Kit 7

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
	@echo " ==> Installing $(NAME)"

	@rm -rf $(DESTDIR)$(prefix)/java
	@ginstall -d $(DESTDIR)$(prefix)/java/jdk
	@(cd $(WORKDIR); pax -r -w -s ',.*/\.git.*,,' $(DISTNAME) $(DESTDIR)$(prefix)/java/jdk)
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
