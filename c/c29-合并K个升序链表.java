import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

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
class MergeKLists {
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

    // 333
    // public ListNode mergeKLists(ListNode[] lists) {
    // PriorityQueue<ListNode> pq = new PriorityQueue<>((o1, o2) ->
    // Integer.compare(o1.val, o2.val));

    // for (ListNode head : lists) {
    // if (head != null) {
    // pq.add(head);
    // }
    // }
    // ListNode res = new ListNode();
    // ListNode dummy = res;
    // while (!pq.isEmpty()) {
    // ListNode temp = pq.poll();
    // dummy.next = temp;
    // dummy = dummy.next;
    // if (temp.next != null) {
    // pq.add(temp.next);
    // }
    // }
    // return res.next;
    // }
    // 222
    private void swap(List<ListNode> list, int i, int j) {
        ListNode temp = list.get(i);
        list.set(i, list.get(j));
        list.set(j, temp);
    }

    private void downFilter(List<ListNode> list, int n, int i) {
        int left = 2 * i + 1;
        int right = left + 1;
        int temp = i;
        if (left < n && list.get(left).val < list.get(temp).val) {
            temp = left;
        }
        if (right < n && list.get(right).val < list.get(temp).val) {
            temp = right;
        }
        if (temp != i) {
            swap(list, temp, i);
            downFilter(list, n, temp);
        }

    }

    public ListNode mergeKLists(ListNode[] lists) {
        List<ListNode> list = new ArrayList<>();
        for (ListNode head : lists) {
            if (head != null) {
                list.add(head);
            }
        }
        int n = list.size();
        for (int i = n / 2 - 1; i >= 0; i--) {
            downFilter(list, n, i);
        }
        ListNode res = new ListNode();
        ListNode dummy = res;
        int i = n;
        while (i > 0) {
            ListNode temp = list.get(0);
            dummy.next = temp;
            dummy = dummy.next;
            if (temp.next != null) {
                list.set(0, temp.next);
            } else {
                swap(list, 0, i - 1);
                i--;
            }
            downFilter(list, i, 0);
        }
        return res.next;
    }
    // 111
    // public ListNode mergeKLists(ListNode[] lists) {
    // if (lists.length == 0) {
    // return null;
    // }
    // ListNode res = lists[0];
    // for (int i = 1; i < lists.length; i++) {
    // res = merge2Lists(res, lists[i]);
    // }
    // return res;
    // }

    // private ListNode merge2Lists(ListNode head1, ListNode head2) {
    // ListNode res = new ListNode();
    // ListNode dummy = res;
    // while (head1 != null && head2 != null) {
    // if (head1.val <= head2.val) {
    // dummy.next = head1;
    // head1 = head1.next;
    // } else {
    // dummy.next = head2;
    // head2 = head2.next;
    // }
    // dummy = dummy.next;
    // }
    // if (head1 != null) {
    // dummy.next = head1;
    // head1 = head1.next;
    // }
    // if (head2 != null) {
    // dummy.next = head2;
    // head2 = head2.next;
    // }
    // return res.next;
    // }
}