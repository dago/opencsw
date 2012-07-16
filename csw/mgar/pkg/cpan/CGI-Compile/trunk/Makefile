NAME = CGI-Compile
VERSION = 0.15
GARTYPE = v2
CATEGORIES = cpan
AUTHOR = MIYAGAWA

DESCRIPTION = Compile .cgi scripts to a code reference like ModPerl::Registry
define BLURB
  Compile .cgi scripts to a code reference like ModPerl::Registry
endef

DISTFILES += COPYING

PACKAGES = CSWpm-cgi-compile
CATALOGNAME = pm_cgi_compile
ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpm-file-pushd

# Remove on next build
CHECKPKG_OVERRIDES_CSWpm-cgi-compile += unidentified-dependency|CSWpm-file-pushd

CONFIGURE_ARGS = 

include gar/category.mk
