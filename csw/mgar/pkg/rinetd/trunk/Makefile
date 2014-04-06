# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = rinetd
VERSION = 0.62
GARTYPE = v2

DESCRIPTION = Internet redirection server - port forwarder
define BLURB
  Redirects TCP connections from one IP address and port to another. rinetd is a single-process server which handles any number of connections to the address/port pairs specified in the file /etc/rinetd.conf. Since rinetd runs as a single process using nonblocking I/O, it is able to redirect a large number of connections without a severe impact on the machine. This makes it practical to run TCP services on machines inside an IP masquerading firewall.
endef

MASTER_SITES = http://www.boutell.com/rinetd/http/
DISTNAME = $(NAME)
DISTFILES  = $(DISTNAME).tar.gz

GARCOMPILER = GCC4

PATCHFILES +=  0001-Makefile.patch
CONFIGURE_SCRIPTS = 
SKIPTEST = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

