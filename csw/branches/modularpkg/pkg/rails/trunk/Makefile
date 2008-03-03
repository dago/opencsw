GARNAME = rails
GARVERSION = 0.14.3
CATEGORIES = server

DESCRIPTION = Ruby web application framework
define BLURB
	Rails is a Web application framework for Ruby modeled after the MVC
	pattern.  It uses Action Pack for the Controller and View, Active Record
	for the Model.
endef

activerecord     = 1.13.0
actionpack       = 1.11.0
actionmailer     = 1.1.3
activesupport    = 1.2.3
actionwebservice = 0.9.3

MASTER_SITES = http://rubyforge.org/frs/download.php/5176/

DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
DISTFILES += activerecord-$(activerecord).tgz
DISTFILES += actionpack-$(actionpack).tgz
DISTFILES += actionmailer-$(actionmailer).tgz
DISTFILES += activesupport-$(activesupport).tgz
DISTFILES += actionwebservice-$(actionwebservice).tgz

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

include gar/category.mk

configure-ruby:
	( cd $(WORKSRC) ; \
		$(CONFIGURE_ENV) ruby ./configure.rb $(CONFIGURE_ARGS) )
	@$(MAKECOOKIE)
