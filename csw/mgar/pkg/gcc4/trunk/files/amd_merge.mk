ifeq ($(AMD_DEBUG),)
	_DBG=@
else
	_DBG=
endif   

AMD_BASE  = $(WORKROOTDIR)/install-isa-i386-5.10-i386/
I386_BASE = $(WORKROOTDIR)/install-isa-i386-5.8-i386/
MPREFIX   = opt/csw/gcc4
APREFIX   = $(AMD_BASE)/$(MPREFIX)
IPREFIX   = $(I386_BASE)/$(MPREFIX)
PPREFIX   = $(PKGROOT)/$(MPREFIX)

AMD_MERGE_TARGETS  = merge-dirs-amd
AMD_MERGE_TARGETS += merge-i386-files
AMD_MERGE_TARGETS += merge-amd64-files

merge-amd: $(AMD_MERGE_TARGETS)
	$(_DBG)$(MAKECOOKIE)

merge-dirs-amd:
	$(_DBG)(ginstall -d $(PKGROOT))
	$(_DBG)(ginstall -d $(PPREFIX)/bin/amd64)
	$(_DBG)(ginstall -d $(PPREFIX)/bin/i386)
	$(_DBG)$(MAKECOOKIE)

merge-i386-files:
	@echo "[===== Merging isa-i386 =====]"
	$(_DBG)(cd $(I386_BASE); /usr/bin/pax -rw -v $(MPREFIX)/bin $(PKGROOT))
	$(_DBG)(cd $(IPREFIX)/bin; /usr/bin/pax -rw -v *solaris2* $(PPREFIX)/bin/amd64)
	$(_DBG)(cd $(I386_BASE); /usr/bin/pax -rw -v $(MPREFIX)/include $(PKGROOT))
	$(_DBG)(cd $(I386_BASE); /usr/bin/pax -rw -v $(MPREFIX)/info $(PKGROOT))
	$(_DBG)(cd $(I386_BASE); /usr/bin/pax -rw -v $(MPREFIX)/man $(PKGROOT))
	$(_DBG)(cd $(I386_BASE); /usr/bin/pax -rw -v $(MPREFIX)/share $(PKGROOT))
	$(_DBG)(cd $(I386_BASE); /usr/bin/pax -rw -v $(MPREFIX)/lib $(PKGROOT))
	$(_DBG)(cd $(I386_BASE); /usr/bin/pax -rw -v $(MPREFIX)/libexec $(PKGROOT))
	$(_DBG)$(MAKECOOKIE)

merge-amd64-files:
	@echo "[===== Merging isa-amd64 =====]"
	$(_DBG)(cd $(AMD_BASE); \
		for dir in `gfind . -name "*solaris2\.10*" -type d` ; do \
		/usr/bin/pax -rw -v $$dir $(PKGROOT); done )
	$(_DBG)(cd $(AMD_BASE); /usr/bin/pax -rw -v $(MPREFIX)/lib/amd64 $(PKGROOT))
	$(_DBG)(cd $(APREFIX)/bin; /usr/bin/pax -rw -v * $(PPREFIX)/bin/amd64)
	$(_DBG)$(MAKECOOKIE)

ifeq ($(shell uname -p), i386)
EXTRA_PKGFILES_CSWgcc4core  = l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gcc
EXTRA_PKGFILES_CSWgcc4core += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/cpp

EXTRA_PKGFILES_CSWgcc4g++  = l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/c++
EXTRA_PKGFILES_CSWgcc4g++ += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/g++

EXTRA_PKGFILES_CSWgcc4gfortran = l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gfortran

EXTRA_PKGFILES_CSWgcc4java  = l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gcj
EXTRA_PKGFILES_CSWgcc4java += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gcov
EXTRA_PKGFILES_CSWgcc4java += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gccbug
EXTRA_PKGFILES_CSWgcc4java += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/addr2name.awk
EXTRA_PKGFILES_CSWgcc4java += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gc-analyze
EXTRA_PKGFILES_CSWgcc4java += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gcjh
EXTRA_PKGFILES_CSWgcc4java += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gjarsigner
EXTRA_PKGFILES_CSWgcc4java += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/grmic
EXTRA_PKGFILES_CSWgcc4java += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gjavah
EXTRA_PKGFILES_CSWgcc4java += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/grmid
EXTRA_PKGFILES_CSWgcc4java += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/jcf-dump
EXTRA_PKGFILES_CSWgcc4java += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gkeytool
EXTRA_PKGFILES_CSWgcc4java += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/grmiregistry
EXTRA_PKGFILES_CSWgcc4java += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/jv-convert
EXTRA_PKGFILES_CSWgcc4java += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gij
EXTRA_PKGFILES_CSWgcc4java += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gnative2ascii
EXTRA_PKGFILES_CSWgcc4java += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gserialver
EXTRA_PKGFILES_CSWgcc4java += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gappletviewer
EXTRA_PKGFILES_CSWgcc4java += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gcj-dbtool
EXTRA_PKGFILES_CSWgcc4java += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gjar
EXTRA_PKGFILES_CSWgcc4java += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gorbd
EXTRA_PKGFILES_CSWgcc4java += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gtnameserv

EXTRA_PKGFILES_CSWgcc4ada  = l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gnat
EXTRA_PKGFILES_CSWgcc4ada += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gnatbind
EXTRA_PKGFILES_CSWgcc4ada += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gnatbl
EXTRA_PKGFILES_CSWgcc4ada += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gnatchop
EXTRA_PKGFILES_CSWgcc4ada += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gnatclean
EXTRA_PKGFILES_CSWgcc4ada += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gnatfind
EXTRA_PKGFILES_CSWgcc4ada += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gnatkr
EXTRA_PKGFILES_CSWgcc4ada += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gnatlink
EXTRA_PKGFILES_CSWgcc4ada += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gnatls
EXTRA_PKGFILES_CSWgcc4ada += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gnatmake
EXTRA_PKGFILES_CSWgcc4ada += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gnatname
EXTRA_PKGFILES_CSWgcc4ada += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gnatprep
EXTRA_PKGFILES_CSWgcc4ada += l none /opt/csw/bin/isaexec=/opt/csw/gcc4/bin/gnatxref
endif
