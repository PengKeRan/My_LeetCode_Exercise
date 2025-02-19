import java.util.*;

public class MySkipList {
    private static final int MAX_LEVEL = 16;
    private static final double PROB = 0.5;
    private int levelCount = 1;
    private Node h = new Node();

    class Node {
        private int data = -1;
        private Node[] forward = new Node[MAX_LEVEL];
        private int maxLevel = 0;

        @Override
        public String toString() {
            return "Node{" +
                    "data=" + data +
                    ", maxLevel=" + maxLevel +
                    '}';
        }
    }

    public MySkipList() {
    }

    private int randomLevel() {
        int level = 1;
        while (Math.random() > PROB && level < MAX_LEVEL) {
            ++level;
        }
        return level;
    }

    public void add(int val) {
        int level = randomLevel();
        Node node = new Node();
        node.data = val;
        node.maxLevel = level;
        Node[] maxOfMinArr = new Node[level];
        for (int i = 0; i < level; i++) {
            maxOfMinArr[i] = h;
        }
        Node head = h;
        for (int i = level - 1; i >= 0; i--) {
            while (head.forward[i] != null && head.forward[i].data < val) {
                head = head.forward[i];
            }
            maxOfMinArr[i] = head;
        }
        for (int i = 0; i < level; i++) {
            node.forward[i] = maxOfMinArr[i].forward[i];
            maxOfMinArr[i].forward[i] = node;
        }
        if (levelCount < level) {
            levelCount = level;
        }
    }

    public Node get(int val) {
        Node head = h;
        for (int i = levelCount - 1; i >= 0; i--) {
            while (head.forward[i] != null && head.forward[i].data < val) {
                head = head.forward[i];
            }
        }
        if (head.forward[0] != null && head.forward[0].data == val) {
            return head.forward[0];
        }
        return null;
    }

    public void delete(int val) {
        Node head = h;
        Node[] maxOfMinArr = new Node[levelCount];
        for (int i = levelCount - 1; i >= 0; i--) {
            while (head.forward[i] != null && head.forward[i].data < val) {
                head = head.forward[i];
            }
            maxOfMinArr[i] = head;
        }

        if (head.forward[0] != null && head.forward[0].data == val) {
            for (int i = levelCount - 1; i >= 0; i--) {
                if (maxOfMinArr[i].forward[i] != null && maxOfMinArr[i].forward[i].data == val) {
                    maxOfMinArr[i].forward[i] = maxOfMinArr[i].forward[i].forward[i];
                }
            }
        }

        while (levelCount > 1 && h.forward[levelCount - 1] == null) {
            levelCount -= 1;
        }

    }

    public void printAll() {
        Node p = h;
        // 基于最底层的非索引层进行遍历，只要后继节点不为空，则速速出当前节点，并移动到后继节点
        while (p.forward[0] != null) {
            System.out.println(p.forward[0]);
            p = p.forward[0];
        }

    }

    public static void main(String[] args) {
        MySkipList skipList = new MySkipList();
        for (int i = 0; i < 24; i++) {
            skipList.add(i);
        }

        System.out.println("**********输出添加结果**********");
        skipList.printAll();

        MySkipList.Node node = skipList.get(22);
        System.out.println("**********查询结果:" + node + " **********");

        skipList.delete(22);
        System.out.println("**********删除结果**********");
        skipList.printAll();
    }
}
