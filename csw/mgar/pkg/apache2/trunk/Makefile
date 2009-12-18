# $Id$

GARNAME = httpd
GARVERSION = 2.2.14
CATEGORIES = server

DESCRIPTION = A high performance Unix-based HTTP server.
define BLURB
  Apache is the world\'s most popular HTTP server, being quite possibly the
  best around in terms of functionality, efficiency, security and speed.
endef

include files/config.mk

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# <maciej> All the admfiles can go away.  Move the static prototype files
# aside, replace them with PKGFILES_CSWfoo = regexp lines.

# <maciej> The PACKAGES variable tell GAR which packages to build
PACKAGES  = CSWapache2
PACKAGES += CSWapache2c
PACKAGES += CSWapache2rt
PACKAGES += CSWap2prefork
PACKAGES += CSWap2suexec
PACKAGES += CSWapache2-devel
PACKAGES += CSWapache2-manual

# Descriptions for every package
SPKG_DESC_CSWapache2 = Apache 2.2 web server
SPKG_DESC_CSWapache2c = Apache 2.2 web server (core)
SPKG_DESC_CSWapache2rt = Apache 2.2 runtime libraries
SPKG_DESC_CSWap2prefork = Apache 2.2 prefork MPM
SPKG_DESC_CSWap2suexec = Apache 2.2 suEXEC support
SPKG_DESC_CSWapache2-devel = Apache 2.2 development support
SPKG_DESC_CSWapache2-manual = Apache 2.2 manual

# Contents for every package.
# <maciej> The CSWapache2 package is supposed to be an empty meta-package
PKGFILES_CSWapache2 = non-existing
# <maciej> You don't define PKGFILES_CSWapache2c, it's going to be the default,
# catch-all package.
# PKGFILES_CSWapache2c =
# <maciej> The runtime package might use the GAR shortcut for the runtime
# files.
PKGFILES_CSWapache2rt = $(PKGFILES_RT)
PKGFILES_CSWap2prefork = $(sbindir)/httpd.prefork
PKGFILES_CSWap2suexec  = $(libexecdir)/mod_suexec.so
PKGFILES_CSWap2suexec += $(mandir)/man8/suexec.8
PKGFILES_CSWap2suexec += $(sbindir)/suexec

# <maciej> The rest of PKGFILES is for you to do.  You look at the rest of the
# prototype files and construct appropriate regexes for every package.

# <maciej> You don't need the $(call admfiles,...) any more.  But you might
# need the files/*.prototype files to figure out how to populate packages by
# writing regexes.
## # Dummy toplevel package
## DISTFILES += $(call admfiles,CSWapache2,prototype)
## # Runtime
## DISTFILES += $(call admfiles,CSWapache2rt,prototype checkinstall)
## # Server (core)
## CSWapache2c_admfiles = prototype postinstall space
## DISTFILES += $(call admfiles,CSWapache2c,$(CSWapache2c_admfiles))
## # Prefork MPM (default)
## CSWap2prefork_admfiles  = prototype postinstall postremove space
## DISTFILES += $(call admfiles,CSWap2prefork,$(CSWap2prefork_admfiles))
## # mod_suexec
## CSWap2suexec_admfiles = prototype postinstall preremove
## DISTFILES += $(call admfiles,CSWap2suexec,$(CSWap2suexec_admfiles))
## # Manual
## DISTFILES += $(call admfiles,CSWapache2-manual,prototype)
## # Development support
## DISTFILES += $(call admfiles,CSWapache2-devel,prototype)

# Standard package bits
DISTFILES += CSWapache2.killproc cswapache2

# Configuration templates
DISTFILES += httpd.conf.CSW
DISTFILES += httpd-mpm.conf.CSW
DISTFILES += httpd-ssl.conf.CSW
DISTFILES += update20to22

