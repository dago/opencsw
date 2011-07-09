NAME = ucspi-tcp
VERSION = 0.88
CATEGORIES = apps

DESCRIPTION = Command-line tools for building TCP client-server applications
define BLURB
endef

MASTER_SITES += http://cr.yp.to/ucspi-tcp/
MASTER_SITES += http://smarden.org/pape/djb/manpages/
DISTFILES += $(DISTNAME).tar.gz
#DISTFILES += doc.tar.gz
DISTFILES += $(DISTNAME)-man.tar.gz

VENDOR_URL = http://cr.yp.to/ucspi-tcp.html
LICENSE = README

PACKAGES += CSWucspi-tcp
SPKG_DESC_CSWucspi-tcp = Command-line tools for building TCP client-server applications
OBSOLETED_BY_CSWucspi-tcp = CSWucspitcp
CATALOGNAME_CSWucspitcp = ucspi_tcp_stub

FILES += addcr
FILES += argv0
FILES += date@
FILES += delcr
FILES += finger@
FILES += fixcrio
FILES += http@
FILES += mconnect-io
FILES += rblsmtpd
FILES += recordio
FILES += tcpcat
FILES += tcpclient
FILES += tcprules
FILES += tcprulescheck
FILES += tcpserver
FILES += mconnect
FILES += who@

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

configure-custom:
	@echo "==> Configuring $(NAME)"
	@echo $(prefix) >$(WORKSRC)/conf-home
	@echo $(CC) $(CFLAGS) >$(WORKSRC)/conf-cc
	@echo $(CC) $(LDFLAGS) >$(WORKSRC)/conf-ld
	@$(MAKECOOKIE)

build-custom:
	@echo "==> building $(NAME)"
	cd $(WORKSRC) && gmake
	@$(MAKECOOKIE)

install-custom:
	@echo "==> installing $(NAME)"
	@echo "==> to $(DESTDIR)$(prefix)/bin"
	rm -rf   $(DESTDIR)$(prefix)
	mkdir -p $(DESTDIR)$(prefix)/bin
	ginstall -m 755 $(addprefix $(WORKSRC)/,$(FILES)) $(DESTDIR)$(prefix)/bin 
	mkdir -p $(DESTDIR)$(mandir)/man1
	ginstall -m 644 $(WORKDIR)/$(DISTNAME)-man/*.1 $(DESTDIR)$(mandir)/man1
	@$(MAKECOOKIE)
