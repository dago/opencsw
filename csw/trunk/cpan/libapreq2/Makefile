GARNAME = libapreq2
GARVERSION = 2.06
DISTVERSION = $(GARVERSION)-dev
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

DISTNAME = $(GARNAME)-$(DISTVERSION)
WORKSRC  = $(WORKDIR)/$(DISTNAME)

MODDIST  = $(DISTNAME).tar.gz
DEPENDS += cpan/Apache-Test cpan/ExtUtils-XSBuilder
#DEPENDS += cpan/mod_perl2

CONFIGURE_ARGS  = --enable-perl-glue
CONFIGURE_ARGS += --with-perl=$(bindir)/perl
CONFIGURE_ARGS += --with-apache2-apxs=$(prefix)/apache2/sbin/apxs
CONFIGURE_ARGS += --with-apr-config=$(bindir)/apr-config
CONFIGURE_ARGS += --with-apu-config=$(bindir)/apu-config
CONFIGURE_ARGS += --with-expat=$(prefix)

# Must be installed to test
ENABLE_TEST = 0

LIBTOOL_LADIR = $(DESTDIR)$(libdir)
STRIP_DIRS   += $(DESTDIR)$(prefix)/apache2/libexec

include ../category.mk

# Remove this when it's not dev
SPKG_REVSTAMP := $(SPKG_REVSTAMP)_dev

pre-package: test
