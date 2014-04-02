# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id: Makefile 22208 2013-10-14 12:42:44Z dmichelsen $

NAME = send_nsca
VERSION = 0.1.4.1
CATEGORIES = python
GARTYPE = v2

MASTER_SITES += $(PYPI_MIRROR)
DISTFILES += $(DISTNAME).tar.gz

BUILD_DEP_PKGS += CSWpy-crypto

PACKAGES += CSWpy-send-nsca
SPKG_DESC_CSWpy-send-nsca = Python implementation of Nagios send_nsca
# PKGFILES is catchall
ARCHALL_CSWpy-send-nsca = 1
# This is indeed needed
RUNTIME_DEP_PKGS_CSWpy-send-nsca += CSWpy-crypto
CHECKPKG_OVERRIDES_CSWpy-send-nsca += surplus-dependency|CSWpy-crypto

REINPLACEMENTS += cfg
REINPLACE_MATCH_cfg = /etc/send_nsca.cfg
REINPLACE_WITH_cfg = $(sysconfdir)/nagios/send_nsca.cfg
REINPLACE_FILES_cfg += bin/py_send_nsca
REINPLACE_FILES_cfg += send_nsca/nsca.py

include gar/category.mk
