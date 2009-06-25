# Todo
# * man page doesn't propely format on Solaris. Upstream notified on
#   2009-06-24, intends to work on it, has access to his own Solaris
#   box. In case of a new upstream version, verify whether man page
#   formats properly (right now no formatting works, no paragraphs
#   no headings, no nothing).
GARNAME = autossh
GARVERSION = 1.4b
CATEGORIES = net

DESCRIPTION = Automatically restart SSH sessions and tunnels
define BLURB
  autossh is a program to start a copy of ssh and monitor it, restarting
  it as necessary should it die or stop passing traffic. The idea is from
  rstunnel (Reliable SSH Tunnel), but implemented in C.
endef

MASTER_SITES = http://www.harding.motd.ca/autossh/
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz

TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

CONFIGURE_ARGS = $(DIRPATHS)
NORUNPATH = 1

include gar/category.mk

# Makefile doesn't honor $(DESTDIR) so we have to do it manually
install-custom: DOCDEST=$(DESTDIR)$(docdir)/$(GARNAME)
install-custom: DOCS=CHANGES README
install-custom:
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(mandir)/man1
	@ginstall -d $(DOCDEST)
	@ginstall -d $(DOCDEST)/examples

	@cp $(WORKSRC)/autossh $(DESTDIR)$(bindir)
	@cp $(FILEDIR)/autossh.1 $(DESTDIR)$(mandir)/man1
	@cp $(FILEDIR)/autossh.1.txt $(DOCDEST)
	@cp $(addprefix $(WORKSRC)/,$(DOCS)) $(DOCDEST)
	@cp $(addprefix $(WORKSRC)/,autossh.host rscreen) $(DOCDEST)/examples
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)

	@$(MAKECOOKIE)
