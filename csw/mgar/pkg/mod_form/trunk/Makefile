NAME = mod_form
VERSION = 0.1
GARTYPE = v2

DESCRIPTION = A utility to decode data submitted from Web forms

MASTER_SITES = http://apache.webthing.com/svn/apache/forms/
DISTFILES += mod_form.c
DISTFILES += mod_form.h
DISTFILES += gpl.html
DISTFILES += CSWap2-mod-form.postinstall
DISTFILES += CSWap2-mod-form.preremove

# Patch from http://mirrorbrain.org/docs/installation/source/
PATCHFILES += formget.patch
PATCHDIRLEVEL = 0

VENDOR_URL = http://apache.webthing.com/mod_form/
LICENSE = gpl.html

PACKAGES = CSWap2-mod-form
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWap2-mod-form += CSWapache2
CHECKPKG_OVERRIDES_CSWap2-mod-form_CSWap2modauthradius += surplus-dependency|CSWapache2

# Apache paths
AP2_ROOT      = $(prefix)/apache2
AP2_LIBEXEC   = $(DESTDIR)$(AP2_ROOT)/libexec
AP2_EXTRACONF = $(DESTDIR)$(AP2_ROOT)/etc/extra
AP2_SBIN      = $(AP2_ROOT)/sbin
APXS          = $(AP2_SBIN)/apxs

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

STRIP_DIRS = $(DESTDIR)$(prefiinclude gar/category.mk

post-extract:
	ginstall -d $(WORKSRC)
	cp $(WORKDIR)/mod_form.c $(WORKDIR)/mod_form.h $(WORKSRC)

build-custom:
	cd $(WORKSRC) && $(APXS) -c mod_form.c
	@$(MAKECOOKIE)

install-custom:
	mkdir -p $(AP2_LIBEXEC)
	cd $(WORKSRC) && $(APXS) -S LIBEXECDIR=$(AP2_LIBEXEC) -i mod_form.la
	ginstall -d $(DESTDIR)$(prefix)/apache2/include
	ginstall -m 0644 $(WORKSRC)/mod_form.h $(DESTDIR)$(prefix)/apache2/include/mod_form.h
	@$(MAKECOOKIE)

