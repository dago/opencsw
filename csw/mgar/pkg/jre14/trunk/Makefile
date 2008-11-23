GARNAME = jre14
SPKG_VERSION = 1.4.2_17
GARVERSION = $(shell echo $(SPKG_VERSION) | sed -e 's/\./_/g')
CATEGORIES = lang

DESCRIPTION = Java Runtime Environment 1.4
define BLURB
endef

# There is no MASTER_SITES because the software must be downloaded
# manually and put into /home/src before packaging.
MASTER_SITES = manual://

SUFFIXES_sparc = sparc sparcv9
SUFFIXES_i386  = i586
SUFFIXES = $(SUFFIXES_sparc) $(SUFFIXES_i386)

DISTNAME = j2re$(SPKG_VERSION)
DISTFILES  = $(foreach S,$(SUFFIXES),j2re-$(GARVERSION)-solaris-$S.sh)
NOEXTRACT  = $(foreach S,$(filter-out $(SUFFIXES_$(GARCH)),$(SUFFIXES)),j2re-$(GARVERSION)-solaris-$S.sh)
DISTFILES += $(call admfiles,CSWjre14)

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

include gar/category.mk

install-custom:
	@echo " ==> Installing $(GARNAME)"
	@rm -rf $(DESTDIR)$(prefix)/$(DISTNAME)
	@ginstall -d $(DESTDIR)$(prefix)
	@(cd $(WORKDIR); pax -r -w -v $(DISTNAME) $(DESTDIR)$(prefix))
	@rm -f $(DESTDIR)$(prefix)/$(GARNAME)
	@gln -sf $(DISTNAME) $(DESTDIR)$(prefix)/$(GARNAME)
	@$(MAKECOOKIE)
