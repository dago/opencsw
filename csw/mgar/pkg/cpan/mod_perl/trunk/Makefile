NAME = mod_perl
VERSION = 1.31
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = GOZER

DESCRIPTION = Persistent Perl interpreter for Apache 1.3.x
define BLURB
  The Apache/Perl integration project brings together the full power of the
  Perl programming language and the Apache HTTP server. With mod_perl it is
  possible to write Apache modules entirely in Perl. In addition, the
  persistent interpreter embedded in the server avoids the overhead of starting
  an external interpreter and the penalty of Perl start-up time.
endef

PACKAGES = CSWmodperl
CATALOGNAME = mod_perl

RUNTIME_DEP_PKGS  = CSWapache CSWbdb

# Disable installation of module using apxs
PATCHFILES += patch-apaci-Makefile.tmpl

CONFIGURE_ARGS  = USE_APXS=1
CONFIGURE_ARGS += WITH_APXS=$(prefix)/apache/bin/apxs
CONFIGURE_ARGS += PREFIX=$(prefix)
CONFIGURE_ARGS += EVERYTHING=1

PERL_CONFIGURE_ARGS  = INSTALLSITEARCH=$(perlcswlib)
PERL_CONFIGURE_ARGS += INSTALLSITEMAN3DIR=$(mandir)/man3
# PERL_CONFIGURE_ARGS += LIBS=-lpthread

INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	( cd $(WORKSRC) ; $(INSTALL_ENV) make install DESTDIR=$(DESTDIR) )
	ginstall -d $(DESTDIR)$(docdir)/mod_perl
	ginstall -m 0644 \
		$(FILEDIR)/README $(DESTDIR)$(docdir)/mod_perl
	ginstall -d $(DESTDIR)$(prefix)/apache/perl
	ginstall -m 0755 \
		$(FILEDIR)/test.pl $(DESTDIR)$(prefix)/apache/perl
	ginstall -d $(DESTDIR)$(prefix)/apache/libexec
	strip $(WORKSRC)/apaci/libperl.so
	ginstall -m 0755 \
		$(WORKSRC)/apaci/libperl.so $(DESTDIR)$(prefix)/apache/libexec
	@$(MAKECOOKIE)
