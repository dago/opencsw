NAME = patch
VERSION = 2.7.1
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = GNU patch utility
define BLURB
  The GNU patch utility.
endef

MASTER_SITES = $(GNU_MIRDISTNAME).tar.xz

VENDOR_URL = https://savannah.gnu.org/projects/patch/

PACKAGES += CSWgpatch
SPKG_DESC_CSWgpatch = GNU patch utilityS = CSWlibgnugetopt

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += -BUILD64 = 1
ISAEXEC = 1

EXTRA_MERGE_EXCLUDE_FILES += $(libdir)/charset.alias

include gar/category.mk)/update-version.sh

post-install-modulated:
	ginstall -d $(DESTDIR)$(prefix)/gnu
	$(foreach G,$(notdir $(wildcard $(DESTDIR)$(bindir)/*)),ln -s ../bin/$G $(DESTDIR)$(prefix)/gnu/$(patsubst g%,%,$G);