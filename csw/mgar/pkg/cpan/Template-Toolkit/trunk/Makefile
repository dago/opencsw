GARNAME = Template-Toolkit
GARVERSION = 2.15
CATEGORIES = cpan
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

DISTFILES += $(call admfiles,CSWpmtt2,depend prototype)
DISTFILES += $(call admfiles,CSWpmtt2-common,depend prototype)

#DEPENDS += cpan/DBI
#DEPENDS += cpan/GD cpan/GDTextUtil cpan/GDGraph cpan/GDGraph3d
#DEPENDS += cpan/XML-Parser cpan/XML-RSS cpan/XML-XPath
DEPENDS += cpan/AppConfig
DEPENDS += cpan/Pod-POM cpan/XML-DOM

CONFIGURE_ARGS  = TT_PREFIX=$(DESTDIR)$(datadir)/tt2
CONFIGURE_ARGS += TT_ACCEPT=y

FIXCONFIG_DIRS = $(DESTDIR)

include gar/category.mk
