// Based on isaexec man page.
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[], char *envp[]) {
  return (isaexec(getexecname(), argv, envp));
}
