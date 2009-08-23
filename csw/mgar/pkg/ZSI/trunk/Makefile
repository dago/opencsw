# BEWARE: 
# For now this build recipe relies on gar/v2-skayser for the python category
#
GARNAME = ZSI
GARVERSION = 2.0
CATEGORIES = python

DESCRIPTION = Web services for Python programmers, both client and servers.
define BLURB
  ZSI, the Zolera SOAP Infrastructure, is a Python package that provides
  an implementation of SOAP messaging, as described in The SOAP 1.1
  Specification. In particular, ZSI parses and generates SOAP messages,
  and converts between native Python datatypes and SOAP syntax. It can
  also be used to build applications using SOAP Messages with Attachments.
  ZSI is ``transport neutral'', and provides only a simple I/O and
  dispatch framework; a more complete solution is the responsibility of
  the application using ZSI. As usage patterns emerge, and common
  application frameworks are more understood, this may change. 
endef

MASTER_SITES = $(SF_MIRRORS)
SF_PROJ = pywebsvcs/$(DISTNAME)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

SPKG_SOURCEURL = http://pywebsvcs.sf.net/
PACKAGES = CSWpyzsi
CATALOGNAME = py_zsi

REQUIRED_PKGS = CSWpyxml

include gar/category.mk
