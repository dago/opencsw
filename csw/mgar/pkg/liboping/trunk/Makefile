# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = liboping
VERSION = 1.8.0

DESCRIPTION = A library to generate ICMP echo requests

MASTER_SITES = http://noping.cc/files/
DISTFILES += $(DISTNAME).tar.bz2

VENDOR_URL = http://noping.cc/

PACKAGES += CSWliboping0
SPKG_DESC_CSWliboping0 = A library to generate ICMP echo requests, liboping.so.0
PKGFILES_CSWliboping0 += $(call pkgfiles_lib,liboping.so.0)

PACKAGES += CSWoping
SPKG_DESC_CSWoping = Generating ICMP echo requests efficiently
PKGFILES_CSWoping += $(bindir)/.*
PKGFILES_CSWoping += .*/oping\.8
RUNTIME_DEP_PKGS_CSWoping += CSWliboping0
RUNTIME_DEP_PKGS_CSWoping += CSWlibncursesw5

PACKAGES += CSWpm-net-oping
SPKG_DESC_CSWpm-net-oping = Perl module for generating ICMP echo requests efficiently
PKGFILES_CSWpm-net-oping += $(libdir)/perl5/.*
PKGFILES_CSWpm-net-oping += .*\.3perl
RUNTIME_DEP_PKGS_CSWpm-net-oping += CSWperl
RUNTIME_DEP_PKGS_CSWpm-net-oping += CSWliboping0

PACKAGES += CSWliboping-dev
SPKG_DESC_CSWliboping-dev = Development files for liboping.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWliboping-dev += CSWliboping0

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS += $(DIRPATHS)

# No 64 bit Perl yet
CONFIGURE_ARGS-64 += --without-perl-bindings
CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(MEMORYMODEL))

EXTRA_MERGE_EXCLUDE_FILES += .*/perllocal\.pod

include gar/category.mk

post-install:
	ginstall -d -m 0755 $(DESTDIR)$(mandir)
	-mv $(DESTDIR)$(prefix)/man/man3 $(DESTDIR)$(mandir)/man3 && rmdir $(DESTDIR)$(prefix)/man
	@$(MAKECOOKIE)
