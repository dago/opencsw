NAME = ganglia
VERSION = 3.2.0
CATEGORIES = utils

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

# How should we set this?
# There is a release number in configure.in, maybe use that?
# RELVER =

USER_GMOND = nobody
# nobody shouldn't really be allowed to own any files
# maybe we should add a ganglia user to own the RRD files?
USER_GMETAD = nobody

DESCRIPTION = A scalable distributed monitoring system
define BLURB
  Ganglia is a scalable distributed monitoring system for high-performance computing
  systems such as clusters and Grids. It is based on a hierarchical design targeted
  at federations of clusters.
endef

SF_PROJ = ganglia
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += CSWgangliaweb.postinstall CSWgangliaweb.preremove
DISTFILES += httpd-ganglia.conf cswgmond cswgmetad

PACKAGES = CSWlibganglia0 CSWgangliaagent CSWganglia-dev CSWgangliagmetad CSWgangliaweb CSWgangliamodpython

CATALOGNAME_CSWganglia		= ganglia
CATALOGNAME_CSWlibganglia0	= libganglia0
CATALOGNAME_CSWgangliart	= ganglia_rt_stub
CATALOGNAME_CSWgangliaagent	= gangliaagent
CATALOGNAME_CSWgangliamodpython	= gangliamodpython
CATALOGNAME_CSWganglia-dev	= ganglia_dev
CATALOGNAME_CSWgangliagmetad	= gangliagmetad
CATALOGNAME_CSWgangliaweb	= gangliaweb

OBSOLETED_BY_CSWlibganglia0	+= CSWgangliart

SPKG_DESC_CSWganglia		= Dummy package
SPKG_DESC_CSWlibganglia0		= Ganglia runtime libraries
SPKG_DESC_CSWgangliaagent	= Ganglia performance monitoring agent gmond
SPKG_DESC_CSWgangliamodpython	= Ganglia agent module for Python metrics
SPKG_DESC_CSWganglia-dev	= Ganglia headers for metric module development
SPKG_DESC_CSWgangliagmetad	= Ganglia gmetad
SPKG_DESC_CSWgangliaweb		= Ganglia web

BUILD_DEP_PKGS = CSWexpat CSWlibconfuse-dev CSWapache2rt CSWapache2-dev CSWpcre
BUILD_DEP_PKGS += CSWrrdtool CSWrrdtool-dev

RUNTIME_DEP_PKGS_CSWlibganglia0 = CSWlibexpat1 CSWlibconfuse0 CSWlibapr1-0
RUNTIME_DEP_PKGS_CSWlibganglia0 += CSWlibpcre0
RUNTIME_DEP_PKGS_CSWgangliaagent = CSWlibexpat1 CSWlibconfuse0 CSWlibapr1-0
RUNTIME_DEP_PKGS_CSWgangliaagent += CSWlibganglia0 CSWlibpcre0
RUNTIME_DEP_PKGS_CSWgangliamodpython = CSWgangliaagent
CHECKPKG_OVERRIDES_CSWgangliamodpython += surplus-dependency|CSWgangliaagent
RUNTIME_DEP_PKGS_CSWganglia-dev = CSWlibganglia0
RUNTIME_DEP_PKGS_CSWgangliagmetad = CSWlibexpat1 CSWlibconfuse0 CSWlibapr1-0
RUNTIME_DEP_PKGS_CSWgangliagmetad += CSWlibganglia0 CSWgangliaagent CSWrrdtool
RUNTIME_DEP_PKGS_CSWgangliagmetad += CSWlibrrd4 CSWlibpcre0
CHECKPKG_OVERRIDES_CSWgangliagmetad += surplus-dependency|CSWgangliaagent
CHECKPKG_OVERRIDES_CSWgangliagmetad += surplus-dependency|CSWrrdtool
RUNTIME_DEP_PKGS_CSWgangliaweb = CSWgangliagmetad 
RUNTIME_DEP_PKGS_CSWgangliaweb += CSWapache2 CSWphp5 CSWap2-modphp5 CSWrrdtool
CHECKPKG_OVERRIDES_CSWgangliaweb += surplus-dependency|CSWgangliagmetad
CHECKPKG_OVERRIDES_CSWgangliaweb += surplus-dependency|CSWphp5
CHECKPKG_OVERRIDES_CSWgangliaweb += surplus-dependency|CSWrrdtool

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=43021
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

# This is attachment #45 from Ganglia bug
#   http://bugzilla.ganglia.info/cgi-bin/bugzilla/show_bug.cgi?id=77
#PATCHFILES = $(NAME)-$(VERSION)-solaris-cc.patch

# Uncomment this if we want to build both 32 bit and 64 bit binaries
# By default, only 32 bit binaries are built
#BUILD64 = 1

