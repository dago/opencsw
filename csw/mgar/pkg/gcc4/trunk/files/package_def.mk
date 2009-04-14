###  Package Section  ###
PACKAGES  = CSWgcc4ada CSWgcc4adart CSWgcc4core CSWgcc4corert CSWgcc4gfortran 
PACKAGES += CSWgcc4gfortranrt CSWgcc4java CSWgcc4javart CSWgcc4objc
PACKAGES += CSWgcc4objcrt CSWgcc4g++ CSWgcc4g++rt
 
## Define Package Catalog Names
CATALOGNAME_CSWgcc4ada        = gcc4ada
CATALOGNAME_CSWgcc4adart      = gcc4adart
CATALOGNAME_CSWgcc4core       = gcc4core
CATALOGNAME_CSWgcc4corert     = gcc4corert
CATALOGNAME_CSWgcc4g++        = gcc4g++
CATALOGNAME_CSWgcc4g++rt      = gcc4g++rt
CATALOGNAME_CSWgcc4gfortran   = gcc4gfortran
CATALOGNAME_CSWgcc4gfortranrt = gcc4gfortranrt
CATALOGNAME_CSWgcc4java       = gcc4java
CATALOGNAME_CSWgcc4javart     = gcc4javart
CATALOGNAME_CSWgcc4objc       = gcc4objc
CATALOGNAME_CSWgcc4objcrt     = gcc4objcrt

## Source URLs
SPKG_SOURCEURL_CSWgcc4ada        = http://gcc.gnu.org
SPKG_SOURCEURL_CSWgcc4adart      = http://gcc.gnu.org
SPKG_SOURCEURL_CSWgcc4core       = http://gcc.gnu.org
SPKG_SOURCEURL_CSWgcc4corert     = http://gcc.gnu.org
SPKG_SOURCEURL_CSWgcc4g++        = http://gcc.gnu.org
SPKG_SOURCEURL_CSWgcc4g++rt      = http://gcc.gnu.org
SPKG_SOURCEURL_CSWgcc4gfortran   = http://gcc.gnu.org
SPKG_SOURCEURL_CSWgcc4gfortranrt = http://gcc.gnu.org
SPKG_SOURCEURL_CSWgcc4java       = http://gcc.gnu.org
SPKG_SOURCEURL_CSWgcc4javart     = http://gcc.gnu.org
SPKG_SOURCEURL_CSWgcc4objc       = http://gcc.gnu.org
SPKG_SOURCEURL_CSWgcc4objcrt     = http://gcc.gnu.org

## Copyright File
LICENSE_CSWgcc4ada        = COPYING3
LICENSE_CSWgcc4adart      = COPYING3
LICENSE_CSWgcc4core       = COPYING3
LICENSE_CSWgcc4corert     = COPYING3
LICENSE_CSWgcc4g++        = COPYING3
LICENSE_CSWgcc4g++rt      = COPYING3
LICENSE_CSWgcc4gfortran   = COPYING3
LICENSE_CSWgcc4gfortranrt = COPYING3
LICENSE_CSWgcc4java       = COPYING3
LICENSE_CSWgcc4javart     = COPYING3
LICENSE_CSWgcc4objc       = COPYING3
LICENSE_CSWgcc4objcrt     = COPYING3

## Define Package Descriptions
SPKG_DESC_CSWgcc4ada        = GNU C ADA Compiler
SPKG_DESC_CSWgcc4adart      = GNU C ADA Compiler Run Time
SPKG_DESC_CSWgcc4core       = GNU C Compiler
SPKG_DESC_CSWgcc4corert     = GNU C Compiler Run Time
SPKG_DESC_CSWgcc4g++        = GNU C++ Compiler
SPKG_DESC_CSWgcc4g++rt      = GNU C++ Compiler Run Time
SPKG_DESC_CSWgcc4gfortran   = GNU Fortran Compiler
SPKG_DESC_CSWgcc4gfortranrt = GNU Fortran Compiler Run Time
SPKG_DESC_CSWgcc4java       = GNU Java Compiler
SPKG_DESC_CSWgcc4javart     = GNU Java Compiler Run Time
SPKG_DESC_CSWgcc4objc       = GNU Objective C Compiler
SPKG_DESC_CSWgcc4objcrt     = GNU Objective C Compiler Run Time

## Define Dependencies 
COMMON_REQUIRE                   = CSWiconv CSWlibgmp CSWlibmpfr
REQUIRED_PKGS_CSWgcc4adart       = CSWggettextrt $(COMMON_REQUIRE)
REQUIRED_PKGS_CSWgcc4ada         = CSWgcc4core $(COMMON_REQUIRE)
REQUIRED_PKGS_CSWgcc4corert      = CSWggettextrt $(COMMON_REQUIRE)
REQUIRED_PKGS_CSWgcc4core        = $(COMMON_REQUIRE) CSWbinutils CSWggettextrt
REQUIRED_PKGS_CSWgcc4g++rt       = CSWgcc4corert CSWiconv
REQUIRED_PKGS_CSWgcc4g++         = CSWgcc4core $(COMMON_REQUIRE)
REQUIRED_PKGS_CSWgcc4gfortranrt  = CSWgcc4corert CSWiconv
REQUIRED_PKGS_CSWgcc4gfortran    = CSWgcc4core $(COMMON_REQUIRE)
REQUIRED_PKGS_CSWgcc4javart      = CSWgcc4corert CSWgcc4g++rt CSWiconv
REQUIRED_PKGS_CSWgcc4java        = CSWgcc4core CSWzlib $(COMMON_REQUIRE)
REQUIRED_PKGS_CSWgcc4objcrt      = CSWgcc4corert CSWiconv
REQUIRED_PKGS_CSWgcc4objc        = CSWgcc4core $(COMMON_REQUIRE)

