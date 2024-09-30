
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
        // 堆排序
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
        int temp = pos;
        if (2 * pos + 1 < n) {
            if (arr.get(pos) == null && arr.get(2 * pos + 1) != null) {
                temp = 2 * pos + 1;
            } else if (arr.get(2 * pos + 1) != null && arr.get(2 * pos + 1).val < arr.get(pos).val) {
                temp = 2 * pos + 1;
            }
            swap(arr, pos, temp);
        }
        temp = pos;
        if (2 * pos + 2 < n) {
            if (arr.get(pos) == null && arr.get(2 * pos + 2) != null) {
                temp = 2 * pos + 2;
            } else if (arr.get(2 * pos + 2) != null && arr.get(2 * pos + 2).val < arr.get(pos).val) {
                temp = 2 * pos + 2;
            }
            swap(arr, pos, temp);
        }
    }

    private void swap(List<ListNode> arr, int i, int j) {
        ListNode temp = new ListNode();
        temp = arr.get(i);
        arr.set(i, arr.get(j));
        arr.set(j, temp);
    }

    public static void main(String[] args) {
        MergeKLists sol = new MergeKLists();
        ListNode[] lists = new ListNode[3];

        // 初始化第一个链表: [1,4,5]
        lists[0] = new ListNode(1);
        lists[0].next = new ListNode(4);
        lists[0].next.next = new ListNode(5);

        // 初始化第二个链表: [1,3,4]
        lists[1] = new ListNode(1);
        lists[1].next = new ListNode(3);
        lists[1].next.next = new ListNode(4);

        // 初始化第三个链表: [2,6]
        lists[2] = new ListNode(2);
        lists[2].next = new ListNode(6);

        // 打印链表以验证初始化
        ListNode res = (sol.mergeKLists(lists));

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