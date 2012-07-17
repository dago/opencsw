NAME = mod_perl
DISTVERSION = 2.0.7
VERSION = $(subst -,,$(DISTVERSION))
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = PHRED

DESCRIPTION = Persistent Perl interpreter for Apache 2.x
define BLURB
  The Apache/Perl integration project brings together the full power of the
  Perl programming language and the Apache HTTP server. With mod_perl it is
  possible to write Apache modules entirely in Perl. In addition, the
  persistent interpreter embedded in the server avoids the overhead of
  starting an external interpreter and the penalty of Perl start-up time.
endef

#
# WARNING: mod_perl tests will fail unless 'dns' is specified somewhere
#          in the 'hosts' line in /etc/nsswitch.conf.  e.g.:
#
#                   hosts: nis files dns
#
#          This is due to the operation of getaddrinfo() on Solaris, and
#          is precipitated by the test apache configuration which uses the
#          _default_ vhost, causing a lookup of 255.255.255.255.
#

# For OpenSSL
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

PACKAGES = CSWap2modperl
# Keep the standard name for now
CATALOGNAME = ap2_modperl
CHECKPKG_OVERRIDES_CSWap2modperl += catalogname-does-not-match-pkgname|pkgname=CSWap2modperl|catalogname=ap2_modperl|expected-catalogname=ap2modperl
SPKG_DESC_CSWap2modperl = Persistent Perl interpreter for Apache 2.x
RUNTIME_DEP_PKGS_CSWap2modperl += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWap2modperl += CSWlibaprutil1-0
RUNTIME_DEP_PKGS_CSWap2modperl += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWap2modperl += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWap2modperl += CSWapache2
RUNTIME_DEP_PKGS_CSWap2modperl += CSWlibapr1-0
RUNTIME_DEP_PKGS_CSWap2modperl += CSWlibldap2-4-2

# These are only examples
CHECKPKG_OVERRIDES_CSWap2modperl += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/Apache2::Directive.3perl
CHECKPKG_OVERRIDES_CSWap2modperl += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/Apache2::Status.3perl
CHECKPKG_OVERRIDES_CSWap2modperl += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/ModPerl::RegistryLoader.3perl
CHECKPKG_OVERRIDES_CSWap2modperl += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/Apache::TestMB.3perl
CHECKPKG_OVERRIDES_CSWap2modperl += file-with-bad-content|/usr/local|root/opt/csw/lib/perl/csw/Apache/TestMB.pm
CHECKPKG_OVERRIDES_CSWap2modperl += file-with-bad-content|/usr/local|root/opt/csw/lib/perl/csw/Apache/TestBuild.pm
CHECKPKG_OVERRIDES_CSWap2modperl += file-with-bad-content|/usr/local|root/opt/csw/lib/perl/csw/Apache2/Directive.pm
CHECKPKG_OVERRIDES_CSWap2modperl += file-with-bad-content|/usr/local|root/opt/csw/lib/perl/csw/Apache2/Status.pm
CHECKPKG_OVERRIDES_CSWap2modperl += file-with-bad-content|/usr/local|root/opt/csw/lib/perl/csw/Apache2/Build.pm
CHECKPKG_OVERRIDES_CSWap2modperl += file-with-bad-content|/usr/local|root/opt/csw/lib/perl/csw/ModPerl/RegistryLoader.pm
CHECKPKG_OVERRIDES_CSWap2modperl += file-with-bad-content|/usr/local|root/opt/csw/lib/perl/csw/ModPerl/CScan.pm


CONFIGURE_ARGS  = MP_APXS=$(prefix)/apache2/sbin/apxs
CONFIGURE_ARGS += MP_PROMPT_DEFAULT=1
CONFIGURE_ARGS += MP_DEBUG=1

# Gtop is platform specific
#CONFIGURE_ARGS += MP_USE_GTOP=1

# MP2 must be installed for test to work
TEST_SCRIPTS =

INSTALL_SCRIPTS = custom

LICENSE = LICENSE

include gar/category.mk

#LDFLAGS += -L$(prefix)/bdb48/lib
#LD_OPTIONS += -R$(prefix)/bdb44/lib

# EXTRA_LIB += $(prefix)/bdb48/lib
# EXTRA_INC += $(prefix)/bdb48/include

install-custom:
	( cd $(WORKSRC) ; $(INSTALL_ENV) make install DESTDIR=$(DESTDIR) )
	@$(MAKECOOKIE)

post-install:
	ginstall -d $(DESTDIR)$(prefix)/apache2/etc
	ginstall -d $(DESTDIR)$(prefix)/apache2/etc/extra
	ginstall -m 0755 \
		$(WORKDIR)/startup.pl.CSW \
		$(DESTDIR)$(prefix)/apache2/etc
	ginstall -m 0644 \
		$(WORKDIR)/httpd-perl.conf.CSW \
		$(DESTDIR)$(prefix)/apache2/etc/extra
	@$(MAKECOOKIE)
