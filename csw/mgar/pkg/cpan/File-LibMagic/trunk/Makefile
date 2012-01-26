NAME = File-LibMagic
VERSION = 0.96
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = FITZNER

DESCRIPTION = Perlwrapper for libmagic
define BLURB
endef

DISTFILES = COPYING
MODDIST = $(NAME)-$(VERSION).tgz

DEP_PKGS = CSWfile CSWzlib

PACKAGES = CSWpmfilelibmagic
CATALOGNAME = pm_filelibmagic

PERL_CONFIGURE_ARGS = INC="-I. -I$(includedir)"

include gar/category.mk
