NAME 		= munin
VERSION 	= 2.0.6
CATEGORIES 	= apps
GARTYPE 	= v2

define BLURB
  Munin the monitoring tool surveys all your computers and remembers what it saw. It presents all the information in graphs through a web interface.
endef

SF_PROJ = munin
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += cswmuninnode
DISTFILES += cswusergroup
DISTFILES += apache-munin-cgi.conf
DISTFILES += CSWmunin-master.preinstall
DISTFILES += CSWmunin-master.README.CSW
DISTFILES += CSWmunin-node.README.CSW

PATCHFILES	+= 0001-paths-and-hostname-in-munin-node.conf.in.patch
PATCHFILES	+= 0001-replace-yourhostname-with-hostname-in-postinstall.patch
PATCHFILES	+= 0006-Expand-paths-with-DESTDIR.patch 
PATCHFILES	+= 0008-paths-in-Makefile.config.patch

#
# Reinplacements
#

# bad file content ...

REINPLACE_USRLOCAL	+= plugins/node.d*/*
REINPLACE_USRLOCAL	+= plugins/node.d.sunos/*
REINPLACE_USRLOCAL	+= master/*lib/lib/Munin/Master/*
REINPLACE_USRLOCAL	+= master/lib/Munin/Master/*

REINPLACE_USRSHARE	+= plugins/node.d*/*
REINPLACE_USRSHARE	+= node/*lib/*
REINPLACE_USRSHARE	+= master/*lib/*
REINPLACE_USRSHARE	+= master/*lib/lib/Munin/Master/*
REINPLACE_USRSHARE	+= master/lib/Munin/Master/*
REINPLACE_USRSHARE	+= plugins/blib/lib/Munin/*
REINPLACE_USRSHARE	+= plugins/lib/Munin/*
REINPLACE_USRSHARE	+= node/lib/Munin/Node/Configure/*
REINPLACE_USRSHARE	+= node/blib/lib/Munin/Node/Configure/*


# put the right shebang into perl files

REINPLACEMENTS 		+= perl
REINPLACE_MATCH_perl 	 = \#!/usr/bin/perl
REINPLACE_WITH_perl 	 = \#!/opt/csw/bin/perl
REINPLACE_FILES_perl 	+= node/bin/*
REINPLACE_FILES_perl 	+= node/sbin/*

#
# Package definitions
#

PACKAGES = CSWmunin-master CSWmunin-node CSWmunin-common

CATALOGNAME_CSWmunin-master	= munin_master
CATALOGNAME_CSWmunin-node	= munin_node
CATALOGNAME_CSWmunin-common	= munin_common

SPKG_DESC_CSWmunin-master	= Master component of the graphical network and system monitoring Munin
SPKG_DESC_CSWmunin-node		= Node component of the graphical network and system monitoring Munin
SPKG_DESC_CSWmunin-common	= Common files for Munin node and master

ARCHALL_CSWmunin-master		= 1
ARCHALL_CSWmunin-node		= 1
ARCHALL_CSWmunin-common		= 1

OBSOLETED_BY_CSWmunin-master		= CSWmuninmaster
SPKG_CATALOG_NAME_CSWmuninmaster	= munin_master_stub

OBSOLETED_BY_CSWmunin-node		= CSWmuninnode
SPKG_CATALOG_NAME_CSWmuninnode		= munin_node_stub

#
# Dependencies
#

RUNTIME_DEP_PKGS_CSWmunin-common = CSWperl

RUNTIME_DEP_PKGS_CSWmunin-master  = CSWperl CSWpmhtmltmpl CSWpmprmsvldt CSWpm-log-log4perl CSWmunin-common
RUNTIME_DEP_PKGS_CSWmunin-master += CSWpm-rrdtool CSWapache2 CSWpmfcgi 	CSWpmfilecpyrecurs
RUNTIME_DEP_PKGS_CSWmunin-master += CSWpmdatemanip
RUNTIME_DEP_PKGS_CSWmunin-master += CSWpm-io-socket-inet6
RUNTIME_DEP_PKGS_CSWmunin-master += CSWpmsocket6
RUNTIME_DEP_PKGS_CSWmunin-master += CSWpm-uri

RUNTIME_DEP_PKGS_CSWmunin-node  = CSWperl CSWpmnetsnmp CSWpmnetserver CSWmunin-common
RUNTIME_DEP_PKGS_CSWmunin-node += CSWpmnetssleay

############### Prototype filters for the different packages ###############

#
# files for CSWmunin-common
#

PKGFILES_CSWmunin-common += .*/Munin::Common.*
PKGFILES_CSWmunin-common += .*/Munin\/Common.*
#PKGFILES_CSWmunin-common += .*munin_common.*

