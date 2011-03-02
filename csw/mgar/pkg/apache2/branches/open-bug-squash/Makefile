# $Id$

NAME = httpd
VERSION = 2.2.17
CATEGORIES = server

DESCRIPTION = A high performance HTTP server.
define BLURB
  Apache is the world\'s most popular HTTP server, being quite possibly the
  best around in terms of functionality, efficiency, security and speed.
endef

# Source location
MASTER_SITES  = http://www.ibiblio.com/pub/mirrors/apache/httpd/

# work around dumb checkpkg not recognizing the license file ...
LICENSE = LICENSE

# Build multiple mpm's and merge them all into one install
EXTRA_MODULATORS = MPM
# !!!NOTE, NOTE, NOTE!!! prefork must be last as it's the one where
# all modules are built.  This affects the default httpd.conf that
# gets generated.  The other modulations will generate httpd.conf
# files that lack the important LoadModule lines.  This is primarily
# useful at version bump time when files/httpd.conf.CSW may need an
# update to reflect new modules, etc.
MODULATIONS_MPM = worker prefork

MERGE_SCRIPTS_isa-default-mpm-prefork = copy-all
MERGE_SCRIPTS_isa-default-mpm-worker = copy-all

# Visitor information
SPKG_SOURCEURL = http://httpd.apache.org/

DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += config.layout
# Standard package bits
DISTFILES += CSWapache2.killproc cswapache2

DISTFILES += CSWapache2.preinstall CSWapache2.postinstall
DISTFILES += CSWap2worker.postinstall CSWap2worker.postremove
DISTFILES += CSWap2worker.preinstall

DISTFILES += CSWapache2-devel.cswreleasenotes

# Configuration templates
DISTFILES += update20to22
DISTFILES += README.CSW.apache2 README.CSW.ap2_prefork
DISTFILES += README.CSW.apache2rt

PATCHFILES += 0001-Apply-a-large-hammer-to-buildconf-to-fix-libtool-set.patch
PATCHFILES += 0002-Adjust-a-few-usr-local-paths-in-the-man-pages.patch
PATCHFILES += 0003-Switch-usr-local-for-opt-csw-in-default-cgi-path.patch

UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# The PACKAGES variable tell GAR which packages to build
PACKAGES  = CSWapache2 CSWapache2-devel CSWapache2-manual CSWap2suexec
PACKAGES += CSWap2worker
# These packages are dummy versions to make dependencies nicer
# as various things depend on CSWap2prefork currently
PACKAGES += CSWap2prefork CSWapache2rt

ARCHALL_CSWapache2-manual = 1
ARCHALL_CSWap2prefork = 1
ARCHALL_CSWapache2rt = 1

OBSOLETES_CSWapache2 = CSWapache2c

CATALOGNAME_CSWapache2 = apache2
CATALOGNAME_CSWapache2-devel = apache2_devel
CATALOGNAME_CSWapache2-manual = apache2_manual
CATALOGNAME_CSWap2suexec = ap2_suexec
CATALOGNAME_CSWap2prefork = ap2_prefork
CATALOGNAME_CSWap2worker = ap2_worker
CATALOGNAME_CSWapache2rt = apache2rt

SPKG_DESC_CSWapache2 = A high performance Unix-based HTTP server.
SPKG_DESC_CSWapache2-devel = The development files for Apache2.
SPKG_DESC_CSWapache2-manual = The Apache2 manual files.
SPKG_DESC_CSWap2suexec = The standard suEXEC binary for Apache2.
SPKG_DESC_CSWap2worker = The apache worker mpm.
SPKG_DESC_CSWap2prefork = A stub for the old prefork mpm package.
SPKG_DESC_CSWapache2rt = A stub for the old apache2rt package.

