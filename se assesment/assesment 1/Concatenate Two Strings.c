#include <stdio.h>
#include <string.h>
void concatenate(char str1[], char str2[]) {
 strcat(str1, str2);
 printf("Concatenated String: %s\n", str1);
}
int main() {
 char str1[100], str2[100];
 printf("Enter first string: ");
 scanf("%s",&str1);
 printf("Enter second string: ");
 scanf("%s",&str2);
 concatenate(str1, str2);
 return 0;
}
