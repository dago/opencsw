NAME = munin
VERSION = 1.4.6
CATEGORIES = apps

SPKG_DESC_CSWmunin-master = Master component of the graphical network and system monitoring munin
SPKG_DESC_CSWmunin-node = Node component of the graphical network and system monitoring munin
SPKG_DESC_CSWmunin-common = Common files for munin node and master

define BLURB
  Munin the monitoring tool surveys all your computers and remembers what it saw. It presents all the information in graphs through a web interface.
endef

SF_PROJ = munin
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += cswmuninnode
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

PACKAGES = CSWmunin-master CSWmunin-node CSWmunin-common
CATALOGNAME_CSWmunin-master = munin_master
CATALOGNAME_CSWmunin-node = munin_node
CATALOGNAME_CSWmunin-common = munin_common

ARCHALL_CSWmunin-master = 1
ARCHALL_CSWmunin-node = 1
ARCHALL_CSWmunin-common = 1

RUNTIME_DEP_PKGS_CSWmunin-common = CSWperl

RUNTIME_DEP_PKGS_CSWmunin-master = CSWperl CSWpmhtmltmpl CSWpmprmsvldt CSWpmlog4perl CSWmunin-common
RUNTIME_DEP_PKGS_CSWmunin-master += CSWpm-rrdtool CSWapache2 

RUNTIME_DEP_PKGS_CSWmunin-node = CSWperl CSWpmnetsnmp CSWpmnetserver CSWmunin-common
RUNTIME_DEP_PKGS_CSWmunin-node += CSWpmnetssleay

############### Prototype filters for the different packages ###############

#
# files for CSWmunin-common
#

PKGFILES_CSWmunin-common += .*/Munin::Common.*
PKGFILES_CSWmunin-common += .*/Munin\/Common.*
PKGFILES_CSWmunin-common += .*munin_common.*

#
# files for CSWmunin-node
#

MUNINNODE_UGFILES 	= /var/opt/csw/munin /var/opt/csw/munin/log /var/opt/csw/munin/db /var/opt/csw/munin/run
MUNINNODE_SMF		= /etc/opt/csw/init.d/cswmuninnode
MUNINNODE_USERGROUP	= /opt/csw/etc/pkg/CSWmunin-node/cswusergroup
MUNINNODE_EXECS		= .*munin-node .*munin-node-configure.* .*munindoc.* .*munin-run.*
MUNINNODE_CONF		= .*munin-node.conf .*munin-node.1 /etc/opt/csw/munin/plugin-conf.d

PKGFILES_CSWmunin-node += .*muninnode.* .*CSWmunin-node.*
PKGFILES_CSWmunin-node += .*plugins.*
PKGFILES_CSWmunin-node += .*Munin::Node.* .*Munin\/Plugin.*
PKGFILES_CSWmunin-node += .*Munin\/Node.*
PKGFILES_CSWmunin-node += $(MUNINNODE_UGFILES)
PKGFILES_CSWmunin-node += $(MUNINNODE_SMF)
PKGFILES_CSWmunin-node += $(MUNINNODE_USERGROUP)
PKGFILES_CSWmunin-node += $(MUNINNODE_EXECS)

PROTOTYPE_MODIFIERS  = muninnode_ugfiles
PROTOTYPE_MODIFIERS += muninnode_smf

PROTOTYPE_FILES_muninnode_ugfiles = $(MUNINNODE_UGFILES)
PROTOTYPE_USER_muninnode_ugfiles = munin
PROTOTYPE_GROUP_muninnode_ugfiles = munin
PROTOTYPE_CLASS_muninnode_ugfiles = ugfiles

PROTOTYPE_FILES_muninnode_smf = $(MUNINNODE_SMF)
PROTOTYPE_PERMS_muninnode_smf = 0755

#
# files for CSWmunin-master
#

