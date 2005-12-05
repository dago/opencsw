GARNAME = mod_perl2
DISTVERSION = 2.0.2
GARVERSION = $(subst -,,$(DISTVERSION))
CATEGORIES = cpan

DESCRIPTION = Persistent Perl interpreter for Apache 2.x
define BLURB
  The Apache/Perl integration project brings together the full power of the
  Perl programming language and the Apache HTTP server. With mod_perl it is
  possible to write Apache modules entirely in Perl. In addition, the
  persistent interpreter embedded in the server avoids the overhead of starting
  an external interpreter and the penalty of Perl start-up time.
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

MASTER_SITES  = http://perl.apache.org/dist/
MASTER_SITES += http://people.apache.org/~pgollucci/mp2/
MODDIST = mod_perl-$(DISTVERSION).tar.gz 
WORKSRC = $(WORKDIR)/mod_perl-$(DISTVERSION)

DISTFILES += CSWap2modperl.gspec CSWap2modperl.prototype CSWap2modperl.depend
DISTFILES += CSWap2modperl.postinstall CSWap2modperl.preremove
DISTFILES += CSWap2modperl.space startup.pl.CSW

#BUILDDEPS += cpan/Apache-Test server/apache2

CONFIGURE_ARGS  = MP_APXS=$(prefix)/apache2/sbin/apxs
#CONFIGURE_ARGS += MP_AP_DESTDIR=$(DESTDIR)
CONFIGURE_ARGS += MP_PROMPT_DEFAULT=1
CONFIGURE_ARGS += MP_DEBUG=1

# Gtop is platform specific
#CONFIGURE_ARGS += MP_USE_GTOP=1

# MP2 must be installed for test to work
ENABLE_TEST = 0

INSTALL_SCRIPTS = custom

include ../category.mk

LDFLAGS += -L$(prefix)/bdb43/lib
LD_OPTIONS += -R$(prefix)/bdb43/lib

install-custom:
	( cd $(WORKSRC) ; $(INSTALL_ENV) make install DESTDIR=$(DESTDIR) )
	@$(MAKECOOKIE)

post-install:
	install -d $(DESTDIR)$(prefix)/apache2/etc
	install -m 0755 $(WORKDIR)/startup.pl.CSW $(DESTDIR)$(prefix)/apache2/etc
	@$(MAKECOOKIE)

