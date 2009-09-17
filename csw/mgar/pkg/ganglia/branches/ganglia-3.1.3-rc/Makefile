GARNAME = ganglia
GARVERSION = 3.1.3
CATEGORIES = utils

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
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWgangliaweb.postinstall CSWgangliaweb.preremove
DISTFILES += httpd-ganglia.conf.CSW cswgmond cswgmetad

PACKAGES = CSWgangliart CSWgangliaagent CSWgangliadevel CSWgangliagmetad CSWgangliaweb CSWgangliamodpython

CATALOGNAME_CSWganglia		= ganglia
CATALOGNAME_CSWgangliart	= ganglia_rt
CATALOGNAME_CSWgangliaagent	= ganglia_agent
CATALOGNAME_CSWgangliamodpython	= ganglia_modpython
CATALOGNAME_CSWgangliadevel	= ganglia_devel
CATALOGNAME_CSWgangliagmetad	= ganglia_gmetad
CATALOGNAME_CSWgangliaweb	= ganglia_web

SPKG_DESC_CSWganglia		= Dummy package
SPKG_DESC_CSWgangliart		= Ganglia runtime libraries
SPKG_DESC_CSWgangliaagent	= Ganglia performance monitoring agent gmond
SPKG_DESC_CSWgangliamodpython	= Ganglia agent module for Python metrics
SPKG_DESC_CSWgangliadevel	= Ganglia headers for metric module development
SPKG_DESC_CSWgangliagmetad	= Ganglia gmetad
SPKG_DESC_CSWgangliaweb		= Ganglia web

PREREQUISITE_PKGS = CSWexpat CSWlibconfuse CSWapache2rt CSWapache2-devel CSWrrd

REQUIRED_PKGS_CSWgangliart = CSWexpat CSWlibconfuse CSWapache2rt
REQUIRED_PKGS_CSWgangliaagent = CSWexpat CSWlibconfuse CSWapache2rt
REQUIRED_PKGS_CSWgangliaagent += CSWgangliart
REQUIRED_PKGS_CSWgangliamodpython = CSWlibconfuse CSWapache2rt CSWgangliart
REQUIRED_PKGS_CSWgangliamodpython += CSWgangliaagent
REQUIRED_PKGS_CSWgangliadevel = CSWexpat CSWlibconfuse CSWapache2rt
REQUIRED_PKGS_CSWgangliagmetad = CSWexpat CSWlibconfuse CSWapache2rt
REQUIRED_PKGS_CSWgangliagmetad += CSWgangliart CSWgangliaagent CSWrrd
REQUIRED_PKGS_CSWgangliaweb = CSWgangliagmetad 
REQUIRED_PKGS_CSWgangliaweb += CSWapache2 CSWphp5 CSWap2modphp5 CSWrrd

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=43021
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

# This is attachment #45 from Ganglia bug
#   http://bugzilla.ganglia.info/cgi-bin/bugzilla/show_bug.cgi?id=77
#PATCHFILES = $(GARNAME)-$(GARVERSION)-solaris-cc.patch

CONFIGURE_ARGS = $(DIRPATHS)

# Don't build gmetad (not tested yet on Solaris, more deps required to build)
#CONFIGURE_ARGS += --without-gmetad
CONFIGURE_ARGS += --with-gmetad

# Reduce dependencies, no gettext:
CONFIGURE_ARGS += --disable-nls

# Use apr from CSWapache2rt
CONFIGURE_ARGS += --with-libapr=/opt/csw/apache2/bin/apr-1-config

# Include the status module
CONFIGURE_ARGS += --with-status

# When we enable this, modpython will have to go in a separate package,
# otherwise CSWgangliaagent will have lots of dependencies
# TODO: define a CSWgangliamodpython package
# Depends: some issues exist getting the Python support working on Solaris,
# Ganglia's configure.in needs to be further enhanced for this to work
CONFIGURE_ARGS += --disable-python
#CONFIGURE_ARGS += --with-python=/opt/csw

