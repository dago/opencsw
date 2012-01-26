# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = ocrad
VERSION = 0.19
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = GNU Optical Character Recognition
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

BUILD_OVERRIDE_VARS = CXXFLAGS
BUILD_OVERRIDE_VAR_CXXFLAGS = $(CXXFLAGS)

include gar/category.mk

post-extract-modulated:
	@# Crappy bashisms
	-perl -npe "s,#! /bin/sh,#!/bin/bash," -i $(WORKSRC)/configure
	@$(MAKECOOKIE)
