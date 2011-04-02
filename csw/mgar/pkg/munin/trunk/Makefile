NAME = munin
VERSION = 1.4.5
CATEGORIES = apps

SPKG_DESC_CSWmuninmaster = master component of the graphical network and system monitoring munin
SPKG_DESC_CSWmuninnode = node component of the graphical network and system monitoring munin
SPKG_DESC_CSWmunincommon = common files for munin node and master

define BLURB
  Munin the monitoring tool surveys all your computers and remembers what it saw. It presents all the information in graphs through a web interface.
endef

SF_PROJ = munin
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += CSWmuninmaster.postinstall
DISTFILES += CSWmuninmaster.prototype CSWmuninmaster.postinstall
DISTFILES += CSWmuninnode.prototype cswmuninnode
DISTFILES += CSWmunincommon.prototype
DISTFILES += cswusergroup
DISTFILES += apache-munin.conf.CSW apache-munin-cgi.conf.CSW
DISTFILES += README.CSW

PATCHFILES += Makefile.patch
PATCHFILES += Makefile.config.patch
PATCHFILES += sunos_memory.in.patch
PATCHFILES += munin-node.conf.in.patch
PATCHFILES += munin.conf.in.patch
PATCHFILES += munin-htaccess.in.patch
PATCHFILES += munin-graph.in.patch # match some paths to /{etc|var}/opt/csw/munin 
PATCHFILES += perl.patch # shebang correctly set
PATCHFILES += if.in.patch # added support for Solaris 10
PATCHFILES += if_err.in.patch # added support for Solaris 10

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PACKAGES = CSWmuninmaster CSWmuninnode CSWmunincommon
CATALOGNAME_CSWmuninmaster = munin_master
CATALOGNAME_CSWmuninnode = munin_node
CATALOGNAME_CSWmunincommon = munin_common

ARCHALL_CSWmuninmaster = 1
ARCHALL_CSWmuninnode = 1
ARCHALL_CSWmunincommon = 1

RUNTIME_DEP_PKGS_CSWmuninmaster = CSWperl CSWpmhtmltmpl CSWpmprmsvldt CSWpmlog4perl CSWmunincommon
RUNTIME_DEP_PKGS_CSWmuninmaster += CSWpm-rrdtool CSWapache2 
RUNTIME_DEP_PKGS_CSWmuninmaster += CSWcswclassutils

RUNTIME_DEP_PKGS_CSWmuninnode = CSWperl CSWpmnetsnmp CSWpmnetserver CSWmunincommon
RUNTIME_DEP_PKGS_CSWmuninnode += CSWcswclassutils

RUNTIME_DEP_PKGS_CSWmuninnode += CSWperl CSWpmnetssleay

SPKG_CLASSES_CSWmuninmaster = none cswusergroup cswpreserveconf ugfiles
SPKG_CLASSES_CSWmuninnode = none cswusergroup ugfiles cswpreserveconf cswinitsmf
SPKG_CLASSES_CSWmunincommon = none

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
	@cat $(WORKSRC)/Makefile | sed -e "s;DESTDIR =;& $(DESTDIR);g" > $(WORKSRC)/Makefile.tmp
	@( cd $(WORKSRC); gmake -f Makefile ; cp Makefile.tmp Makefile ; gmake -f Makefile install)
	@mv $(DESTDIR)/etc/opt/csw/munin/munin-node.conf $(DESTDIR)/etc/opt/csw/munin/munin-node.conf.CSW
	@mv $(DESTDIR)/etc/opt/csw/munin/munin.conf $(DESTDIR)/etc/opt/csw/munin/munin.conf.CSW
	@mv $(DESTDIR)/var/opt/csw/munin/www/.htaccess $(DESTDIR)/var/opt/csw/munin/www/.htaccess.CSW
	#@ginstall -d $(DESTDIR)/opt/csw/munin
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
	#@ginstall -m 644 $(DESTDIR)/opt/csw/libexec/munin/VeraMono.ttf $(DESTDIR)/opt/csw/share/munin/fonts/VeraMono.ttf
	@ginstall -m 644 $(WORKSRC)/master/VeraMono.ttf $(DESTDIR)/opt/csw/share/munin/fonts/VeraMono.ttf
	#@rm $(DESTDIR)/opt/csw/libexec/munin/VeraMono.ttf
	@$(MAKECOOKIE)