MUNINMASTER_UGFILES	= /var/opt/csw/munin.* /etc/opt/csw/munin/apache.* /etc/opt/csw/munin/templates.*
MUNINMASTER_USERGROUP	= /opt/csw/etc/pkg/CSWmunin-master/cswusergroup
MUNINMASTER_EXECS	= .*munin-check.* .*munin-cron.* .*munin-graph.* .*munin-html.* .*munin-limits.* .*munin-update.*
MUNINMASTER_FONTS	= .*ttf.*
MUNINMASTER_CRONTABS	= /etc/opt/csw/pkg/CSWmunin-master/crontabs/munin
MUNINMASTER_POSTMSG	= /opt/csw/share/doc/munin_master/README.CSW

PKGFILES_CSWmunin-master += .*muninmaster.*
PKGFILES_CSWmunin-master += .*Munin::Master.*
PKGFILES_CSWmunin-master += .*munin_master.* .*CSWmunin-master.*
PKGFILES_CSWmunin-master += .*Munin\/Master.*
PKGFILES_CSWmunin-master += $(MUNINMASTER_UGFILES) 
PKGFILES_CSWmunin-master += $(MUNINMASTER_USERGROUP) 
PKGFILES_CSWmunin-master += $(MUNINMASTER_EXECS) 
PKGFILES_CSWmunin-master += $(MUNINMASTER_FONTS)

PROTOTYPE_MODIFIERS = muninmaster_ugfiles

PROTOTYPE_FILES_muninmaster_ugfiles = $(MUNINMASTER_UGFILES)
PROTOTYPE_USER_muninmaster_ugfiles = munin
PROTOTYPE_GROUP_muninmaster_ugfiles = munin
PROTOTYPE_CLASS_muninmaster_ugfiles = ugfiles

############### End of prototype filters for the different packages ###############

INITSMF 	+= $(MUNINNODE_SMF)
USERGROUP	+= $(MUNINNODE_USERGROUP)
USERGROUP	+= $(MUNINMASTER_USERGROUP)
POSTMSG		+= $(MUNINMASTER_POSTMSG)
CRONTABS	+= $(MUNINMASTER_CRONTABS)

#SPKG_CLASSES_CSWmunin-master = none cswusergroup ugfiles cswcrontab cswcptemplates cswpostmsg
#SPKG_CLASSES_CSWmunin-node = none cswusergroup ugfiles cswcptemplates cswinitsmf 
#SPKG_CLASSES_CSWmunin-common = none

OBSOLETED_BY_CSWmunin-master = CSWmuninmaster
SPKG_CATALOG_NAME_CSWmuninmaster = munin_master_stub

OBSOLETED_BY_CSWmunin-node = CSWmuninnode
SPKG_CATALOG_NAME_CSWmuninnode = munin_node_stub


#
# checkpkg overrides
#
# the following files contain "/usr/local" and "/usr/share" - these strings appear in perldoc or as fallback path values
# so it's uncritical to leave them unpatched
#

