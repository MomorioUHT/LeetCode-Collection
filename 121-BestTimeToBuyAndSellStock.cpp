class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minimum = 999999;
        int maxProfit = 0;

        for (int i = 0; i < prices.size(); i++) {
            int diff = prices[i] - minimum;
            if (diff > maxProfit) {
                maxProfit = diff;
            }
            if (prices[i] < minimum) {
                minimum = prices[i];
            }
        }

        return maxProfit;        
    }
};