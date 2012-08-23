NAME = LWP-Protocol-https
VERSION = 6.03
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = GAAS

DESCRIPTION = Provide https support for LWP::UserAgent
define BLURB
  The LWP::Protocol::https module provides support for using https schemed URLs
  with LWP. This module is a plug-in to the LWP protocol handling, so you don't
  use it directly. Once the module is installed LWP is able to access sites
  using HTTP over SSL/TLS.
endef

LICENSE_TEXT = This module is licensed under the perl license

PACKAGES = CSWpm-lwp-protocol-https
CATALOGNAME = pm_lwp_protocol_https
RUNTIME_DEP_PKGS += CSWpm-io-socket-ssl
RUNTIME_DEP_PKGS += CSWpm-libwww-perl
RUNTIME_DEP_PKGS += CSWpm-net-http
RUNTIME_DEP_PKGS += CSWpm-mozilla-ca

include gar/category.mk
