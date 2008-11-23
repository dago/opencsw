GARNAME = Config-General
GARVERSION = 2.40
CATEGORIES = cpan
AUTHOR = TLINDEN

DESCRIPTION = Generic Config Module
define BLURB
  This module opens a config file and parses it's contents for you.
  The new method requires one parameter which needs to be a filename.
  The method getall returns a hash which contains all options and it's associated values of your config file.

  The format of config files supported by Config::General is inspired by the well known apache config format,
  in fact, this module is 100% compatible to apache configs, 
  but you can also just use simple name/value pairs in your config files.

  In addition to the capabilities of an apache config file it supports some enhancements such as here-documents,
  C-style comments or multiline options
endef

DISTFILES += CSWpmconfiggeneral.gspec

CONFIGURE_ARGS = 

include gar/category.mk
