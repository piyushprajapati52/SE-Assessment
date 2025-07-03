#include <stdio.h>
#include <string.h>
void copyString(char src[]) {
 char dest[100];
 strcpy(dest, src);
 printf("Copied String: %s\n", dest);
}
int main() {
 char str[100];
 printf("Enter a string: ");
 gets(str);
 copyString(str);
 
 return 0;
}