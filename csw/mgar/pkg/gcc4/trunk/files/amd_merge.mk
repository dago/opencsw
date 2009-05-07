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
AMD_MERGE_TARGETS += merge-fix-links
AMD_MERGE_TARGETS += merge-i386-files
AMD_MERGE_TARGETS += merge-amd64-files

merge-amd: $(AMD_MERGE_TARGETS)
	$(_DBG)$(MAKECOOKIE)

merge-dirs-amd:
	$(_DBG)(ginstall -d $(PKGROOT))
	$(_DBG)(ginstall -d $(PPREFIX)/bin/amd64)
	$(_DBG)(ginstall -d $(PPREFIX)/bin/i386)
	$(_DBG)$(MAKECOOKIE)

## Remove the Hard Links and re-create as files
merge-fix-links:
	@echo "[===== Merging Fixing Hard Links =====]"
	$(_DBG)(cd $(IPREFIX)/bin; grm -f *gcc *c++ g++ gcj gfortran)
	$(_DBG)(cd $(IPREFIX)/bin; \
		gcp i386-pc-solaris2.8-gcc-4.3.3 i386-pc-solaris2.8-gcc)
	$(_DBG)(cd $(IPREFIX)/bin; gcp i386-pc-solaris2.8-gcc-4.3.3 gcc)
	$(_DBG)(cd $(IPREFIX)/bin; \
		gcp i386-pc-solaris2.8-g++ i386-pc-solaris2.8-c++)
	$(_DBG)(cd $(IPREFIX)/bin; gcp i386-pc-solaris2.8-g++ g++)
	$(_DBG)(cd $(IPREFIX)/bin; gcp i386-pc-solaris2.8-g++ c++)
	$(_DBG)(cd $(IPREFIX)/bin; gcp i386-pc-solaris2.8-gcj gcj)
	$(_DBG)(cd $(IPREFIX)/bin; gcp i386-pc-solaris2.8-gfortran gfortran)
	$(_DBG)(cd $(APREFIX)/bin; grm -f *gcc *c++ g++ gcj gfortran)
	$(_DBG)(cd $(APREFIX)/bin; \
		gcp i386-pc-solaris2.10-gcc-4.3.3 i386-pc-solaris2.10-gcc)
	$(_DBG)(cd $(APREFIX)/bin; gcp i386-pc-solaris2.10-gcc-4.3.3 gcc)
	$(_DBG)(cd $(APREFIX)/bin; \
		gcp i386-pc-solaris2.10-g++ i386-pc-solaris2.10-c++)
	$(_DBG)(cd $(APREFIX)/bin; gcp i386-pc-solaris2.10-g++ g++)
	$(_DBG)(cd $(APREFIX)/bin; gcp i386-pc-solaris2.10-g++ c++)
	$(_DBG)(cd $(APREFIX)/bin; gcp i386-pc-solaris2.10-gcj gcj)
	$(_DBG)(cd $(APREFIX)/bin; gcp i386-pc-solaris2.10-gfortran gfortran)
	$(_DBG)$(MAKECOOKIE)

merge-i386-files:
	@echo "[===== Merging isa-i386 =====]"
	$(_DBG)(cd $(I386_BASE); /usr/bin/pax -rw -v $(MPREFIX)/bin $(PKGROOT))
	$(_DBG)(cd $(PPREFIX)/bin; gmv *solaris2* $(PPREFIX)/bin/i386)
	$(_DBG)(cd $(I386_BASE); /usr/bin/pax -rw -v $(MPREFIX)/include $(PKGROOT))
	$(_DBG)(cd $(I386_BASE); /usr/bin/pax -rw -v $(MPREFIX)/info $(PKGROOT))
	$(_DBG)(cd $(I386_BASE); /usr/bin/pax -rw -v $(MPREFIX)/man $(PKGROOT))
	$(_DBG)(cd $(I386_BASE); /usr/bin/pax -rw -v $(MPREFIX)/share $(PKGROOT))
	$(_DBG)(cd $(I386_BASE); /usr/bin/pax -rw -v $(MPREFIX)/lib $(PKGROOT))
	$(_DBG)(cd $(I386_BASE); /usr/bin/pax -rw -v $(MPREFIX)/libexec $(PKGROOT))
	$(_DBG)(cd $(PPREFIX)/lib; gln . 32)
	$(_DBG)$(MAKECOOKIE)

