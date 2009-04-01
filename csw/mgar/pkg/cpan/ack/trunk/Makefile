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

install-custom:
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(mandir)/man1
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@cp $(WORKSRC)/ack $(DESTDIR)$(bindir)
	@pod2man --section=1 $(WORKSRC)/ack > $(DESTDIR)$(mandir)/man1/ack.1
	@cp $(WORKSRC)/Changes $(DESTDIR)$(docdir)/$(GARNAME)/changelog
	@$(MAKECOOKIE)

pre-merge-modulated:
	@$(WORKSRC)/ack --version | sed -n '/^Copyright/,$$p' > $(WORKSRC)/COPYING
	@$(MAKECOOKIE)
