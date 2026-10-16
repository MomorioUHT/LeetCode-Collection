class Solution {
public:
    int strStr(string haystack, string needle) {
        int h_length = haystack.length();
        int n_length = needle.length();

        if (n_length > h_length) {
            return -1;
        }

        int n_index = 0;

        for (int i = 0; i < h_length; i++) {
            if (haystack[i] == needle[n_index]) {
                n_index++;
            } else {
                i = i - n_index;
                n_index = 0;
            }

            if (n_index == n_length) {
                return i - n_length + 1;
            }
        }

        return -1;
    }
};