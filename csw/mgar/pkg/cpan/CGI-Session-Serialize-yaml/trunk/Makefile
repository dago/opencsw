NAME = CGI-Session-Serialize-yaml
VERSION = 4.26
GARTYPE = v2
CATEGORIES = cpan
AUTHOR = RSAVAGE

DESCRIPTION = Serializer for CGI::Session
define BLURB
  Serializer for CGI::Session
endef

MODDIST = CGI-Session-Serialize-yaml-$(VERSION).tgz

DISTFILES += COPYING

PACKAGES = CSWpm-cgi-session-serializ-yaml
CATALOGNAME = pm_cgi_session_serialize_yaml
SPKG_DESC_CSWpm-cgi-session-serializ-yaml = $(DESCRIPTION)
ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpm-cgi-session

CONFIGURE_ARGS = 

CHECKPKG_OVERRIDES_CSWpm-cgi-session-serializ-yaml += catalogname-does-not-match-pkgname|pkgname=CSWpm-cgi-session-serializ-yaml|catalogname=pm_cgi_session_serialize_yaml|expected-catalogname=pm_cgi_session_serializ_yaml

include gar/category.mk
