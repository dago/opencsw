GARNAME = jre13
SPKG_VERSION = 1.3.1_22
GARVERSION = $(shell echo $(SPKG_VERSION) | sed -e 's/\./_/g')
CATEGORIES = lang

DESCRIPTION = Java Runtime Environment 1.3
define BLURB
endef

# There is no MASTER_SITES because the software must be downloaded
# manually and put into /home/src before packaging.
MASTER_SITES = manual://

SUFFIXES_sparc = sparc
SUFFIXES_i386  = i586
SUFFIXES = $(SUFFIXES_sparc) $(SUFFIXES_i386)

DISTNAME = j2re$(GARVERSION)
DISTFILES  = $(foreach S,$(SUFFIXES),j2re-$(GARVERSION)-solaris-$S.sh)
NOEXTRACT  = $(foreach S,$(filter-out $(SUFFIXES_$(GARCH)),$(SUFFIXES)),j2re-$(GARVERSION)-solaris-$S.sh)
DISTFILES += $(call admfiles,CSWjre13)

SPKG_SOURCEURL = http://java.sun.com/products/archive/

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

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
	@echo "yes" | (D=$(abspath $(DOWNLOADDIR)/$*); cd $(EXTRACTDIR); MORE="-10000" sh $$D)
	@$(MAKECOOKIE)

extract-%.sh: shell-extract-%.sh
	@$(MAKECOOKIE)

include ../category.mk

install-custom:
	@echo " ==> Installing $(GARNAME)"
	@rm -rf $(DESTDIR)$(prefix)/$(DISTNAME)
	@ginstall -d $(DESTDIR)$(prefix)
	@cp -r $(WORKSRC) $(DESTDIR)$(prefix)
	@$(MAKECOOKIE)
