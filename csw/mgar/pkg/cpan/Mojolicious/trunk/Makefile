# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME       = Mojolicious
VERSION    = 5.21
GARTYPE    = v2
CATEGORIES = cpan
AUTHOR     = SRI

DESCRIPTION = A next generation web framework for the Perl programming language
define BLURB
  Back in the early days of the web, many people learned Perl because of a wonderful Perl library called CGI. It was simple enough to get started without knowing much about the language and powerful enough to keep you going, learning by doing was much fun. While most of the techniques used are outdated now, the idea behind it is not. Mojolicious is a new attempt at implementing this idea using state of the art technology.
endef

PACKAGES    = CSWpm-mojolicious
CATALOGNAME = pm_mojolicious
SPKG_DESC_CSWpm-mojolicious = $(DESCRIPTION)

ARCHALL = 1

# Comes from the CLI help example
CHECKPKG_OVERRIDES_CSWpm-mojolicious += file-with-bad-content|/usr/local|root/opt/csw/bin/morbo

include gar/category.mk

