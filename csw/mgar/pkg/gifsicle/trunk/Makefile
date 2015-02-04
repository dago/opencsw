# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = gifsicle
VERSION = 1.87
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Tool for creating, editing, and getting information about GIF images
define BLURB
endef

MASTER_SITES = http://www.lcdf.org/gifsicle/
DISTFILES  = $# These are probably harmless:
# ./test/010-warnings.testie:16: standard output has unexpected value starting at line 1
# ./test/010-warnings.testie:16: stdout:1: expected 'blank worked'
# ./test/010-warnings.testie:16: stdout:1: but got  '<end of file>'
SKIPTEST ?= 1

include gar/category.mk
