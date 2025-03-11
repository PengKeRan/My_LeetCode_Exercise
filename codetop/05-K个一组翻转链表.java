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
class ReverseKGroup {
    public static class ListNode {
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

    private ListNode reverseList(ListNode head) {
        ListNode cur, next, prev;
        prev = null;
        cur = head;
        while (cur != null) {
            next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        return prev;
    }

    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode();
        ListNode prev, tail, start, end;
        int cnt = 0;
        dummy.next = head;
        prev = dummy;
        start = head;
        end = dummy;
        tail = end.next;

        while (true) {
            cnt = 0;
            prev = end;
            start = end.next;
            while (cnt < k && end != null) {
                end = end.next;
                cnt += 1;
            }
            if (end == null) {
                break;
            }
            tail = end.next;
            end.next = null;
            reverseList(start);
            prev.next = end;
            start.next = tail;

            end = start;
        }

        return dummy.next;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
        ReverseKGroup sol = new ReverseKGroup();
        sol.reverseKGroup(head, 2);
    }
}