RUNTIME_DEP_PKGS_CSWapache2       += CSWexpat CSWiconv CSWosslutils
RUNTIME_DEP_PKGS_CSWapache2       += CSWoldaprt CSWosslrt CSWzlib
RUNTIME_DEP_PKGS_CSWapache2       += CSWapr CSWapr-util CSWbdb48
RUNTIME_DEP_PKGS_CSWapache2-manual = CSWapache2
RUNTIME_DEP_PKGS_CSWapache2-devel  = CSWapache2
RUNTIME_DEP_PKGS_CSWap2suexec	   = CSWapache2
RUNTIME_DEP_PKGS_CSWap2prefork     = CSWapache2
RUNTIME_DEP_PKGS_CSWap2worker      = CSWapache2 CSWapr CSWexpat CSWap2prefork
RUNTIME_DEP_PKGS_CSWap2worker 	  += CSWbdb48 CSWapr-util CSWiconv
RUNTIME_DEP_PKGS_CSWapache2rt	   = CSWapache2

CHECKPKG_OVERRIDES_CSWapache2 += surplus-dependency|CSWalternatives
CHECKPKG_OVERRIDES_CSWapache2 += surplus-dependency|CSWosslutils
CHECKPKG_OVERRIDES_CSWap2prefork += surplus-dependency|CSWapache2
CHECKPKG_OVERRIDES_CSWap2worker += surplus-dependency|CSWalternatives
CHECKPKG_OVERRIDES_CSWap2worker += surplus-dependency|CSWap2prefork
CHECKPKG_OVERRIDES_CSWapache2rt += surplus-dependency|CSWapache2

CHECKPKG_OVERRIDES_CSWapache2-devel += file-with-bad-content|/usr/local|root/opt/csw/apache2/include/httpd.h

# We need this to get bdb48/lib into the runpath
EXTRA_LIB = $(prefix)/bdb48/lib

# The SMF support: you don't need to specify cswinitsmf any more.  You need to
# make sure the the /etc/opt/csw/init.d/cswapache file gets installed during
# the post-install stage, and add "INITSMF = /etc/opt/csw/init.d/cswapache" to
# the Makefile.
INITSMF = /etc/opt/csw/init.d/cswapache2

POSTMSG = /opt/csw/share/doc/apache2/README.CSW

AP2_MODS = 1
AP2_MODFILES = *suexec*\.so

ALTERNATIVES_CSWapache2 = prefork
ALTERNATIVES_CSWap2worker = worker
ALTERNATIVE_prefork = /opt/csw/apache2/sbin/httpd httpd /opt/csw/apache2/sbin/httpd.prefork 50
ALTERNATIVE_worker = /opt/csw/apache2/sbin/httpd httpd /opt/csw/apache2/sbin/httpd.worker 100

# Build Configuration
CONFIGURE_ARGS += --with-apr=$(prefix)/bin/apr-1-config
CONFIGURE_ARGS += --with-apr-util=$(prefix)/bin/apu-1-config
CONFIGURE_ARGS += --with-mpm=$(MPM)
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --enable-layout=csw
CONFIGURE_ARGS += --enable-rule=SSL_EXPERIMENTAL
CONFIGURE_ARGS += --enable-ssl
CONFIGURE_ARGS += --with-z=$(prefix)
CONFIGURE_ARGS += --with-ssl=$(prefix)

