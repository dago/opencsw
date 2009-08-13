GARNAME = munin
GARVERSION = 1.3.4
CATEGORIES = apps

SPKG_DESC_CSWmuninmaster = munin master
SPKG_DESC_CSWmuninnode = munin node

#DESCRIPTION = graphical network and system monitoring
define BLURB
  Long description
endef

SF_PROJ = munin
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)_$(GARVERSION).tar.gz
DISTFILES += CSWmuninmaster.prototype CSWmuninmaster.postinstall
DISTFILES += CSWmuninnode.prototype
DISTFILES += cswusergroup
DISTFILES += apache-munin.conf.CSW apache-munin-cgi.conf.CSW
DISTFILES += README.CSW

PATCHFILES += makefile.diff
PATCHFILES += makefile.config.diff 
PATCHFILES += sunos_memory.in.diff
PATCHFILES += munin-node.conf.in.diff
PATCHFILES += munin.conf.in.diff
PATCHFILES += munin-graph.in.diff # use monospace instead of VeraMono.ttf
PATCHFILES += munin-update.in.diff # http://munin.projects.linpro.no/ticket/699
PATCHFILES += munindoc.in.diff # PATH to perl set to /opt/csw/bin/perl
PATCHFILES += perlpath.diff # shebang changed to #!@@PERL@@ -w

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PACKAGES = CSWmuninmaster CSWmuninnode
CATALOGNAME_CSWmuninmaster = munin_master
CATALOGNAME_CSWmuninnode = munin_node

ARCHALL_CSWmuninmaster = 1
ARCHALL_CSWmuninnode = 1

REQUIRED_PKGS_CSWmuninmaster = CSWpmnetserver CSWperl CSWpython CSWpmparserecdescent 
REQUIRED_PKGS_CSWmuninmaster = CSWpmhtmltmpl CSWpmdatemanip CSWpmmd5 CSWrrd CSWapache2
REQUIRED_PKGS_CSWmuninmaster = CSWcswclassutils

REQUIRED_PKGS_CSWmuninnode = CSWpmdbi CSWpmnetsnmp CSWpmnetserver CSWperl CSWtop CSWcswclassutils

SPKG_CLASSES_CSWmuninmaster = none cswusergroup cswpreserveconf ugfiles
SPKG_CLASSES_CSWmuninnode = none cswusergroup ugfiles cswpreserveconf cswinitsmf

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom
SKIPTEST = 1

ENABLE_CHECK = 0

include gar/category.mk

configure-custom:
	@$(MAKECOOKIE)

build-custom:
	@$(MAKECOOKIE)

install-custom:
	cat $(WORKSRC)/Makefile.config | sed -e "s;$$(DESTDIR);$(DESTDIR);g" > $(WORKSRC)/Makefile.config.tmp
	mv $(WORKSRC)/Makefile.config.tmp $(WORKSRC)/Makefile.config
	( cd $(WORKSRC); gmake -f Makefile install)
	#mv $(DESTDIR)/opt/csw/lib/plugins $(DESTDIR)/opt/csw/lib/munin_plugins
	mv $(DESTDIR)/etc/opt/csw/munin/munin-node.conf $(DESTDIR)/etc/opt/csw/munin/munin-node.conf.CSW
	mv $(DESTDIR)/etc/opt/csw/munin/munin.conf $(DESTDIR)/etc/opt/csw/munin/munin.conf.CSW
	@ginstall -d $(DESTDIR)/opt/csw/munin
	@ginstall -d $(DESTDIR)/etc/opt/csw/munin/apache
	@ginstall -m 644 $(FILEDIR)/apache-munin.conf.CSW $(DESTDIR)/etc/opt/csw/munin/apache/apache-munin.conf.CSW
	@ginstall -m 644 $(FILEDIR)/apache-munin-cgi.conf.CSW $(DESTDIR)/etc/opt/csw/munin/apache/apache-munin-cgi.conf.CSW
	@ginstall -d $(DESTDIR)/opt/csw/etc/pkg/CSWmuninmaster
	@ginstall -d $(DESTDIR)/opt/csw/etc/pkg/CSWmuninnode
	@ginstall -d $(DESTDIR)/opt/csw/share/doc
	@ginstall -d $(DESTDIR)/opt/csw/share/doc/munin_master
	@ginstall -m 644 $(FILEDIR)/README.CSW $(DESTDIR)/opt/csw/share/doc/munin_master/README.CSW
	@ginstall -m 644 $(FILEDIR)/cswusergroup $(DESTDIR)/opt/csw/etc/pkg/CSWmuninmaster/cswusergroup
	@ginstall -m 644 $(FILEDIR)/cswusergroup $(DESTDIR)/opt/csw/etc/pkg/CSWmuninnode/cswusergroup
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/cswmuninnode $(DESTDIR)/etc/opt/csw/init.d/cswmuninnode
	@ginstall -d $(DESTDIR)/opt/csw/share/munin/fonts
	@ginstall -m 644 $(DESTDIR)/opt/csw/libexec/munin/VeraMono.ttf $(DESTDIR)/opt/csw/share/munin/fonts/VeraMono.ttf
	@rm $(DESTDIR)/opt/csw/libexec/munin/VeraMono.ttf
	@$(MAKECOOKIE)
