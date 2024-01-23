#include <iostream>

using namespace std;

// Function to find the maximum of two integers
int max(int a, int b) {
    return (a > b) ? a : b;
}

// Function to solve 0/1 Knapsack problem
int knapsack(int capacity, int weights[], int values[], int n, bool selectedItems[]) {
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

    // Backtrack to find selected items
    int i = n, w = capacity;
    while (i > 0 && w > 0) {
        if (dp[i][w] != dp[i - 1][w]) {
            selectedItems[i - 1] = true;
            w -= weights[i - 1];
        }
        i--;
    }

    return dp[n][capacity];
}

int main() {
    int n; // Number of items
    cout << "Enter the number of items: ";
    cin >> n;

    int* weights = new int[n];
    int* values = new int[n];
    bool* selectedItems = new bool[n]; 

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

    int result = knapsack(capacity, weights, values, n, selectedItems);

    cout << "The maximum profit for the given items is: " << result << endl;
    cout << "Items selected in the knapsack: ";
    
    for (int i = 0; i < n; ++i) {
        if (selectedItems[i]) {
            cout << "Item " << i + 1 << " ";
        }
    }

    cout << endl;

    // Release dynamically allocated memory
    delete[] weights;
    delete[] values;
    delete[] selectedItems;

    return 0;
}
