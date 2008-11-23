GARNAME = libapreq2
GARVERSION = 2.08
CATEGORIES = cpan
AUTHOR = JOESUF

DESCRIPTION = methods for dealing with Apache request data
define BLURB
  Apache::Request is a subclass of the Apache class, which adds methods for
  parsing GET requests and POST requests where Content-type is one of
  application/x-www-form-urlencoded or multipart/form-data. See the libapreq(3)
  manpage for more details.
endef

DISTFILES  = $(call admfiles,CSWlibapreq2,depend prototype)
DISTFILES += $(call admfiles,CSWlibapreq2-devel,depend prototype)
CSWap2modapreq2_admfiles = depend prototype postinstall preremove
DISTFILES += $(call admfiles,CSWap2modapreq2,$(CSWap2modapreq2_admfiles))
DISTFILES += $(call admfiles,CSWpmapreq2,depend prototype)

# Ensure args are requestrecs
PATCHFILES += requestrec.diff

MODDIST  = $(GARNAME)-$(GARVERSION).tar.gz
DEPENDS += cpan/Apache-Test
DEPENDS += cpan/ExtUtils-XSBuilder
DEPENDS += cpan/mod_perl2

AP2_ROOT = $(prefix)/apache2

CONFIGURE_ARGS  = --enable-perl-glue
CONFIGURE_ARGS += --with-perl=$(bindir)/perl
CONFIGURE_ARGS += --with-apache2-apxs=$(AP2_ROOT)/sbin/apxs
CONFIGURE_ARGS += --with-apr-config=$(AP2_ROOT)/bin/apr-config
CONFIGURE_ARGS += --with-apu-config=$(AP2_ROOT)/bin/apu-config
CONFIGURE_ARGS += --with-expat=$(prefix)
CONFIGURE_ARGS += --with-mm-opts="INSTALLDIRS=vendor"

PERL_CONFIGURE_ARGS =

FIXCONFIG_DIRS += $(DESTDIR)$(prefix)/apache2/lib
STRIP_DIRS   += $(DESTDIR)$(prefix)/apache2/libexec

EXTRA_INC = $(prefix)/bdb43/include
EXTRA_LIB = $(prefix)/bdb43/lib $(prefix)/apache2/lib

SKIPTEST = 1

include gar/category.mk

pre-package: test fix-cfgscript

fix-cfgscript:
	@perl -i -plne 's/(APREQ_(?:SOURCE|BUILD)_DIR=).*$$/\1""/' \
		$(DESTDIR)$(prefix)/apache2/bin/apreq2-config

