###  Package Section  ###
PACKAGES  = CSWgcc4ada
CATALOGNAME_CSWgcc4ada        = gcc4ada
SPKG_DESC_CSWgcc4ada        = GNU C ADA Compiler
PKGFILES_CSWgcc4ada  = $(libexecdir)/.*gnat1
PKGFILES_CSWgcc4ada += $(libdir)/.*libgnat.*a
PKGFILES_CSWgcc4ada += $(libdir)/.*libgnarl.*a
PKGFILES_CSWgcc4ada += .*/gcc4/.*/adalib/.*
PKGFILES_CSWgcc4ada += .*/gcc4/.*/adainclude/.*
PKGFILES_CSWgcc4ada += .*/gcc4/info/.*gnat.*
PKGFILES_CSWgcc4ada += $(bindir)/gnat(?!ive).*
RUNTIME_DEP_PKGS_CSWgcc4ada = CSWgcc4adart
RUNTIME_DEP_PKGS_CSWgcc4ada += CSWlibmpfr4
RUNTIME_DEP_PKGS_CSWgcc4ada += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgcc4ada += CSWlibgmp10

PACKAGES += CSWgcc4adart
CATALOGNAME_CSWgcc4adart      = gcc4adart
SPKG_DESC_CSWgcc4adart      = GNU C ADA Compiler Run Time
PKGFILES_CSWgcc4adart  = $(libdir)/.*libgnat.*\.so.*
PKGFILES_CSWgcc4adart += $(libdir)/.*libgnarl.*\.so.*
RUNTIME_DEP_PKGS_CSWgcc4adart       = CSWgcc4corert

PACKAGES += CSWgcc4core
CATALOGNAME_CSWgcc4core       = gcc4core
SPKG_DESC_CSWgcc4core       = GNU C Compiler
RUNTIME_DEP_PKGS_CSWgcc4core = CSWgcc4corert CSWbinutils
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibmpfr4
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgcc4core += CSWlibgmp10

PACKAGES += CSWgcc4corert
CATALOGNAME_CSWgcc4corert     = gcc4corert
SPKG_DESC_CSWgcc4corert     = GNU C Compiler Run Time
PKGFILES_CSWgcc4corert  = $(libdir)/.*libgcc_s.*\.so.*
PKGFILES_CSWgcc4corert += $(libdir)/.*libgomp.*\.so.*
PKGFILES_CSWgcc4corert += $(libdir)/.*libssp.*\.so.*

PACKAGES += CSWgcc4g++
CATALOGNAME_CSWgcc4g++ = gcc4g++
SPKG_DESC_CSWgcc4g++ = GNU C++ Compiler
PKGFILES_CSWgcc4g++  = $(bindir)/.*g\+\+
PKGFILES_CSWgcc4g++ += $(bindir)/.*c\+\+
PKGFILES_CSWgcc4g++ += $(libexecdir)/.*cc1plus
PKGFILES_CSWgcc4g++ += $(libdir)/.*libstdc.*a
PKGFILES_CSWgcc4g++ += $(libdir)/.*libsupc\+\+.*a
PKGFILES_CSWgcc4g++ += .*/gcc4/man/.*g\+\+.1
PKGFILES_CSWgcc4g++ += $(includedir)/c\+\+/(\d+(?:\.\d+)*)/[a-fA-F,h-iH-I,k-nI-N,p-zP-Z,]+.*
PKGFILES_CSWgcc4g++ += $(includedir)/c\+\+/(\d+(?:\.\d+)*)/ostream.*
RUNTIME_DEP_PKGS_CSWgcc4g++  = CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWgcc4g++ += CSWlibmpfr4
RUNTIME_DEP_PKGS_CSWgcc4g++ += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgcc4g++ += CSWlibgmp10

