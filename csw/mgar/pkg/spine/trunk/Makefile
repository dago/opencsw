# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! Convert postinstall to POSTMSG
# ! Test that the package is actually working
# ! Check the user handling (cswusergroup file exists, but not used?!)
# * Document and merge patches, ./configure LD* hack really required?!
# * libtool hack really required?
#
NAME = spine
VERSION = 0.8.7e
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Very fast poller for cacti
define BLURB
  Spine, formally Cactid, is a poller for Cacti that primarily strives
  to be as fast as possible. For this reason it is written in native C,
  makes use of POSIX threads, and is linked directly against the net-snmp
  library for minmumal SNMP polling overhead. Spine is a replacement for
  the default cmd.php poller so you must decide if using Spine makes sense
  for your installation.
endef

VENDOR_URL   = http://www.cacti.net/
MASTER_SITES = http://www.cacti.net/downloads/spine/
DISTFILES    = cacti-$(NAME)-$(VERSION).tar.gz
DISTFILES   += cswusergroup CSWspine.postinstall
WORKSRC      = $(WORKDIR)/cacti-$(NAME)-$(VERSION)

PATCHFILES += configure.diff
PATCHFILES += spine.h.diff
PATCHFILES += util.c.diff
PATCHFILES += spine.conf.diff

NOISALIST = 1

RUNTIME_DEP_PKGS += CSWmysql5rt
RUNTIME_DEP_PKGS += CSWnetsnmp
RUNTIME_DEP_PKGS += CSWosslrt
RUNTIME_DEP_PKGS += CSWzlib

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-mysql=/opt/csw/mysql5
CONFIGURE_ARGS += --with-snmp=/opt/csw/include/net-snmp
EXTRA_LIB       = /opt/csw/mysql5/lib/mysql

CONFIGURE_SCRIPTS = custom
INSTALL_SCRIPTS = custom

# Spine doesn't come with a test suite
SKIPTEST = 1

sysconfdir = /etc/opt/csw
PRESERVECONF = $(sysconfdir)/spine.conf

EXTRA_PAX_ARGS = '-s,ChangeLog,changelog,p'

include gar/category.mk

configure-custom:
	@echo " ==> Configuring in $(WORKSRC)"
	rm $(WORKSRC)/config/ltmain.sh
	rm $(WORKSRC)/config/config.sub
	rm $(WORKSRC)/config/config.guess
	ln -s /opt/csw/share/libtool/config/ltmain.sh  $(WORKSRC)/config/ltmain.sh
	ln -s /opt/csw/share/libtool/config/config.sub  $(WORKSRC)/config/config.sub
	ln -s /opt/csw/share/libtool/config/config.guess  $(WORKSRC)/config/config.guess
	( cd $(WORKSRC) ; ./configure $(CONFIGURE_ARGS) )
	@$(MAKECOOKIE)

install-custom: EXTRA_DOCS = README LICENSE LICENSE.LGPL ChangeLog
install-custom: BINDIR = $(DESTDIR)$(bindir)
install-custom: CFGDIR = $(DESTDIR)$(sysconfdir)
install-custom: DOCDEST = $(DESTDIR)$(docdir)/spine
install-custom:
	ginstall -d $(DOCDEST)
	(cd $(WORKSRC); ginstall -m 644 $(EXTRA_DOCS) $(DOCDEST))
	ginstall -Dm 755 $(WORKSRC)/spine $(BINDIR)
	ginstall -Dm 644 $(WORKSRC)/spine.conf $(CFGDIR)/spine.conf
	@$(MAKECOOKIE)
