GARNAME = tightvnc
GARVERSION = 1.3.10
CATEGORIES = utils

DESCRIPTION = TightVNC server is a free remote control package derived from the popular VNC software

define BLURB
  TightVNC is a free remote control software package. With TightVNC, you can see
  the desktop of a remote machine and control it with your local mouse and
  keyboard, just like you would do it sitting in the front of that computer.
endef

SF_PROJ = vnc-tight
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION)_unixsrc.tar.bz2
DISTFILES += vncservers
DISTFILES += cswvncserver
PACKAGES = CSWvncs CSWvncv
CATALOGNAME_CSWvncs = vncserver
CATALOGNAME_CSWvncv = vncviewer
SPKG_SOURCEURL = http://www.tightvnc.org/
UPSTREAM_USE_SF = 1
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=14067
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)_unixsrc.tar.bz2
DISTNAME = vnc_unixsrc
PKGFILES_CSWvncv  = $(bindir)/vncviewer
PKGFILES_CSWvncv += $(mandir)/man1/vncviewer\.1
SPKG_DESC_CSWvncs = TightVNC server
SPKG_DESC_CSWvncv = TightVNC viewer

MIGRATE_FILES_CSWvncs = vncservers
INITSMF = /etc/opt/csw/init.d/cswvncserver

REQUIRED_PKGS  = CSWbash
REQUIRED_PKGS += CSWjpeg
REQUIRED_PKGS += CSWlibice
REQUIRED_PKGS += CSWlibsm
REQUIRED_PKGS += CSWlibxext
REQUIRED_PKGS += CSWtcpwrap
REQUIRED_PKGS += CSWzlib

PREREQUISITE_PKGS = $(REQUIRED_PKGS)

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw

EXTRA_DEFINES = -DUSE_LIBWRAP=1
EXTRA_INC = /usr/openwin/share/include/X11
EXTRA_INCLUDES = $(EXTRA_INC)
EXTRA_LDFLAGS = /opt/csw/lib
LOCAL_LDFLAGS = $(LINKER_FLAGS)
EXTRA_LIBRARIES = -lwrap -lsocket
BUILD_OVERRIDE_DIRS = EXTRA_DEFINES EXTRA_INCLUDES LOCAL_LDFLAGS EXTRA_LIBRARIES
CONFIGURE_SCRIPTS = vnc
BUILD_SCRIPTS = vnc
TEST_SCRIPTS =
INSTALL_SCRIPTS = vnc
PATCHFILES  = 0001-Sun-compiler-in-sun.cf.patch
PATCHFILES += 0002-GNU-make-by-default.patch
PATCHFILES += 0003-libdix.a-after-libos.a.patch
PATCHFILES += 0001-Force-the-use-of-libwrap.patch

include gar/category.mk

pre-configure-modulated:
	perl -pi -e "s|/usr/local/vnc/classes|$(datadir)/vnc/classes|" $(WORKSRC)/vncserver
	@$(MAKECOOKIE)

configure-vnc:
	(cd $(WORKSRC) && $(CONFIGURE_ENV) xmkmf)
	@$(MAKECOOKIE)

build-vnc:
	(cd $(WORKSRC) && $(BUILD_ENV) \
		EXTRA_INCLUDES="-I/opt/csw/include" \
		EXTRA_DEFINES="$(CFLAGS)" \
		LOCAL_LDFLAGS="-L/opt/csw/lib" \
		gmake World)
	(cd $(WORKSRC)/Xvnc && $(CONFIGURE_ENV) \
		EXTRA_LIBRARIES="-lwrap -lsocket" \
		EXTRA_DEFINES="-DUSE_LIBWRAP=1 $(CFLAGS)" \
		EXTRA_INCLUDES="-I/opt/csw/include" \
		LOCAL_LDFLAGS="-L/opt/csw/lib" \
		./configure)
	(cd $(WORKSRC)/Xvnc && $(BUILD_ENV) \
		EXTRA_LIBRARIES="-lwrap -lsocket" \
		EXTRA_DEFINES="-DUSE_LIBWRAP=1 $(CFLAGS)" \
		LOCAL_LDFLAGS="-L/opt/csw/lib" \
		EXTRA_INCLUDES="-I/opt/csw/include" \
		$(MAKE))
	@$(MAKECOOKIE)

install-vnc:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(mandir)/man1
	(cd $(WORKSRC); ./vncinstall $(DESTDIR)$(bindir) $(DESTDIR)$(mandir))
	ginstall -d $(DESTDIR)$(datadir)/vnc
	(cd $(WORKSRC); cp -pR classes $(DESTDIR)$(datadir)/vnc)
	#mkdir -p %{buildroot}/etc/rc.d/init.d
	#install -m755 vncserver.init %{buildroot}/etc/rc.d/init.d/vncserver
	ginstall -d $(DESTDIR)$(sysconfdir)/vncservers
	ginstall -m 644 $(WORKDIR)/vncservers $(DESTDIR)$(sysconfdir)/vncservers
	ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 644 $(FILEDIR)/cswvncserver $(DESTDIR)/etc/opt/csw/init.d
	ginstall -d -m 755 $(DESTDIR)$(libexecdir)
	mv $(DESTDIR)$(bindir)/vncserver $(DESTDIR)$(libexecdir)
	ginstall -m 755 \
		$(FILEDIR)/vncserver-wrapper.sh \
		$(DESTDIR)$(bindir)/vncserver
	@$(MAKECOOKIE)
