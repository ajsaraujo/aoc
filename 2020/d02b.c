#include <stdio.h>

int main() {
    int i, j;
    char symbol, password[100];

    int validPasswordCount = 0;

    while (scanf("%d-%d %c: %s", &i, &j, &symbol, password) != EOF) {
        int symbolCount = 0;
        
        int oneMatch = password[i - 1] == symbol;
        int anotherMatch = password[j - 1] == symbol;

        validPasswordCount += oneMatch ^ anotherMatch;
    }

    printf("Valid passwords: %d\n", validPasswordCount);

    return 0;
}