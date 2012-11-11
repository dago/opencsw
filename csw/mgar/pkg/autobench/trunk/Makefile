NAME = autobench
VERSION = 2.1.2
GARTYPE = v2

DESCRIPTION = Wrapper around httperf which automates the benchmarking process
define BLURB
  Autobench is a simple Perl script for automating the process of
  benchmarking a web server (or for conducting a comparative test of two
  different web servers). The script is a wrapper around  httperf.
  Autobench runs httperf a number of times against each host, increasing
  the number of requested connections per second on each iteration, and
  extracts the significant data from the httperf output, delivering a CSV
  or TSV format file which can be imported directly into a spreadsheet for
  analysis/graphing. 
endef

VENDOR_URL   = http://www.xenoclast.org/autobench/
MASTER_SITES = http://www.xenoclast.org/autobench/downloads/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = LICENCE

# Make the Makefile honor our defaults
PATCHFILES  = 0001-Makefile-only-set-defaults-if-not-explicitly-given.patch
# Adjust config file location paths
PATCHFILES += 0002-man-pages-adjust-default-conf-location.patch

CONFIGURE_SCRIPTS =
TEST_SCRIPTS =

# Override the /usr/local installation defaults, the config is only used
# to pre-populate a user config, so we move it to examples
BINDIR=$(DESTDIR)$(bindir)
MANDIR=$(DESTDIR)$(mandir)/man1
ETCDIR=$(DESTDIR)$(docdir)/$(NAME)/examples
INSTALL_EXPORTS=BINDIR MANDIR ETCDIR 

EXTRA_PAX_ARGS = '-s,ChangeLog$$,changelog,p'

include gar/category.mk

# See above, config is only used as a template
pre-install-modulated:
	gsed -i -e 's,/etc/autobench.conf,$(ETCDIR)/autobench.conf,' \
		$(WORKSRC)/autobench \
		$(WORKSRC)/autobench_admin
	@$(MAKECOOKIE)

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
post-install-modulated: DOCS=ChangeLog
post-install-modulated:
	mkdir -p $(DOCDEST)
	cp $(addprefix $(WORKSRC)/,$(DOCS)) $(DOCDEST)
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
