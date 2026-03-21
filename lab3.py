#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void) {
    char s[81];
    printf("Введите строку: ");
    scanf("%s", s);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == 'a' || s[i]=='b') {
            s[i] = toupper(s[i]);
        }
    }
    printf("полученная строка: %s");
    return 0;
}