CHECKPKG_OVERRIDES_CSWmunin-node += file-with-bad-content|/usr/local|root/opt/csw/libexec/munin/plugins/hddtemp_smartctl
CHECKPKG_OVERRIDES_CSWmunin-node += file-with-bad-content|/usr/local|root/opt/csw/libexec/munin/plugins/lpstat
CHECKPKG_OVERRIDES_CSWmunin-node += file-with-bad-content|/usr/local|root/opt/csw/libexec/munin/plugins/foldingathome
CHECKPKG_OVERRIDES_CSWmunin-node += file-with-bad-content|/usr/local|root/opt/csw/libexec/munin/plugins/mhttping
CHECKPKG_OVERRIDES_CSWmunin-node += file-with-bad-content|/usr/local|root/opt/csw/libexec/munin/plugins/ejabberd_
CHECKPKG_OVERRIDES_CSWmunin-node += file-with-bad-content|/usr/local|root/opt/csw/libexec/munin/plugins/smart_
CHECKPKG_OVERRIDES_CSWmunin-node += file-with-bad-content|/usr/local|root/opt/csw/libexec/munin/plugins/squeezebox_
CHECKPKG_OVERRIDES_CSWmunin-node += file-with-bad-content|/usr/local|root/opt/csw/libexec/munin/plugins/sybase_space
CHECKPKG_OVERRIDES_CSWmunin-node += file-with-bad-content|/usr/share|root/opt/csw/libexec/munin/plugins/if_err_
CHECKPKG_OVERRIDES_CSWmunin-node += file-with-bad-content|/usr/share|root/opt/csw/share/perl/site_perl/Munin/Plugin.pm
CHECKPKG_OVERRIDES_CSWmunin-node += file-with-bad-content|/usr/share|root/opt/csw/share/man/man3/Munin::Node::Configure::PluginList.3perl
CHECKPKG_OVERRIDES_CSWmunin-node += file-with-bad-content|/usr/share|root/opt/csw/libexec/munin/plugins/if_
CHECKPKG_OVERRIDES_CSWmunin-node += file-with-bad-content|/usr/share|root/opt/csw/libexec/munin/plugins/ps_
CHECKPKG_OVERRIDES_CSWmunin-node += file-with-bad-content|/usr/share|root/opt/csw/libexec/munin/plugins/squeezebox_
CHECKPKG_OVERRIDES_CSWmunin-node += file-with-bad-content|/usr/share|root/opt/csw/libexec/munin/plugins/smart_
CHECKPKG_OVERRIDES_CSWmunin-node += file-with-bad-content|/usr/share|root/opt/csw/libexec/munin/plugins/io_busy_
CHECKPKG_OVERRIDES_CSWmunin-node += file-with-bad-content|/usr/share|root/opt/csw/libexec/munin/plugins/io_bytes_
CHECKPKG_OVERRIDES_CSWmunin-node += file-with-bad-content|/usr/share|root/opt/csw/libexec/munin/plugins/nvidia_
CHECKPKG_OVERRIDES_CSWmunin-node += file-with-bad-content|/usr/share|root/opt/csw/libexec/munin/plugins/io_ops_
CHECKPKG_OVERRIDES_CSWmunin-node += file-with-bad-content|/usr/share|root/opt/csw/share/perl/site_perl/Munin/Node/Configure/PluginList.pm
CHECKPKG_OVERRIDES_CSWmunin-master += file-with-bad-content|/usr/local|root/opt/csw/share/perl/site_perl/Munin/Master/HTMLOld.pm

#
# checkpkg overrides
#
# yes, we need these dependencies
#

CHECKPKG_OVERRIDES_CSWmunin-master += surplus-dependency|CSWmunin-common
CHECKPKG_OVERRIDES_CSWmunin-master += surplus-dependency|CSWapache2
CHECKPKG_OVERRIDES_CSWmunin-master += surplus-dependency|CSWpmhtmltmpl
CHECKPKG_OVERRIDES_CSWmunin-master += surplus-dependency|CSWpmlog4perl
CHECKPKG_OVERRIDES_CSWmunin-master += surplus-dependency|CSWpm-rrdtool
CHECKPKG_OVERRIDES_CSWmunin-master += surplus-dependency|CSWpmprmsvldt

CHECKPKG_OVERRIDES_CSWmunin-node += surplus-dependency|CSWmunin-common
CHECKPKG_OVERRIDES_CSWmunin-node += surplus-dependency|CSWpmnetsnmp
CHECKPKG_OVERRIDES_CSWmunin-node += surplus-dependency|CSWpmnetssleay
CHECKPKG_OVERRIDES_CSWmunin-node += surplus-dependency|CSWpmnetserver


CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
INSTALL_SCRIPTS = custom
SKIPTEST = 1

include gar/category.mk

