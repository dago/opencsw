# $Id$

NAME = openldap
VERSION = 2.3-1
GARTYPE = v2
CATEGORIES = server

DESCRIPTION = OpenLDAP legacy files
define BLURB
  The OpenLDAP Project is a collaborative effort to develop a robust,
  commercial-grade, fully featured, and open source LDAP suite of applications
  and development tools. The project is managed by a worldwide community of
  volunteers that use the Internet to communicate, plan, and develop the
  OpenLDAP Suite and its related documentation.
endef

MASTER_SITES = ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/
DISTFILES  = libs-2.3.tar.gz
DISTFILES += COPYRIGHT

VENDOR_URL = http://www.openldap.org

LICENSE = COPYRIGHT

BUILD64 = 1

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS =
TEST_SCRIPTS =

PACKAGES += CSWliblber2-3-0
CATALOGNAME_CSWliblber2-3-0 = liblber2_3_0
PKGFILES_CSWliblber2-3-0 += $(call baseisadirs,$(libdir),liblber-2\.3\.so\.0(\.\d+)*)
SPKG_DESC_CSWliblber2-3-0 += $(DESCRIPTION), liblber-2.3.so.0

PACKAGES += CSWlibldap2-3-0
CATALOGNAME_CSWlibldap2-3-0 = libldap2_3_0
PKGFILES_CSWlibldap2-3-0 += $(call baseisadirs,$(libdir),libldap-2\.3\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibldap2-3-0 += $(DESCRIPTION), libldap-2.3.so.0
RUNTIME_DEP_PKGS_CSWlibldap2-3-0 += CSWlibnet
RUNTIME_DEP_PKGS_CSWlibldap2-3-0 += CSWlibssl0-9-8
RUNTIME_DEP_PKGS_CSWlibldap2-3-0 += CSWoldaprt
RUNTIME_DEP_PKGS_CSWlibldap2-3-0 += CSWlibsasl2-2
# We aren't rebuilding this library, so we can't remove the linking.
CHECKPKG_OVERRIDES_CSWlibldap2-3-0 += deprecated-library|file=opt/csw/lib/libldap-2.3.so.0.2.31|lib=/opt/csw/lib/libnet.so

PACKAGES += CSWlibldap-r2-3-0
CATALOGNAME_CSWlibldap-r2-3-0 = libldap_r2_3_0
PKGFILES_CSWlibldap-r2-3-0 += $(call baseisadirs,$(libdir),libldap_r-2\.3\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibldap-r2-3-0 += $(DESCRIPTION), libldap_r-2.3.so.0
RUNTIME_DEP_PKGS_CSWlibldap-r2-3-0 += CSWlibnet
RUNTIME_DEP_PKGS_CSWlibldap-r2-3-0 += CSWlibssl0-9-8
RUNTIME_DEP_PKGS_CSWlibldap-r2-3-0 += CSWlibsasl2-2
# Because of a file collision at the moment.
CHECKPKG_OVERRIDES_CSWlibldap-r2-3-0 += missing-dependency|CSWoldaprt
# We aren't rebuilding this library, so we can't remove the linking.
CHECKPKG_OVERRIDES_CSWlibldap-r2-3-0 += deprecated-library|file=opt/csw/lib/libldap_r-2.3.so.0.2.31|lib=/opt/csw/lib/libnet.so

# Because of splitting of the CSWoldaprt package - it hasn't been done yet.
# It's a transient override, once 2.4 libs are released aond CSWoldaprt is
# split, these overrides can be removed.
CHECKPKG_OVERRIDES_CSWliblber2-3-0 += file-collision|/opt/csw/lib/sparcv9/liblber-2.3.so.0.2.31|CSWliblber2-3-0|CSWoldaprt
CHECKPKG_OVERRIDES_CSWliblber2-3-0 += file-collision|/opt/csw/lib/liblber-2.3.so.0|CSWliblber2-3-0|CSWoldaprt
CHECKPKG_OVERRIDES_CSWliblber2-3-0 += file-collision|/opt/csw/lib/sparcv9/liblber-2.3.so.0|CSWliblber2-3-0|CSWoldaprt
CHECKPKG_OVERRIDES_CSWliblber2-3-0 += file-collision|/opt/csw/lib/liblber-2.3.so.0.2.31|CSWliblber2-3-0|CSWoldaprt
CHECKPKG_OVERRIDES_CSWlibldap-r2-3-0 += file-collision|/opt/csw/lib/libldap_r-2.3.so.0|CSWlibldap-r2-3-0|CSWoldaprt
CHECKPKG_OVERRIDES_CSWlibldap-r2-3-0 += file-collision|/opt/csw/lib/sparcv9/libldap_r-2.3.so.0|CSWlibldap-r2-3-0|CSWoldaprt
CHECKPKG_OVERRIDES_CSWlibldap-r2-3-0 += file-collision|/opt/csw/lib/sparcv9/libldap_r-2.3.so.0.2.31|CSWlibldap-r2-3-0|CSWoldaprt
CHECKPKG_OVERRIDES_CSWlibldap-r2-3-0 += file-collision|/opt/csw/lib/libldap_r-2.3.so.0.2.31|CSWlibldap-r2-3-0|CSWoldaprt
CHECKPKG_OVERRIDES_CSWlibldap2-3-0 += file-collision|/opt/csw/lib/libldap-2.3.so.0.2.31|CSWlibldap2-3-0|CSWoldaprt
CHECKPKG_OVERRIDES_CSWlibldap2-3-0 += file-collision|/opt/csw/lib/sparcv9/libldap-2.3.so.0.2.31|CSWlibldap2-3-0|CSWoldaprt
CHECKPKG_OVERRIDES_CSWlibldap2-3-0 += file-collision|/opt/csw/lib/libldap-2.3.so.0|CSWlibldap2-3-0|CSWoldaprt
CHECKPKG_OVERRIDES_CSWlibldap2-3-0 += file-collision|/opt/csw/lib/sparcv9/libldap-2.3.so.0|CSWlibldap2-3-0|CSWoldaprt
CHECKPKG_OVERRIDES_CSWlibldap2-3-0 += file-collision|/opt/csw/lib/amd64/libldap-2.3.so.0|CSWlibldap2-3-0|CSWoldaprt
CHECKPKG_OVERRIDES_CSWlibldap2-3-0 += file-collision|/opt/csw/lib/amd64/libldap-2.3.so.0.2.31|CSWlibldap2-3-0|CSWoldaprt
CHECKPKG_OVERRIDES_CSWlibldap-r2-3-0 += file-collision|/opt/csw/lib/amd64/libldap_r-2.3.so.0.2.31|CSWlibldap-r2-3-0|CSWoldaprt
CHECKPKG_OVERRIDES_CSWlibldap-r2-3-0 += file-collision|/opt/csw/lib/amd64/libldap_r-2.3.so.0|CSWlibldap-r2-3-0|CSWoldaprt
CHECKPKG_OVERRIDES_CSWliblber2-3-0 += file-collision|/opt/csw/lib/amd64/liblber-2.3.so.0|CSWliblber2-3-0|CSWoldaprt
CHECKPKG_OVERRIDES_CSWliblber2-3-0 += file-collision|/opt/csw/lib/amd64/liblber-2.3.so.0.2.31|CSWliblber2-3-0|CSWoldaprt

include gar/category.mk

post-merge-modulated:
	$(FILEDIR)/install_legacy.sh "$(GARCH)" "$(WORKDIR)" "$(PKGROOT)"
