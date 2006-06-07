GARNAME = Template-Toolkit
GARVERSION = 2.14
CATEGORIES = cpan
AUTHOR = ABW

DESCRIPTION = front-end module to the Template Toolkit
define BLURB
  This documentation describes the Template module which is the direct Perl
  interface into the Template Toolkit. It covers the use of the module and
  gives a brief summary of configuration options and template directives.
  Please see Template::Manual for the complete reference manual which goes
  into much greater depth about the features and use of the Template Toolkit.
  The Template::Tutorial is also available as an introductory guide to using
  the Template Toolkit.
endef

DISTFILES += $(call admfiles,CSWpmtt2,depend)

DEPENDS += cpan/DBI cpan/GD cpan/GDTextUtil cpan/GDGraph cpan/GDGraph3d
DEPENDS += cpan/Pod-POM cpan/XML-Parser cpan/XML-DOM cpan/XML-RSS
DEPENDS += cpan/XML-XPath

CONFIGURE_ARGS  = TT_PREFIX=$(datadir)/tt2
CONFIGURE_ARGS += TT_ACCEPT=y
CONFIGURE_ARGS += TT_DBI=n

include ../category.mk
