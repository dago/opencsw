# $HeadURL$

GARNAME = cswclassutils
GARVERSION = 1.42
CATEGORIES = utils

# a few handy functions for defining 'generic' things dynmaically
set = $(eval $1 := $2)

define cas_shortname
$(subst csw,,$(1))
endef

define csw_pkgname
CSWcas-$(call cas_shortname,$(1))
endef

define var_name
$(1)_$(call csw_pkgname,$(2))
endef

define spkg_desc_val
Class action script $(call cas_shortname,$(1))
endef

define pkgfiles_val
/usr/sadm/install/scripts/.*$(1)
endef

define catname_val
cas_$(call cas_shortname,$(1))
endef

define spkg_desc
$(call set,$(call var_name,SPKG_DESC,$(1)),$(call spkg_desc_val,$(1)))
endef

define pkg_files
$(call set,$(call var_name,PKGFILES,$(1)),$(call pkgfiles_val,$(1)))
endef

define catname
$(call set,$(call var_name,CATALOGNAME,$(1)),$(call catname_val,$(1)))
endef

define surplus_dep
$(eval CHECKPKG_OVERRIDES_CSWcswclassutils += surplus-dependency|$(call csw_pkgname,$(1)))
endef

# end of handy functions

DESCRIPTION = CSW class action utilities

MASTER_SITES =
DISTFILES = COPYING

ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

SPKG_SOURCEURL = http://www.opencsw.org

FILEDIR = files

CASFILES = $(wildcard $(FILEDIR)/CSW$(GARNAME).[ir].*)
CASLIST = $(foreach F,$(CASFILES), $(subst $(FILEDIR)/CSW$(GARNAME).,,$(F)))
CSWCLASSES = $(subst .,,$(sort $(suffix $(CASLIST))))

DISTFILES += $(subst $(FILEDIR)/,,$(CASFILES))

CASPACKAGES += $(foreach C,$(CSWCLASSES),CSWcas-$(call cas_shortname,$(C)))

PACKAGES = CSWcswclassutils
PACKAGES += $(CASPACKAGES)

RUNTIME_DEP_PKGS_CSWcswclassutils = $(CASPACKAGES)

PROTOTYPE_MODIFIERS = cas
PROTOTYPE_FILES_cas = /usr/sadm/install/scripts/.*
PROTOTYPE_USER_cas = bin
PROTOTYPE_GROUP_cas = sys

CHECKPKG_OVERRIDES_CSWcswclassutils += init-file-missing-cswinitsmf-class
CHECKPKG_OVERRIDES_CSWcswclassutils += init-file-wrong-location
CHECKPKG_OVERRIDES_CSWcswclassutils += init-file-wrong-location|/opt/csw/etc/init.d/csw.smf.sample

# set a unique description for each CAS
$(foreach C,$(CSWCLASSES),$(call spkg_desc,$(C)))
SPKG_DESC_CSWcswclassutils = $(DESCRIPTION)

# and add the base set of files belonging to the CAS
$(foreach C,$(CSWCLASSES),$(call pkg_files,$(C)))
# and the catalog names
$(foreach C,$(CSWCLASSES),$(call catname,$(C)))

# tell checkpkg to ignore the surplus dep on the subpkgs
$(foreach C,$(CSWCLASSES),$(call surplus_dep,$(C)))

include gar/category.mk

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@rm -rf $(DESTDIR)
	@ginstall -m 0755 -d $(DESTDIR)/opt/csw/etc/init.d
	@ginstall -m 0755 -d $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 0755 -d $(DESTDIR)/usr/sadm/install/scripts
	@ginstall -m 0755 -d $(DESTDIR)/var/opt/csw/svc/manifest
	@ginstall -m 0755 -d $(DESTDIR)/var/opt/csw/svc/method
	@ginstall -m 0755 -d $(DESTDIR)/var/opt/csw/cswclassutils
	@ginstall -m 0755 $(FILEDIR)/CSW$(GARNAME).csw.smf.sample $(DESTDIR)/opt/csw/etc/init.d/csw.smf.sample
	@ginstall -m 0444 $(FILEDIR)/CSW$(GARNAME).README.CSW $(DESTDIR)$(docdir)/$(GARNAME)/README.CSW
	@$(foreach CAS,$(CASLIST),ginstall -m 0555 $(FILEDIR)/CSW$(GARNAME).$(CAS) $(DESTDIR)/usr/sadm/install/scripts/$(CAS);)
	@$(MAKECOOKIE)
