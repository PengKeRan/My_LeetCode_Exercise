import java.util.*;

class ListNode {
    int val;
    ListNode next = null;

    public ListNode(int val) {
        this.val = val;
    }
}

class Solution {
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     * 
     * @param a ListNode类一维数组 所有的无序单链表
     * @return ListNode类
     */
    public ListNode solve(ListNode[] a) {
        return null;
    }

    // 合并两个链表
    private void mergeList(ListNode a, ListNode b) {
        ListNode h1 = a;
        ListNode h2 = b;
        ListNode ans = new ListNode(0);
        ListNode tail = ans;
        while (h1 != null && h2 != null) {
            if (h1.val < h2.val) {
                tail.next = h1;
                h1 = h1.next;
            } else {
                tail.next = h2;
                h2 = h2.next;
            }
            tail = tail.next;
        }
        if (h1 != null) {
            tail.next = h1;
        }
        if (h2 != null) {
            tail.next = h2;
        }
        a.next = ans.next;
    }

}