CONFIGURE_ARGS = $(DIRPATHS)

# For compatibility on Solaris 10
CONFIGURE_ARGS += CFLAGS="-xc99"

# Don't build gmetad (not tested yet on Solaris, more deps required to build)
#CONFIGURE_ARGS += --without-gmetad
CONFIGURE_ARGS += --with-gmetad

# Reduce dependencies, no gettext:
CONFIGURE_ARGS += --disable-nls

# Use apr from CSWapache2rt
CONFIGURE_ARGS += --with-libapr=/opt/csw/apache2/bin/apr-1-config

# Use rrd from CSWlibrrd4
CONFIGURE_ARGS += --with-librrd=/opt/csw

# Use confuse from CSWlibconfuse0
CONFIGURE_ARGS += --with-libconfuse=/opt/csw

# Include the status module
CONFIGURE_ARGS += --with-status

# When we enable this, modpython will have to go in a separate package,
# otherwise CSWgangliaagent will have lots of dependencies
# TODO: define a CSWgangliamodpython package
# Depends: some issues exist getting the Python support working on Solaris,
# Ganglia's configure.in needs to be further enhanced for this to work
CONFIGURE_ARGS += --disable-python
#CONFIGURE_ARGS += --with-python=/opt/csw

# modgstatus - for Ganglia version and internal status metrics
CONFIGURE_ARGS += --enable-status

# For Ganglia 3.1.2, the test suite doesn't compile cleanly on Solaris,
# so we skip it.  This should be re-assessed with each new release
# from upstream.  Proposed fixes for the test suite to be submitted
# upstream.
ifeq ($(VERSION),3.1.3)
TEST_SCRIPTS = 
endif
ifeq ($(VERSION),3.1.4)
TEST_SCRIPTS =
endif
ifeq ($(VERSION),3.1.5)
TEST_SCRIPTS =
endif
ifeq ($(VERSION),3.1.6)
TEST_SCRIPTS =
endif
ifeq ($(VERSION),3.1.7)
TEST_SCRIPTS =
endif
ifeq ($(VERSION),3.2.0)
TEST_SCRIPTS =
endif

#INSTALL_SCRIPTS = $(WORKSRC)/Makefile custom

WWWROOT = /opt/csw/share/www
WWWGANGLIA = $(WWWROOT)/ganglia
sysconfdir = /etc/opt/csw/ganglia
ETCGANGLIA = $(sysconfdir)

PKGFILES_CSWganglia = 
PKGFILES_CSWgangliaagent  = /etc/opt/csw/ganglia/gmond.conf.CSW
PKGFILES_CSWgangliaagent += /etc/opt/csw/ganglia/modgstatus.conf.CSW
PKGFILES_CSWgangliaagent += /opt/csw/sbin/gmond
PKGFILES_CSWgangliaagent += /opt/csw/bin/gmetric
PKGFILES_CSWgangliaagent += /etc/opt/csw/init.d/cswgmond
PKGFILES_CSWgangliaagent += /opt/csw/share/man/man1/gmond.1
PKGFILES_CSWgangliaagent += /opt/csw/share/man/man1/gmetric.1
PKGFILES_CSWgangliaagent += /opt/csw/share/man/man5/gmond.conf.5
PKGFILES_CSWgangliaagent += /opt/csw/lib/ganglia/modsys.so
PKGFILES_CSWgangliaagent += /opt/csw/lib/ganglia/modcpu.so
PKGFILES_CSWgangliaagent += /opt/csw/lib/ganglia/modnet.so
PKGFILES_CSWgangliaagent += /opt/csw/lib/ganglia/modmulticpu.so
PKGFILES_CSWgangliaagent += /opt/csw/lib/ganglia/modmem.so
PKGFILES_CSWgangliaagent += /opt/csw/lib/ganglia/modload.so
PKGFILES_CSWgangliaagent += /opt/csw/lib/ganglia/moddisk.so
PKGFILES_CSWgangliaagent += /opt/csw/lib/ganglia/modproc.so
PKGFILES_CSWgangliaagent += /opt/csw/lib/ganglia/modgstatus.so

PKGFILES_CSWlibganglia0 += $(call pkgfiles_lib,libganglia-3.2.0.so.0)

CHECKPKG_OVERRIDES_CSWlibganglia0 += shared-lib-pkgname-mismatch|file=opt/csw/lib/libganglia-3.2.0.so.0.0.0|soname=libganglia-3.2.0.so.0|pkgname=CSWlibganglia0|expected=CSWlibganglia3-2-0-0

