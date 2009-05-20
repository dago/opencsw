GARNAME = multitail
GARVERSION = 5.2.2
CATEGORIES = utils

DESCRIPTION = View one or multiple files like the original tail program
define BLURB
  MultiTail lets you view one or multiple files like the original tail program.
  The difference is that it creates multiple windows on your console (with
  ncurses). It can also use colors while displaying the logfiles (through
  regular expressions), for faster recognition of what is important and what 
  not. It can also filter lines (again with regular expressions). It has 
  interactive menus for editing given regular expressions and deleting and 
  adding windows. One can also have windows with the output of shell scripts 
  and other software. When viewing the output of external software, MultiTail 
  can mimic the functionality of tools like 'watch' and such.
endef

MASTER_SITES = http://www.vanheusden.com/multitail/
DISTFILES = $(GARNAME)-$(GARVERSION).tgz
LICENSE = license.txt

REQUIRED_PKGS = CSWncurses

CONFIGURE_SCRIPTS = 
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

# Adjust path to configuration file and compiler options
PATCHFILES = patch-CSW.diff

# Use provided Solaris Makefile
BUILD_ARGS  = -f makefile.solaris_sunwspro

PROTOTYPE_FILTER  = awk '\
	$$$$3 ~ /multitail.conf.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } \
	 { print }'

include gar/category.mk

install-custom: EXTRA_DOCS = readme.txt thanks.txt manual.html
install-custom: EXTRA_DATA = convert-geoip.pl convert-simple.pl
install-custom: EXTRA_DATA += colors-example.pl colors-example.sh
install-custom: DOCDEST = $(DESTDIR)$(docdir)/$(GARNAME)
install-custom: DATADEST = $(DESTDIR)$(datadir)/$(GARNAME)
install-custom:
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(mandir)/man1
	@ginstall -d $(DESTDIR)$(sysconfdir)
	@ginstall -m 755 $(WORKSRC)/multitail $(DESTDIR)$(bindir)
	@ginstall -m 644 $(WORKSRC)/multitail.1 $(DESTDIR)$(mandir)/man1
	@ginstall -m 644 $(WORKSRC)/multitail.conf \
		$(DESTDIR)$(sysconfdir)/multitail.conf.CSW
	@ginstall -d $(DATADEST) $(DOCDEST)
	@(cd $(WORKSRC); ginstall -m 644 $(EXTRA_DATA) $(DATADEST))
	@(cd $(WORKSRC); ginstall -m 644 $(EXTRA_DOCS) $(DOCDEST))
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
