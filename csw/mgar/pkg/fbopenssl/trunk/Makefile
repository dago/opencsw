NAME = fbopenssl
VERSION = 0.0.4
CATEGORIES = lib

DESCRIPTION = Extensions to OpenSSL including support for GSS-API and SPNEGO
define BLURB
  fbopenssl is a library containing extensions to OpenSSL, including support for:
  - GSS-API (RFC 2743)
  - SPNEGO (RFC 2478)
endef

SF_PROJ = modgssapache
MASTER_SITES = $(SF_MIRRORS)
DISTNAME = $(NAME)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += COPYING

VENDOR_URL = http://sourceforge.net/projects/modgssapache

BUILD_DEP_PKGS = CSWossldevel
RUNTIME_DEP_PKGS = CSWosslrt

PACKAGES += CSWlibfbopenssl0
SPKG_DESC_CSWlibfbopenssl0 = Extensions to OpenSSL including support for GSS-API and SPNEGO, libfbopenssl.so.0
PKGFILES_CSWlibfbopenssl0 += $(call pkgfiles_lib,libfbopenssl.so.0)
OBSOLETED_BY_CSWlibfbopenssl0 += CSWlibfbopenssl

PACKAGES += CSWlibfbopenssl-dev
SPKG_DESC_CSWlibfbopenssl-dev = Development files for libfbopenssl.so.0
# PKGFILES is catchall
# These are no header files in there, is this correct?
RUNTIME_DEP_PKGS_CSWlibfbopenssl-dev += CSWlibfbopenssl0

BUILD64 = 1

CONFIGURE_SCRIPTS = 
BUILD_SCRIPTS = custom
TEST_SCRIPTS = custom
INSTALL_SCRIPTS = custom
EXTRA_CFLAGS = -Kpic

FILES += src/asn1/asn1help
FILES += src/file/filehelp
FILES += src/gssapi/gssapi
FILES += src/krb5/krb5help
FILES += src/spnego/spnego
FILES += src/spnego/spnegohelp

.c.o:
	$(CC) -c $(CFLAGS) $(CPPFLAGS) -o $@ $<

include gar/category.mk

# The Makefile is hardcoded to gcc. Patching it is more complicated than
# just compiling the needed stuff here. Please take care on version bumps!

build-custom: $(foreach F,$(FILES),$(WORKSRC)/$F.o)
	cd $(WORKSRC) && $(BUILD_ENV) $(CC) $(LDFLAGS) $(foreach F,$(FILES),$F.o) -lcrypto -G -h libfbopenssl.so.0 -o libfbopenssl.so.$(VERSION)
	gln -s libfbopenssl.so.$(VERSION) $(WORKSRC)/libfbopenssl.so.0
	gln -s libfbopenssl.so.0 $(WORKSRC)/libfbopenssl.so
	@$(MAKECOOKIE)

test-custom:
	# makespnego
	(cd $(WORKSRC)/test/makespnego; $(BUILD_ENV) $(CC) $(CPPFLAGS) $(CFLAGS) makespnego.c -L../.. -R../.. -lfbopenssl $(LDFLAGS) -lcrypto -o makespnego)
	(cd $(WORKSRC)/test/parsespnego; $(BUILD_ENV) $(CC) $(CPPFLAGS) $(CFLAGS) parsespnego.c -L../.. -R../.. -lfbopenssl $(LDFLAGS) -lcrypto -o parsespnego)
	ginstall -d $(WORKSRC)/test/temp
	-(cd $(WORKSRC)/test/makespnego; ./makespnego init 1.2.840.113554.1.2.2 ../tokens/kerberos-req.der ../temp/spnego-req.der)
	-(cd $(WORKSRC)/test/makespnego; ./makespnego targ 0 1.2.840.113554.1.2.2 ../tokens/kerberos-rep.der ../temp/spnego-rep.der)
	-(cd $(WORKSRC)/test/parsespnego; ./parsespnego init ../tokens/spnego-req.der 1.2.840.113554.1.2.2 ../temp/kerberos-req.der)
	-(cd $(WORKSRC)/test/parsespnego; ./parsespnego targ ../tokens/spnego-rep.der ../temp/kerberos-rep.der)
	@$(MAKECOOKIE)

install-custom:
	ginstall -d $(DESTDIR)$(libdir)
	ginstall $(WORKSRC)/libfbopenssl.so.$(VERSION) $(DESTDIR)$(libdir)
	gln -s libfbopenssl.so.$(VERSION) $(DESTDIR)$(libdir)/libfbopenssl.so.0
	gln -s libfbopenssl.so.0 $(DESTDIR)$(libdir)/libfbopenssl.so
	ginstall -d $(DESTDIR)$(docdir)/$(CATALOGNAME)
	ginstall $(WORKSRC)/readme.txt $(DESTDIR)$(docdir)/$(CATALOGNAME)/
	@$(MAKECOOKIE)