REQUIRED_PKGS_CSWapache2 = CSWapache2c CSWap2prefork
REQUIRED_PKGS_CSWapache2c = CSWapache2rt CSWbdb CSWexpat CSWgdbm CSWiconv
REQUIRED_PKGS_CSWapache2c += CSWlibnet CSWoldaprt CSWosslrt CSWsasl CSWzlib
REQUIRED_PKGS_CSWapache2c += CSWsqlite3 CSWcswclassutils
REQUIRED_PKGS_CSWapache2rt = CSWbdb CSWexpat CSWgdbm CSWggettextrt CSWgsed
REQUIRED_PKGS_CSWapache2rt += CSWiconv CSWoldaprt CSWosslrt CSWperl CSWsasl
REQUIRED_PKGS_CSWapache2rt += CSWzlib CSWsqlite3 CSWlibnet CSWsqlite3rt
REQUIRED_PKGS_CSWap2prefork = CSWapache2c CSWapache2rt CSWbdb CSWexpat CSWgdbm
REQUIRED_PKGS_CSWap2prefork += CSWiconv CSWlibnet CSWoldaprt CSWosslrt CSWsasl
REQUIRED_PKGS_CSWap2prefork += CSWzlib CSWsqlite3
REQUIRED_PKGS_CSWap2suexec = CSWapache2
REQUIRED_PKGS_CSWapache2-devel = CSWapache2rt
REQUIRED_PKGS_CSWapache2-manual = CSWapache2

# The SMF support: you don't need to specify cswinitsmf any more.  You need to
# make sure the the /etc/opt/csw/init.d/cswapache file gets installed during
# the post-install stage, and add "INITSMF = /etc/opt/csw/init.d/cswapache" to
# the Makefile.

# The following line can go:
## SPKG_CLASSES_CSWapache2c = none cswinitsmf

pre-configure-modulated:
	(cd $(WORKDIR)/$(GARNAME)-$(GARVERSION); \
	./buildconf)

# Build Configuration
CONFIGURE_ARGS += --with-mpm=prefork

# Fixup target variables
APACHE_ROOT   = $(DESTDIR)$(prefix)/apache2
LIBTOOL_LADIR = $(APACHE_ROOT)/lib
STRIP_DIRS    = $(APACHE_ROOT)/sbin $(APACHE_ROOT)/libexec

include gar/category.mk
include files/rules.mk

CFLAGS := -DSSL_EXPERIMENTAL -DSSL_ENGINE $(CFLAGS)

FIXCONFIG_DIRS     = $(DESTDIR)
FIXCONFIG_RMPATHS  = $(DESTDIR)
FIXCONFIG_RMPATHS += $(CURDIR)/$(WORKSRC)/$(GARNAME)-$(GARVERSION)/srclib/apr-util
FIXCONFIG_RMPATHS += $(CURDIR)/$(WORKSRC)/$(GARNAME)-$(GARVERSION)/srclib/apr-util/include
FIXCONFIG_RMPATHS += $(CURDIR)/$(WORKSRC)/$(GARNAME)-$(GARVERSION)/srclib/apr
FIXCONFIG_RMPATHS += $(CURDIR)/$(WORKSRC)/$(GARNAME)-$(GARVERSION)/srclib/apr/include

post-install-modulated: rename-httpd copy-local-files create-templates

rename-httpd:
	@if test -f $(APACHE_ROOT)/sbin/httpd ; then \
	    ( cd $(APACHE_ROOT)/sbin ; mv httpd httpd.prefork ) ; \
	fi

# Copy in specialized templates
copy-local-files:
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall $(WORKDIR)/cswapache2 $(DESTDIR)/etc/opt/csw/init.d
	@ginstall $(WORKDIR)/httpd.conf.CSW $(APACHE_ROOT)/etc
	@ginstall $(WORKDIR)/httpd-mpm.conf.CSW $(APACHE_ROOT)/etc/extra
	@ginstall $(WORKDIR)/httpd-ssl.conf.CSW $(APACHE_ROOT)/etc/extra
	@ginstall $(WORKDIR)/update20to22 $(APACHE_ROOT)/sbin

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
template_list += etc/magic
template_list += etc/mime.types

create-templates:
	@echo "  => Creating template files"
	@( cd $(DESTDIR)$(prefix)/apache2 ; \
			for file in $(template_list) ; do \
				gmv -v $$file $$file.CSW ; \
			done )
	@$(MAKECOOKIE)