PACKAGES += CSWgcc4g++rt
CATALOGNAME_CSWgcc4g++rt = gcc4g++rt
SPKG_DESC_CSWgcc4g++rt = GNU C++ Compiler Run Time
RUNTIME_DEP_PKGS_CSWgcc4g++rt = CSWgcc4corert
PKGFILES_CSWgcc4g++rt  = $(libdir)/.*libstdc.*\.so.*
PKGFILES_CSWgcc4g++rt += $(libdir)/.*libsupc\+\+.*\.so.*


PACKAGES += CSWgcc4gfortran
CATALOGNAME_CSWgcc4gfortran   = gcc4gfortran
SPKG_DESC_CSWgcc4gfortran   = GNU Fortran Compiler
RUNTIME_DEP_PKGS_CSWgcc4gfortran    = CSWgcc4gfortranrt
RUNTIME_DEP_PKGS_CSWgcc4gfortran += CSWlibmpfr4
RUNTIME_DEP_PKGS_CSWgcc4gfortran += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgcc4gfortran += CSWlibgmp10
PKGFILES_CSWgcc4gfortran  = $(bindir)/.*gfortran
PKGFILES_CSWgcc4gfortran += $(libdir)/.*libgfortran.*a
PKGFILES_CSWgcc4gfortran += $(libexecdir)/.*f951
PKGFILES_CSWgcc4gfortran += .*/gcc4/man/.*gfortran.1
PKGFILES_CSWgcc4gfortran += .*/gcc4/info/gfortran.*

PACKAGES += CSWgcc4gfortranrt
CATALOGNAME_CSWgcc4gfortranrt = gcc4gfortranrt
SPKG_DESC_CSWgcc4gfortranrt = GNU Fortran Compiler Run Time
RUNTIME_DEP_PKGS_CSWgcc4gfortranrt  = CSWgcc4corert
PKGFILES_CSWgcc4gfortranrt  = $(libdir)/.*libgfortran.*\.so.*

PACKAGES += CSWgcc4java
CATALOGNAME_CSWgcc4java       = gcc4java
SPKG_DESC_CSWgcc4java       = GNU Java Compiler
RUNTIME_DEP_PKGS_CSWgcc4java        = CSWgcc4corert CSWgcc4javart
RUNTIME_DEP_PKGS_CSWgcc4java += CSWzlib
RUNTIME_DEP_PKGS_CSWgcc4java += CSWlibmpfr4
RUNTIME_DEP_PKGS_CSWgcc4java += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgcc4java += CSWlibgmp10

