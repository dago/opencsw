GARNAME = IO-String
GARVERSION = 1.08
CATEGORIES = cpan
AUTHOR = GAAS

DESCRIPTION = emulate file interface for in-core strings
define BLURB
  The IO::String module provides the IO::File interface for in-core strings.
  An IO::String object can be attached to a string, and makes it possible to
  use the normal file operations for reading or writing data, as well as for
  seeking to various locations of the string. This is useful when you want to
  use a library module that only provides an interface to file handles on data
  that you have in a string variable.
endef

DISTFILES = $(call admfiles,CSWpmiostring,depend prototype)

include ../category.mk