PKGFILES_CSWgangliamodpython = .*python.*
PKGFILES_CSWganglia-dev = .*/include/.*.h .*/bin/ganglia-config $(libdir)/libganglia.so
PKGFILES_CSWgangliagmetad = .*/sbin/gmetad .*/gmetad.conf.CSW /var/opt/csw/ganglia/rrds /etc/opt/csw/init.d/cswgmetad .*/gmetad.1
PKGFILES_CSWgangliaweb = $(WWWGANGLIA)/.* /opt/csw/apache2/etc/extra/httpd-ganglia.conf.CSW

PRESERVECONF = /opt/csw/apache2/etc/extra/httpd-ganglia.conf
PRESERVECONF += /etc/opt/csw/ganglia/gmond.conf
PRESERVECONF += /etc/opt/csw/ganglia/gmetad.conf
PRESERVECONF += /etc/opt/csw/ganglia/conf.d/modgstatus.conf
PRESERVECONF += /etc/opt/csw/ganglia/conf.d/modpython.conf
PRESERVECONF += $(WWWGANGLIA)/conf.php

# For gmond
INITSMF = /etc/opt/csw/init.d/cswgmond
# For gmetad
INITSMF += /etc/opt/csw/init.d/cswgmetad

PROTOTYPE_FILTER_CSWgangliagmetad = awk '\
$$$$3 ~ /\/var\/opt\/csw\/ganglia\/rrds/ { $$$$5 = "nobody"; $$$$6 = "nogroup" } \
{ print }'


#ARCHALL_CSWganglia-dev = 1
ARCHALL_CSWgangliaweb = 1
ARCHALL_CSWgangliamodpython = 1

include gar/category.mk

post-install-modulated:
	-@rm $(DESTDIR)/opt/csw/bin/gstat
	@ginstall -D $(DOWNLOADDIR)/cswgmond \
		$(PKGROOT)/etc/opt/csw/init.d/cswgmond
	@ginstall -D $(DOWNLOADDIR)/cswgmetad \
		$(PKGROOT)/etc/opt/csw/init.d/cswgmetad
	@ginstall -d $(DESTDIR)$(WWWGANGLIA)
	@cd $(WORKSRC)/web; \
		cp -R * $(DESTDIR)$(WWWGANGLIA)
	@rm -rf $(DESTDIR)$(WWWGANGLIA)/conf.php
	@ginstall -D $(FILEDIR)/conf.php \
		$(DESTDIR)$(WWWGANGLIA)/conf.php.CSW
	@rm -rf $(DESTDIR)$(WWWGANGLIA)/*.in
	@ginstall -D $(FILEDIR)/httpd-ganglia.conf \
		$(DESTDIR)/opt/csw/apache2/etc/extra/httpd-ganglia.conf.CSW
	@ginstall -d $(DESTDIR)$(ETCGANGLIA)/conf.d
	@$(WORKSRC)/gmond/gmond -t | grep -v "^include" \
		> $(DESTDIR)$(ETCGANGLIA)/gmond.conf.CSW
	@echo "include ('/etc/opt/csw/ganglia/conf.d/*.conf')" \
		>> $(DESTDIR)$(ETCGANGLIA)/gmond.conf.CSW
	@ginstall -D $(FILEDIR)/gmetad.conf \
		$(DESTDIR)$(ETCGANGLIA)/gmetad.conf
	@cd $(WORKSRC)/gmond/modules/conf.d ; \
		for CONF_FILE in *.conf ; \
		do cp -R "$${CONF_FILE}" $(DESTDIR)$(ETCGANGLIA)/conf.d/"$${CONF_FILE}.CSW" ; done
	@cd $(FILEDIR)/conf.d ; \
		for CONF_FILE in *.conf ; \
		do cp -R "$${CONF_FILE}" $(DESTDIR)$(ETCGANGLIA)/conf.d/"$${CONF_FILE}.CSW" ; done
	@rm -rf $(DESTDIR)$(ETCGANGLIA)/conf.d/example.conf.CSW \
		$(DESTDIR)$(ETCGANGLIA)/conf.d/multicpu.conf.CSW
ifeq ($(VERSION),3.1.2)
	@rm -rf $(DESTDIR)$(ETCGANGLIA)/conf.d/modgstatus.conf.CSW
endif
	@ginstall -d $(DESTDIR)/var/opt/csw/ganglia/rrds
	@ginstall -D $(WORKSRC)/gmond/gmond.conf.5 $(DESTDIR)$(mandir)/man5/gmond.conf.5
	@ginstall -D $(WORKSRC)/mans/gmetad.1 $(DESTDIR)$(mandir)/man1/gmetad.1
	@ginstall -D $(WORKSRC)/mans/gmond.1 $(DESTDIR)$(mandir)/man1/gmond.1
	@ginstall -D $(WORKSRC)/mans/gmetric.1 $(DESTDIR)$(mandir)/man1/gmetric.1
	


