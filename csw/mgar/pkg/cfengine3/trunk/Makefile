# $Id$
#
NAME = cfengine3
VERSION = 3.2.3
CATEGORIES = utils

DESCRIPTION = Open source configuration management system
define BLURB
  CFEngine Community is the Open Source foundation of CFEngine's innovative
  configuration management technology that helps systems administrators
  automate and ensure the availability, security and compliance of
  mission-critical applications and services.
endef

DISTNAME = cfengine-$(VERSION)
MASTER_SITES = http://www.cfengine.com/source-code/download?file=
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += $(NAME)rc
DISTFILES += CSW$(NAME)rt.postinstall
DISTFILES += csw$(NAME)-cfexecd
DISTFILES += csw$(NAME)-cfmonitord
DISTFILES += csw$(NAME)-cfserverd
DISTFILES += README.CSW
VENDOR_URL = http://www.cfengine.com/community

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES =

#
# CUSTOM VARIABLES
#
cfengine_workdir	= $(localstatedir)/$(NAME)
cfengine_workdir_bin	= $(cfengine_workdir)/bin
initddir		= $(sysconfdir)/init.d

EXTRA_MERGE_EXCLUDE_FILES = $(datadir)/cfengine.*

PACKAGES = CSW$(NAME)rt
CATALOGNAME_CSW$(NAME)rt = $(NAME)_rt
SPKG_DESC_CSW$(NAME)rt = CFEngine 3 runtime and documentation
RUNTIME_DEP_PKGS_CSW$(NAME)rt += CSWbdb48
RUNTIME_DEP_PKGS_CSW$(NAME)rt += CSWosslrt
RUNTIME_DEP_PKGS_CSW$(NAME)rt += CSWlibpcre0


PACKAGES += CSW$(NAME)server
CATALOGNAME_CSW$(NAME)server = $(NAME)_server
SPKG_DESC_CSW$(NAME)server = CFEngine 3 server binary
RUNTIME_DEP_PKGS_CSW$(NAME)server += CSWbdb48
RUNTIME_DEP_PKGS_CSW$(NAME)server += CSWosslrt
RUNTIME_DEP_PKGS_CSW$(NAME)server += CSWlibpcre0
RUNTIME_DEP_PKGS_CSW$(NAME)server += CSW$(NAME)rt
PKGFILES_CSW$(NAME)server += $(sbindir)/cf-serverd
PKGFILES_CSW$(NAME)server += $(sbindir)/cf-runagent
PKGFILES_CSW$(NAME)server += $(mandir)/.*/cf-serverd.*
PKGFILES_CSW$(NAME)server += $(mandir)/.*/cf-runagent.*
PKGFILES_CSW$(NAME)server += $(initddir)/csw$(NAME)-cfserverd
PKGFILES_CSW$(NAME)server += $(docdir)/$(NAME)_server/README.CSW

PACKAGES += CSW$(NAME)client
CATALOGNAME_CSW$(NAME)client = $(NAME)_client
SPKG_DESC_CSW$(NAME)client = CFEngine 3 client binaries
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWbdb48
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWosslrt
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWlibpcre0
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSW$(NAME)rt
PKGFILES_CSW$(NAME)client += $(sbindir)/cf-agent
PKGFILES_CSW$(NAME)client += $(sbindir)/cf-execd
PKGFILES_CSW$(NAME)client += $(sbindir)/cf-monitord
PKGFILES_CSW$(NAME)client += $(mandir)/.*/cf-agent.*
PKGFILES_CSW$(NAME)client += $(mandir)/.*/cf-execd.*
PKGFILES_CSW$(NAME)client += $(mandir)/.*/cf-monitord.*
PKGFILES_CSW$(NAME)client += $(cfengine_workdir_bin)/cf-agent
PKGFILES_CSW$(NAME)client += $(initddir)/csw$(NAME)-cfexecd
PKGFILES_CSW$(NAME)client += $(initddir)/csw$(NAME)-cfmonitord
PKGFILES_CSW$(NAME)client += $(docdir)/$(NAME)_client/README.CSW