#
# files for CSWmunin-node
#

MUNINNODE_UGFILES 	= /var/opt/csw/munin /var/opt/csw/munin/log /var/opt/csw/munin/db /var/opt/csw/munin/run
MUNINNODE_SMF		= /etc/opt/csw/init.d/cswmuninnode
MUNINNODE_USERGROUP	= /opt/csw/etc/pkg/CSWmunin-node/cswusergroup
MUNINNODE_EXECS		= .*munin-node .*munin-node-configure.* .*munindoc.* .*munin-run.* .*munin-sched.*
MUNINNODE_CONF		= .*munin-node.conf .*munin-node.conf.5 .*munin-node.1 /etc/opt/csw/munin/munin-conf.d /etc/opt/csw/munin/plugin-conf.d
MUNINNODE_POSTMSG	 = /opt/csw/share/doc/munin_node/CSWmunin-node.README.CSW

PKGFILES_CSWmunin-node += .*muninnode.* .*CSWmunin-node.*
PKGFILES_CSWmunin-node += .*plugins.*
PKGFILES_CSWmunin-node += .*Munin::Node.* .*Munin\/Plugin.* .*Munin::Plugin.*
PKGFILES_CSWmunin-node += .*Munin\/Node.*
PKGFILES_CSWmunin-node += $(MUNINNODE_UGFILES)
PKGFILES_CSWmunin-node += $(MUNINNODE_SMF)
PKGFILES_CSWmunin-node += $(MUNINNODE_USERGROUP)
PKGFILES_CSWmunin-node += $(MUNINNODE_EXECS)
PKGFILES_CSWmunin-node += $(MUNINNODE_CONF)

PROTOTYPE_MODIFIERS  = muninnode_ugfiles muninnode_smf

PROTOTYPE_FILES_muninnode_ugfiles = $(MUNINNODE_UGFILES)
PROTOTYPE_USER_muninnode_ugfiles = munin
PROTOTYPE_GROUP_muninnode_ugfiles = munin
PROTOTYPE_CLASS_muninnode_ugfiles = ugfiles

PROTOTYPE_FILES_muninnode_smf = $(MUNINNODE_SMF)
PROTOTYPE_PERMS_muninnode_smf = 0755

#
# files for CSWmunin-master
#

MUNINMASTER_UGFILES	 = /var/opt/csw/munin.* /etc/opt/csw/munin/apache.* /etc/opt/csw/munin/templates.*
MUNINMASTER_UGFILES	+= /etc/opt/csw/munin/static.*
MUNINMASTER_UGFILES	+= /etc/opt/csw/munin/munin.conf
MUNINMASTER_USERGROUP	 = /opt/csw/etc/pkg/CSWmunin-master/cswusergroup
MUNINMASTER_EXECS	 = .*munin-check.* .*munin-cron.* .*munin-graph.* .*munin-html.* .*munin-limits.* .*munin-update.*
MUNINMASTER_EXECS	+= .*munin-datafile2storable.* .*munin-storable2datafile.* .*munin-cgi-graph.* .*munin-cgi-html.*
MUNINMASTER_FONTS	 = .*ttf.*
MUNINMASTER_CRONTABS	 = /etc/opt/csw/pkg/CSWmunin-master/crontabs/munin
MUNINMASTER_POSTMSG	 = /opt/csw/share/doc/munin_master/CSWmunin-master.README.CSW

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

PROTOTYPE_MODIFIERS		+= munin_log_dir
PROTOTYPE_FILES_munin_log_dir	 = /var/opt/csw/munin/log /var/opt/csw/munin/db/cgi-tmp
PROTOTYPE_PERMS_munin_log_dir	 = 0775
PROTOTYPE_USER_munin_log_dir	 = munin
PROTOTYPE_GROUP_munin_log_dir	 = munin
PROTOTYPE_CLASS_munin_log_dir	 = ugfiles

############### End of prototype filters for the different packages ###############

INITSMF 	+= $(MUNINNODE_SMF)
USERGROUP	+= $(MUNINNODE_USERGROUP)
USERGROUP	+= $(MUNINMASTER_USERGROUP)
POSTMSG		+= $(MUNINMASTER_POSTMSG)
POSTMSG		+= $(MUNINNODE_POSTMSG)
CRONTABS	+= $(MUNINMASTER_CRONTABS)

#
# checkpkg overrides
#
# yes, we need these dependencies
#