PKGFILES_CSWgcc4java  = $(bindir)/.*gcj.*
PKGFILES_CSWgcc4java += $(bindir)/.*jv-scan
PKGFILES_CSWgcc4java += $(bindir)/.*jv-convert
PKGFILES_CSWgcc4java += $(bindir)/.*jcf-dump
PKGFILES_CSWgcc4java += $(bindir)/.*grmi.*
PKGFILES_CSWgcc4java += $(bindir)/.*grepjar
PKGFILES_CSWgcc4java += $(bindir)/.*gjnih
PKGFILES_CSWgcc4java += $(bindir)/.*gij
PKGFILES_CSWgcc4java += $(bindir)/.*fastjar
PKGFILES_CSWgcc4java += $(bindir)/.*gjar.*
PKGFILES_CSWgcc4java += $(bindir)/.*gjavah
PKGFILES_CSWgcc4java += $(bindir)/.*gorbd
PKGFILES_CSWgcc4java += $(bindir)/.*addr2name.awk
PKGFILES_CSWgcc4java += $(bindir)/.*gappletviewer
PKGFILES_CSWgcc4java += $(bindir)/.*gkeytool
PKGFILES_CSWgcc4java += $(bindir)/.*gserialver
PKGFILES_CSWgcc4java += $(bindir)/.*gtnameserv
PKGFILES_CSWgcc4java += $(bindir)/.*gnative2ascii
PKGFILES_CSWgcc4java += $(bindir)/.*gc-analyze
PKGFILES_CSWgcc4java += .*/gcc4/man/.*/gcj.*
PKGFILES_CSWgcc4java += .*/gcc4/man/.*/gij.*
PKGFILES_CSWgcc4java += .*/gcc4/man/.*/jv.*
PKGFILES_CSWgcc4java += .*/gcc4/man/.*/jcf.*
PKGFILES_CSWgcc4java += .*/gcc4/man/.*/grmi.*
PKGFILES_CSWgcc4java += .*/gcc4/man/.*jar.*
PKGFILES_CSWgcc4java += .*/gcc4/man/.*jni.*
PKGFILES_CSWgcc4java += .*/gcc4/man/.*java.*
PKGFILES_CSWgcc4java += .*/gcc4/man/.*/gorbd.*
PKGFILES_CSWgcc4java += .*/gcc4/man/.*/gapplet.*
PKGFILES_CSWgcc4java += .*/gcc4/man/.*/gkeytool.*
PKGFILES_CSWgcc4java += .*/gcc4/man/.*/gserialver.*
PKGFILES_CSWgcc4java += .*/gcc4/man/.*/gtnameserv.*
PKGFILES_CSWgcc4java += .*/gcc4/man/.*/gnative2ascii.*
PKGFILES_CSWgcc4java += .*/gcc4/man/.*/gc-analyze.*
PKGFILES_CSWgcc4java += .*/gcc4/share/java/.*
PKGFILES_CSWgcc4java += $(libdir)/.*libgij.*a
PKGFILES_CSWgcc4java += $(libdir)/.*libffi.*a
PKGFILES_CSWgcc4java += $(libdir)/.*lib-gnu-awt.*a
PKGFILES_CSWgcc4java += $(libdir)/.*security.*
PKGFILES_CSWgcc4java += $(libdir)/.*logging.properties
PKGFILES_CSWgcc4java += $(libdir)/.*pkgconfig.*
PKGFILES_CSWgcc4java += $(libdir)/.*gcj.*a
PKGFILES_CSWgcc4java += $(libdir)/.*libgcj.*a
PKGFILES_CSWgcc4java += $(libexecdir)/.*collect.*
PKGFILES_CSWgcc4java += $(libexecdir)/.*jvgenmain
PKGFILES_CSWgcc4java += $(libexecdir)/.*jc1.*
PKGFILES_CSWgcc4java += .*/gcc4/info/gcj.*
PKGFILES_CSWgcc4java += $(includedir)/.*gcj/.*
PKGFILES_CSWgcc4java += $(includedir)/.*awt/.*
PKGFILES_CSWgcc4java += $(includedir)/.*classpath/.*
PKGFILES_CSWgcc4java += $(includedir)/.*java.*
PKGFILES_CSWgcc4java += $(includedir)/.*ffi.h
PKGFILES_CSWgcc4java += $(includedir)/.*org/.*

PACKAGES += CSWgcc4javart
CATALOGNAME_CSWgcc4javart     = gcc4javart
SPKG_DESC_CSWgcc4javart     = GNU Java Compiler Run Time
RUNTIME_DEP_PKGS_CSWgcc4javart      = CSWgcc4corert CSWgcc4g++rt
PKGFILES_CSWgcc4javart  = $(libdir)/.*libgij.*\.so.*
PKGFILES_CSWgcc4javart += $(libdir)/.*libffi.*\.so.*
PKGFILES_CSWgcc4javart += $(libdir)/.*lib-gnu-awt.*\.so.*
PKGFILES_CSWgcc4javart += $(libdir)/.*security/classpath.*
PKGFILES_CSWgcc4javart += $(libdir)/.*logging.properties
PKGFILES_CSWgcc4javart += $(libdir)/.*pkgconfig.*
PKGFILES_CSWgcc4javart += $(libdir)/.*gcj.*\.so.*
PKGFILES_CSWgcc4javart += $(libdir)/.*libgcj.*\.so.*

