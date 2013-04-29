# $Id$

NAME	=	libmtp
VERSION	=	1.1.6
GARTYPE	=	v2

DESCRIPTION	=	A LGPL library implementation of the Media Transfer Protocol
define BLURB
  A LGPL library implementation of the Media Transfer Protocol (MTP),
  a superset of the Picture Transfer Protocol (PTP).
endef

MASTER_SITES=	$(SF_MIRRORS)
DISTFILES	=	$(DISTNAME).tar.gz

GARCOMPILER		=	GNU
EXTRA_INC		=	/usr/sfw/include
EXTRA_LDFLAGS	=	-L/usr/sfw/lib -R/usr/sfw/lib -lusb
CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--enable-doxygen

include gar/category.mk

