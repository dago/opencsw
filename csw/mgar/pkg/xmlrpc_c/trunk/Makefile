GARNAME = xmlrcp-c
GARVERSION = 1.06.32
CATEGORIES = lib

DESCRIPTION = A lightweight RPC library based on XML and HTTP.
define BLURB
	It's a spec and a set of implementations that allow software 
	running on disparate operating systems, running in different 
	environments to make procedure calls over the Internet.
	It's remote procedure calling using HTTP as the transport and 
	XML as the encoding. XML-RPC is designed to be as simple as possible, 
	while allowing complex data structures to be transmitted, 
	processed and returned.
endef

MASTER_SITES = $(SF_MIRRORS)
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=16847
SPKG_SOURCEURL = http://xmlrpc-c.sourceforge.net
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz

PACKAGES = CSWxmlrpc-c
CATALOGNAME_CSWxmlrpc-c = xmlrpc_c
SPKG_DESC_CSWgd = $(DESCRIPTION)

#PATCHFILES = 

#REQUIRED_PKGS_CSWxmlrpc-c  = 

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tgz

#BUILD64 = 1
#NO_ISAEXEC = 1

CONFIGURE_ARGS  = $(DIRPATHS)

include gar/category.mk
