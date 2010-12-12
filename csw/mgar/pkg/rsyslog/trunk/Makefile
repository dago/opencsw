NAME = rsyslog
VERSION = 4.7.1
CATEGORIES = server

DESCRIPTION = Enhanced multi-threaded syslogd with a focus on security and reliability
define BLURB
  Enhanced multi-threaded syslogd with a focus on security and reliability
endef

MASTER_SITES = http://download.rsyslog.com/rsyslog/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS_CSWrsyslog += CSWzlib
RUNTIME_DEP_PKGS_CSWrsyslog += CSWgcc4corert

GARCOMPILER = GNU

TEST_SCRIPTS = 
TEST_TARGET = check

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
