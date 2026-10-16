
#include <stdio.h>

int main()
{
    int coins[20], n, amount;
    int dp[1000];
    int i, j;

    printf("Enter number of coin types: ");
    scanf("%d", &n);

    printf("Enter coin values: ");
    for (i = 0; i < n; i++)
        scanf("%d", &coins[i]);

    printf("Enter amount: ");
    scanf("%d", &amount);

    dp[0] = 0;

    for (i = 1; i <= amount; i++)
        dp[i] = 10000;

    for (i = 1; i <= amount; i++)
    {
        for (j = 0; j < n; j++)
        {
            if (coins[j] <= i &&
                dp[i - coins[j]] + 1 < dp[i])
            {
                dp[i] = dp[i - coins[j]] + 1;
            }
        }
    }

    if (dp[amount] == 10000)
        printf("Change cannot be made\n");
    else
        printf("Minimum number of coins = %d\n",
               dp[amount]);

    return 0;
}

