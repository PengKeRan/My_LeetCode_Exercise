
// 23. 合并 K 个升序链表
// 给你一个链表数组，每个链表都已经按升序排列。
// 请你将所有链表合并到一个升序链表中，返回合并后的链表。
import java.util.*;

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

    // 堆排序
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode ans = new ListNode();
        int n = lists.length;
        List<ListNode> list = new ArrayList<>();
        for (ListNode node : lists) {
            list.add(node);
        }

        ListNode temp = new ListNode();
        ans = temp;
        if (list.size() == 0) {
            return ans.next;
        }
        while (true) {
            for (int j = n / 2 - 1; j >= 0; j--) {
                upfilter(list, j, n);
            }
            if (list.get(0) == null) {
                break;
            }
            temp.next = list.get(0);
            temp = temp.next;

            list.set(0, temp.next);
        }
        return ans.next;
    }

    private void upfilter(List<ListNode> arr, int pos, int n) {
        for (int childPos = 2 * pos + 1; childPos <= 2 * pos + 2 && childPos < n; childPos++) {
            if (arr.get(pos) == null && arr.get(childPos) != null ||
                    (arr.get(childPos) != null && arr.get(childPos).val < arr.get(pos).val)) {
                swap(arr, pos, childPos);
            }
        }
    }

    private void swap(List<ListNode> arr, int i, int j) {
        ListNode temp = new ListNode();
        temp = arr.get(i);
        arr.set(i, arr.get(j));
        arr.set(j, temp);
    }

    // 合并两个链表
    public ListNode mergeKLists2(ListNode[] lists) {
        ListNode ans = null;
        int n = lists.length;
        for (ListNode root : lists) {
            if (root == null) {
                continue;
            }
            ans = merge2lists(ans, root);
        }

        return ans;
    }

    private ListNode merge2lists(ListNode l1, ListNode l2) {
        ListNode res = new ListNode();
        ListNode temp = new ListNode();
        res = temp;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                temp.next = l1;
                l1 = l1.next;
                temp = temp.next;
            } else {
                temp.next = l2;
                l2 = l2.next;
                temp = temp.next;
            }
        }
        if (l1 != null) {
            temp.next = l1;
        }
        if (l2 != null) {
            temp.next = l2;
        }
        return res.next;
    }

    public static void main(String[] args) {
        MergeKLists sol = new MergeKLists();
        ListNode[] lists = new ListNode[3];

        // 初始化第一个链表: [1,4,5]
        lists[0] = new ListNode(2);
        // lists[0].next = new ListNode(4);
        // lists[0].next.next = new ListNode(5);

        // 初始化第二个链表: [1,3,4]
        lists[1] = null;
        // lists[1].next = new ListNode(3);
        // lists[1].next.next = new ListNode(4);

        // 初始化第三个链表: [2,6]
        lists[2] = new ListNode(-1);
        // lists[2].next = new ListNode(6);

        // 打印链表以验证初始化
        ListNode res = (sol.mergeKLists2(lists));

        printList(res);
    }

    private static void printList(ListNode head) {
        ListNode current = head;
        while (current != null) {
            System.out.print(current.val + " ");
            current = current.next;
        }
        System.out.println();
    }
}