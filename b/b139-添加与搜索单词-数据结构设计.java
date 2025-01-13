import java.util.HashMap;

class WordDictionary {
    HashMap<Character, WordDictionary> memo;
    boolean isEnd;

    public WordDictionary() {
        this.memo = new HashMap<Character, WordDictionary>();
        this.isEnd = false;
    }

    public void addWord(String word) {
        WordDictionary node = this;
        for (char ch : word.toCharArray()) {
            if (!node.memo.containsKey(ch)) {
                node.memo.put(ch, new WordDictionary());
            }
            node = node.memo.get(ch);
        }
        node.isEnd = true;
    }

    public boolean search(String word) {
        return subSearch(this, word, 0);
    }

    private boolean subSearch(WordDictionary node, String word, int idx) {
        if (word.length() == idx) {
            return node.isEnd;
        }
        char ch = word.charAt(idx);
        if (ch == '.') {
            for (char key : node.memo.keySet()) {
                if (subSearch(node.memo.get(key), word, idx + 1)) {
                    return true;
                }
            }
        }
        if (!node.memo.containsKey(ch)) {
            return false;
        }
        return subSearch(node.memo.get(ch), word, idx + 1);
    }

    public static void main(String[] args) {
        WordDictionary obj = new WordDictionary();
        obj.addWord("abx");
        boolean param_2 = obj.search("ab.");
        System.out.println(param_2);
    }
}
