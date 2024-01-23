#include <iostream>

using namespace std;

// Function to find the maximum of two integers
int max(int a, int b) {
    return (a > b) ? a : b;
}

// Function to solve 0/1 Knapsack problem
int knapsack(int capacity, int weights[], int values[], int n) {
    int dp[n + 1][capacity + 1];

    // Initializing the dp array
    for (int i = 0; i <= n; ++i) {
        for (int w = 0; w <= capacity; ++w) {
            if (i == 0 || w == 0) {
                dp[i][w] = 0;
            } else if (weights[i - 1] <= w) {
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]);
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    return dp[n][capacity];
}

int main() {
    int n; // Number of items
    cout << "Enter the number of items: ";
    cin >> n;

    int weights[n];
    int values[n];

    cout << "Enter the weights of items:\n";
    for (int i = 0; i < n; ++i) {
        cout << "Item " << i + 1 << ": ";
        cin >> weights[i];
    }

    cout << "Enter the values of items:\n";
    for (int i = 0; i < n; ++i) {
        cout << "Item " << i + 1 << ": ";
        cin >> values[i];
    }

    int capacity; // Maximum capacity of the knapsack
    cout << "Enter the maximum capacity of the knapsack: ";
    cin >> capacity;

    int result = knapsack(capacity, weights, values, n);
    cout << "The maximum profit for the given items is: " << result << endl;

    return 0;
}
