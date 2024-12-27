
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}


// LeetCode 21. Merge Two Sorted Lists

// n is sum of list1 and list2 size
 // time: O(n)
 // space: O(n)
class MergeTwoSortedLists {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode newListHead = new ListNode(-1);
        ListNode newCurr = newListHead;

        if (list1 == null && list2 == null) {
            return null;
        }

        else if (list1 == null) {
            return list2;
        }

        else if (list2 == null) {
            return list1;
        }

        while (list1 != null && list2 != null) {
            // compare left and right
            // if list1 smaller add to new list
            if (list1.val < list2.val) {
                newCurr.next = list1;
                list1 = list1.next;
            }

            // compare left and right
            // if list2 smaller add to new list
            // if equal add list2 to new list
            else {
                newCurr.next = list2;
                list2 = list2.next;
            }

            newCurr = newCurr.next;
            //System.out.println(newCurr.val);
        }

        while (list1 != null) {
            newCurr.next = list1;
            //System.out.println(newCurr.val);
            list1 = list1.next;
            newCurr = newCurr.next;
        }

        while (list2 != null) {
            newCurr.next = list2;
            //System.out.println(newCurr.val);
            list2 = list2.next;
            newCurr = newCurr.next;
        }

        return newListHead.next;
    }
}