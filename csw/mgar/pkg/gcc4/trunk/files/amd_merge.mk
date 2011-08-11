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
		gcp i386-pc-solaris2.8-gcc-4.4.3 i386-pc-solaris2.8-gcc)
	$(_DBG)(cd $(IPREFIX)/bin; gcp i386-pc-solaris2.8-gcc-4.4.3 gcc)
	$(_DBG)(cd $(IPREFIX)/bin; \
		gcp i386-pc-solaris2.8-g++ i386-pc-solaris2.8-c++)
	$(_DBG)(cd $(IPREFIX)/bin; gcp i386-pc-solaris2.8-g++ g++)
	$(_DBG)(cd $(IPREFIX)/bin; gcp i386-pc-solaris2.8-g++ c++)
	$(_DBG)(cd $(IPREFIX)/bin; gcp i386-pc-solaris2.8-gcj gcj)
	$(_DBG)(cd $(IPREFIX)/bin; gcp i386-pc-solaris2.8-gfortran gfortran)
	$(_DBG)(cd $(APREFIX)/bin; grm -f *gcc *c++ g++ gcj gfortran)
	$(_DBG)(cd $(APREFIX)/bin; \
		gcp i386-pc-solaris2.10-gcc-4.4.3 i386-pc-solaris2.10-gcc)
	$(_DBG)(cd $(APREFIX)/bin; gcp i386-pc-solaris2.10-gcc-4.4.3 gcc)
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
ISAEXEC_DIRS   = $(bindir)
ISAEXEC_FILES += $(bindir)/gcc
ISAEXEC_FILES += $(bindir)/gcov
ISAEXEC_FILES += $(bindir)/gccbug
ISAEXEC_FILES += $(bindir)/gfortran
ISAEXEC_FILES += $(bindir)/c++
ISAEXEC_FILES += $(bindir)/g++
ISAEXEC_FILES += $(bindir)/cpp
ISAEXEC_FILES += $(bindir)/addr2name.awk
ISAEXEC_FILES += $(bindir)/gc-analyze
ISAEXEC_FILES += $(bindir)/gcjh
ISAEXEC_FILES += $(bindir)/gjarsigner
ISAEXEC_FILES += $(bindir)/grmic
ISAEXEC_FILES += $(bindir)/gjavah
ISAEXEC_FILES += $(bindir)/grmid
ISAEXEC_FILES += $(bindir)/jcf-dump
ISAEXEC_FILES += $(bindir)/gkeytool
ISAEXEC_FILES += $(bindir)/grmiregistry
ISAEXEC_FILES += $(bindir)/jv-convert
ISAEXEC_FILES += $(bindir)/gcj
ISAEXEC_FILES += $(bindir)/gij
ISAEXEC_FILES += $(bindir)/gserialver
ISAEXEC_FILES += $(bindir)/gappletviewer
ISAEXEC_FILES += $(bindir)/gcj-dbtool
ISAEXEC_FILES += $(bindir)/gjar
ISAEXEC_FILES += $(bindir)/gorbd
ISAEXEC_FILES += $(bindir)/gtnameserv
ISAEXEC_FILES += $(bindir)/gnative2ascii
ISAEXEC_FILES += $(bindir)/gnat
ISAEXEC_FILES += $(bindir)/gnatls
ISAEXEC_FILES += $(bindir)/gnatname
ISAEXEC_FILES += $(bindir)/gnatmake
ISAEXEC_FILES += $(bindir)/gnatclean
ISAEXEC_FILES += $(bindir)/gnatkr
ISAEXEC_FILES += $(bindir)/gnatbind
ISAEXEC_FILES += $(bindir)/gnatbl
ISAEXEC_FILES += $(bindir)/gnatchop
ISAEXEC_FILES += $(bindir)/gnatfind
ISAEXEC_FILES += $(bindir)/gnatxref
ISAEXEC_FILES += $(bindir)/gnatprep
ISAEXEC_FILES += $(bindir)/gnatlink
endif
