// 427. 建立四叉树
// Definition for a QuadTree node.

class Solution {
    static class Node {
        public boolean val;
        public boolean isLeaf;
        public Node topLeft;
        public Node topRight;
        public Node bottomLeft;
        public Node bottomRight;

        public Node() {
            this.val = false;
            this.isLeaf = false;
            this.topLeft = null;
            this.topRight = null;
            this.bottomLeft = null;
            this.bottomRight = null;
        }

        public Node(boolean val, boolean isLeaf) {
            this.val = val;
            this.isLeaf = isLeaf;
            this.topLeft = null;
            this.topRight = null;
            this.bottomLeft = null;
            this.bottomRight = null;
        }

        public Node(boolean val, boolean isLeaf, Node topLeft, Node topRight, Node bottomLeft, Node bottomRight) {
            this.val = val;
            this.isLeaf = isLeaf;
            this.topLeft = topLeft;
            this.topRight = topRight;
            this.bottomLeft = bottomLeft;
            this.bottomRight = bottomRight;
        }
    }

    int[][] grid;

    public Node construct(int[][] grid) {
        this.grid = grid;
        int n = grid.length;
        return nodeConstruct(0, n, 0, n);
    }

    private Node nodeConstruct(int rowL, int rowR, int colL, int colR) {
        if (rowL == rowR - 1 || colL == colR - 1) {
            return new Node(grid[rowL][colL] == 1, true);
        }
        if (rowL == rowR || colL == colR) {
            return null;
        }
        int first = grid[rowL][colL];
        for (int i = rowL; i < rowR; i++) {
            for (int j = colL; j < colR; j++) {
                if (grid[i][j] != first) {
                    return new Node(true, false,
                            nodeConstruct(rowL, (rowR + rowL) / 2, colL, (colL + colR) / 2),
                            nodeConstruct(rowL, (rowR + rowL) / 2, (colL + colR) / 2, colR),
                            nodeConstruct((rowR + rowL) / 2, rowR, colL, (colL + colR) / 2),
                            nodeConstruct((rowR + rowL) / 2, rowR, (colL + colR) / 2, colR));
                }
            }
        }
        return new Node(grid[rowL][colL] == 1, true);
    }
}