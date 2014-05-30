# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = darkstat
VERSION = 3.0.718
GARTYPE = v2

DESCRIPTION = Network traffic analyzer
define BLURB
 Captures network traffic, calculates statistics about usage, and serves reports over HTTP.
endef

MASTER_SITES = http://unix4lyfe.org/darkstat/
DISTFILES  = $(DISTNAME).tar.bz2

RUNTIME_DEP_PKGS_CSWdarkstat += CSWlibpcap1
RUNTIME_DEP_PKGS_CSWdarkstat += CSWlibz1

TEST_SCRIPTS =

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

