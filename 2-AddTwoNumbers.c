/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
	dummy->val = 0;
	dummy->next = NULL;
	
	struct ListNode* iterator = dummy;
	
    int sum, carry = 0;
    while (l1 != NULL || l2 != NULL || carry != 0) {
		sum = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + carry;
		if (l1) l1 = l1->next;
        if (l2) l2 = l2->next;
		
		struct ListNode* temp = (struct ListNode*)malloc(sizeof(struct ListNode));
		temp->val = sum%10;
		temp->next = NULL;
		
		iterator->next = temp;
		iterator = iterator->next;
		
		carry = sum/10;
		sum = 0;
    }
	
	return dummy->next;
}