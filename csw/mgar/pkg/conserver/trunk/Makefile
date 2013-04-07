# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = conserver
VERSION = 8.1.11
GARTYPE = v2

DESCRIPTION = Client/Server console server software
define BLURB
    Conserver is an application that allows multiple users to watch a
    serial console at the same time.  It can log the data, allows users
    to take write-access of a console (one at a time), and has a
    variety of bells and whistles to accentuate that basic
    functionality.  The idea is that conserver will log all your serial
    traffic so you can go back and review why something crashed, look
    at changes (if done on the console), or tie the console logs into a
    monitoring system (just watch the logfiles it creates).  With
    multi-user capabilities you can work on equipment with others,
    mentor, train, etc.  It also does all that client-server stuff so
    that, assuming you have a network connection, you can interact with
    any of the equipment from home or wherever.

endef

MASTER_SITES = http://www.conserver.com/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

RUNTIME_DEP_PKGS = CSWlibssl1-0-0

CHECKPKG_OVERRIDES  = file-with-bad-content|/usr/local|root/opt/csw/share/examples/conserver/conserver.rc
CHECKPKG_OVERRIDES += file-with-bad-content|/usr/local|root/opt/csw/share/examples/conserver/conserver.cf

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-uds
CONFIGURE_ARGS += --with-libwrap
CONFIGURE_ARGS += --with-openssl
CONFIGURE_ARGS += --with-pam

LICENSE = LICENSE

DISTFILES += cswconserver
INITSMF = $(sysconfdir)/init.d/cswconserver

TEST_SCRIPTS = 

include gar/category.mk

post-merge: merge-init-script

#
merge-init-script:
	ginstall -m 755 -d $(PKGROOT)$(sysconfdir)/init.d/
	ginstall -m 755 $(FILEDIR)/cswconserver $(PKGROOT)$(sysconfdir)/init.d/cswconserver

