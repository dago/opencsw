NAME = Dancer
VERSION = 1.3132
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = YANICK

DESCRIPTION = A minimal-effort oriented web application framework
define BLURB
endef

LICENSE = LICENSE

PACKAGES += CSWpm-dancer
CATALOGNAME_CSWpm-dancer = pm_dancer

ARCHALL_CSWpm-dancer = 1

RUNTIME_DEP_PKGS_CSWpm-dancer += CSWpm-hash-merge-simple
RUNTIME_DEP_PKGS_CSWpm-dancer += CSWpm-http-body
RUNTIME_DEP_PKGS_CSWpm-dancer += CSWpm-http-server-simple-psgi
RUNTIME_DEP_PKGS_CSWpm-dancer += CSWpm-libwww-perl
RUNTIME_DEP_PKGS_CSWpm-dancer += CSWpm-uri
RUNTIME_DEP_PKGS_CSWpm-dancer += CSWpmmimetypes

include gar/category.mk

post-install-modulated:
	-perl -pi -e 's,/usr/local,$(prefix),g' \
		$(DESTDIR)$(prefix)/share/man/man3/Dancer::Deployment.3perl \
		$(DESTDIR)$(prefix)/share/perl/csw/Dancer/Deployment.pod
