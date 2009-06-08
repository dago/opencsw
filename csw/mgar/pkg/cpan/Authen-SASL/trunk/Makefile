GARNAME = Authen-SASL
GARVERSION = 2.12
CATEGORIES = cpan
AUTHOR = GBARR

DESCRIPTION = SASL Authentication framework
define BLURB
  SASL is a generic mechanism for authentication used by several network
  protocols. Authen::SASL provides an implementation framework that all
  protocols should be able to share.
endef

DISTFILES += COPYING

PACKAGES = CSWpmauthensasl
CATALOGNAME = pm_authensasl

REQUIRED_PKGS = CSWpmgssapi CSWpmdigesthmac
PREREQUISITE_PKGS = CSWperl

ARCHALL = 1

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

include gar/category.mk
