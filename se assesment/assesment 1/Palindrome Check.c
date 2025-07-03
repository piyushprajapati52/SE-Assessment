#include <stdio.h>
#include <string.h>

void checkPalindrome(char str[]) {
    int len = strlen(str);
    int i;

    for (i = 0; i < len / 2; i++) {
        if (str[i] != str[len - 1 - i]) {
            printf("The string is NOT a Palindrome.\n");
            return;  
        }
    }

    
    printf("The string is a Palindrome.\n");
}

int main() {
    char str[100];
    printf("Enter a string: ");
    gets(str);  
    checkPalindrome(str);
    return 0;
}
