/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class SReverseBetween {
    static class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode dummy = new ListNode(), leftEnd = head, rightStart = head, prev, cur, next;
        dummy.next = head;
        leftEnd = dummy;
        while (left > 1) {
            leftEnd = leftEnd.next;
            left--;
        }
        ListNode h = leftEnd.next;
        ListNode t = rightStart;
        while (right > 0) {
            t = rightStart;
            rightStart = rightStart.next;
            right--;
        }
        leftEnd.next = null;
        t.next = null;
        cur = h;
        prev = null;
        while (cur != null) {
            next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        leftEnd.next = prev;
        h.next = rightStart;
        return dummy.next;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        SReverseBetween sol = new SReverseBetween();
        sol.reverseBetween(head, 1, 1);
    }
}