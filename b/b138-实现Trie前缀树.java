
class Trie {

    Trie[] children;
    boolean isEnd;

    public Trie() {
        this.children = new Trie[26];
        this.isEnd = false;
    }

    public void insert(String word) {
        char[] word_arr = word.toCharArray();
        int idx = 0;
        Trie node = this;
        while (idx < word_arr.length) {
            char ch = word_arr[idx];
            int index = (int) ch - (int) ('a');
            if (node.children[index] == null) {
                node.children[index] = new Trie();
            }
            node = node.children[index];
            idx++;
        }
        node.isEnd = true;
    }

    public boolean search(String word) {
        Trie node = this;
        for (char ch : word.toCharArray()) {
            int index = (int) ch - (int) ('a');
            if (node.children[index] == null) {
                return false;
            }
            node = node.children[index];
        }
        if (node.isEnd != true) {
            return false;
        }
        return true;
    }

    public boolean startsWith(String prefix) {
        Trie node = this;
        for (char ch : prefix.toCharArray()) {
            int index = (int) ch - (int) ('a');
            if (node.children[index] == null) {
                return false;
            }
            node = node.children[index];
        }
        return true;
    }

    public static void main(String[] args) {
        Trie obj = new Trie();
        obj.insert("trie");
        boolean param_2 = obj.search("trie");
        System.out.println(param_2);
        boolean param_3 = obj.startsWith("tr");
        System.out.println(param_3);
    }
}

// Your Trie object will be instantiated and called as such:
// Trie obj = new Trie();
// obj.insert(word);
// boolean param_2 = obj.search(word);
// boolean param_3 = obj.startsWith(prefix);
