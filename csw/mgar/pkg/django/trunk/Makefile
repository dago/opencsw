GARNAME = django
GARVERSION = 1.0.2
CATEGORIES = lib

DESCRIPTION = high-level Python Web framework
define BLURB
  Django is a high-level Python Web framework that encourages rapid development
  and clean, pragmatic design.

  Developed four years ago by a fast-moving online-news operation, Django was
  designed to handle two challenges: the intensive deadlines of a newsroom and
  the stringent requirements of the experienced Web developers who wrote it. It
  lets you build high-performing, elegant Web applications quickly.
endef

MASTER_SITES = http://www.djangoproject.com/download/$(GARVERSION)/tarball/
DISTFILES  = Django-$(GARVERSION)-final.tar.gz

SPKG_CLASSES = none cswpycompile
ARCHALL = 1

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

WORKSRC = $(WORKDIR)/Django-$(GARVERSION)-final

REQUIRED_PKGS = CSWpython CSWcswclassutils
PREREQUISITE_PKGS = $(REQUIRED_PKGS) CSWpython-devel

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = $(WORKSRC)/setup.py

INSTALL_SCRIPTS = $(WORKSRC)/setup.py
INSTALL_ARGS += --root=$(DESTDIR) --prefix=$(prefix)

TEST_SCRIPTS =

PROTOTYPE_FILTER = awk ' \
  $$$$3 ~/.*\.py$$$$/ { $$$$2 = "cswpycompile" } \
  { print }'

post-install-modulated:
	gfind $(DESTDIR) -type f -name '*.pyc' -exec rm {} \;
	@$(MAKECOOKIE)

# There's a problem that the download URL of the Django source tarball does not
# contain the file name. The browser is being redirected instead. Hard-coding
# the URL and using a custom target to fit the rest of mGAR.
http//www.djangoproject.com/download/$(GARVERSION)/tarball/Django-$(GARVERSION)-final.tar.gz:
	@wget $(WGET_OPTS) -T 30 -c -P $(PARTIALDIR) http://www.djangoproject.com/download/$(GARVERSION)/tarball

include gar/category.mk
