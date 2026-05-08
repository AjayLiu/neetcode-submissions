/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        ListNode* startNode;
        ListNode* prevNode = nullptr;
        while(l1 || l2){
            int sum = carry;
            if(l1){
                sum += l1->val;
                l1 = l1->next;
            }
            if(l2){
                sum += l2->val;
                l2 = l2->next;
            }
            if(sum >= 10){
                carry = sum / 10;
                sum %= 10;
            } else {
                carry = 0;
            }
            ListNode* sumNode = new ListNode(sum);
            if(prevNode){
                prevNode->next = sumNode;
            } else {
                startNode = sumNode;
            }
            prevNode = sumNode;

        }

        if(carry){
            ListNode* finalNode = new ListNode(carry);
            prevNode->next = finalNode;
        }

        return startNode;
    }
};
