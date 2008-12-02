GARNAME = mod_auth_pam
ABIVERSION = 2.0
GARVERSION = 1.1.1
CATEGORIES = server

DESCRIPTION = Implements basic authentication on top of PAM
define BLURB
  The PAM authentication module implements Basic authentication on top of the
  Pluggable Authentication Module library. Thereby it supports standard unix
  passwd, shadow, NIS, SMB auth and radius (-> complete list of modules)
  authentication transparently and easily interchangeable, wherever the HTTP
  protocol allows it.
endef

MASTER_SITES = http://pam.sourceforge.net/mod_auth_pam/dist/
DISTFILES  = $(GARNAME)-$(ABIVERSION)-$(GARVERSION).tar.gz
CSWadmin   = depend prototype postinstall preremove space
DISTFILES += $(call admfiles,CSWap2modauthpam,$(CSWadmin))

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)-(\d+(?:\.\d+)*).tar.gz

# Fix up installation routine
PATCHFILES += install.diff

WORKSRC = $(WORKDIR)/$(GARNAME)

CONFIGURE_SCRIPTS =

# No test suite
TEST_SCRIPTS =

# Exports for the makefile
APXS = $(prefix)/apache2/sbin/apxs
export APXS

STRIP_DIRS = $(DESTDIR)$(prefix)/apache2/libexec

include gar/category.mk

post-install:
	install -d $(DESTDIR)$(docdir)/ap2modauthpam
	( cd $(WORKSRC) ; \
		cp -R samples $(DESTDIR)$(docdir)/ap2modauthpam ; \
	  cp    README doc/*.html $(DESTDIR)$(docdir)/ap2modauthpam )
	$(DONADA)

