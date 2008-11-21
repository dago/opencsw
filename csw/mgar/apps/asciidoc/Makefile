GARNAME = asciidoc
GARVERSION = 8.2.5
CATEGORIES = apps

DESCRIPTION = Text based document generation
define BLURB
  AsciiDoc is a text document format for writing short documents,
  articles, books and UNIX man pages. AsciiDoc files can be translated
  to HTML and DocBook markups using the asciidoc(1) command.
endef

MASTER_SITES = http://www.methods.co.nz/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWasciidoc,depend)

PATCHFILES = blastwave-locations.patch

# No configure there, just a Python script
CONFIGURE_SCRIPTS = 

BUILD_SCRIPTS =

TEST_SCRIPTS =

CONFDIR=$(DESTDIR)$(sysconfdir)/$(GARNAME)
BINDIR=$(DESTDIR)$(bindir)
MANDIR=$(DESTDIR)$(mandir)
VIM_CONFDIR=$(DESTDIR)$(sharestatedir)/vim/vim71

INSTALL_OVERRIDE_DIRS = CONFDIR BINDIR MANDIR VIM_CONFDIR

INSTALL_SCRIPTS = custom

include ../category.mk

# The install.sh is so crappy I don't even bother writing a patch
# Pull in the whole procedure...
install-custom:
	@ginstall $(WORKSRC)/asciidoc.py $(BINDIR)/asciidoc
	@ginstall $(WORKSRC)/a2x $(BINDIR)/a2x
	@ginstall -d $(MANDIR)/man1
	@ginstall $(WORKSRC)/doc/*.1 $(MANDIR)/man1
	@ginstall -d $(CONFDIR)/filters
	@ginstall -d $(CONFDIR)/docbook-xsl
	@ginstall -d $(CONFDIR)/stylesheets
	@ginstall -d $(CONFDIR)/javascripts
	@ginstall -d $(CONFDIR)/images/icons/callouts
	@ginstall -m 644 $(WORKSRC)/*.conf $(CONFDIR)
	@ginstall $(WORKSRC)/filters/*.py $(CONFDIR)/filters
	@ginstall -m 644 $(WORKSRC)/filters/*.conf $(CONFDIR)/filters
	@ginstall -m 644 $(WORKSRC)/docbook-xsl/*.xsl $(CONFDIR)/docbook-xsl
	@ginstall -m 644 $(WORKSRC)/stylesheets/*.css $(CONFDIR)/stylesheets
	@ginstall -m 644 $(WORKSRC)/javascripts/*.js $(CONFDIR)/javascripts
	@ginstall -m 644 $(WORKSRC)/images/icons/callouts/* $(CONFDIR)/images/icons/callouts
	@ginstall -m 644 $(WORKSRC)/images/icons/README $(WORKSRC)/images/icons/*.png $(CONFDIR)/images/icons
	
	@ginstall -d $(VIM_CONFDIR)/syntax
	@ginstall -m 644 $(WORKSRC)/vim/syntax/asciidoc.vim \
		$(VIM_CONFDIR)/syntax/asciidoc.vim
	@ginstall -d $(VIM_CONFDIR)/ftdetect
	@ginstall -m 644 $(WORKSRC)/vim/ftdetect/asciidoc_filetype.vim \
		$(VIM_CONFDIR)/ftdetect/asciidoc_filetype.vim

