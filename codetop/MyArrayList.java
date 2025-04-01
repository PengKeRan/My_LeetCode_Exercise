import java.util.*;

public class MyArrayList<E> {

    private static final int DEFAULT_CAPACITY = 10;
    private static final Object[] DEFAULT_EMPTY_ELEMENTS = {};
    private int size = 0;
    transient Object[] elementData;

    public MyArrayList() {
        this.elementData = DEFAULT_EMPTY_ELEMENTS;
    }

    public MyArrayList(int capcity) {
        if (capcity > 0) {
            this.elementData = new Object[capcity];
        } else if (capcity == 0) {
            this.elementData = DEFAULT_EMPTY_ELEMENTS;
        } else {
            throw new IllegalArgumentException("Illegal Capacity");
        }
    }

    private void grow() {
        if (size == 0) {
            elementData = new Object[DEFAULT_CAPACITY];
        } else {
            int oldCapacity = elementData.length;
            int newCapacity = oldCapacity + (oldCapacity >> 1);
            elementData = Arrays.copyOf(elementData, newCapacity);
        }
    }

    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean contains(Object o) {
        return indexOf(o) >= 0;
    }

    public int indexOf(Object o) {
        if (o != null) {
            for (int i = 0; i < size; i++) {
                if (elementData[i].equals(o)) {
                    return i;
                }
            }
        } else {
            for (int i = 0; i < size; i++) {
                if (elementData[i] == null) {
                    return i;
                }
            }
        }
        return -1;
    }

    public void add(Object o) {
        if (size == 0 || size == elementData.length) {
            grow();
        }
        elementData[size] = o;
        size += 1;
    }

    public E remove(int index) {
        rangeCheck(index);
        E removeElemenet = (E) elementData[index];
        if (index != size - 1) {
            for (int i = index; i < size - 1; i++) {
                elementData[i] = elementData[i + 1];
            }
        }
        elementData[size - 1] = null;
        size--;
        return removeElemenet;
    }

    private void rangeCheck(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException(index + "out of max length" + size);
        }
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for (int i = 0; i < size; i++) {
            E e = (E) elementData[i];
            sb.append(e).append((i == size - 1 ? "" : ","));
        }
        sb.append("]");
        return sb.toString();
    }

    public static void main(String[] args) {
        MyArrayList<String> mylist = new MyArrayList<>();
        mylist.add("aaa");
        mylist.add("bb");
        mylist.add("cccc");
        System.out.println(mylist.contains("bb"));
        System.out.println(mylist.toString());
        System.out.println(mylist.size());
        System.out.println(mylist.remove(1));
        System.out.println(mylist.toString());
        System.out.println(mylist.size());
    }

}
