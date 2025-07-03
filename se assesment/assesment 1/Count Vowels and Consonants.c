#include <stdio.h>
#include <ctype.h>
void countVowelsConsonants(char str[]) {
 int vowels = 0, consonants = 0;
 for (int i = 0; str[i] != '\0'; i++) {
 char ch = tolower(str[i]);
 if (isalpha(ch)) {
 if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
 vowels++;
 else
 consonants++;
 }
 }
 printf("Vowels: %d\n", vowels);
 printf("Consonants: %d\n", consonants);
}
int main() {
 char str[100];
 printf("Enter a string: ");
 gets(str);
 countVowelsConsonants(str);
 return 0;
}