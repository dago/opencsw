# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = pypcap
VERSION = 1.1
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Simplified object-oriented Python extension module for libpcap

MASTER_SITES = $(GOOGLE_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

CONFIGURE_ARGS = --with-pcap /opt/csw
CONFIGURE_SCRIPTS = $(WORKSRC)/setup.py

PACKAGES = CSWpy-pcap

include gar/category.mk

