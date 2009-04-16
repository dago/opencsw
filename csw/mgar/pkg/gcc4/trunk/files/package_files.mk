## Define the Contents of the Packages

## gcc4ada Definitions
PKGFILES_CSWgcc4ada  = .*/gcc4/libexec/.*gnat1
PKGFILES_CSWgcc4ada += .*/gcc4/lib/.*libgnat.*a
PKGFILES_CSWgcc4ada += .*/gcc4/lib/.*libgnarl.*a
PKGFILES_CSWgcc4ada += .*/gcc4/.*/adalib/.*
PKGFILES_CSWgcc4ada += .*/gcc4/.*/adainclude/.*
PKGFILES_CSWgcc4ada += .*/gcc4/info/.*gnat.*
PKGFILES_CSWgcc4ada += .*/gcc4/bin/gnat.*

## gcc4gfortran Definitions
PKGFILES_CSWgcc4gfortran  = .*/gcc4/bin/.*gfortran
PKGFILES_CSWgcc4gfortran += .*/gcc4/lib/.*libgfortran.*a
PKGFILES_CSWgcc4gfortran += .*/gcc4/libexec/.*f951
PKGFILES_CSWgcc4gfortran += .*/gcc4/man/.*gfortran.1
PKGFILES_CSWgcc4gfortran += .*/gcc4/info/gfortran.*

## gcc4g++ Definitions
PKGFILES_CSWgcc4g++  = .*/gcc4/bin/.*g\+\+
PKGFILES_CSWgcc4g++ += .*/gcc4/bin/.*c\+\+
PKGFILES_CSWgcc4g++ += .*/gcc4/libexec/.*cc1plus
PKGFILES_CSWgcc4g++ += .*/gcc4/lib/.*libstdc.*a
PKGFILES_CSWgcc4g++ += .*/gcc4/lib/.*libsupc\+\+.*a
PKGFILES_CSWgcc4g++ += .*/gcc4/man/.*g\+\+.1
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
PKGFILES_CSWgcc4java += .*/gcc4/lib/.*libgij.*a
PKGFILES_CSWgcc4java += .*/gcc4/lib/.*libffi.*a
PKGFILES_CSWgcc4java += .*/gcc4/lib/.*lib-gnu-awt.*a
PKGFILES_CSWgcc4java += .*/gcc4/lib/.*security.*
PKGFILES_CSWgcc4java += .*/gcc4/lib/.*logging.properties
PKGFILES_CSWgcc4java += .*/gcc4/lib/.*pkgconfig.*
PKGFILES_CSWgcc4java += .*/gcc4/lib/.*gcj.*a
PKGFILES_CSWgcc4java += .*/gcc4/lib/.*libgcj.*a
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
PKGFILES_CSWgcc4objc += .*/gcc4/lib/.*libobjc.*a
PKGFILES_CSWgcc4objc += .*/gcc4/include/.*objc/.*
PKGFILES_CSWgcc4objc += .*/gcc4/lib/.*/include/objc/.*

#######  RunTime Packages

## gcc4adart
PKGFILES_CSWgcc4adart  = .*/gcc4/lib/.*libgnat.*\.so.*
PKGFILES_CSWgcc4adart += .*/gcc4/lib/.*libgnarl.*\.so.*

## gcc4corert
PKGFILES_CSWgcc4corert  = .*/gcc4/lib/.*libgcc_s.*\.so.*
PKGFILES_CSWgcc4corert += .*/gcc4/lib/.*libgomp.*\.so.*
PKGFILES_CSWgcc4corert += .*/gcc4/lib/.*libssp.*\.so.*

## gcc4gfortranrt 
PKGFILES_CSWgcc4gfortranrt  = .*/gcc4/lib/.*libgfortran.*\.so.*

## gcc4g++rt
PKGFILES_CSWgcc4g++rt  = .*/gcc4/lib/.*libstdc.*\.so.*
PKGFILES_CSWgcc4g++rt += .*/gcc4/lib/.*libsupc\+\+.*\.so.*

## gcc4javart
PKGFILES_CSWgcc4javart  = .*/gcc4/lib/.*libgij.*\.so.*
PKGFILES_CSWgcc4javart += .*/gcc4/lib/.*libffi.*\.so.*
PKGFILES_CSWgcc4javart += .*/gcc4/lib/.*lib-gnu-awt.*\.so.*
PKGFILES_CSWgcc4javart += .*/gcc4/lib/.*security/classpath.*
PKGFILES_CSWgcc4javart += .*/gcc4/lib/.*logging.properties
PKGFILES_CSWgcc4javart += .*/gcc4/lib/.*pkgconfig.*
PKGFILES_CSWgcc4javart += .*/gcc4/lib/.*gcj.*\.so.*
PKGFILES_CSWgcc4javart += .*/gcc4/lib/.*libgcj.*\.so.*

## gcc4objc Runtime
PKGFILES_CSWgcc4objcrt = .*/gcc4/lib/.*libobjc.*\.so.*