PACKAGES += CSWgcc4objc
CATALOGNAME_CSWgcc4objc       = gcc4objc
SPKG_DESC_CSWgcc4objc       = GNU Objective C Compiler
PKGFILES_CSWgcc4objc  = $(libexecdir)/.*cc1obj
PKGFILES_CSWgcc4objc += $(libdir)/.*libobjc.*a
PKGFILES_CSWgcc4objc += $(includedir)/.*objc/.*
PKGFILES_CSWgcc4objc += $(libdir)/.*/include/objc/.*
RUNTIME_DEP_PKGS_CSWgcc4objc += CSWgcc4objcrt
RUNTIME_DEP_PKGS_CSWgcc4objc += CSWlibmpfr4
RUNTIME_DEP_PKGS_CSWgcc4objc += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgcc4objc += CSWlibgmp10


PACKAGES += CSWgcc4objcrt
CATALOGNAME_CSWgcc4objcrt     = gcc4objcrt
SPKG_DESC_CSWgcc4objcrt     = GNU Objective C Compiler Run Time
RUNTIME_DEP_PKGS_CSWgcc4objcrt      = CSWgcc4corert
PKGFILES_CSWgcc4objcrt = $(libdir)/.*libobjc.*\.so.*
 
## Source URLs
VENDOR_URL = http://gcc.gnu.org

## Copyright File
LICENSE = COPYING3

DISTFILES += CSWgcc4core.space

define CSWgcc4core_postinstall
#!/bin/sh

Error()
{
	echo "=====> postinstall Error: $$1" >&2
	exit 1
}

OS_REV="`/usr/bin/uname -r | sed -e 's/[^.]*//'`"
case `/usr/bin/uname -p` in
	"sparc") OS_TARGET="sparc-sun-solaris2.8" ;;
	 "i386") OS_TARGET="i386-pc-solaris2$${OS_REV}" ;;
esac

TOOLS_DIR="$${PKG_INSTALL_ROOT}/opt/csw/gcc4/libexec/gcc"
TOOLS_DIR="$${TOOLS_DIR}/$${OS_TARGET}/$(VERSION)/install-tools"
MKHEADERS_CMD="$${PKG_INSTALL_ROOT}/opt/csw/gcc4/bin/mkheaders"
INCLUDE_DIR="$${PKG_INSTALL_ROOT}/opt/csw/gcc4/lib/gcc"
INCLUDE_DIR="$${INCLUDE_DIR}/$${OS_TARGET}/$(VERSION)/include"

cat << _EOF_
******************************************************************************
* NOTICE: Fixing the system headers
*
* Do not forget: whenever your system headers change 
* Run the $${MKHEADERS_CMD} script!
******************************************************************************
_EOF_

if [ -f $${TOOLS_DIR}/mkheaders ]; then
	cp $${TOOLS_DIR}/mkheaders $${MKHEADERS_CMD}
	installf $${PKGINST} "$${MKHEADERS_CMD}"
else
	Error "$${TOOLS_DIR}/mkheaders Not Found"
fi

if [ -f $${MKHEADERS_CMD} ];then
	chmod 0755 $${MKHEADERS_CMD} 2>/dev/null
	chown root:bin $${MKHEADERS_CMD} 2>/dev/null
	"$${MKHEADERS_CMD}" || Error "$${MKHEADERS_CMD} Failed."
else
	Error "Could not find $${MKHEADERS_CMD}"
fi

if [ -d $${INCLUDE_DIR} ]; then
	chmod 0755 $${INCLUDE_DIR} || Error "Failed to chmod $${INCLUDE_DIR}"
	chown -R root:bin $${INCLUDE_DIR} || 
			Error "Failed to change ownership for $${INCLUDE_DIR}"
	find $${INCLUDE_DIR} -print | installf $${PKGINST} -
fi


cat << _EOF_
******************************************************************************
* NOTICE: Successfully fixed system headers
*
* Do not forget: whenever your system headers change 
* Run the $${MKHEADERS_CMD} script!
******************************************************************************
_EOF_
	
installf -f $${PKGINST}

exit 0
endef
