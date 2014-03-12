NAME = cgit
VERSION = 0.10.1
GARTYPE = v2

DESCRIPTION = Web front-end for Git

MASTER_SITES += http://git.zx2c4.com/cgit/snapshot/
DISTFILES += $(NAME)-$(VERSION).tar.xz

MASTER_SITES += https://git-core.googlecode.com/files/
DISTFILES += git-1.8.3.tar.gz

DISTFILES += cgit.conf
EXPANDVARS += cgit.conf

# The existing one ends at Solaris 9, we added Solaris 10 and 11
DISTFILES += config.mak.uname

DISTFILES += httpd-cgit.conf.CSW
DISTFILES += cgitrc.CSW

PATCHFILES += 0001-Add-substitute-for-timegm-on-Solaris.patch

PACKAGES += CSWcgit
SPKG_DESC_CSWcgit = Web front-end for Git
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWcgit += CSWlibintl8
RUNTIME_DEP_PKGS_CSWcgit += CSWlibz1
RUNTIME_DEP_PKGS_CSWcgit += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWcgit += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWcgit += CSWliblua5-2
RUNTIME_DEP_PKGS_CSWcgit += CSWperl

# This may be used with any other webserver, just preconfigured for apache
CHECKPKG_OVERRIDES_CSWcgit += missing-dependency|CSWapache2

PRESERVECONF += $(sysconfdir)/cgitrc
PRESERVECONF += $(prefix)/apache2/etc/extra/httpd-cgit.conf

GARCOMPILER = GNU

# There is no configure step
CONFIGURE_SCRIPTS = 

BUILD_ARGS += V=1

TEST_TARGET = test
# Tetsuite has major problems on this platform due to shell and calling conventions
SKIPTEST ?= 1

INSTALL_ENV_PATH = /opt/csw/gnu:$(PATH)

# pdf-doc does not work yet
INSTALL_ARGS += install install-man install-html

include gar/category.mk

post-extract:
	@# Link in GIT
	rmdir $(WORKSRC)/git
	mv $(WORKDIR)/git-1.8.3 $(WORKSRC)/git
	cp $(WORKDIR)/config.mak.uname $(WORKSRC)/git/config.mak.uname
	@$(MAKECOOKIE)

post-patch:
	@# EXPANDVARS is done at patch phase
	cp $(WORKDIR)/cgit.conf $(WORKSRC)/cgit.conf
	@$(MAKECOOKIE)

post-install:
	ginstall -D $(WORKDIR)/cgitrc.CSW $(DESTDIR)$(sysconfdir)/cgitrc.CSW
	ginstall -D $(WORKDIR)/httpd-cgit.conf.CSW $(DESTDIR)$(prefix)/apache2/etc/extra/httpd-cgit.conf.CSW
	mkdir -p $(DESTDIR)$(prefix)/apache2/share/htdocs
	ln -s ../../../share/www/cgit/htdocs $(DESTDIR)$(prefix)/apache2/share/htdocs/cgit
	mkdir -p $(DESTDIR)$(prefix)/apache2/share/cgi-bin
	ln -s ../../../share/www/cgit/cgi-bin $(DESTDIR)$(prefix)/apache2/share/cgi-bin/cgit
	@$(MAKECOOKIE)
