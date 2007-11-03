GARNAME = openldap
GARVERSION = 2.3.39
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
DISTFILES += $(call admfiles,CSWoldapclient)
DISTFILES += $(call admfiles,CSWoldapdevel)
DISTFILES += $(call admfiles,CSWoldaprt)

PATCHFILES = patch-oldap-2.3.24-ntlm.diff


EXTRA_LIB = $(prefix)/bdb4/lib 
EXTRA_INC = $(prefix)/bdb4/include

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include ../category.mk

