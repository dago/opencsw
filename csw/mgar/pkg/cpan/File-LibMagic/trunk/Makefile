GARNAME = File-LibMagic
GARVERSION = 0.96
CATEGORIES = cpan
AUTHOR = FITZNER

DESCRIPTION = Perlwrapper for libmagic
define BLURB
endef

DISTFILES = COPYING
MODDIST = $(GARNAME)-$(GARVERSION).tgz

DEP_PKGS = CSWfile CSWzlib

PACKAGES = CSWpmfilelibmagic
CATALOGNAME = pm_filelibmagic

PERL_CONFIGURE_ARGS = INC="-I. -I$(includedir)"

include gar/category.mk
