# $Id$
NAME = lighttpd
VERSION = 1.4.28
CATEGORIES = devel

DESCRIPTION = lighttpd - Security, speed, compliance, and flexibility http server
define BLURB
  Security, speed, compliance, and flexibility -- all of these describe lighttpd
  (pron. lighty) which is rapidly redefining efficiency of a webserver; as it is
  designed and optimized for high performance environments. With a small memory
  footprint compared to other web-servers, effective management of the cpu-load,
  and advanced feature set (FastCGI, SCGI, Auth, Output-Compression,
  URL-Rewriting and many more) lighttpd is the perfect solution for every server
  that is suffering load problems. And best of all it's Open Source licensed
  under the revised BSD license. 
endef

MASTER_SITES = http://download.lighttpd.net/lighttpd/releases-1.4.x/
DISTFILES    = $(NAME)-$(VERSION).tar.gz

PATCHFILES += 0001-Work-around-linking-problem-buffer.c.patch

include gar/category.mk
