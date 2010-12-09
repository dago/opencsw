# TODO (release-critical prefixed with !, non release-critical with *)
# ! As soon as AUTOSSH_PORT is set, the invocation of autossh will
#   pass wrong options to ssh.
# * man page doesn't properly format on Solaris. Upstream notified on
#   2009-06-24, intends to work on it, has access to his own Solaris
#   box. In case of a new upstream version, verify whether man page
#   formats properly (for now see install-preformatted-manpage: below).
# * DESTDIR and --with-ssh handling could be fixed. See the Debian
#   patch tracker: http://patch-tracker.debian.org/package/autossh/1.4b-1
GARNAME = autossh
GARVERSION = 1.4b
CATEGORIES = net

DESCRIPTION = Automatically restart SSH sessions and tunnels
define BLURB
  autossh is a program to start a copy of ssh and monitor it, restarting
  it as necessary should it die or stop passing traffic. The idea is from
  rstunnel (Reliable SSH Tunnel), but implemented in C.
endef

VENDOR_URL   = http://www.harding.motd.ca/autossh/
MASTER_SITES = http://www.harding.motd.ca/autossh/
DISTFILES    = $(GARNAME)-$(GARVERSION).tgz

TEST_SCRIPTS =
INSTALL_SCRIPTS = custom preformatted-manpage

CONFIGURE_ARGS = $(DIRPATHS)
NORUNPATH = 1

# --with-ssh=/usr/bin/ssh doesn't work -> checking for ssh... /opt/csw/bin/ssh
BUILD_ARGS = 'SSH=/usr/bin/ssh'

# autossh doesn't ship a license and can't find one on $VENDOR_URL either
CHECKPKG_OVERRIDES_CSWautossh += license-missing

include gar/category.mk

# Makefile install target doesn't honor $(DESTDIR) so we install manually
install-custom: DOCDEST=$(DESTDIR)$(docdir)/$(GARNAME)
install-custom: DOCS=CHANGES README
install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(prefix)/libexec/autossh
	ginstall -d $(DOCDEST)
	ginstall -d $(DOCDEST)/examples

	ginstall -m 755 $(FILEDIR)/autossh $(DESTDIR)$(bindir)/autossh
	cp $(WORKSRC)/autossh $(DESTDIR)$(prefix)/libexec/autossh
	cp $(addprefix $(WORKSRC)/,$(DOCS)) $(DOCDEST)
	cp $(addprefix $(WORKSRC)/,autossh.host rscreen) $(DOCDEST)/examples
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)

	@$(MAKECOOKIE)

# The autossh man page comes with macros from the mdoc macro package which
# Solaris man doesn't handle by default. As a workaround we ship a pre-
# formatted man page as catman page. For some background see
#   http://www.opencsw.org/mantis/view.php?id=4280
# or the very enlightening roff(7) introduction to the whole roff stack.
install-preformatted-manpage:
	ginstall -d $(DESTDIR)$(mandir)/catman1
	groff -m doc -Tascii -P-cuob $(WORKSRC)/autossh.1 > \
		$(DESTDIR)$(mandir)/catman1/autossh.1
	@$(MAKECOOKIE)
