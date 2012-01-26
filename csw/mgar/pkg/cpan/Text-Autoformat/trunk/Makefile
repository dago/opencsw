NAME = Text-Autoformat
VERSION = 1.669002
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DCONWAY

DESCRIPTION = Automatic text wrapping and reformatting
define BLURB
  The fundamental task of the autoformat subroutine is to identify and
  rearrange independent paragraphs in a text. Paragraphs typically consist of
  a series of lines containing at least one non-whitespace character, followed
  by one or more lines containing only optional whitespace. This is a more
  liberal definition than many other formatters use: most require an empty
  line to terminate a paragraph. Paragraphs may also be denoted by bulleting,
  numbering, or quoting (see the following sections).
endef

DISTFILES += COPYING

PACKAGES = CSWpmtxtautofmt
CATALOGNAME = pm_txtautofmt
ARCHALL = 1

RUNTIME_DEP_PKGS += CSWpmtxtreform

include gar/category.mk
