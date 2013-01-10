/* Allow 32 and 64 bit headers to coexist */
#if defined __amd64 || defined __x86_64 || defined __sparcv9
/*
 * Eventually, enable this. For now, say we have no headers for 64-bit Python.
 * #include "pyport-64.h"
 */
#else
#include "pyport-32.h"
#endif
