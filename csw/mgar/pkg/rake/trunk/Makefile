# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

NAME = rake
VERSION = 0.8.7
CATEGORIES = devel
GARTYPE = v2

DESCRIPTION = Simple ruby build program similar to make
define BLURB
  Rakefiles (rake's version of Makefiles) are completely defined in standard
  Ruby syntax. No XML files to edit. No quirky Makefile syntax to worry about
  (is that a tab or a space?)
endef

MASTER_SITES = http://rubyforge.org/frs/download.php/56872/
DISTFILES  = $(NAME)-$(VERSION).tgz

LICENSE = MIT-LICENSE
ARCHALL = 1

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

BUILD_SCRIPTS     =
CONFIGURE_SCRIPTS =
INSTALL_SCRIPTS   = ruby

VENDOR_URL = http://rake.rubyforge.org/

include gar/category.mk

install-ruby:
	@( cd $(WORKSRC) ; $(INSTALL_ENV) ruby install.rb )
	@$(MAKECOOKIE)

# Copy samples and project docs
post-install:
	@mkdir -p $(DESTDIR)$(docdir)
	@cp -R $(WORKSRC)/doc $(DESTDIR)$(docdir)/rake
	@$(MAKECOOKIE)
