#include <bits/stdc++.h>
using namespace std;

vector<int> expenses;

int main() {
    int expense;

    while (scanf("%d", &expense) != EOF) {
        expenses.push_back(expense);
    }

    for (int i = 0; i < expenses.size(); i++) {
        for (int j = i + 1; j < expenses.size(); j++) {
            for (int k = j + 1; k < expenses.size(); k++) {
                if (expenses[i] + expenses[j] + expenses[k] == 2020) {
                    printf("%d + %d + %d = 2020\n", expenses[i], expenses[j], expenses[k]);
                    printf("%d x %d x %d = %d\n", expenses[i], expenses[j], expenses[k], expenses[i] * expenses[j]);
                    break;
                }
            }
        }
    }
}