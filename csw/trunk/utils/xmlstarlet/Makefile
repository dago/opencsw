GARNAME = xmlstarlet
GARVERSION = 1.0.1
CATEGORIES = utils

DESCRIPTION = XML transformation utility
define BLURB
  XMLStarlet is a set of command line utilities (tools)
  to transform, query, validate, and edit XML documents
  and files using simple set of shell commands in similar
  way it is done for text files with UNIX grep, sed, awk,
  diff, patch, join, etc utilities.
endef

PWD = $(shell pwd)

LIBXMLNAME = libxml2
LIBXMLVERSION = 2.6.29
LIBXMLSRC = $(PWD)/$(WORKDIR)/$(LIBXMLNAME)-$(LIBXMLVERSION)

LIBXSLTNAME = libxslt
LIBXSLTVERSION = 1.1.21
LIBXSLTSRC = $(PWD)/$(WORKDIR)/$(LIBXSLTNAME)-$(LIBXSLTVERSION)


SF_PROJ = xmlstar
MASTER_SITES  = ftp://xmlsoft.org/libxml2/
MASTER_SITES += $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(LIBXMLNAME)-$(LIBXMLVERSION).tar.gz
DISTFILES += $(LIBXSLTNAME)-$(LIBXSLTVERSION).tar.gz
DISTFILES += $(call admfiles,CSWxmlstarlet,depend)

PATCHFILES = $(GARNAME)-$(GARVERSION)-cc.patch

include ../category.mk

configure-$(LIBXMLSRC)/configure:
	echo $(CONFIGURE_ENV)
	@echo " ==> Running configure in $(LIBXMLSRC)"
	cd $(LIBXMLSRC) && ./configure \
		--enable-shared=no --enable-static=yes
	@$(MAKECOOKIE)

configure-$(LIBXSLTSRC)/configure:
	@echo " ==> Running configure in $(LIBXSLTSRC)"
	cd $(LIBXSLTSRC) && ./configure \
		--with-libxml-src=$(LIBXMLSRC) \
		--with-crypto=no
	@$(MAKECOOKIE)

CONFIGURE_ARGS = $(DIRPATHS) \
	--with-libxml-src=$(LIBXMLSRC) \
	--with-libxslt-src=$(LIBXSLTSRC) \
	--with-libiconv-include-prefix=$(prefix)/include \
	--with-libiconv-libs-prefix=$(prefix)/lib

pre-configure: configure-$(LIBXMLSRC)/configure configure-$(LIBXSLTSRC)/configure
	@$(MAKECOOKIE)

pre-build: build-$(LIBXMLSRC)/Makefile build-$(LIBXSLTSRC)/Makefile
	@$(MAKECOOKIE)
