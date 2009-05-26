GARNAME = openldap
GARVERSION = 2.4.16
CATEGORIES = server

DESCRIPTION = Open source implementation of the Lightweight Directory Access Protocol
define BLURB
  The OpenLDAP Project is a collaborative effort to develop a robust,
  commercial-grade, fully featured, and open source LDAP suite of applications
  and development tools. The project is managed by a worldwide community of
  volunteers that use the Internet to communicate, plan, and develop the
  OpenLDAP Suite and its related documentation.
endef

MASTER_SITES = ftp://ftp.openldap.org/pub/OpenLDAP/openldap-release/
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
DISTFILES += $(call admfiles,CSWoldap)
DISTFILES += cswopenldap openldap.xml svc-openldap
DISTFILES += README.CSW openldaprc

LICENSE = COPYRIGHT

PACKAGES = CSWoldap CSWoldapclient CSWoldapdevel CSWoldaprt

CATALOGNAME_CSWoldapclient = openldap_client
CATALOGNAME_CSWoldapdevel  = openldap_devel
CATALOGNAME_CSWoldaprt     = openldap_rt

SPKG_DESC_CSWoldapclient = OpenLDAP client executables
SPKG_DESC_CSWoldapdevel  = OpenLDAP development support
SPKG_DESC_CSWoldaprt     = OpenLDAP runtime libraries

REQUIRED_PKGS_CSWoldap       = CSWbdb4 CSWiconv CSWlibnet CSWlibtoolrt CSWoldaprt
REQUIRED_PKGS_CSWoldap      += CSWosslrt CSWsasl CSWtcpwrap CSWunixodbc
REQUIRED_PKGS_CSWoldapclient = CSWlibnet CSWoldaprt CSWosslrt CSWsasl
REQUIRED_PKGS_CSWoldapdevel  = CSWoldaprt
REQUIRED_PKGS_CSWoldaprt     = CSWlibnet CSWosslrt CSWsasl

SPKG_SOURCEURL = http://www.openldap.org

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PATCHFILES = patch-oldap-2.4.16-ntlm.diff
DISTFILES += $(PATCHFILES)

EXTRA_DOCS = README.CSW openldaprc $(PATCHFILES)

EXTRA_LIB = $(prefix)/bdb44/lib 
EXTRA_INC = $(prefix)/bdb44/include

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

CONFIGURE_ARGS = $(DIRPATHS)

EXTRA_BUILD_ISAS_sparc = sparcv9
EXTRA_BUILD_ISAS_i386  = pentium_pro amd64

PKGFILES_CSWoldapclient  = $(bindir)/.*
PKGFILES_CSWoldapclient += $(mandir)/man1/.*

PKGFILES_CSWoldapdevel  = $(PKGFILES_DEVEL)
PKGFILES_CSWoldapdevel += $(mandir)/man3/.*

PKGFILES_CSWoldaprt  = $(PKGFILES_RT)
PKGFILES_CSWoldaprt += $(sysconfdir)/ldap.conf
PKGFILES_CSWoldaprt += $(mandir)/man5/ldap.conf.5

include gar/category.mk

CFLAGS := $(filter-out -I%,$(CFLAGS))
DIRECTORY_EXPORTS := $(filter-out includedir,$(DIRECTORY_EXPORTS))

INSTALL_SCRIPTS += custom

install-custom:
	@for file in $(EXTRA_DOCS); do \
		ginstall -D $(WORKDIR)/$$file $(DESTDIR)$(docdir)/$(GARNAME)/$$file; \
	done
	@$(MAKECOOKIE)
