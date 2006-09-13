GARNAME = gm4
GARVERSION = 1.4.5
CATEGORIES = utils

DESCRIPTION = GNU m4 Unix macro processor
define BLURB
	GNU M4 is an implementation of the traditional Unix macro processor. It is mostly SVR4 compatible although it has some extensions (for example, handling more than 9 positional parameters to macros). GNU m4 also has built-in functions for including files, running shell commands, doing arithmetic, etc.
endef

MASTER_SITES = ftp://ftp.gnu.org/gnu/m4/
DISTFILES  = m4-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWgm4,prototype)

CONFIGURE_ARGS = $(DIRPATHS) --program-prefix=g
TEST_SCRIPTS =

include ../category.mk

post-extract:
	files/post-extract $(DESTIMG) $(GARVERSION) 