# For Ganglia 3.1.2, the test suite doesn't compile cleanly on Solaris,
# so we skip it.  This should be re-assessed with each new release
# from upstream.  Proposed fixes for the test suite to be submitted
# upstream.
ifeq ($(GARVERSION),3.1.3)
TEST_SCRIPTS = 
endif

INSTALL_SCRIPTS = $(WORKSRC)/Makefile custom

WWWROOT = /opt/csw/share/www
WWWGANGLIA = $(WWWROOT)/ganglia
ETCGANGLIA = /etc/opt/csw/ganglia

PKGFILES_CSWganglia = 
PKGFILES_CSWgangliart = $(libdir)/libganglia.*
PKGFILES_CSWgangliamodpython = .*python.*
PKGFILES_CSWgangliadevel = .*/include/.*.h .*/bin/ganglia-config
PKGFILES_CSWgangliagmetad = .*/gmetad.* /opt/csw/var/ganglia/rrds /etc/opt/csw/init.d/cswgmetad
PKGFILES_CSWgangliaweb = $(WWWGANGLIA)/.* /opt/csw/apache2/etc/extra/.*

PRESERVECONF = /opt/csw/apache2/etc/extra/httpd-ganglia.conf.CSW

# For gmond
INITSMF = /etc/opt/csw/init.d/cswgmond
# For gmetad
INITSMF += /etc/opt/csw/init.d/cswgmetad

PROTOTYPE_FILTER_CSWgangliagmetad = awk '\
$$$$3 ~ /\/opt\/csw\/var\/ganglia\/rrds/ { $$$$5 = "nobody"; $$$$6 = "nogroup" } \
{ print }'


#ARCHALL_CSWgangliadevel = 1
#ARCHALL_CSWgangliaweb = 1

include gar/category.mk

install-custom:
	@ginstall -D $(DOWNLOADDIR)/cswgmond \
		$(PKGROOT)/etc/opt/csw/init.d/cswgmond
	@ginstall -D $(DOWNLOADDIR)/cswgmetad \
		$(PKGROOT)/etc/opt/csw/init.d/cswgmetad
	@ginstall -d $(DESTDIR)$(WWWGANGLIA)
	@cd $(WORKSRC)/web; \
		cp -R * $(DESTDIR)$(WWWGANGLIA)
	@ginstall -D $(FILEDIR)/conf.php \
		$(DESTDIR)$(WWWGANGLIA)/conf.php
	@rm -rf $(DESTDIR)$(WWWGANGLIA)/*.in
	@ginstall -D $(FILEDIR)/httpd-ganglia.conf.CSW \
		$(DESTDIR)/opt/csw/apache2/etc/extra/httpd-ganglia.conf.CSW
	@ginstall -d $(DESTDIR)$(ETCGANGLIA)/conf.d
	@$(WORKSRC)/gmond/gmond -t | grep -v "^include" \
		> $(DESTDIR)$(ETCGANGLIA)/gmond.conf
	@echo "include ('/etc/opt/csw/ganglia/conf.d/*.conf')" \
		>> $(DESTDIR)$(ETCGANGLIA)/gmond.conf
#	@ginstall -D $(FILEDIR)/gmond.conf \
#		$(DESTDIR)$(ETCGANGLIA)/gmond.conf
	@ginstall -D $(FILEDIR)/gmetad.conf \
		$(DESTDIR)$(ETCGANGLIA)/gmetad.conf
	@cd $(WORKSRC)/gmond/modules/conf.d; \
		cp -R *.conf $(DESTDIR)$(ETCGANGLIA)/conf.d
	@rm -rf $(DESTDIR)$(ETCGANGLIA)/conf.d/example.conf \
		$(DESTDIR)$(ETCGANGLIA)/conf.d/multicpu.conf
ifeq ($(GARVERSION),3.1.2)
	@rm -rf $(DESTDIR)$(ETCGANGLIA)/conf.d/modgstatus.conf
endif
	@ginstall -d $(DESTDIR)/opt/csw/var/ganglia/rrds
	


