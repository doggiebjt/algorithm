public class MaxHeap<E extends Comparable<E>> {
    private Array<E> data;

    public MaxHeap(int capacity){
        data = new Array<>(capacity);
    }

    public MaxHeap(){
        data = new Array<>();
    }

    // 返回堆中元素个数
    public int size(){
        return data.getSize();
    }

    // 返回一个布尔值，表示堆中是否为空
    public boolean isEmpty(){
        return data.isEmpty();
    }

    private int parent(int index){
        if (index == 0)
            throw new IllegalArgumentException("index 0 does not have parent.");
        return (index - 1) / 2;
    }

    private int leftChild(int index){
        return index * 2 + 1;
    }

    private int rightChild(int index){
        return index * 2 + 2;
    }

    // 向堆中添加元素
    public void add(E e){
        data.addLast(e);
        siftUp(data.getSize() - 1);
    }

    private void siftUp(int k){
        while (k > 0 && data.get(parent(k)).compareTo(data.get(k)) < 0){
            data.swap(k, parent(k));
            k = parent(k);
        }
    }

    public E findMax(){
        if(data.getSize() == 0)
            throw new IllegalArgumentException("heap is empty.");
        return data.get(0);
    }

    // 从堆中取出元素
    public E extractMax(){
        E ret = findMax();

        data.swap(0, data.getSize() - 1);
        data.removeLast();
        siftDown(0);

        return ret;
    }

    private void siftDown(int k){
        while (leftChild(k) < data.getSize()){  // 注意左孩子小于数组长度
            // 寻找左右孩子最大值
            int j = leftChild(k);
            if(j + 1 < data.getSize() && data.get(j + 1).compareTo(data.get(j)) > 0)
                j = rightChild(k);

            if(data.get(k).compareTo(data.get(j)) >= 0)
                break;
            data.swap(k, j);
            k = j;
        }
    }

    // raplace 取出最大元素并放入新元素
    // 堆顶元素替换后 siftDown
    public E replace(E e){
        E ret = findMax();
        data.set(0, e);
        siftDown(0);
        return ret;
    }

    // 数组 heapify O(n)
    // 从最后一个非叶子节点 siftDown
    // 寻找最后一个节点的父亲节点
    // n个元素逐一插入空堆 siftUp O(nlogn)
    public MaxHeap(E[] arr){
        data = new Array<>(arr);  // 修改Array构造函数 动态数组
        for(int i = parent(arr.length - 1); i>= 0; i--)
            siftDown(i);
    }
}
