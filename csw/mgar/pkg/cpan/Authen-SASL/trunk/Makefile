NAME = Authen-SASL
VERSION = 2.16
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = GBARR

DESCRIPTION = SASL Authentication framework
define BLURB
endef

DISTFILES += COPYING

PACKAGES = CSWpm-authen-sasl
CATALOGNAME = pm_authen_sasl
SPKG_DESC_CSWpm-authen-sasl = $(DESCRIPTION)

RUNTIME_DEP_PKGS  = CSWpm-gssapi
RUNTIME_DEP_PKGS += CSWpm-digest-hmac

BUILD_DEP_PKGS = CSWperl

ARCHALL = 1

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

include gar/category.mk
