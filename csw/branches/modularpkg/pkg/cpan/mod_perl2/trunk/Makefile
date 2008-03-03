GARNAME = mod_perl
DISTVERSION = 2.0.3
GARVERSION = $(subst -,,$(DISTVERSION))
CATEGORIES = cpan
AUTHOR = PGOLLUCCI

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

#MASTER_SITES  = http://perl.apache.org/dist/
#MASTER_SITES += http://people.apache.org/~pgollucci/mp2/
#MODDIST = mod_perl-$(DISTVERSION).tar.gz 
#WORKSRC = $(WORKDIR)/mod_perl-$(DISTVERSION)

pkgfiles   = prototype depend postinstall preremove space
DISTFILES += $(call admfiles,CSWap2modperl,$(pkgfiles))
DISTFILES += startup.pl.CSW httpd-perl.conf.CSW

#BUILDDEPS += cpan/Apache-Test server/apache2

CONFIGURE_ARGS  = MP_APXS=$(prefix)/apache2/sbin/apxs
CONFIGURE_ARGS += MP_PROMPT_DEFAULT=1
CONFIGURE_ARGS += MP_DEBUG=1

# Gtop is platform specific
#CONFIGURE_ARGS += MP_USE_GTOP=1

# MP2 must be installed for test to work
TEST_SCRIPTS =

INSTALL_SCRIPTS = custom

include gar/category.mk

LDFLAGS += -L$(prefix)/bdb44/lib
LD_OPTIONS += -R$(prefix)/bdb44/lib

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

