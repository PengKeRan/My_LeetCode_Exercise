import java.util.*;

class LRUCache {
    class Node {
        Node prev;
        Node next;
        int key;
        int val;
    }

    Map<Integer, Node> memo;
    Node head;
    Node tail;
    int max_capacity;

    public LRUCache(int capacity) {
        memo = new HashMap<>();
        head = new Node();
        tail = new Node();
        head.next = tail;
        tail.prev = head;
        max_capacity = capacity;
    }

    public int get(int key) {
        if (memo.containsKey(key)) {
            Node node = memo.get(key);
            moveToHead(node);
            return node.val;
        }
        return -1;
    }

    public void put(int key, int value) {
        if (memo.containsKey(key)) {
            memo.get(key).val = value;
            moveToHead(memo.get(key));
        } else {
            if (memo.size() >= max_capacity) {
                removeLastNode();
            }
            Node newNode = new Node();
            newNode.val = value;
            newNode.key = key;
            memo.put(key, newNode);
            addToHead(newNode);
        }
    }

    private void addToHead(Node node) {
        head.next.prev = node;
        node.next = head.next;
        head.next = node;
        node.prev = head;
    }

    private void moveToHead(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
        head.next.prev = node;
        node.next = head.next;
        head.next = node;
        node.prev = head;
    }

    private void removeLastNode() {
        memo.remove(tail.prev.key);
        tail.prev.prev.next = tail;
        tail.prev = tail.prev.prev;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */