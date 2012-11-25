/* Allow 32 and 64 bit headers to coexist */
#if defined __amd64 || defined __x86_64 || defined __sparcv9
#include "gmpxx-64.h"
#else
#include "gmpxx-32.h"
#endif
