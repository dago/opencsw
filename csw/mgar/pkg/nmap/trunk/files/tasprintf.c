extern int asprintf(char **ptr, const char *fmt, ...);

#include <stdio.h>

int main()
{
  char *my_string;

  asprintf (&my_string, "Being %d is cool, but being free is best of all.", 4);
  puts (my_string);

  return 0;
}
