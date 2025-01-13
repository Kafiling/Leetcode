/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ArrayList<Integer> arr = new ArrayList<Integer>();
        ListNode pointer = list1;
        while(pointer != null){
            arr.add(pointer.val);
            pointer = pointer.next;
        }
        pointer = list2;
        while(pointer != null){
            arr.add(pointer.val);
            pointer = pointer.next;
        }
        if(arr.size() == 0){
            return null;
        }
        Collections.sort(arr);
        ListNode first = new ListNode(arr.get(0));
        ListNode last = first;
        for(int i=1;i<arr.size();i++){
        ListNode temp = new ListNode(arr.get(i));
        last.next = temp;
        last = temp;
        }
        return first;
    }
}
