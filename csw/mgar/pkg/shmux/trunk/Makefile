# Todo
# * Review patches from http://cr.opensolaris.org/~lilyli/shmux/
NAME = shmux
VERSION = 1.0.2
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Executes the same command on many hosts in parallel
define BLURB
  shmux is program for executing the same command on many hosts in
  parallel. For each target, a child process is spawned by shmux, and a
  shell on the target obtained one of the supported methods: rsh, ssh, or
  sh. The output produced by the children is received by shmux and either
  (optionally) output in turn to the user using an easy to read format, or
  written to files for later processing making it well suited for use in
  scripts.
endef

SPKG_SOURCEURL = http://web.taranis.org/shmux/
MASTER_SITES = http://web.taranis.org/shmux/dist/
DISTFILES  = $(NAME)-$(VERSION).tgz

RUNTIME_DEP_PKGS = CSWpcrert

# We define upstream file regex so we can be notifed of new upstream software 
# release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tgz

LICENSE = LICENSE

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
