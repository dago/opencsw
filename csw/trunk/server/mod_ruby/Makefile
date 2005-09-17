GARNAME = mod_ruby
GARVERSION = 1.2.4
CATEGORIES = server

DESCRIPTION = an Apache/Ruby integration module
define BLURB
  mod_ruby is an Apache module that embeds the Ruby language interpreter
  within the server, allowing for Apache handlers to be written in Ruby for
  faster and more powerful applications than plain CGI.
endef

MASTER_SITES = http://www.modruby.net/archive/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWap2modruby.gspec
#DISTFILES += CSWap2modruby.depend
#DISTFILES += CSWap2modruby.prototype
#DISTFILES += CSWap2modruby.postinstall
#DISTFILES += CSWap2modruby.preremove
#DISTFILES += CSWap2modruby.space

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
