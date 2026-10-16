class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        int prev1 = 0, prev2 = 0;
        int curr;

        for (int i = 0; i < n; i++) {
            curr = max(nums[i] + prev1, prev2);
            prev1 = prev2;
            prev2 = curr;
        }

        return curr;        
    }
};