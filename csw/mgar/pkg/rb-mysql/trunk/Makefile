NAME = rb-mysql
VERSION = 2.8.1
CATEGORIES = lang
GARTYPE = v2

DESCRIPTION = Mysql Bindings for Fuby

MASTER_SITES = http://rubygems.org/downloads/
DISTFILES  = mysql-$(VERSION).gem

BUILD_DEP_PKGS = CSWrubygems
RUNTIME_DEP_PKGS = CSWrubygems

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz


CONFIGURE_SCRIPTS = 
BUILD_SCRIPTS = 
TEST_SCRIPTS = 

INSTALL_SCRIPTS = custom

include gar/category.mk

GEMDIR = /opt/csw/lib/ruby/gems/1.8
install-custom:
	( cd $(WORKSRC)/..; gem install --no-test --install-dir $(DESTDIR)$(GEMDIR) $(DISTFILES) )
