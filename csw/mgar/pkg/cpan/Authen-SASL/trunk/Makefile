NAME = Authen-SASL
VERSION = 2.15
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = GBARR

DESCRIPTION = SASL Authentication framework
define BLURB
  SASL is a generic mechanism for authentication used by several network
  protocols. Authen::SASL provides an implementation framework that all
  protocols should be able to share.
endef

DISTFILES += COPYING

PACKAGES = CSWpm-authen-sasl
CATALOGNAME = pm_authen_sasl
SPKG_DESC_CSWpm-authen-sasl = $(DESCRIPTION)
OBSOLETED_BY_CSWpm-authen-sasl = CSWpmauthensasl
CATALOGNAME_CSWpmauthensasl = pm_authensasl

RUNTIME_DEP_PKGS = CSWpmgssapi CSWpmdigesthmac
BUILD_DEP_PKGS = CSWperl

ARCHALL = 1

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

include gar/category.mk