## Define the Contents of the Packages

## gcc4ada Definitions
PKGFILES_CSWgcc4ada  = .*/gcc4/libexec/.*gnat1
PKGFILES_CSWgcc4ada += .*/gcc4/lib/.*libgnat.*
PKGFILES_CSWgcc4ada += .*/gcc4/lib/.*libgnarl.*
PKGFILES_CSWgcc4ada += .*/gcc4/.*/adalib/.*
PKGFILES_CSWgcc4ada += .*/gcc4/.*/adainclude/.*
PKGFILES_CSWgcc4ada += .*/gcc4/info/.*gnat.*
PKGFILES_CSWgcc4ada += .*/gcc4/bin/gnat.*

## gcc4gfortran Definitions
PKGFILES_CSWgcc4gfortran  = .*/gcc4/bin/.*gfortran
PKGFILES_CSWgcc4gfortran += .*/gcc4/lib/.*libgfortran.*
PKGFILES_CSWgcc4gfortran += .*/gcc4/libexec/.*f951
PKGFILES_CSWgcc4gfortran += .*/gcc4/man/.*gfortran.1
PKGFILES_CSWgcc4gfortran += .*/gcc4/info/gfortran.*

## gcc4g++ Definitions
PKGFILES_CSWgcc4g++  = .*/gcc4/bin/.*g\+\+
PKGFILES_CSWgcc4g++ += .*/gcc4/bin/.*c\+\+
PKGFILES_CSWgcc4g++ += .*/gcc4/libexec/.*cc1plus
PKGFILES_CSWgcc4g++ += .*/gcc4/lib/.*libstdc.*
PKGFILES_CSWgcc4g++ += .*/gcc4/lib/.*libsupc\+\+.*
PKGFILES_CSWgcc4g++ += .*/gcc4/man/.*g\+\+.1
PKGFILES_CSWgcc4g++ += .*/gcc4/man/.*libstdc\+\+.1
PKGFILES_CSWgcc4g++ += .*/gcc4/man/.*libsupc\+\+.1
PKGFILES_CSWgcc4g++ += .*/gcc4/include/c\+\+/(\d+(?:\.\d+)*)/[a-fA-F,h-iH-I,k-nI-N,p-zP-Z,]+.*
PKGFILES_CSWgcc4g++ += .*/gcc4/include/c\+\+/(\d+(?:\.\d+)*)/ostream.*

