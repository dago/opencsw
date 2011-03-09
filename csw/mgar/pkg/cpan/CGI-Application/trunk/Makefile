NAME = CGI-Application
VERSION = 4.31
CATEGORIES = cpan
AUTHOR = MARKSTOS

DESCRIPTION = Framework for building reusable web-applications
define BLURB
  CGI::Application is intended to make it easier to create sophisticated,
  reusable web-based applications. This module implements a methodology which,
  if followed, will make your web software easier to design, easier to
  document, easier to write, and easier to evolve.
endef

LICENSE = ARTISTIC

PACKAGES = CSWpm-cgi-application
CATALOGNAME_CSWpm-cgi-application = pm_cgi_application
SPKG_DESC_CSWpm-cgi-application = $(DESCRIPTION)
OBSOLETES_CSWpm-cgi-application = CSWpmcgiapp
CATALOGNAME_CSWpmcgiapp = pm_cgiapp

ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpmhtmltmpl

include gar/category.mk
