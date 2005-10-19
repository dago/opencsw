GARNAME = rails
GARVERSION = 0.13.1
CATEGORIES = server

DESCRIPTION = Ruby web application framework
define BLURB
	Rails is a Web application framework for Ruby modeled after the MVC
	pattern.  It uses Action Pack for the Controller and View, Active Record
	for the Model.
endef

MASTER_SITES = http://rubyforge.org/frs/download.php/5176/

DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
DISTFILES += activerecord-1.11.1.tgz
DISTFILES += actionpack-1.9.1.tgz
DISTFILES += actionmailer-1.0.1.tgz
DISTFILES += activesupport-1.1.1.tgz
DISTFILES += actionwebservice-0.8.1.tgz

#DISTFILES += CSWrails.gspec
#DISTFILES += CSWrails.depend
#DISTFILES += CSWrails.prototype
#DISTFILES += CSWrails.postinstall
#DISTFILES += CSWrails.preremove
#DISTFILES += CSWrails.space

CONFIGURE_SCRIPTS = ruby

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apxs=$(prefix)/apache2/sbin/apxs
#CONFIGURE_ARGS += --with-python=$(bindir)/python
#CONFIGURE_ARGS += --with-flex=$(prefix)/flex-2.5.31/bin/flex

include ../category.mk

configure-ruby:
	( cd $(WORKSRC) ; \
		$(CONFIGURE_ENV) ruby ./configure.rb $(CONFIGURE_ARGS) )
	@$(MAKECOOKIE)