# CFEngine provides three daemons
#  - cf-execd (client)
#  - cf-monitord (client)
#  - cf-serverd (server)
INITSMF =  $(initddir)/csw$(NAME)-cfexecd
INITSMF += $(initddir)/csw$(NAME)-cfmonitord
INITSMF += $(initddir)/csw$(NAME)-cfserverd

# This file gets installed by CSW$(NAME)rt since it is used by
# the server and client component
PRESERVECONF = $(sysconfdir)/$(NAME)rc

BUILD64 = 1

BUILD_DEP_PKGS = CSWbdb48devel
BUILD_DEP_PKGS += CSWlibpcre-dev
BUILD_DEP_PKGS += CSWossldevel
BUILD_DEP_PKGS += CSWflex
BUILD_DEP_PKGS += CSWbison

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-silent-rules
CONFIGURE_ARGS += --with-berkeleydb=$(prefix)/bdb48
CONFIGURE_ARGS += --with-openssl=$(prefix)
CONFIGURE_ARGS += --with-pcre=$(prefix)
CONFIGURE_ARGS += --with-workdir=$(cfengine_workdir)
CONFIGURE_ARGS += --without-sqlite3
CONFIGURE_ARGS += --without-qdbm
CONFIGURE_ARGS += --without-postgresql
CONFIGURE_ARGS += --without-mysql

EXTRA_INC = $(prefix)/bdb48/include

EXTRA_RUNPATH_DIRS = $(prefix)/bdb48/lib
EXTRA_RUNPATH_ISALIST   = $(EXTRA_RUNPATH_DIRS)
EXTRA_LDFLAGS = -L$(prefix)/bdb48/lib/$(MM_LIBDIR)

include gar/category.mk

post-install-modulated: rename-cfengine-dir make-cfengine-workdir install-cfengine-links install-smf-manifests install-cfengine3rc install-cfengine3-csw-doc
	@$(MAKECOOKIE)

rename-cfengine-dir:
	if test -d $(DESTDIR)$(datadir)/cfengine ; then \
		mv $(DESTDIR)$(datadir)/cfengine $(DESTDIR)$(datadir)/$(NAME) ;\
	fi
	if test -d $(DESTDIR)$(docdir)/cfengine ; then \
		mv $(DESTDIR)$(docdir)/cfengine $(DESTDIR)$(docdir)/$(NAME) ;\
	fi

install-smf-manifests:
	ginstall -d $(DESTDIR)$(initddir)
	ginstall $(WORKDIR)/csw$(NAME)-cfexecd $(DESTDIR)$(initddir)/
	ginstall $(WORKDIR)/csw$(NAME)-cfmonitord $(DESTDIR)$(initddir)/
	ginstall $(WORKDIR)/csw$(NAME)-cfserverd $(DESTDIR)$(initddir)/

make-cfengine-workdir:
	if test ! -d $(DESTDIR)$(cfengine_workdir) ; then \
		ginstall -d $(DESTDIR)$(cfengine_workdir); \
	fi
	if test ! -d $(DESTDIR)$(cfengine_workdir_bin) ; then\
		ginstall -d $(DESTDIR)$(cfengine_workdir_bin) ;\
	fi

install-cfengine-links: make-cfengine-workdir
	if test ! -h $(DESTDIR)$(cfengine_workdir_bin)/cf-promises ; then \
		ln -s $(sbindir)/cf-promises $(DESTDIR)$(cfengine_workdir_bin)/cf-promises ;\
	fi
	if test ! -h $(DESTDIR)$(cfengine_workdir_bin)/cf-agent ; then \
		ln -s $(sbindir)/cf-agent $(DESTDIR)$(cfengine_workdir_bin)/cf-agent ;\
	fi

install-cfengine3rc:
	ginstall $(WORKDIR)/$(NAME)rc $(DESTDIR)$(sysconfdir)/$(NAME)rc.CSW

install-cfengine3-csw-doc: rename-cfengine-dir
	ginstall $(WORKDIR)/README.CSW $(DESTDIR)$(docdir)/$(NAME)
