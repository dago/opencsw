# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = gtk-gnutella
VERSION = 1.0.1
GARTYPE = v2
CATEGORIES = default

DESCRIPTION = shares files in a peer to peer network
define BLURB
   Gtk-Gnutella is a reliable and efficient Gnutella client, supporting the latest Gnutella protocol, bandwidth limitation (both incoming and outgoing) traffic compression, and advanced search filters among other features.

Gnutella is a peer-based file-sharing protocol that allows a user running a Gnutella client to search for and download files from other Gnutella users, as well as share some files of his/her own.

Gtk-Gnutella offers all the extra features you expect from a modern client: persistent downloads, searches and filters, intuitive interface, upload statistics, queuing, and of course total control over many configuration parameters. 
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.bz2

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS = custom

include gar/category.mk

configure-custom:
	cd $(WORKSRC) && CC=gcc ./build.sh --prefix=/opt/csw
	@$(MAKECOOKIE)
