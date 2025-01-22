import java.util.ArrayList;
import java.util.List;

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
class SortList {
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

    private List<ListNode> split(ListNode head) {
        if (head == null || head.next == null) {
            List<ListNode> res = new ArrayList<>();
            res.add(head);
            res.add(null);
            return res;
        }
        ListNode slow = head, fast = head, prev = null;
        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode head2 = slow; // 第二部分的起点
        prev.next = null; // 断开链表
        List<ListNode> res = new ArrayList<>();
        res.add(head);
        res.add(head2);
        return res;
    }

    private ListNode merge(ListNode head1, ListNode head2) {
        ListNode res = new ListNode();
        ListNode dummy = res;
        while (head1 != null && head2 != null) {
            if (head1.val < head2.val) {
                dummy.next = head1;
                head1 = head1.next;
            } else {
                dummy.next = head2;
                head2 = head2.next;
            }
            dummy = dummy.next;
        }
        while (head1 != null) {
            dummy.next = head1;
            head1 = head1.next;
            dummy = dummy.next;
        }
        while (head2 != null) {
            dummy.next = head2;
            head2 = head2.next;
            dummy = dummy.next;
        }
        return res.next;
    }

    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        List<ListNode> temp = split(head);
        ListNode left = sortList(temp.get(0));
        ListNode right = sortList(temp.get(1));
        return merge(left, right);
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));
        SortList sol = new SortList();
        ListNode res = sol.sortList(head);
        System.out.println(sol.sortList(head));
    }
}