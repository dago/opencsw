# $Id$
NAME = liborc
VERSION = 0.4.6
CATEGORIES = lib

DESCRIPTION = The Oil Runtime Compiler
define BLURB
  Orc is a library and set of tools for compiling and executing very simple programs that operate on arrays of data.
  The language is a generic assembly language that represents many of the features available in SIMD architectures,
  including saturated addition and subtraction, and many arithmetic operations.
endef

MASTER_SITES = http://code.entropywave.com/download/orc/
DISTNAME = orc-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://code.entropywave.com/projects/orc/

BUILD64 = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk
