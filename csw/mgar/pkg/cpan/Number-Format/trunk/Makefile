GARNAME = Number-Format
GARVERSION = 1.70
CATEGORIES = cpan
AUTHOR = WRW

DESCRIPTION = Perl extension for formatting numbers
define BLURB
  Number::Format is a library for formatting numbers. Functions are provided for
  converting numbers to strings in a variety of ways, and to convert strings that
  contain numbers back into numeric form. The output formats may include thousands
  separators - characters inserted between each group of three characters counting
  right to left from the decimal point. The characters used for the decimal point and
  the thousands separator come from the locale information or can be specified by the
  user.
endef

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWpmnumberformat,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

#CONFIGURE_ARGS = $(DIRPATHS)

EXTRA_MERGE_EXCLUDE_FILES = .*~ .*perllocal\.pod

include gar/category.mk
