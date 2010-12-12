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
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += COPYING

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://sourceforge.net/projects/modgssapache

BUILD_DEP_PKGS = CSWossldevel
RUNTIME_DEP_PKGS = CSWosslrt

PACKAGES = CSWlibfbopenssl
CATALOGNAME = libfbopenssl

BUILD64 = 1
WORKSRC = $(WORKDIR)/$(NAME)
CONFIGURE_SCRIPTS = 
BUILD_SCRIPTS = custom
TEST_SCRIPTS = custom
INSTALL_SCRIPTS = custom
EXTRA_CFLAGS = -Kpic

FILES=src/asn1/asn1help src/file/filehelp src/gssapi/gssapi src/krb5/krb5help src/spnego/spnego src/spnego/spnegohelp

.c.o:
	$(CC) -c $(CFLAGS) $(CPPFLAGS) -o $@ $<

include gar/category.mk

# The Makefile is hardcoded to gcc. Patching it is more complicated than
# just compiling the needed stuff here. Please take care on version bumps!

build-custom: $(foreach F,$(FILES),$(WORKSRC)/$F.o)
	cd $(WORKSRC) && $(BUILD_ENV) $(CC) $(LDFLAGS) $(foreach F,$(FILES),$F.o) -lcrypto -G -o libfbopenssl.so
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
	ginstall $(WORKSRC)/libfbopenssl.so $(DESTDIR)$(libdir)
	ginstall -d $(DESTDIR)$(docdir)/$(CATALOGNAME)
	ginstall $(WORKSRC)/readme.txt $(DESTDIR)$(docdir)/$(CATALOGNAME)/
