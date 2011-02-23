NAME = HTTP-Body
VERSION = 1.11
CATEGORIES = cpan
AUTHOR = GETTY

DESCRIPTION = HTTP Body Parser
define BLURB
endef

BUILD_DEP_PKGS += CSWpmtestdeep

PACKAGES += CSWpm-http-body
CATALOGNAME_CSWpm-http-body = pm_http_body
ARCHALL_CSWpm-http-body = 1
RUNTIME_DEP_PKGS_CSWpm-http-body = CSWpmlibwww

# License is really unknown
CHECKPKG_OVERRIDES_CSWpm-http-body += license-missing|/opt/csw/share/doc/pm_http_body/license

include gar/category.mk
