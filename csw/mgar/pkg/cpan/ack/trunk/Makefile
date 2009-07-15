GARNAME = ack
GARVERSION = 1.88
CATEGORIES = cpan
AUTHOR = PETDANCE

DESCRIPTION = grep-like text finder, aimed at programmers
define BLURB
  ack is a tool like grep, aimed at programmers with large trees of 
  heterogeneous source code. ack is written purely in Perl, and takes 
  advantage of the power of Perl's regular expressions. 
endef

PACKAGES = CSWack
CATALOGNAME = ack
ARCHALL = 1

INSTALL_SCRIPTS = custom

include gar/category.mk

# Make sure ack uses our perl, stock perl version on Sol 8 / 9 bail out
post-extract-modulated:
	@perl -pi -e '\
		s|^#!.*$$|#!/opt/csw/bin/perl| if $$. eq 1;' \
		$(WORKSRC)/t/*.t
	@perl -pi -e '\
		s|/usr/bin/env perl|/opt/csw/bin/perl|' \
		$(WORKSRC)/squash
	@$(MAKECOOKIE)

install-custom: DOCDEST = $(DESTDIR)$(docdir)/$(GARNAME)
install-custom:
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(mandir)/man1
	@ginstall -d $(DOCDEST)
	@cp $(WORKSRC)/ack $(DESTDIR)$(bindir)
	@pod2man --section=1 $(WORKSRC)/ack > $(DESTDIR)$(mandir)/man1/ack.1
	@cp $(WORKSRC)/Changes $(DOCDEST)/changelog
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)

pre-merge-modulated:
	@$(WORKSRC)/ack --version | sed -n '/^Copyright/,$$p' > $(WORKSRC)/COPYING
	@$(MAKECOOKIE)
