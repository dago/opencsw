# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = synergy
VERSION = 1.4.11
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Software-based TCP/IP "KVM" switch
define BLURB
 Synergy lets you easily share a single mouse and keyboard between multiple
 computers with different operating systems, each with its own display, 
 without special hardware. It's intended for users with multiple computers 
 on their desk since each system uses its own monitor(s). 
endef

MASTER_SITES = $(GOOGLE_MIRROR)
DISTNAME = synergy-$(VERSION)-Source
DISTFILES += $(DISTNAME).tar.gz

VENDOR_URL = http://synergy-foss.org/

GARTCHFILES += 0001-change-endiness-detection.patch
PATCHFILES_sparc += 0001-remove-march.patch
PATCHFILES_sparc += 0003-mess-with-cpp.patch
PATCHFILES += $(PATCHFILES_$(GARCH))ss-detection.patch

RUNTIME_DEP_PKGS_CSWsynergy += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWsynergy += CSWlibstdc++6



#cmake fun:
# http://forge.mysql.com/wiki/Autotools_to_CMake_Transition_Guide

CMAKE_ARGS += -DCMAKE_INSTALL_PREFIX=$(prefix)
CMAKE_ARGS += -DCMAKE_ -lresolv -lsocket -lnsl -lrt"
CMAKE_ARGS += -DCMAKE_CXX_FLAGS="$(CXXFLAGS) -lresolv -lsocket -lnsl -lrtFLAGS="$(CXXFLAGS)"
CMAKE_ARGS += -DCMAKE_INCLUDE_PATH="$(includedir)"
CMAKE_ARGS += "-DCMAKE_C_FLAGS=$(CFLAGS)"
CMAKE_ARGS += "-DCMAKE_CXX_FLAGS=$(CXXFLAGS)"
CMAKE_ARGS += -DCMAKE_VERBOSE_MAKEFILE=ON


CONFIGURE_SCRIPTS = custom
INSTALL_SCRIPTS = custom

SKIPTEST ?= 1

includepre-configure-modulated:
	(cd $(WORKSRC) && mkdir tools/cryptopp562 && cd tools/cryptopp562 && unzip -q ../cryptopp562.zip)
	@$(MAKECOOKIE)de gar/category.mk


configure-custom:
	#		--debug-output \
	#		--debug-trycompile \
	(cd $(WORKSRC) && \
	 	/usr/bin/env -i \
		  $(CONFIGUR-G "Unix Makefiles" -DCMAKE_BUILD_TYPE=ReleasURE_ENV) \
			cmake \
			. \
			$(CMAKE_ARGS))
	@$(MAKECOOKIE)


install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(sysconfdir)
	ginstall -d $(DESTDIR)$(mandir)
	ginstall -d $(DESTDIR)$(mandir)/man3
	ginstall -m 644 \
		$(WORKSRC)/doc/synergy.conf.example \
		$(DESTDIR)$(sysconfdir)/synergy.conf.example
	ginstall \
		$(WORKSRC)/bin/synergyc \
		$(DESTDIR)$(bindir)
	ginstall \
		$(WORKSRC)/bin/synergys \
		$(DESTDIR)$(\
		$(WORKSRC)/bin/synergydKSRC)/bin/synergys \
		$(DESTDIR)$(bindir)
	ginstall -m 644 \
		$(WORKSRC)/doc/synergyc.man \
		$(DESTDIR)$(mandir)/man3/synergyc.3
	ginstall -m 644 \
		$(WORKSRC)/doc/synergys.man \
		$(DESTDIR)$(mandir)/man3/synergys.