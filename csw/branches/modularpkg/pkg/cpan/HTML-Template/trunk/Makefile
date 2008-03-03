GARNAME = HTML-Template
GARVERSION = 2.9
CATEGORIES = cpan
AUTHOR = SAMTREGAR

DESCRIPTION = Perl module to use HTML Templates from CGI scripts
define BLURB
  This module attempts to make using HTML templates simple and natural. It
  extends standard HTML with a few new HTML-esque tags - <TMPL_VAR>,
  <TMPL_LOOP>, <TMPL_INCLUDE>, <TMPL_IF>, <TMPL_ELSE> and <TMPL_UNLESS>. The
  file written with HTML and these new tags is called a template. It is
  usually saved separate from your script - possibly even created by someone
  else! Using this module you fill in the values for the variables, loops and
  branches declared in the template.  This allows you to separate design - the
  HTML - from the data, which you generate in the Perl script.
endef

DISTFILES += $(call admfiles,CSWpmhtmltmpl,prototype)

CONFIGURE_ARGS = -n

include gar/category.mk
