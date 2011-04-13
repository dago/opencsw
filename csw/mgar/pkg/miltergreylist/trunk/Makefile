NAME = miltergreylist
VERSION = 4.2.7
#RELEASE = rc1
#DISTVERSION = $(VERSION)$(RELEASE)
DISTVERSION = $(VERSION)
DISTNAME = milter-greylist-$(DISTVERSION)
WORKSRC = $(WORKDIR)/$(DISTNAME)
CATEGORIES = net

DESCRIPTION = Greylist mail filtering method
define BLURB
   Greylist mail filtering method
endef

MASTER_SITES = http://ftp.espci.fr/pub/milter-greylist/
DISTFILES    = milter-greylist-$(DISTVERSION).tgz
DISTFILES   += COPYING

RUNTIME_DEP_PKGS = CSWcurlrt CSWgeoip CSWlibspf2

PACKAGING_PLATFORMS += solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

CHECKPKG_OVERRIDES += surplus-dependency|CSWgeoip
CHECKPKG_OVERRIDES += file-with-bad-content

PATCHFILES += 0001-Path-and-user-changes-in-conf-file.patch

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS  = --prefix=/opt/csw
CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw
CONFIGURE_ARGS += --with-user=`/usr/xpg4/bin/id -u`
CONFIGURE_ARGS += --with-conffile=/etc/opt/csw/greylist.conf
CONFIGURE_ARGS += --enable-dnsrbl
CONFIGURE_ARGS += --enable-stdio-hack
CONFIGURE_ARGS += --localstatedir=/var/opt/csw/miltergreylist
CONFIGURE_ARGS += --with-libGeoIP=/opt/csw/lib
CONFIGURE_ARGS += --with-libcurl=/opt/csw/lib
CONFIGURE_ARGS += --with-libspf2=/opt/csw/lib
CONFIGURE_ARGS += --mandir=/opt/csw/share/man

# milter-greylist has no tests
TEST_SCRIPTS = 

INSTALL_SCRIPTS = custom

USERGROUP  = /opt/csw/etc/pkg/CSWmiltergreylist/cswusergroup
SAMPLECONF = /etc/opt/csw/greylist.conf
INITSMF    = /etc/opt/csw/init.d/cswmiltergreylist
POSTMSG    = /opt/csw/share/doc/miltergreylist/README.CSW

MIGRATE_FILES      = greylist.conf
MIGRATE_SOURCE_DIR = /opt/csw/etc/mail
MIGRATE_DEST_DIR   = /etc/opt/csw

PROTOTYPE_MODIFIERS = 1
PROTOTYPE_FILES_1   = /var/opt/csw/miltergreylist
PROTOTYPE_CLASS_1   = ugfiles
PROTOTYPE_PERMS_1   = 0700
PROTOTYPE_USER_1    = greylist

include gar/category.mk

#WORKSRC := $(WORKDIR)/$(NAME)-$(VERSION)b1
SPKG_SOURCEURL = http://hcpnet.free.fr/milter-greylist
#SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)

DOCLIST = README ChangeLog greylist.conf greylist2.conf milter-greylist.m4

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@( cd $(WORKSRC) ; \
	   gmake DESTDIR=$(DESTDIR) install )
	@ginstall -d -m 755 $(DESTDIR)/etc/opt/csw
	@mv $(DESTDIR)/etc/mail/greylist.conf $(DESTDIR)/etc/opt/csw/greylist.conf
	@rmdir $(DESTDIR)/etc/mail
	@ginstall -d -m 755 $(DESTDIR)$(docdir)/$(NAME)
	@$(foreach DOC,$(DOCLIST),cp $(WORKSRC)/$(DOC) $(DESTDIR)$(docdir)/$(NAME);)
	@ginstall -d -m 755 $(DESTDIR)/var/opt/csw/$(NAME)
	@rmdir $(DESTDIR)/var/milter-greylist
	@ginstall -d -m 755 $(DESTDIR)/opt/csw/etc/pkg/CSW$(NAME)
	@cp $(FILEDIR)/CSWmiltergreylist.ug $(DESTDIR)/opt/csw/etc/pkg/CSW$(NAME)/cswusergroup
	@ginstall -d -m 755 $(DESTDIR)/etc/opt/csw/init.d
	@cp $(FILEDIR)/CSWmiltergreylist.init $(DESTDIR)/etc/opt/csw/init.d/cswmiltergreylist
	@chmod 755 $(DESTDIR)/etc/opt/csw/init.d/cswmiltergreylist
	@cp $(FILEDIR)/README.CSW $(DESTDIR)$(docdir)/$(NAME)
	@$(MAKECOOKIE)