## gcc4java Definitions
PKGFILES_CSWgcc4java  = .*/gcc4/bin/.*gcj.*
PKGFILES_CSWgcc4java += .*/gcc4/bin/.*jv-scan
PKGFILES_CSWgcc4java += .*/gcc4/bin/.*jv-convert
PKGFILES_CSWgcc4java += .*/gcc4/bin/.*jcf-dump
PKGFILES_CSWgcc4java += .*/gcc4/bin/.*grmi.*
PKGFILES_CSWgcc4java += .*/gcc4/bin/.*grepjar
PKGFILES_CSWgcc4java += .*/gcc4/bin/.*gjnih
PKGFILES_CSWgcc4java += .*/gcc4/bin/.*gij
PKGFILES_CSWgcc4java += .*/gcc4/bin/.*fastjar
PKGFILES_CSWgcc4java += .*/gcc4/bin/.*gjar.*
PKGFILES_CSWgcc4java += .*/gcc4/bin/.*gjavah
PKGFILES_CSWgcc4java += .*/gcc4/bin/.*gorbd
PKGFILES_CSWgcc4java += .*/gcc4/bin/.*addr2name.awk
PKGFILES_CSWgcc4java += .*/gcc4/bin/.*gappletviewer
PKGFILES_CSWgcc4java += .*/gcc4/bin/.*gkeytool
PKGFILES_CSWgcc4java += .*/gcc4/bin/.*gserialver
PKGFILES_CSWgcc4java += .*/gcc4/bin/.*gtnameserv
PKGFILES_CSWgcc4java += .*/gcc4/bin/.*gnative2ascii
PKGFILES_CSWgcc4java += .*/gcc4/bin/.*gc-analyze
PKGFILES_CSWgcc4java += .*/gcc4/man.*/gcj.*
PKGFILES_CSWgcc4java += .*/gcc4/man.*/gij.*
PKGFILES_CSWgcc4java += .*/gcc4/man.*/jv.*
PKGFILES_CSWgcc4java += .*/gcc4/man.*/jcf.*
PKGFILES_CSWgcc4java += .*/gcc4/man.*/grmi.*
PKGFILES_CSWgcc4java += .*/gcc4/man/.*jar.*
PKGFILES_CSWgcc4java += .*/gcc4/man/.*jni.*
PKGFILES_CSWgcc4java += .*/gcc4/man/.*java.*
PKGFILES_CSWgcc4java += .*/gcc4/man.*/gorbd.*
PKGFILES_CSWgcc4java += .*/gcc4/man.*/gapplet.*
PKGFILES_CSWgcc4java += .*/gcc4/man.*/gkeytool.*
PKGFILES_CSWgcc4java += .*/gcc4/man.*/gserialver.*
PKGFILES_CSWgcc4java += .*/gcc4/man.*/gtnameserv.*
PKGFILES_CSWgcc4java += .*/gcc4/man.*/gnative2ascii.*
PKGFILES_CSWgcc4java += .*/gcc4/man.*/gc-analyze.*
PKGFILES_CSWgcc4java += .*/gcc4/share/java/.*
PKGFILES_CSWgcc4java += .*/gcc4/lib/.*libgij.*
PKGFILES_CSWgcc4java += .*/gcc4/lib/.*libffi.*
PKGFILES_CSWgcc4java += .*/gcc4/lib/.*lib-gnu-awt.*
PKGFILES_CSWgcc4java += .*/gcc4/lib/.*security/classpath.*
PKGFILES_CSWgcc4java += .*/gcc4/lib/.*logging.properties
PKGFILES_CSWgcc4java += .*/gcc4/lib/.*pkgconfig.*
PKGFILES_CSWgcc4java += .*/gcc4/lib/.*gcj.*
PKGFILES_CSWgcc4java += .*/gcc4/lib/.*libgcj.*
PKGFILES_CSWgcc4java += .*/gcc4/libexec/.*collect.*
PKGFILES_CSWgcc4java += .*/gcc4/libexec/.*jvgenmain
PKGFILES_CSWgcc4java += .*/gcc4/libexec/.*jc1.*
PKGFILES_CSWgcc4java += .*/gcc4/info/gcj.*
PKGFILES_CSWgcc4java += .*/gcc4/include/.*gcj/.*
PKGFILES_CSWgcc4java += .*/gcc4/include/.*awt/.*
PKGFILES_CSWgcc4java += .*/gcc4/include/.*classpath/.*
PKGFILES_CSWgcc4java += .*/gcc4/include/.*java.*
PKGFILES_CSWgcc4java += .*/gcc4/include/.*ffi.h
PKGFILES_CSWgcc4java += .*/gcc4/include/.*org/.*

## gcc4objc Definitions
PKGFILES_CSWgcc4objc  = .*/gcc4/libexec/.*cc1obj
PKGFILES_CSWgcc4objc += .*/gcc4/lib/.*libobjc.*
PKGFILES_CSWgcc4objc += .*/gcc4/include/.*objc/.*
PKGFILES_CSWgcc4objc += .*/gcc4/lib/.*/include/objc/.*

#######  RunTime Packages

## gcc4adart
PKGFILES_CSWgcc4adart  = .*/opt/csw/lib/.*libgnat.*
PKGFILES_CSWgcc4adart += .*/opt/csw/lib/.*libgnarl.*

## gcc4corert
PKGFILES_CSWgcc4corert  = .*/opt/csw/lib/.*libgcc_s.*
PKGFILES_CSWgcc4corert += .*/opt/csw/lib/.*libgomp.*
PKGFILES_CSWgcc4corert += .*/opt/csw/lib/.*libiberty.*
PKGFILES_CSWgcc4corert += .*/opt/csw/lib/.*libssp.*

## gcc4gfortranrt 
PKGFILES_CSWgcc4gfortranrt  = .*/opt/csw/lib/.*libgfortran.*

## gcc4g++rt
PKGFILES_CSWgcc4g++rt  = .*/opt/csw/lib/.*libstdc.*
PKGFILES_CSWgcc4g++rt += .*/opt/csw/lib/.*libsupc\+\+.*

## gcc4javart
PKGFILES_CSWgcc4javart  = .*/opt/csw/lib/.*libgij.*
PKGFILES_CSWgcc4javart += .*/opt/csw/lib/.*libffi.*
PKGFILES_CSWgcc4javart += .*/opt/csw/lib/.*lib-gnu-awt.*
PKGFILES_CSWgcc4javart += .*/opt/csw/lib/.*security/classpath.*
PKGFILES_CSWgcc4javart += .*/opt/csw/lib/.*logging.properties
PKGFILES_CSWgcc4javart += .*/opt/csw/lib/.*pkgconfig.*
PKGFILES_CSWgcc4javart += .*/opt/csw/lib/.*gcj.*
PKGFILES_CSWgcc4javart += .*/opt/csw/lib/.*libgcj.*

## gcc4objc Runtime
PKGFILES_CSWgcc4objcrt = .*/opt/csw/lib/.*libobjc.*