ifneq ($(MPM),prefork)
CONFIGURE_ARGS += --enable-modules=none
CONFIGURE_ARGS += --disable-actions
CONFIGURE_ARGS += --disable-alias
CONFIGURE_ARGS += --disable-authn-file
CONFIGURE_ARGS += --disable-authn-default
CONFIGURE_ARGS += --disable-authz-host
CONFIGURE_ARGS += --disable-authz-user
CONFIGURE_ARGS += --disable-authz-groupfile 
CONFIGURE_ARGS += --disable-authz-default
CONFIGURE_ARGS += --disable-auth-basic
CONFIGURE_ARGS += --disable-asis
CONFIGURE_ARGS += --disable-auth
CONFIGURE_ARGS += --disable-autoindex
CONFIGURE_ARGS += --disable-cgi
CONFIGURE_ARGS += --disable-cgid
CONFIGURE_ARGS += --disable-charset-lite
CONFIGURE_ARGS += --disable-dir
CONFIGURE_ARGS += --disable-env
CONFIGURE_ARGS += --disable-filter
CONFIGURE_ARGS += --disable-imap
CONFIGURE_ARGS += --disable-include
CONFIGURE_ARGS += --disable-log-config
CONFIGURE_ARGS += --disable-mime
CONFIGURE_ARGS += --disable-negotiation
CONFIGURE_ARGS += --disable-setenvif
CONFIGURE_ARGS += --disable-ssl
CONFIGURE_ARGS += --disable-status
CONFIGURE_ARGS += --disable-userdir
CONFIGURE_ARGS += --disable-version
else
CONFIGURE_ARGS += --enable-suexec
CONFIGURE_ARGS += --with-suexec-caller=nobody
CONFIGURE_ARGS += --with-suexec-docroot=$(prefix)/apache2/share/htdocs
CONFIGURE_ARGS += --with-suexec-userdir=public_html
CONFIGURE_ARGS += --with-suexec-uidmin=100
CONFIGURE_ARGS += --with-suexec-gidmin=100
CONFIGURE_ARGS += --with-suexec-logfile=$(prefix)/apache2/var/log/suexec_log
CONFIGURE_ARGS += --with-suexec-bin=$(prefix)/apache2/sbin/suexec
CONFIGURE_ARGS += --with-suexec-safepath=/opt/csw/bin:/usr/bin:/bin
CONFIGURE_ARGS += --enable-authn-alias
CONFIGURE_ARGS += --enable-authnz-ldap
CONFIGURE_ARGS += --enable-file-cache
CONFIGURE_ARGS += --enable-cache
CONFIGURE_ARGS += --enable-disk-cache
CONFIGURE_ARGS += --enable-mem-cache
CONFIGURE_ARGS += --enable-bucketeer
CONFIGURE_ARGS += --enable-charset-lite
CONFIGURE_ARGS += --enable-ldap
CONFIGURE_ARGS += --enable-log-forensic
CONFIGURE_ARGS += --enable-usertrack
CONFIGURE_ARGS += --enable-unique-id
CONFIGURE_ARGS += --enable-version
CONFIGURE_ARGS += --enable-proxy
CONFIGURE_ARGS += --enable-proxy-connect
CONFIGURE_ARGS += --enable-proxy-ftp
CONFIGURE_ARGS += --enable-proxy-http
CONFIGURE_ARGS += --enable-proxy-ajp
CONFIGURE_ARGS += --enable-proxy-balancer
CONFIGURE_ARGS += --enable-cgid
CONFIGURE_ARGS += --enable-dav-lock
CONFIGURE_ARGS += --enable-mods-shared=all
endif

# Fixup target variables
APACHE_ROOT   = $(DESTDIR)$(prefix)/apache2
LIBTOOL_LADIR = $(APACHE_ROOT)/lib
STRIP_DIRS    = $(APACHE_ROOT)/sbin $(APACHE_ROOT)/libexec

PKGFILES_CSWap2suexec = .*sbin/suexec .*libexec/.*suexec.* .*/man/.*suexec.*
PKGFILES_CSWap2suexec += .*ap2mod/suexec
PKGFILES_CSWapache2-devel = .*include/.* .*\.(a|la)
PKGFILES_CSWapache2-manual = .*share/.*manual.* .*etc/extra/httpd-manual.conf
PKGFILES_CSWap2prefork = .*share/doc/ap2_prefork.*
PKGFILES_CSWap2worker = .*share/doc/ap2_worker.* .*sbin/httpd.worker
PKGFILES_CSWapache2rt = .*share/doc/apache2rt.*

#PROTOTYPE_FILTER  = awk '$$$$3 == "/opt/csw/apache2/sbin/suexec" { $$$$4 = "4755" }; $$$$3 ~ /cswap2mod/ { $$$$4 = "0555" }; { print }'

#include checkpkg.mak

include gar/category.mk

CFLAGS := -DSSL_EXPERIMENTAL -DSSL_ENGINE $(CFLAGS)

FIXCONFIG_DIRS     = $(DESTDIR)
FIXCONFIG_RMPATHS  = $(DESTDIR)

