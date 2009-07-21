GARNAME = siege
GARVERSION = 2.66
CATEGORIES = xtra

DESCRIPTION = A http regression testing and benchmarking utility
define BLURB
  Siege is an http regression testing and benchmarking utility. It was
  designed to let web developers measure the performance of their code
  under duress, to see how it will stand up to load on the internet. It
  lets the user hit a web server with a configurable number of
  concurrent simulated users.
endef

MASTER_SITES = ftp://sid.joedog.org/pub/siege/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# we require
REQUIRED_PKGS = CSWcswclassutils CSWosslrt

# handle config file
PRESERVECONF = $(sysconfdir)/urls.txt.CSW

# patch bombardment
PATCHFILES  = patch-bombardment.in
PATCHFILES += patch-configure

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl=$(prefix)

TEST_SCRIPTS =

INSTALL_SCRIPTS = bin man additional

include gar/category.mk

# install is broken..
bin-list  = $(WORKSRC)/src/siege
bin-list += $(WORKSRC)/utils/bombardment
bin-list += $(WORKSRC)/utils/siege2csv.pl
bin-list += $(WORKSRC)/utils/siege.config
share-list  = $(WORKSRC)/doc/urls.txt
share-list += $(WORKSRC)/doc/siegerc

install-bin:
	ginstall -d $(DESTDIR)$(bindir)
	@( for file in $(bin-list) ; do \
		ginstall -m 751 $$file $(DESTDIR)$(bindir) ; \
			done )

install-additional:
	ginstall -d $(DESTDIR)$(sysconfdir)
	ginstall -m 644 $(WORKSRC)/doc/urls.txt \
		$(DESTDIR)$(sysconfdir)/urls.txt.CSW
	ginstall -d $(DESTDIR)$(sharedstatedir)/$(GARNAME)
	ginstall -m 644 $(WORKSRC)/doc/siegerc \
		$(DESTDIR)$(sharedstatedir)/$(GARNAME)

install-man:
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall -m 644 $(WORKSRC)/doc/siege.1 $(DESTDIR)$(mandir)/man1
	ginstall -m 644 $(WORKSRC)/doc/bombardment.1 $(DESTDIR)$(mandir)/man1
	ginstall -m 644 $(WORKSRC)/doc/siege2csv.1 $(DESTDIR)$(mandir)/man1
	ginstall -d $(DESTDIR)$(mandir)/man5
	ginstall -m 644 $(WORKSRC)/doc/urls_txt.5 $(DESTDIR)$(mandir)/man5
	ginstall -d $(DESTDIR)$(mandir)/man7
	ginstall -m 644 $(WORKSRC)/doc/layingsiege.7 $(DESTDIR)$(mandir)/man7
	@$(MAKECOOKIE)
