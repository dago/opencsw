# $Id$

NAME		=	dnspython
VERSION		=	1.10.0
CATEGORIES	=	python
GARTYPE		=	v2

DESCRIPTION = A DNS toolkit for Python
define BLURB
  dnspython is a DNS toolkit for Python. It supports almost all record
  types. It can be used for queries, zone transfers, and dynamic
  updates.  It supports TSIG authenticated messages and EDNS0.

  dnspython provides both high and low level access to DNS. The high
  level classes perform queries for data of a given name, type, and
  class, and return an answer set.  The low level classes allow direct
  manipulation of DNS zones, messages, names, and records.
endef

MASTER_SITES	=	http://www.dnspython.org/kits/$(VERSION)/
DISTFILES 		=	$(DISTNAME).tar.gz
PATCHFILES		+=	0001-consistent-use-of-tabs-and-spaces-in-indentation.patch
SPKG_SOURCEURL	=	$(MASTER_SITES)
BUILD_DEP_PKGS	=	CSWpysetuptools

TEST_SCRIPTS	=	nominal

include gar/category.mk

test-nominal:
	cd $(WORKSRC)/tests && /usr/bin/env -i $(BUILD_ENV) && $(MAKE) -i -k check
	$(MAKECOOKIE)
