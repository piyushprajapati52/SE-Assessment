#include <stdio.h>
#include <ctype.h>
void countSpacesDigits(char str[]) {
 int spaces = 0, digits = 0;
 for (int i = 0; str[i] != '\0'; i++) {
 if (str[i] == ' ')
 spaces++;
 else if (isdigit(str[i]))
 digits++;
 }
 printf("Spaces: %d\n", spaces);
 printf("Digits: %d\n", digits);
}
int main() {
 char str[100];
 printf("Enter a string: ");
 gets(str);
 countSpacesDigits(str);
 return 0;
}