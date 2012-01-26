# TODO (release-critical prefixed with !, non release-critical with *)
# * dot seems to put an extraneous header line in png output files
#   -36 3393.7 translate newpath user_shape_0
#   Filed as http://www.opencsw.org/mantis/view.php?id=4276
NAME = scfdot
VERSION = 1.0
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = SMF Dependency Graph Generator
define BLURB
  Solaris 10 features the Service Management Facility (SMF), which starts
  services in dependency order.  Run "man smf" for more information.  scfdot
  reads the service names and dependencies from the Service Configuration
  Facility (SCF) repository and writes a file which the dot program from the
  graphviz package can render into a graph.
endef

VENDOR_URL   = http://hub.opensolaris.org/bin/view/Community+Group+smf/scfdot
MASTER_SITES = http://hub.opensolaris.org/bin/download/Community+Group+smf/scfdot/
DISTFILES    = $(NAME)-$(VERSION).tar.gz

# Only makes sense on Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

LICENSE = CDDL.LICENSE

RUNTIME_DEP_PKGS = CSWgraphviz

CONFIGURE_SCRIPTS =
BUILD_ARGS        = scfdot legend.ps
TEST_SCRIPTS      =
INSTALL_SCRIPTS   = custom

include gar/category.mk

install-custom: DOCS=AUTHORS
install-custom: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
install-custom:
	ginstall -d	$(DOCDEST)/examples
	cp $(WORKSRC)/snv_24_x86.* $(DOCDEST)/examples
	cp $(addprefix $(WORKSRC)/,$(DOCS)) $(DOCDEST)
	cp $(FILEDIR)/README.CSW $(DOCDEST)

	@# We place the scfdot binary in libexec and instead put a
	@# readily usable wrapper in bindir
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(libexecdir)
	ginstall -m755 $(FILEDIR)/smfdepgraph $(DESTDIR)$(bindir)
	ginstall -m755  $(WORKSRC)/scfdot $(DESTDIR)$(libexecdir)

	@# smfdepgraph includes a legend which we also ship
	ginstall -Dm644 $(WORKSRC)/legend.ps \
		$(DESTDIR)$(datadir)/$(NAME)/legend.ps
	gsed -i -e 's,legend.ps,$(datadir)/$(NAME)/legend.ps,' \
		$(DOCDEST)/examples/snv_24_x86.dot
	@$(MAKECOOKIE)

# Install changelog.CSW
post-merge: $(foreach P,$(_PKG_SPECS),install-changelog-$P)
install-changelog-%:
	ginstall -D $(FILEDIR)/changelog.CSW \
		$(PKGROOT)$(docdir)/$(call catalogname,$*)/changelog.CSW
	@$(MAKECOOKIE)
