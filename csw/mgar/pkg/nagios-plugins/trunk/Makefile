GARNAME = nagios-plugins
GARVERSION = 1.4.13
CATEGORIES = apps

DESCRIPTION = Plugins for Nagios
define BLURB
  Long description
endef

MASTER_SITES = http://surfnet.dl.sourceforge.net/sourceforge/nagiosplug/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWnagiosp,prototype depend)

PATCHFILES  = makefile.diff # add target 'none'
PATCHFILES += plugins-root.diff # 
PATCHFILES += legal.diff

CFLAGS += -I /opt/csw/postgresql/include/

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-mysql-dir=/opt/csw/mysql5/bin
CONFIGURE_ARGS += --with-pg-dir=/opt/csw/postgresql/include/
CONFIGURE_ARGS += --disable-largefile

libexecdir ?= $(prefix)/libexec/nagios-plugins

# Extra libs
EXTRA_LIB += /opt/csw/mysql5/lib/mysql
EXTRA_LIB += /opt/csw/postgresql/lib

# Extra includes
EXTRA_INC = /opt/csw/postgresql/include

INSTALL_ARGS += install-contrib
INSTALL_ARGS += install-legal

TEST_TARGET = none

include gar/category.mk
