GARNAME = Text-Autoformat
GARVERSION = 1.13
CATEGORIES = cpan
AUTHOR = DCONWAY

DESCRIPTION = automatic text wrapping and reformatting
define BLURB
  The fundamental task of the autoformat subroutine is to identify and
  rearrange independent paragraphs in a text. Paragraphs typically consist of
  a series of lines containing at least one non-whitespace character, followed
  by one or more lines containing only optional whitespace. This is a more
  liberal definition than many other formatters use: most require an empty
  line to terminate a paragraph. Paragraphs may also be denoted by bulleting,
  numbering, or quoting (see the following sections).
endef

DISTFILES += CSWpmtxtautofmt.gspec CSWpmtxtautofmt.depend

DEPENDS += cpan/Text-Reform

include gar/category.mk
