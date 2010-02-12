/* Allow 32 and 64 bit headers to coexist */
#if defined __amd64 || defined __x86_64 || defined __sparcv9
#include "ares_build-64.h"
#else
#include "ares_build-32.h"
#endif