pre-configure-modulated:
	(cd $(WORKDIR)/$(NAME)-$(VERSION); ./buildconf)
	@gsed -e s,INSTALL_PREFIX,$(prefix)/apache2,g \
		$(WORKDIR)/config.layout > $(WORKDIR)/$(NAME)-$(VERSION)/config.layout
	@$(MAKECOOKIE)


post-install-modulated: rename-httpd copy-local-files create-templates copy-readmes

copy-readmes:
	@(cd $(WORKDIR); for f in README.CSW*; do \
		p=`echo $$f | sed 's/README.CSW.//'`; \
		ginstall -d -m0755 $(DESTDIR)/$(prefix)/share/doc/$$p; \
		ginstall -m 0644 $$f $(DESTDIR)/$(prefix)/share/doc/$$p/README.CSW; \
	done)
	@$(MAKECOOKIE)

rename-httpd:
	@if test -f $(APACHE_ROOT)/sbin/httpd ; then \
	    ( cd $(APACHE_ROOT)/sbin ; mv httpd httpd.$(MPM) ) ; \
	fi


# Copy in specialized templates
copy-local-files:
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall $(WORKDIR)/cswapache2 $(DESTDIR)/etc/opt/csw/init.d
	@ginstall $(WORKDIR)/update20to22 $(APACHE_ROOT)/sbin
	@$(MAKECOOKIE)

# Create stock templates
template_list  = share/htdocs/index.html
template_list += etc/extra/httpd-autoindex.conf
template_list += etc/extra/httpd-dav.conf
template_list += etc/extra/httpd-default.conf
template_list += etc/extra/httpd-info.conf
template_list += etc/extra/httpd-languages.conf
template_list += etc/extra/httpd-multilang-errordoc.conf
template_list += etc/extra/httpd-userdir.conf
template_list += etc/extra/httpd-vhosts.conf
template_list += etc/extra/httpd-mpm.conf
template_list += etc/magic
template_list += etc/mime.types

create-templates:
	@echo "  => Creating template files"
	@( cd $(DESTDIR)$(prefix)/apache2 ; \
			for file in $(template_list) ; do \
				gmv -v $$file $$file.CSW ; \
			done )
	@$(MAKECOOKIE)


post-merge:
	@(cd $(PKGROOT)/$(prefix)/apache2/etc/; \
		for f in httpd.conf extra/httpd-ssl.conf; do \
		perl -pi -e 's/User.*daemon.*/User \@USER\@/; \
		s/Group.*daemon.*/Group \@GROUP\@/; \
		s/#*ServerName www.example.com/ServerName \@HOSTNAME\@/; \
		s/ServerAdmin you\@example.com/ServerAdmin \@ADMIN\@/; \
		s/^(LoadModule.*suexec.*)/#$$1/; \
		s/^#(Include.*httpd-mpm.conf)/$$1/; \
		s/^#(Include.*httpd-ssl.conf)/$$1/' $$f; \
		mv $$f $$f.CSW; \
		done )
	@echo Fixing usr/local references in the online manaual...
	@(cd $(PKGROOT)/$(prefix)/apache2/share/manual; \
		/opt/csw/bin/gfind . -type f -print0 | \
		/opt/csw/bin/gxargs -0 \
			 perl -pi \
			  -e 's@/usr/local/apache2*@/opt/csw/apache2@g;' \
			  -e 's@/usr/local@/opt/csw/apache2@g')
	@echo Fixing export/home references in the online manaual...
	@(cd $(PKGROOT)/$(prefix)/apache2/share/manual; \
		/opt/csw/bin/gfind . -type f -print0 | \
		/opt/csw/bin/gxargs -0 \
			 perl -pi \
			  -e 's@/export/home@/home@g;')
	@echo Fixing usr/local reference in the cgi-bin scripts
	@(cd $(PKGROOT)/$(prefix)/apache2/share/cgi-bin; \
		perl -pi -e 's@/usr/local/bin@/opt/csw/bin@g' *)
	@$(MAKECOOKIE)

