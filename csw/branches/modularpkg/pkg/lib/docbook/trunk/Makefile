GARNAME = docbook
GARVERSION = 1.68.1
CATEGORIES = lib

DESCRIPTION = docbook xsl stylesheets
define BLURB
  DocBook is an XML/SGML vocabulary that enables you to create document
  content in a presentation-neutral form that captures the logical structure
  of the content. Using the DocBook stylesheets, you can publish DocBook
  content as HTML pages and PDF files and other formats, including man pages,
  HTML Help, and JavaHelp.
endef

MASTER_SITES = $(SF_MIRROR)/$(GARNAME)/
DISTFILES = $(GARNAME)-xsl-$(GARVERSION).tar.bz2

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@echo how the heck does this get installed??!
	@false
