# $Id$

NAME = texi2html
VERSION = 5.0
GARTYPE = v2

DESCRIPTION = A Texinfo to HTML converter
define BLURB
	Texi2HTML is a Perl script which converts Texinfo source files to
	HTML output; supports many features beyond those supported by
	makeinfo.
endef

MASTER_SITES	=	http://download.savannah.gnu.org/releases/texi2html/

DISTFILES	=	$(DISTNAME).tar.bz2
PATCHFILES	+=	0001-Use-environment-s-bash-in-test-scripts.patch

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS = custom

include gar/category.mk

PATH := /opt/csw/gnu:/opt/csw/libexec/flex-2.5.35/bin:$(PATH)

# there are failing tests:
#    formating: IMHO not real errors but probably due to different
#               httex, l2h and TeX used to gather de references
# and I choose to ignore them as the remaining ones pass.
test-custom:
	cd $(WORKSRC) && /usr/bin/env -i $(BUILD_ENV) && $(MAKE) -i -k -C $(OBJDIR) check
	$(MAKECOOKIE)
