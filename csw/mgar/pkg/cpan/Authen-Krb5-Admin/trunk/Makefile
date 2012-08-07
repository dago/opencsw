NAME = Authen-Krb5-Admin
VERSION = 0.13
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = SJQUINNEY

DESCRIPTION = Perl extension for MIT Kerberos 5 admin interface
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = COPYING

# The Krb5 module is available only for Solaris 10 because of the libcrypto part of libssl
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES += CSWpm-authen-krb5-admin
CATALOGNAME_CSWpm-authen-krb5-admin = pm_authen_krb5_admin
SPKG_DESC_CSWpm-authen-krb5-admin = Perl extension for MIT Kerberos 5 admin interface
RUNTIME_DEP_PKGS_CSWpm-authen-krb5-admin += CSWpm-krb5
RUNTIME_DEP_PKGS_CSWpm-authen-krb5-admin += CSWlibkrb5-priv
RUNTIME_DEP_PKGS_CSWpm-authen-krb5-admin += CSWlibcom-err3

# Make sure to use OpenCSW kerberos libs
EXTRA_CONFIGURE_EXPORTS += KRB5_CONFIG
CONFIGURE_ENV_KRB5_CONFIG = $(bindir)/krb5-config

# These are for the testsuite. If they are not preset in environment variables
# the configure step will be interactiv.
EXTRA_CONFIGURE_EXPORTS += PERL_KADM5_PRINCIPAL
CONFIGURE_ENV_PERL_KADM5_PRINCIPAL = none
EXTRA_CONFIGURE_EXPORTS += PERL_KADM5_TEST_NAME
CONFIGURE_ENV_PERL_KADM5_TEST_NAME = none
EXTRA_CONFIGURE_EXPORTS += PERL_KADM5_TEST_NAME_2
CONFIGURE_ENV_PERL_KADM5_TEST_NAME_2 = none

# The testsuite requires a running Kerberos server
SKIPTEST ?= 1

include gar/category.mk
