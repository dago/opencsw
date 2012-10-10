# $HeadURL$

NAME = cswclassutils
VERSION = 1.48
CATEGORIES = utils
GARTYPE = v2

# a few handy functions for defining 'generic' things dynamically
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

# checkpkg understands this relationship now, so no need to override it
# any more.  keep it here in case it ever becomes useful for something else
# define surplus_dep
# $(eval CHECKPKG_OVERRIDES_CSWcswclassutils += surplus-dependency|$(call csw_pkgname,$(1)))
# endef

define bad_location
$(eval CHECKPKG_OVERRIDES_CSWcas-$(1) += bad-location-of-file|file=/usr/sadm/install/scripts/$(2).csw$(1))
endef

# end of handy functions

DESCRIPTION = CSW class action utilities

MASTER_SITES =
DISTFILES = COPYING CSWcas-initsmf.cswreleasenotes cas-ssl.conf

ARCHALL = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

SPKG_SOURCEURL = http://www.opencsw.org

FILEDIR = files

CASFILES = $(wildcard $(FILEDIR)/CSW$(NAME).[ir].*)
CASLIST = $(foreach F,$(CASFILES), $(subst $(FILEDIR)/CSW$(NAME).,,$(F)))
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

PRESERVECONF = /etc/opt/csw/cas-ssl.conf

# set a unique description for each CAS
$(foreach C,$(CSWCLASSES),$(call spkg_desc,$(C)))
SPKG_DESC_CSWcswclassutils = $(DESCRIPTION)

# and add the base set of files belonging to the CAS
$(foreach C,$(CSWCLASSES),$(call pkg_files,$(C)))
# and the catalog names
$(foreach C,$(CSWCLASSES),$(call catname,$(C)))

# tell checkpkg to ignore the surplus dep on the subpkgs
#$(foreach C,$(CSWCLASSES),$(call surplus_dep,$(C)))

# tell checkpkg to ignore the bad file location in the subpackages
$(foreach C,$(CSWCLASSES),$(call bad_location,$(call cas_shortname,$(C)),i))
$(foreach C,$(CSWCLASSES),$(call bad_location,$(call cas_shortname,$(C)),r))


# Add non-auto changes to checkpkg overrides, pkg files, etc.

PKGFILES_CSWcas-cptemplates += /opt/csw/etc/templates
PKGFILES_CSWcas-initsmf += /opt/csw/etc/init.d/.*
PKGFILES_CSWcas-initsmf += /etc/opt/csw/init.d.*
PKGFILES_CSWcas-initsmf += /var/opt/csw/svc/.*

# Mark these as _extra_ so they're applied after the excludes, which would
# include files from the other packages and thus clash.
PKGFILES_CSWcas-inetd_SHARED += /var/opt/csw/cswclassutils
PKGFILES_CSWcas-pycompile_SHARED += /var/opt/csw/cswclassutils

PKGFILES_CSWcas-sslcert += /etc/opt/csw/cas-ssl.conf.CSW

CHECKPKG_OVERRIDES_CSWcas-initsmf += init-file-missing-cswinitsmf-class
CHECKPKG_OVERRIDES_CSWcas-initsmf += init-file-wrong-location
CHECKPKG_OVERRIDES_CSWcas-initsmf += init-file-wrong-location|/opt/csw/etc/init.d/csw.smf.sample

# the doctype string
CHECKPKG_OVERRIDES_CSWcas-initsmf += file-with-bad-content|/usr/share|root/usr/sadm/install/scripts/i.cswinitsmf

include gar/category.mk

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@rm -rf $(DESTDIR)
	@ginstall -m 0755 -d $(DESTDIR)/opt/csw/etc/init.d
	@ginstall -m 0755 -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 0755 -d $(DESTDIR)/opt/csw/etc/templates
	@ginstall -m 0755 -d $(DESTDIR)$(docdir)/$(NAME)
	@ginstall -m 0755 -d $(DESTDIR)/usr/sadm/install/scripts
	@ginstall -m 0755 -d $(DESTDIR)/var/opt/csw/svc/manifest
	@ginstall -m 0755 -d $(DESTDIR)/var/opt/csw/svc/method
	@ginstall -m 0755 -d $(DESTDIR)/var/opt/csw/cswclassutils
	@ginstall -m 0755 $(FILEDIR)/CSW$(NAME).csw.smf.sample $(DESTDIR)/opt/csw/etc/init.d/csw.smf.sample
	@ginstall -m 0444 $(FILEDIR)/CSW$(NAME).README.CSW $(DESTDIR)$(docdir)/$(NAME)/README.CSW
	@$(foreach CAS,$(CASLIST),ginstall -m 0555 $(FILEDIR)/CSW$(NAME).$(CAS) $(DESTDIR)/usr/sadm/install/scripts/$(CAS);)
	@ginstall -m 0644 $(FILEDIR)/cas-ssl.conf $(DESTDIR)/etc/opt/csw/
	@$(MAKECOOKIE)