merge-amd64-files:
	@echo "[===== Merging isa-amd64 =====]"
	$(_DBG)(cd $(AMD_BASE); \
		for dir in `gfind . -name "*solaris2\.10*" -type d` ; do \
		/usr/bin/pax -rw -v $$dir $(PKGROOT); done )
	$(_DBG)(cd $(AMD_BASE); /usr/bin/pax -rw -v $(MPREFIX)/lib/amd64 $(PKGROOT))
	$(_DBG)(cd $(APREFIX)/bin; /usr/bin/pax -rw -v * $(PPREFIX)/bin/amd64)
	$(_DBG)(cd $(PPREFIX)/lib; gln amd64 64)
	$(_DBG)$(MAKECOOKIE)

ifeq ($(shell uname -p), i386)
ISAEXEC_DIRS   = /opt/csw/gcc4/bin
ISAEXEC_FILES += /opt/csw/gcc4/bin/gcc
ISAEXEC_FILES += /opt/csw/gcc4/bin/gcov
ISAEXEC_FILES += /opt/csw/gcc4/bin/gccbug
ISAEXEC_FILES += /opt/csw/gcc4/bin/gfortran
ISAEXEC_FILES += /opt/csw/gcc4/bin/c++
ISAEXEC_FILES += /opt/csw/gcc4/bin/g++
ISAEXEC_FILES += /opt/csw/gcc4/bin/cpp
ISAEXEC_FILES += /opt/csw/gcc4/bin/addr2name.awk
ISAEXEC_FILES += /opt/csw/gcc4/bin/gc-analyze
ISAEXEC_FILES += /opt/csw/gcc4/bin/gcjh
ISAEXEC_FILES += /opt/csw/gcc4/bin/gjarsigner
ISAEXEC_FILES += /opt/csw/gcc4/bin/grmic
ISAEXEC_FILES += /opt/csw/gcc4/bin/gjavah
ISAEXEC_FILES += /opt/csw/gcc4/bin/grmid
ISAEXEC_FILES += /opt/csw/gcc4/bin/jcf-dump
ISAEXEC_FILES += /opt/csw/gcc4/bin/gkeytool
ISAEXEC_FILES += /opt/csw/gcc4/bin/grmiregistry
ISAEXEC_FILES += /opt/csw/gcc4/bin/jv-convert
ISAEXEC_FILES += /opt/csw/gcc4/bin/gcj
ISAEXEC_FILES += /opt/csw/gcc4/bin/gij
ISAEXEC_FILES += /opt/csw/gcc4/bin/gserialver
ISAEXEC_FILES += /opt/csw/gcc4/bin/gappletviewer
ISAEXEC_FILES += /opt/csw/gcc4/bin/gcj-dbtool
ISAEXEC_FILES += /opt/csw/gcc4/bin/gjar
ISAEXEC_FILES += /opt/csw/gcc4/bin/gorbd
ISAEXEC_FILES += /opt/csw/gcc4/bin/gtnameserv
ISAEXEC_FILES += /opt/csw/gcc4/bin/gnative2ascii
ISAEXEC_FILES += /opt/csw/gcc4/bin/gnat
ISAEXEC_FILES += /opt/csw/gcc4/bin/gnatls
ISAEXEC_FILES += /opt/csw/gcc4/bin/gnatname
ISAEXEC_FILES += /opt/csw/gcc4/bin/gnatmake
ISAEXEC_FILES += /opt/csw/gcc4/bin/gnatclean
ISAEXEC_FILES += /opt/csw/gcc4/bin/gnatkr
ISAEXEC_FILES += /opt/csw/gcc4/bin/gnatbind
ISAEXEC_FILES += /opt/csw/gcc4/bin/gnatbl
ISAEXEC_FILES += /opt/csw/gcc4/bin/gnatchop
ISAEXEC_FILES += /opt/csw/gcc4/bin/gnatfind
ISAEXEC_FILES += /opt/csw/gcc4/bin/gnatxref
ISAEXEC_FILES += /opt/csw/gcc4/bin/gnatprep
ISAEXEC_FILES += /opt/csw/gcc4/bin/gnatlink
endif
