GARNAME = nrpe
GARVERSION = 2.12
CATEGORIES = apps

DESCRIPTION = NRPE daemon for Nagios
define BLURB
  NRPE allows you to remotely execute Nagios plugins on other Linux/Unix machines. This allows you to monitor remote machine metrics (disk usage, CPU load, etc.). NRPE can also communicate with some of the Windows agent addons, so you can execute scripts and check metrics on remote Windows machines as well.
endef

#MASTER_SITES = http://surfnet.dl.sourceforge.net/sourceforge/nagios/
MASTER_SITES = $(SF_MASTERS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWnrpe, prototype checkinstall preinstall postinstall preremove depend)
DISTFILES += svc-nrpe nrpe.xml nrpe
DISTFILES += $(call admfiles,CSWnrpeplugin, prototype depend)

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl-lib=/opt/csw/lib
CONFIGURE_ARGS += --with-ssl-inc=/opt/csw/include
CONFIGURE_ARGS += --with-ssl-dir=/opt/csw/bin
CONFIGURE_ARGS += --with-kerberos-inc=/opt/csw/include
CONFIGURE_ARGS += --prefix=/opt/csw/nagios
CONFIGURE_ARGS += --exec-prefix=/opt/csw/nagios
CONFIGURE_ARGS += --with-command-user=nagios
CONFIGURE_ARGS += --with-command-group=nagios

PATCHFILES = patch.diff	# Removal of LOG_AUTHPRIV and LOG_FTP
			# Solaris doesn't have these log facilities
PATCHFILES += configure.diff 
PATCHFILES += makefile.diff
PATCHFILES += doc.diff	# changes made to global Makefile.in to copy some docs

sysconfdir ?= $(prefix)/nagios/etc
bindir ?= $(prefix)/bin
libexecdir ?= $(prefix)/libexec/nagios-plugins
datadir ?= $(prefix)/share


#EXTRA_LIB = /opt/csw/lib

TEST_TARGET = all

INSTALL_ARGS += install-docs
INSTALL_ARGS += install-daemon-config

include gar/category.mk
