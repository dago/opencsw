GARNAME = xmlrpc-c
GARVERSION = 1.16.13
SVN_REVISION = 1679
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

MASTER_SITES  = svn-http://xmlrpc-c.svn.sourceforge.net/svnroot/xmlrpc-c/
DISTFILES = stable
DISTNAME = stable
NOCHECKSUM = stable
SVNHTTP_CO_ARGS = -r $(SVN_REVISION) --no-auth-cache --username guest --password guest

LICENSE = doc/COPYING
DOCFILES += CREDITS DEVELOPING HISTORY INSTALL SECURITY TESTING TODO

SPKG_SOURCEURL = http://xmlrpc-c.sourceforge.net

PACKAGES = CSWxmlrpc-c
CATALOGNAME_CSWxmlrpc-c = xmlrpc_c
SPKG_DESC_CSWxmlrpc-c = $(DESCRIPTION)

PATCHFILES = mainpatch

REQUIRED_PKGS_CSWxmlrpc-c  = CSWcurlrt CSWlibidn CSWoldaprt CSWosslrt CSWzlib

# We define upstream file regex so we can be notifed of 
# new upstream software release
#UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tgz

#BUILD64 = 1
#NO_ISAEXEC = 1

CONFIGURE_ARGS  = $(DIRPATHS)

TEST_TARGET = check 

include gar/category.mk