install-custom:
	@#
	@# because the configure / installation process of munin is somewhat unusual
	@# we have to do it manually
	@#
	@cat $(WORKSRC)/Makefile | sed -e "s;DESTDIR =;& $(DESTDIR);g" > $(WORKSRC)/Makefile.tmp
	@( cd $(WORKSRC); gmake -f Makefile ; cp Makefile.tmp Makefile ; gmake -f Makefile install)
	@#
	@# we are using cswclassutils -> cswcptemplate
	@#
	@ginstall -d $(DESTDIR)/opt/csw/etc/templates/CSWmunin-node/etc/opt/csw/munin
	@ginstall -d $(DESTDIR)/opt/csw/etc/templates/CSWmunin-master/etc/opt/csw/munin
	@ginstall -d $(DESTDIR)/opt/csw/etc/templates/CSWmunin-master/etc/opt/csw/munin/apache
	@ginstall -d $(DESTDIR)/opt/csw/etc/templates/CSWmunin-master/var/opt/csw/munin/www
	@mv $(DESTDIR)/etc/opt/csw/munin/munin-node.conf $(DESTDIR)/opt/csw/etc/templates/CSWmunin-node/etc/opt/csw/munin/
	@mv $(DESTDIR)/etc/opt/csw/munin/munin.conf $(DESTDIR)/opt/csw/etc/templates/CSWmunin-master/etc/opt/csw/munin/
	@ginstall -m 644 $(FILEDIR)/apache-munin.conf.CSW \
		$(DESTDIR)/opt/csw/etc/templates/CSWmunin-master/etc/opt/csw/munin/apache/apache-munin.conf
	@ginstall -m 644 $(FILEDIR)/apache-munin-cgi.conf.CSW \
		$(DESTDIR)/opt/csw/etc/templates/CSWmunin-master/etc/opt/csw/munin/apache/apache-munin-cgi.conf
	@mv $(DESTDIR)/var/opt/csw/munin/www/.htaccess $(DESTDIR)/opt/csw/etc/templates/CSWmunin-master/var/opt/csw/munin/www/
	@#
	@mv $(DESTDIR)/etc/opt/csw/munin/templates $(DESTDIR)/opt/csw/etc/templates/CSWmunin-master/etc/opt/csw/munin
	@ginstall -d $(DESTDIR)/etc/opt/csw/munin/apache
	@ginstall -d $(DESTDIR)/etc/opt/csw/munin/templates
	@ginstall -d $(DESTDIR)/etc/opt/csw/munin/templates/partial
	@#
	@# create user munin during package deployment -> cswusergroup
	@#
	@ginstall -d $(DESTDIR)/opt/csw/etc/pkg/CSWmunin-master
	@ginstall -d $(DESTDIR)/opt/csw/etc/pkg/CSWmunin-node
	@ginstall -m 644 $(FILEDIR)/cswusergroup $(DESTDIR)/opt/csw/etc/pkg/CSWmunin-master/cswusergroup
	@ginstall -m 644 $(FILEDIR)/cswusergroup $(DESTDIR)/opt/csw/etc/pkg/CSWmunin-node/cswusergroup
	@#
	@# create init script / smf -> cswinitsmf
	@#
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 644 $(FILEDIR)/cswmuninnode $(DESTDIR)/etc/opt/csw/init.d/cswmuninnode
	@#
	@# create crontab for user munin -> cswcrontab
	@#
	@ginstall -d $(DESTDIR)/etc/opt/csw/pkg/CSWmunin-master/crontabs
	@ginstall -m 644 $(FILEDIR)/crontab.munin $(DESTDIR)/etc/opt/csw/pkg/CSWmunin-master/crontabs/munin
	@#
	@# print a postmessage -> cswpostmessage
	@#
	@ginstall -d $(DESTDIR)/opt/csw/share/doc
	@ginstall -d $(DESTDIR)/opt/csw/share/doc/munin_master
	@ginstall -m 644 $(FILEDIR)/README.CSW $(DESTDIR)/opt/csw/share/doc/munin_master/README.CSW
	@#
	@# handle some other files
	@#
	@ginstall -d $(DESTDIR)/opt/csw/share/munin/fonts
	@ginstall -m 644 $(WORKSRC)/master/VeraMono.ttf $(DESTDIR)/opt/csw/share/munin/fonts/VeraMono.ttf
	@$(MAKECOOKIE)
	@#
	@# make some links for munin node
	@#
	@ln -s /opt/csw/libexec/munin/plugins/load $(DESTDIR)/etc/opt/csw/munin/plugins/load
	@ln -s /opt/csw/libexec/munin/plugins/uptime $(DESTDIR)/etc/opt/csw/munin/plugins/uptime
	@ln -s /opt/csw/libexec/munin/plugins/cpu $(DESTDIR)/etc/opt/csw/munin/plugins/cpu
	@ln -s /opt/csw/libexec/munin/plugins/df $(DESTDIR)/etc/opt/csw/munin/plugins/df
