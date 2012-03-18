# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libivykis
VERSION = 0.26
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Async I/O-assisting library
define BLURB
  libivykis is a thin wrapper over various OS'es implementation of I/O readiness
  notification facilities (such as poll(2), kqueue(2)) and is mainly intended
  for writing portable high-performance network servers.
endef

MASTER_SITES = $(SF_MIRRORS)
# UPSTREAM_USE_SF = 1
# UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=
DISTNAME = ivykis-$(VERSION)
DISTFILES  = $(DISTNAME).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
# Need something like this, or fix the configure script
# CONFIGURE_ARGS = --host=core2-pc-solaris2.10

include gar/category.mk

