GARNAME = tightvnc
GARVERSION = 1.3.10
CATEGORIES = utils

DESCRIPTION = TightVNC server is a free remote control package derived from the popular VNC software
define BLURB
endef

SF_PROJ = vnc-tight
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION)_unixsrc.tar.bz2
DISTFILES += vncservers

PACKAGES = CSWvncs
CATALOGNAME = vncserver

SPKG_SOURCEURL = http://www.tightvnc.org/

REQUIRED_PKGS = CSWjpeg CSWtcpwrap

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_USE_SF = 1
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=14067
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*)_unixsrc.tar.bz2

DISTNAME = vnc_unixsrc

# Use tightvnc.spec

EXTRA_DEFINES = -DUSE_LIBWRAP=1
EXTRA_INCLUDE = $(CFLAGS)
LOCAL_LDFLAGS = $(LINKER_FLAGS)
BUILD_OVERRIDE_DIRS = EXTRA_DEFINES EXTRA_INCLUDE LOCAL_LDFLAGS

CONFIGURE_SCRIPTS = $(WORKSRC)/Imakefile Xvnc
CONFIGURE_ARGS = -a

BUILD_SCRIPTS = vnc Xvnc

# VNC doesn't come with tests
TEST_SCRIPTS =

INSTALL_SCRIPTS = vnc

include gar/category.mk

pre-configure-modulated:
	perl -pi -e "s|/usr/local/vnc/classes|$(datadir)/vnc/classes|" $(WORKSRC)/vncserver
	$(MAKECOOKIE)

configure-Xvnc:
	banner "Config Xvnc"
	perl -pi -e "s|^(\s*make)\s*$$|\1 CC=$(CC)|" $(WORKSRC)/Xvnc/configure
	cd $(WORKSRC)/Xvnc && ./configure
	$(MAKECOOKIE)

build-vnc:
	banner "Build VNC"
        #$(BUILD_ENV) $(MAKE) $(PARALLELMFLAGS) $(foreach TTT,$(BUILD_OVERRIDE_DIRS),$(TTT)="$($(TTT))") -C $* $(BUILD_ARGS)
	cd $(WORKSRC) && $(BUILD_ENV) $(MAKE) $(PARALLELMFLAGS) $(foreach TTT,$(BUILD_OVERRIDE_DIRS),$(TTT)="$($(TTT))") World
	$(MAKECOOKIE)

build-Xvnc: configure-Xvnc
	banner "Build Xvnc"
	cd $(WORKSRC)/Xvnc && $(MAKE) EXTRA_LIBRARIES="-lwrap" EXTRA_DEFINES="-DUSE_LIBWRAP=1"

#xmkmf -a
#make CDEBUGFLAGS="$RPM_OPT_FLAGS" World
#cd Xvnc
#./configure
#make EXTRA_LIBRARIES="-lwrap -lnss_nis" CDEBUGFLAGS="$RPM_OPT_FLAGS" \
#     EXTRA_DEFINES="-DUSE_LIBWRAP=1"

install-vnc:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(mandir)/man1
	(cd $(WORKSRC); ./vncinstall $(DESTDIR)$(bindir) $(DESTDIR)$(mandir))
	ginstall -d $(DESTDIR)$(datadir)/vnc
	(cd $(WORKSRC); cp -pR classes $(DESTDIR)$(datadir)/vnc)
	#mkdir -p %{buildroot}/etc/rc.d/init.d
	#install -m755 vncserver.init %{buildroot}/etc/rc.d/init.d/vncserver
	ginstall -m 644 $(WORKDIR)/vncservers $(DESTDIR)$(sysconfdir)/vncservers

	

# Build

#patch < vnc-xclients.patch

#xmkmf -a
#make CDEBUGFLAGS="$RPM_OPT_FLAGS" World
#cd Xvnc
#./configure
#make EXTRA_LIBRARIES="-lwrap -lnss_nis" CDEBUGFLAGS="$RPM_OPT_FLAGS" \
#     EXTRA_DEFINES="-DUSE_LIBWRAP=1"




# Install

#rm -rf %{buildroot}

#mkdir -p %{buildroot}%{_bindir}
#mkdir -p %{buildroot}%{_mandir}/man1
#./vncinstall %{buildroot}%{_bindir} %{buildroot}%{_mandir}

#mkdir -p %{buildroot}%{_datadir}/vnc
#cp -aR classes %{buildroot}%{_datadir}/vnc

#strip %{buildroot}%{_bindir}/* || :

#mkdir -p %{buildroot}/etc/rc.d/init.d
#install -m755 vncserver.init %{buildroot}/etc/rc.d/init.d/vncserver
#
#mkdir -p %{buildroot}/etc/sysconfig
#cat > %{buildroot}/etc/sysconfig/vncservers << EOF
# The VNCSERVERS variable is a list of display:user pairs.
#
# Uncomment the line below to start a VNC server on display :1
# as my 'myusername' (adjust this to your own).  You will also
# need to set a VNC password; run 'man vncpasswd' to see how
# to do that.  
#
# DO NOT RUN THIS SERVICE if your local area network is
# untrusted!  For a secure way of using VNC, see
# <URL:http://www.uk.research.att.com/vnc/sshvnc.html>.

# VNCSERVERS="1:myusername"
#EOF
#chmod 644 %{buildroot}/etc/sysconfig/vncservers

