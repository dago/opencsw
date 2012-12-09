# $Id$
#
NAME = cfengine3
VERSION = 3.4.1
GARTYPE = v2
GARCOMPILER = SOS12U2

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

DESCRIPTION = Open source configuration management system
define BLURB
  CFEngine Community is the Open Source foundation of CFEngine's innovative
  configuration management technology that helps systems administrators
  automate and ensure the availability, security and compliance of
  mission-critical applications and services.
endef

DISTNAME = cfengine-$(VERSION)
MASTER_SITES = http://www.cfengine.com/source-code/download/
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += $(NAME)rc
DISTFILES += CSW$(NAME)utils.postinstall
DISTFILES += csw$(NAME)-cfexecd
DISTFILES += csw$(NAME)-cfmonitord
DISTFILES += csw$(NAME)-cfserverd
DISTFILES += README.CSW
DISTFILES += changelog.CSW
VENDOR_URL = http://www.cfengine.com/community

UFILES_REGEX = cfengine-(\d+(?:\.\d+)*).tar.gz

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES =

# See comment in patch
PATCHFILES += 0000-Do-not-perform-acceptance-test.patch
# Make build and tests work
PATCHFILES += 0001-Fix-preprocessor-macro-FUNC_DEPRECATED-to-avoid-synt.patch
PATCHFILES += 0003-Fix-empty-initializer.-Add-mkdtemp.patch
PATCHFILES += 0003-Remove-unsupported-compiler-flags.-Add-z-interpose-w.patch

#
# CUSTOM VARIABLES
#
cfengine_workdir	= $(localstatedir)/$(NAME)
cfengine_workdir_bin	= $(cfengine_workdir)/bin
initddir		= $(sysconfdir)/init.d

PACKAGES = CSW$(NAME)utils
# Catch all
CATALOGNAME_CSW$(NAME)utils = $(NAME)_utils
SPKG_DESC_CSW$(NAME)utils = CFEngine 3 utilities and documentation
RUNTIME_DEP_PKGS_CSW$(NAME)utils += CSWlibtokyocabinet9
RUNTIME_DEP_PKGS_CSW$(NAME)utils += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSW$(NAME)utils += CSWlibpcre1
CHECKPKG_OVERRIDES_CSW$(NAME)utils += catalogname-does-not-match-pkgname|pkgname=CSW$(NAME)utils|catalogname=$(NAME)_utils|expected-catalogname=$(NAME)utils
CHECKPKG_OVERRIDES_CSW$(NAME)utils += file-with-bad-content|/usr/local|root/opt/csw/share/doc/$(NAME)_utils/CoreBase/failsafe/failsafe.cf
CHECKPKG_OVERRIDES_CSW$(NAME)utils += file-with-bad-content|/usr/local|root/opt/csw/share/doc/$(NAME)_utils/ChangeLog
OBSOLETED_BY_CSW$(NAME)utils = CSWlibpromises1 CSW$(NAME)rt
CATALOGNAME_CSWlibpromises1 = libpromises1_stub
CATALOGNAME_CSW$(NAME)rt = $(NAME)_rt_stub

PACKAGES += CSW$(NAME)server
CATALOGNAME_CSW$(NAME)server = $(NAME)_server
SPKG_DESC_CSW$(NAME)server = CFEngine 3 server binary
RUNTIME_DEP_PKGS_CSW$(NAME)server += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSW$(NAME)server += CSW$(NAME)utils
PKGFILES_CSW$(NAME)server += $(sbindir)/cf-serverd
PKGFILES_CSW$(NAME)server += $(sbindir)/cf-runagent
PKGFILES_CSW$(NAME)server += $(mandir)/.*/cf-serverd.*
PKGFILES_CSW$(NAME)server += $(mandir)/.*/cf-runagent.*
PKGFILES_CSW$(NAME)server += $(initddir)/csw$(NAME)-cfserverd
PKGFILES_CSW$(NAME)server += $(docdir)/$(NAME)_server/.*\.CSW
CHECKPKG_OVERRIDES_CSW$(NAME)server += catalogname-does-not-match-pkgname|pkgname=CSW$(NAME)server|catalogname=$(NAME)_server|expected-catalogname=$(NAME)server

PACKAGES += CSW$(NAME)client
CATALOGNAME_CSW$(NAME)client = $(NAME)_client
SPKG_DESC_CSW$(NAME)client = CFEngine 3 client binaries
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSW$(NAME)utils
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWlibpcre1
RUNTIME_DEP_PKGS_CSW$(NAME)client += CSWlibxml2-2
PKGFILES_CSW$(NAME)client += $(sbindir)/cf-agent
PKGFILES_CSW$(NAME)client += $(sbindir)/cf-execd
PKGFILES_CSW$(NAME)client += $(sbindir)/cf-monitord
PKGFILES_CSW$(NAME)client += $(mandir)/.*/cf-agent.*
PKGFILES_CSW$(NAME)client += $(mandir)/.*/cf-execd.*
PKGFILES_CSW$(NAME)client += $(mandir)/.*/cf-monitord.*
PKGFILES_CSW$(NAME)client += $(cfengine_workdir_bin)/cf-agent
PKGFILES_CSW$(NAME)client += $(initddir)/csw$(NAME)-cfexecd
PKGFILES_CSW$(NAME)client += $(initddir)/csw$(NAME)-cfmonitord
PKGFILES_CSW$(NAME)client += $(docdir)/$(NAME)_client/.*\.CSW
CHECKPKG_OVERRIDES_CSW$(NAME)client += catalogname-does-not-match-pkgname|pkgname=CSW$(NAME)client|catalogname=$(NAME)_client|expected-catalogname=$(NAME)client

