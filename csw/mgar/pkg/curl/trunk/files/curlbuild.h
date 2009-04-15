#Allow 32 and 64 bit headers to coexist
#if defined __arch64__ || defined __sparcv9
#include "curlbuild-64.h"
#else
#include "curlbuild-32.h"
#endif
