GARNAME = openldap
GARVERSION = 2.3.40
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
DISTFILES += $(call admfiles,CSWoldap,depend)
DISTFILES += cswopenldap openldap.xml svc-openldap
DISTFILES += $(call admfiles,CSWoldapclient,depend)
DISTFILES += $(call admfiles,CSWoldapdevel,depend)
DISTFILES += $(call admfiles,CSWoldaprt,depend)
DISTFILES += README.CSW openldaprc

PATCHFILES = patch-oldap-2.3.24-ntlm.diff
DISTFILES += $(PATCHFILES)

EXTRA_DOCS = README.CSW openldaprc $(PATCHFILES)

EXTRA_LIB = $(prefix)/bdb4/lib 
EXTRA_INC = $(prefix)/bdb4/include

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

include ../category.mk

INSTALL_SCRIPTS += custom

install-custom:
	@for file in $(EXTRA_DOCS); do \
		ginstall -D $(WORKDIR)/$$file $(DESTDIR)$(docdir)/$(GARNAME)/$$file; \
	done
	@$(MAKECOOKIE)