# CFEngine provides three daemons
#  - cf-execd (client)
#  - cf-monitord (client)
#  - cf-serverd (server)
INITSMF =  $(initddir)/csw$(NAME)-cfexecd
INITSMF += $(initddir)/csw$(NAME)-cfmonitord
INITSMF += $(initddir)/csw$(NAME)-cfserverd

LICENSE = LICENSE

# This file gets installed by CSW$(NAME)util since it is used by
# the server and client component
PRESERVECONF = $(sysconfdir)/$(NAME)rc

BUILD_DEP_PKGS  = CSWlibssl-dev
BUILD_DEP_PKGS += CSWlibpcre-dev
BUILD_DEP_PKGS += CSWlibxml2-dev
BUILD_DEP_PKGS += CSWlibtokyocabinet-dev
BUILD_DEP_PKGS += CSWflex
BUILD_DEP_PKGS += CSWbison

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-silent-rules
CONFIGURE_ARGS += --with-tokyocabinet=$(prefix)
CONFIGURE_ARGS += --with-openssl=$(prefix)
CONFIGURE_ARGS += --with-pcre=$(prefix)
CONFIGURE_ARGS += --with-workdir=$(cfengine_workdir)
CONFIGURE_ARGS += --without-qdbm
CONFIGURE_ARGS += --without-postgresql
CONFIGURE_ARGS += --without-mysql

EXTRA_CPPFLAGS = -xc99=all
# -features=extensions is needed since some void functions return values...
EXTRA_CFLAGS   = -xc99=all -features=extensions

# We use this because libpromises will be moved to this private
# directory (see also move-libpromises:)
EXTRA_LDFLAGS += -R$(libdir)/$(NAME)

# Those libs are used by configure to detect getaddrinfo()
EXTRA_CONFIGURE_ENV = LIBS="-lsocket -lnsl"

include gar/category.mk

post-install-modulated: rename-cfengine-dir make-cfengine-workdir install-cfengine-links install-smf-manifests install-cfengine3rc install-cfengine3-csw-doc fix-paths-in-files move-libpromises move-binaries
	@$(MAKECOOKIE)

rename-cfengine-dir:
	ginstall -d $(DESTDIR)$(docdir)/$(NAME)_utils
	if [ -d $(DESTDIR)$(datadir)/CoreBase ] ; then \
		mv $(DESTDIR)$(datadir)/CoreBase $(DESTDIR)$(docdir)/$(NAME)_utils ; \
	fi
	for f in example_config README ChangeLog examples ; do \
		mv $(DESTDIR)$(docdir)/$$f $(DESTDIR)$(docdir)/$(NAME)_utils/ || echo "Unable to move $$f" ; \
	done

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
	ginstall -m 644 $(WORKDIR)/README.CSW $(DESTDIR)$(docdir)/$(NAME)_utils/

fix-paths-in-files: rename-cfengine-dir
	for d in $(DESTDIR)$(docdir)/$(NAME)_utils/example_config $(DESTDIR)$(docdir)/$(NAME)_utils/examples $(DESTDIR)$(docdir)/$(NAME)_utils/CoreBase; do \
		if test -d $$d ; then \
			for f in $${d}/*.cf ; do \
				sed -e 's|/var/cfengine/|/var/opt/csw/$(NAME)/|g' \
					-e 's|_var_cfengine_|_var_opt_csw_$(NAME)_|g' \
					-e 's|/usr/local/|/opt/csw/|g' \
					-e 's|_usr_local_|_opt_csw_|g' $$f > $${f}.tmp ;\
				mv $${f}.tmp $$f ; \
			done ; \
		fi ; \
	done

# We move libpromises to a prive directory, since there is no publicly
# available API. Please note, the rpath has to be set appropriately
move-libpromises:
	ginstall -d $(DESTDIR)$(libdir)/$(NAME)
	if test -f $(DESTDIR)$(libdir)/libpromises.so.1.0.0 ; then \
		mv $(DESTDIR)$(libdir)/libpromises.* $(DESTDIR)$(libdir)/$(NAME)/ ; \
	fi

# The cfengine guys decided to put binaries into $(prefix)/bin starting
# with 3.3.0. I don't see the point and keep the binaries in $(prefix)/sbin
move-binaries:
	ginstall -d $(DESTDIR)$(prefix)/sbin
	if test -f $(DESTDIR)$(prefix)/bin/cf-agent  ; then \
		mv $(DESTDIR)$(prefix)/bin/* $(DESTDIR)$(prefix)/sbin/ ; \
		rmdir $(DESTDIR)$(prefix)/bin ; \
	fi

post-merge:
# Get rid of the .so files. Since there are no header files provided,
# .so files are pretty much useless
	find $(PKGROOT)$(libdir) -name libpromises.so -exec rm \{\} \;

