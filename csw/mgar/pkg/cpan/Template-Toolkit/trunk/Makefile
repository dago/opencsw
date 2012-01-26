NAME = Template-Toolkit
VERSION = 2.22
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = ABW

DESCRIPTION = Template Toolkit 2
define BLURB
  This documentation describes the Template module which is the direct Perl
  interface into the Template Toolkit. It covers the use of the module and
  gives a brief summary of configuration options and template directives.
  Please see Template::Manual for the complete reference manual which goes
  into much greater depth about the features and use of the Template Toolkit.
  The Template::Tutorial is also available as an introductory guide to using
  the Template Toolkit.
endef

PACKAGES  = CSWpmtt2
CATALOGNAME = pm_tt2

BUILD_DEP_PKGS = CSWpmxmldom CSWpmappconfig CSWpmpodpom
RUNTIME_DEP_PKGS = CSWpmxmldom CSWpmappconfig CSWpmpodpom

CONFIGURE_ARGS  = TT_PREFIX=$(DESTDIR)$(datadir)/tt2
CONFIGURE_ARGS += TT_ACCEPT=y

FIXCONFIG_DIRS = $(DESTDIR)

include gar/category.mk
