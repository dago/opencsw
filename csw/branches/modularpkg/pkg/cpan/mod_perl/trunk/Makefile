GARNAME = mod_perl
GARVERSION = 1.29
CATEGORIES = cpan
AUTHOR = GOZER

DESCRIPTION = Persistent Perl interpreter for Apache 1.3.x
define BLURB
  The Apache/Perl integration project brings together the full power of the
  Perl programming language and the Apache HTTP server. With mod_perl it is
  possible to write Apache modules entirely in Perl. In addition, the
  persistent interpreter embedded in the server avoids the overhead of starting
  an external interpreter and the penalty of Perl start-up time.
endef

pkgfiles   = prototype depend postinstall preremove space
DISTFILES += $(call admfiles,CSWmodperl,$(pkgfiles))
DISTFILES += test.pl README

# Disable installation of module using apxs
PATCHFILES += apxsinstall.diff

CONFIGURE_ARGS  = USE_APXS=1
CONFIGURE_ARGS += WITH_APXS=$(prefix)/apache/bin/apxs
CONFIGURE_ARGS += PREFIX=$(prefix)
CONFIGURE_ARGS += EVERYTHING=1

PERL_CONFIGURE_ARGS  = INSTALLSITEARCH=$(prefix)/apache/lib/perl
PERL_CONFIGURE_ARGS += INSTALLSITEMAN3DIR=$(prefix)/apache/man/man3

INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	( cd $(WORKSRC) ; $(INSTALL_ENV) make install DESTDIR=$(DESTDIR) )
	@$(MAKECOOKIE)

post-install:
	install -d $(DESTDIR)$(docdir)/mod_perl
	install -m 0644 \
		$(WORKDIR)/README $(DESTDIR)$(docdir)/mod_perl
	install -d $(DESTDIR)$(prefix)/apache/perl
	install -m 0755 \
		$(WORKDIR)/test.pl $(DESTDIR)$(prefix)/apache/perl
	install -d $(DESTDIR)$(prefix)/apache/libexec
	strip $(WORKSRC)/apaci/libperl.so
	install -m 0755 \
		$(WORKSRC)/apaci/libperl.so $(DESTDIR)$(prefix)/apache/libexec
	@$(MAKECOOKIE)

