# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = mocha
VERSION = 0.9.7
CATEGORIES = lib
GARTYPE = v2
DESCRIPTION = a library for mocking and stubbing using a syntax like that of JMock
define BLURB
  Mocha is a library for mocking and stubbing using a syntax like that of
  JMock.  It can be used with many testing frameworks e.g. Test::Unit, RSpec,
  test/spec, expectations, Dust, MiniTest and even JtestR.  Mocha provides
  a unified, simple and readable syntax for both traditional mocking and
  partial mocking.
endef
SPKG_SOURCEURL = http://mocha.rubyforge.org/
MASTER_SITES = http://rubyforge.org/frs/download.php/59668/
DISTFILES  = $(NAME)-$(VERSION).tgz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz
ARCHALL = 0
RUNTIME_DEP_PKGS = CSWruby
BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS) CSWrake
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = ruby
TEST_SCRIPTS =

install-ruby:
	gfind $(WORKSRC) -name '._*' -exec rm {} \;
	ginstall -d -m 755 $(DESTDIR)$(libdir)/ruby/site_ruby/1.8
	(cd $(WORKSRC)/lib; gcp -a * $(DESTDIR)$(libdir)/ruby/site_ruby/1.8)
	# TODO(maciej): Use the provided gem specification for installation.
	# (cd $(WORKSRC)/lib; \
	#  rake gem; \
	#  gem install --install-dir=$(DESTDIR) --local ./pkg/$(NAME)-$(VERSION).gem)
	@$(MAKECOOKIE)

include gar/category.mk