CHECKPKG_OVERRIDES_CSWmunin-master += surplus-dependency|CSWmunin-common
CHECKPKG_OVERRIDES_CSWmunin-master += surplus-dependency|CSWapache2
CHECKPKG_OVERRIDES_CSWmunin-master += surplus-dependency|CSWpmhtmltmpl
CHECKPKG_OVERRIDES_CSWmunin-master += surplus-dependency|CSWpm-rrdtool
CHECKPKG_OVERRIDES_CSWmunin-master += surplus-dependency|CSWpmprmsvldt
CHECKPKG_OVERRIDES_CSWmunin-master += surplus-dependency|CSWpmsocket6
CHECKPKG_OVERRIDES_CSWmunin-master += surplus-dependency|CSWpmfilecpyrecurs
CHECKPKG_OVERRIDES_CSWmunin-master += surplus-dependency|CSWpm-log-log4perl
CHECKPKG_OVERRIDES_CSWmunin-master += surplus-dependency|CSWpm-io-socket-inet6
CHECKPKG_OVERRIDES_CSWmunin-master += surplus-dependency|CSWpm-uri
CHECKPKG_OVERRIDES_CSWmunin-master += surplus-dependency|CSWpmdatemanip
CHECKPKG_OVERRIDES_CSWmunin-master += surplus-dependency|CSWpmfcgi

CHECKPKG_OVERRIDES_CSWmunin-node += surplus-dependency|CSWmunin-common
CHECKPKG_OVERRIDES_CSWmunin-node += surplus-dependency|CSWpmnetsnmp
CHECKPKG_OVERRIDES_CSWmunin-node += surplus-dependency|CSWpmnetssleay
CHECKPKG_OVERRIDES_CSWmunin-node += surplus-dependency|CSWpmnetserver

#
#
#

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
	@#( cd $(WORKSRC); cp Makefile.tmp Makefile ; gmake -f Makefile)
	@#
	@# we are using cswclassutils -> cswcptemplate
	@#
	@ginstall -d $(DESTDIR)/opt/csw/etc/templates/CSWmunin-node/etc/opt/csw/munin
	@ginstall -d $(DESTDIR)/opt/csw/etc/templates/CSWmunin-master/etc/opt/csw/munin
	@ginstall -d $(DESTDIR)/opt/csw/etc/templates/CSWmunin-master/etc/opt/csw/munin/apache
	@ginstall -d $(DESTDIR)/opt/csw/etc/templates/CSWmunin-master/var/opt/csw/munin/www
	@mv $(DESTDIR)/etc/opt/csw/munin/munin-node.conf $(DESTDIR)/opt/csw/etc/templates/CSWmunin-node/etc/opt/csw/munin/
	@mv $(DESTDIR)/etc/opt/csw/munin/munin.conf $(DESTDIR)/opt/csw/etc/templates/CSWmunin-master/etc/opt/csw/munin/
	@ginstall -m 644 $(FILEDIR)/apache-munin-cgi.conf \
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
	@ginstall -m 755 $(FILEDIR)/cswmuninnode $(DESTDIR)/etc/opt/csw/init.d/cswmuninnode
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
	@ginstall -m 644 $(FILEDIR)/CSWmunin-master.README.CSW $(DESTDIR)/opt/csw/share/doc/munin_master/CSWmunin-master.README.CSW
	@ginstall -d $(DESTDIR)/opt/csw/share/doc/munin_node
	@ginstall -m 644 $(FILEDIR)/CSWmunin-node.README.CSW $(DESTDIR)/opt/csw/share/doc/munin_node/CSWmunin-node.README.CSW
	@#
	@# handle some other files
	@#
	@#ginstall -d $(DESTDIR)/opt/csw/share/munin/fonts
	@#ginstall -m 644 $(WORKSRC)/master/VeraMono.ttf $(DESTDIR)/opt/csw/share/munin/fonts/VeraMono.ttf
	@#
	@# make some links for munin node
	@#
	@ln -s /opt/csw/libexec/munin/plugins/load $(DESTDIR)/etc/opt/csw/munin/plugins/load
	@ln -s /opt/csw/libexec/munin/plugins/uptime $(DESTDIR)/etc/opt/csw/munin/plugins/uptime
	@ln -s /opt/csw/libexec/munin/plugins/cpu $(DESTDIR)/etc/opt/csw/munin/plugins/cpu
	@ln -s /opt/csw/libexec/munin/plugins/df $(DESTDIR)/etc/opt/csw/munin/plugins/df
	@$(MAKECOOKIE)
