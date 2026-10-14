/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head) {
    if (head == NULL || head->next == NULL) return true;

    struct ListNode *curr = head;

    //find the listnode length
    int count = 0;
    while (curr) {
        count++;
        curr = curr->next;
    }

    //add the val to array
    curr = head;
    int i = 0;
    int values[count];
    while (curr) {
        values[i] = curr->val;
        curr = curr->next;
        i++;
    }

    //2 pointers
    for (int i=0, j=count-1; i < j; i++, j--) {
        if (values[i] != values[j]) {
            return false;
        }
    }

    return true;
}