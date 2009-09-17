# TODO/Issues
# - Submit 001- (DESTDIR) and 002- (man page) patches upstream
# - What about --logdir perms? Any other special perms required?
GARNAME = sudosh2
GARVERSION = 1.0.2
CATEGORIES = apps

DESCRIPTION = Extensive auditing of user shell usage
define BLURB
  sudosh can be used as a default login shell or a filter that takes
  advantage of PTY devices in order to sit between the user's keyboard and
  a program, in this case a shell. It was designed specifically to be used
  in conjunction with sudo, and allows the execution of a root or
  application shell with logging. It is basically a VCR and will record
  root shell sessions and also has the ability to play back the sessions
  as they were originally recorded. It records all input/output, keyboard
  input, and timing information so that the session can be played back in
  the original format. 

  Sudosh2 is a fork of sudosh (by Douglas Hanks).
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw

SAMPLECONF = $(sysconfdir)/sudosh.conf

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-logdir=$(localstatedir)/sudosh

# No tests available
TEST_SCRIPTS = 

# Installation for sudosh.conf doesn't honor DESTDIR
PATCHFILES  = 001-installsudosh.conf-destdir.patch
# Man pages contain an empty line that becomes a full first blank page
PATCHFILES += 002-strip-man-page-blank.patch
# The binary is called sudosh (not sudosh2 - only leave sudosh2 in the title)
PATCHFILES += 003-adjust-sudosh-man-binary-name.patch

include gar/category.mk

pre-configure-modulated:
	# -errwarn bails out with implicit function declarations
	# http://lists.opencsw.org/pipermail/maintainers/2009-September/004159.html
	#perl -pi -e 's|-Werror|-errwarn|g' \
	perl -pi -e 's|-Werror||g' \
		$(WORKSRC)/src/Makefile.in \
		$(WORKSRC)/Makefile.in \
		$(WORKSRC)/configure
	@$(MAKECOOKIE)

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated: DOCS=AUTHORS NEWS README
post-install-modulated:
	ginstall -d $(DESTDIR)$(localstatedir)/sudosh
	ginstall -d $(DOCDEST)
	cp $(addprefix $(WORKSRC)/,$(DOCS)) $(DOCDEST)
	cp $(WORKSRC)/ChangeLog $(DOCDEST)/changelog
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
