GARNAME = Test-LongString
GARVERSION = 0.11
CATEGORIES = cpan
AUTHOR = RGARCIA

DESCRIPTION = Tests strings for equality
define BLURB
  This module provides some drop-in replacements for the string comparison
  functions of Test::More, but which are more suitable when you test against
  long strings. If you've ever had to search for text in a multi-line string
  like an HTML document, or find specific items in binary data, this is the
  module for you.
endef

DISTFILES += $(call admfiles,CSWpmtestlongstr,)

BUILDDEPS += cpan/Test-Builder-Tester

include ../category.mk
