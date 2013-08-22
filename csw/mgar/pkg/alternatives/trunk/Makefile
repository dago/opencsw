# $Id$
NAME = alternatives
VERSION = 1.0

DESCRIPTION = Alternatives implementation specific to OpenCSW
define BLURB
endef

MASTER_SITES = 
DISTFILES	=	alternatives
DISTFILES	+=	CSWalternatives.i.cswalternatives
DISTFILES	+=	CSWalternatives.r.cswalternatives
DISTFILES	+=	LICENSE-2.0.txt
DISTFILES	+=	README
DISTFILES	+=	README.user

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = LICENSE-2.0.txt

VENDOR_URL = http://wiki.opencsw.org/project-alternatives

CONFIGURE_SCRIPTS = 

BUILD_DEP_PKGS	=	CSWhelp2man

BUILD_SCRIPTS = man
INSTALL_SCRIPTS = custom
TEST_SCRIPTS = 

ARCHALL	=	1

include gar/category.mk

build-man:
	cd $(WORKDIR) && help2man --section=8 --source='Open CSW' --no-info --output=alternatives.8 ./alternatives
	@$(MAKECOOKIE)

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKDIR)/alternatives $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(mandir)/man8
	ginstall $(WORKDIR)/alternatives.8 $(DESTDIR)$(mandir)/man8
	ginstall -d $(DESTDIR)/etc/opt/csw/alternatives
	ginstall -d $(DESTDIR)/etc/opt/csw/preserve/CSWalternatives/alternatives
	ginstall -d $(DESTDIR)/var/opt/csw/alternatives
	ginstall -d $(DESTDIR)/usr/sadm/install/scripts
	ginstall $(WORKDIR)/CSWalternatives.i.cswalternatives $(DESTDIR)/usr/sadm/install/scripts/i.cswalternatives
	ginstall $(WORKDIR)/CSWalternatives.r.cswalternatives $(DESTDIR)/usr/sadm/install/scripts/r.cswalternatives
	ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	ginstall $(WORKDIR)/README $(DESTDIR)$(docdir)/$(NAME)
	ginstall $(WORKDIR)/README.user $(DESTDIR)$(docdir)/$(NAME)
	@$(MAKECOOKIE)
