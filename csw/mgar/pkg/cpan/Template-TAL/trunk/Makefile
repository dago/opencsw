GARNAME = Template-TAL
GARVERSION = 0.9
CATEGORIES = cpan
AUTHOR = TOMI

DESCRIPTION = Process TAL templates with Perl
define BLURB
  TAL is a templating language used in the Zope CMS. Template-TAL is a Perl
  implementation of TAL based on the published specs on the Zope wiki.
endef

DISTFILES += $(call admfiles,CSWpmtemplatetal,depend prototype)

DEPENDS += cpan/Test-XML
DEPENDS += cpan/XML-LibXML

include gar/category.mk
