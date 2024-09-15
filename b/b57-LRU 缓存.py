# 146. LRU 缓存
# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# 实现 LRUCache 类：
# LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。
# 如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
class DLinkedNode:
    def __init__(self, key=0, val=0):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = dict()
        self.capacity = capacity
        self.length = 0
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def locate_and_moveToHead(self, key, val=None):
        target = self.head.next
        while target.key != key:
            target = target.next
        prev = target.prev
        next = target.next
        prev.next = next
        next.prev = prev

        target.prev = self.head
        target.next = self.head.next
        self.head.next.prev = target
        self.head.next = target
        if val:
            target.val = val
            return 0

    def add_newNode_toHead(self, key, val):
        node = DLinkedNode(key=key, val=val)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def delete_last(self):
        target = self.tail.prev
        target.prev.next = target.next
        target.next.prev = target.prev
        self.cache.pop(target.key)

    def print_list(self, node=None):
        if node:
            temp = node
        else:
            temp = self.head
        while temp:
            print(str(temp.key)+"("+str(temp.val)+")", end="-")
            temp = temp.next
        temp = self.tail
        while temp:
            print(str(temp.key)+"("+str(temp.val)+")", end="-")
            temp = temp.prev
        print("\n")

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache.keys():
            return -1
        else:
            self.locate_and_moveToHead(key=key)
            res = self.cache[key].val
            return res


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.cache.keys():
            self.cache[key] = value
            if self.length == self.capacity:
                self.delete_last()
                self.length -= 1
                self.add_newNode_toHead(key, value)
                self.length += 1
            else:
                self.length += 1
                self.add_newNode_toHead(key, value)
        else:
            self.locate_and_moveToHead(key, value)
            self.cache[key] = value
        self.print_list()


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(2, 1)  # 缓存是 {1=1}
obj.put(2, 2)  # 缓存是 {1=1, 2=2}
obj.get(2)  # 返回 1
obj.put(1, 1)  # 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
obj.put(4, 1)  # 返回 -1 (未找到)
obj.get(2)  # 返回 -1 (未找到)
