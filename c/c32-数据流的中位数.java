import java.util.*;

class MedianFinder {

    PriorityQueue<Integer> pq_small;
    PriorityQueue<Integer> pq_large;
    int n1, n2;

    public MedianFinder() {
        this.pq_small = new PriorityQueue<>((a, b) -> (b - a));
        this.pq_large = new PriorityQueue<>();
        this.n1 = 0;
        this.n2 = 0;
    }

    public void addNum(int num) {
        if (n1 == 0) {
            pq_small.add(num);
            n1 += 1;
            return;
        }
        if (num <= findMedian()) {
            pq_small.add(num);
            n1 += 1;
        } else {
            pq_large.add(num);
            n2 += 1;
        }
        if (n1 - n2 == 2) {
            pq_large.add(pq_small.poll());
            n1 -= 1;
            n2 += 1;
        }
        if (n2 - n1 == 2) {
            pq_small.add(pq_large.poll());
            n1 += 1;
            n2 -= 1;
        }
    }

    public double findMedian() {
        if (n1 == n2) {
            return (pq_small.peek() + pq_large.peek()) / 2.0;
        }
        return n1 > n2 ? pq_small.peek() : pq_large.peek();
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */