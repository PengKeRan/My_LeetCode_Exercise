import java.util.*;

public class MyHashMap<K, V> {
    static final class Node<K, V> {
        int hash;
        K key;
        V val;
    }

    static final class TreeNode<K, V> {
        int hash;
        K key;
        V val;

        public TreeNode putTreeVal(int hash, K key, V val) {
            return null;
        }
    }

    Node<K, V>[] table;

    static final int hash(Object key) {
        int h;
        return (key == null) ? 0 : (h = key.hashCode()) ^ (h >>> 16);
    }

    public V put(K key, V val) {
        return putVal(hash(key), key, val, false, true);
    }

    final V putVal(int hash, K key, V val, boolean onlyIfAbsent, boolean evict) {
        Node<K, V>[] tab;
        Node<K, V> p;
        int n, i;
        tab = table;
        // 整个map未初始化或为空
        if (tab == null || tab.length == 0) {
            n = (tab = resize()).length;
        }
        // 对应的桶为空
        if (tab[hash & (n - 1)] == null) {
            tab[i] = newNode(hash, key, val, null);
        } else {
            Node<K, V> e;
            K k;
            p = tab[hash & (n - 1)];
            if (p.hash == hash && (p.key == key || (key != null && key.equals(k)))) {
                e = p;
            } else if (p instanceof TreeNode) { // 红黑树
                e = ((TreeNode<K, V>) p).putTreeVal(hash, key, val);
            } else {
                for (int cnt = 0;; cnt += 1) {
                    if ((e = p.next) == null) {
                        p.next = newNode(hash, key, val, null);
                        if (cnt >= 8 - 1) {
                            treeifyBin(tab, hash);
                        }
                    }
                    if (e.hash == hash && e.key == key) {
                        break;
                    }
                    p = e;
                }
            }
            if (e != null) {
                V oldVal = e.val;
                e.val = val;
                return oldVal;
            }
        }
        modcount += 1;
        if (++size > threshold) {
            resize();
        }
        return null;
    }

}
