import jdk.nashorn.internal.objects.annotations.Getter;

import java.util.Objects;

public class Array<Element> {
    // Element 表示类型
    private Element[] data;
    private int size;  // 数组中元素数量 指向第一个没有元素的位置

    /**
     *
     * @param capacity 数组容量构造函数
     */
    public Array(int capacity){
        data = (Element[]) new Object[capacity];  // 使用范型方法 强制类型转换
        size = 0;
    }

    /**
     * 无参构造函数
     */
    public Array(){
        this(16);  // TODO 语法问题
    }

    public int getSize(){
        return size;
    }

    public int getCapacity(){
        return data.length;
    }

    public boolean isEmpty(){
        return size == 0;
    }

    public void addLast(Element e){
        if(size == data.length){
            // 抛出异常
            throw new IllegalArgumentException("AddLast failed. Array is full.");
        }
        data[size] = e;
        size ++;
    }

    public void addFirst(Element e){
        add(0, e);
    }

    // 向数组中添加元素
    public void add(int index, Element e){
        if(index < 0 || index > size){
            throw new IllegalArgumentException("Add failed. Index is abnormal.");
        }

        if(size == data.length){
            resize(2 * data.length);  // resize 操作
        }

        for(int i = size - 1; i >= index; i--){
            data[i+1] = data[i];
        }

        data[index] = e;
        size ++;
    }

    public Element get(int index){
        if(index < 0 || index >= size){
            throw new IllegalArgumentException("Get failed. Index is abnormal.");
        }
        return data[index];
    }
    public Element getLast(){
        return get(size-1);
    }

    public Element getFirst(){
        return get(0);
    }

    public void set(int index, Element e){
        if(index < 0 || index >= size){
            throw new IllegalArgumentException("Get failed. Index is abnormal.");
        }
        data[index] = e;
    }

    // 查找数组中是否有元素 e
    public boolean contains(Element e){
        for(int i = 0; i < size; i ++){
            if(data[i].equals(e)){  // 注意 equals 和 == 区别
                return true;
            }
        }
        return false;
    }

    // 查找元素 e 并返回索引
    public int find(Element e){
        for(int i = 0; i < size; i ++){
            if(data[i].equals(e)){
                return i;
            }
        }
        return -1;
    }

    // 从数组中删除元素 并返回元素
    public Element remove(int index){
        // 返回删除元素值
        if(index < 0 || index >= size) {
            throw new IllegalArgumentException("Remove failed. Index is abnormal.");
        }
        Element ret = data[index];
        for (int i = index+1; i < size; i++){
            data[i-1] = data[i];
        }
        size --;
        data[size] = null;  // Java 垃圾回收

        if(size == data.length / 4 && data.length / 2 != 0){  // 使用 lazy 方式防止复杂度震荡
            resize(data.length / 2);
        }

        return ret;
    }

    // 删除第一个元素
    public Element removeFirst(){
        return remove(0);
    }

    // 删除最后一个元素
    public Element removeLast(){
        return remove(size-1);
    }

    // 从数组中删除元素 返回是否删除元素
    public boolean removeElement(Element e){
        int index = find(e);
        if(index != -1){
            remove(index);
            return true;
        }
        return false;
    }

    @Override
    public String toString(){
        StringBuilder res = new StringBuilder();
        res.append(String.format("Array: size = %d, capacity = %d\n", size, data.length));
        res.append(String.format("["));
        for(int i=0; i<size; i++){
            res.append(String.format("%s, ", data[i]));
        }
        res.append(String.format("]"));

        return res.toString();
    }

    private void resize(int newCapacity){
        Element[] newData = (Element[]) new Object[newCapacity];
        for(int i = 0; i < size; i ++){
            newData[i] = data[i];
        }
        data = newData;
    }
}
