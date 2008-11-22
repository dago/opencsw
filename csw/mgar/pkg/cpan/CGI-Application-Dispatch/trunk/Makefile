GARNAME = CGI-Application-Dispatch
GARVERSION = 2.10
CATEGORIES = cpan
AUTHOR = WONKO

DESCRIPTION = Dispatch requests to CGI::Application based objects
define BLURB
  This module provides a way (as a mod_perl handler or running under vanilla
  CGI) to look at the path (r->path_info or ENV{PATH_INFO}) of the incoming
  request, parse off the desired module and it's run mode, create an instance
  of that module and run it.
endef

DISTFILES += $(call admfiles,CSWpmcgiappdisp,depend prototype)

DEPENDS += cpan/Module-Build cpan/Apache-Test
DEPENDS += cpan/CGI-Application

CONFIGURE_ARGS = destdir=$(DESTDIR)

APACHE_TEST_HTTPD=$(prefix)/apache2/sbin/httpd
export APACHE_TEST_HTTPD

include ../category.mk
