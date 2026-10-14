class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> map(128, -1);
        int maxLength = 0;
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            char currentChar = s[right];
            
            if (map[currentChar] >= left) {
                left = map[currentChar] + 1;
            }

            map[currentChar] = right;

            maxLength = max(maxLength, right - left + 1);
        }

        return maxLength;
    }
};