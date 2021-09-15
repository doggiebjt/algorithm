public class LinkedList<E> {

    // 设计为内部类
    private class Node {
        public E e;
        public Node next;

        public Node(E e, Node next) {
            this.e = e;
            this.next = next;
        }

        public Node(E e) {
            this(e, null);
        }

        public Node() {
            this(null, null);
        }

        @Override
        public String toString(){
            return e.toString();
        }
    }

    private Node dummyHead;  // 使用虚拟头节点
    int size;

    // 初始化增加虚拟头节点
    public void  LinkedList(){
        dummyHead = new Node(null, null);
        size = 0;
    }

    // 获取链表重的元素个数
    public int getSize(){
        return size;
    }

    // 返回链表是否为空
    public boolean inEmpty(){
        return size == 0;
    }

    // 链表中间添加元素
    // 链表的index位置添加元素e
    public void add(int index, E e){

        if(index < 0 || index > size){
            throw new IllegalArgumentException("Add failed. Illegal index.");
        }

        // KEY: 寻找待插入节点的前一个节点
        Node prev = dummyHead;
        for(int i = 0; i < index; i ++){
            prev = prev.next;
        }

//            Node node = new Node(e);
//            node.next = prev.next;
//            prev.next = node;

        prev.next = new Node(e, prev.next);  // 与上面三句同意
        size ++;
    }

    // 在链表头添加新元素
    public void addFirst(E e){
//            Node node = new Node(e);
//            node.next = head;
//            head = node;

        add(0, e);
    }

    // 再链表的末尾添加元素e
    public void addLast(E e){
        add(size, e);
    }

    // 获取链表中index元素
    public E get(int index){
        if(index < 0 || index > size){
            throw new IllegalArgumentException("Add failed. Illegal index.");
        }

        Node cur = dummyHead.next;  // 从dummyHead的下一个元素开始遍历
        for(int i = 0; i < index; i ++){
            cur = cur.next;
        }
        return cur.e;
    }

    // 获取链表第一个元素
    public E getFirst(){
        return get(0);
    }

    // 获取链表最后一个元素
    public E getLast(){
        return get(size - 1);
    }

    // 更新链表中index元素
    public void set(int index, E e){
        if(index < 0 || index > size){
            throw new IllegalArgumentException("Add failed. Illegal index.");
        }

        Node cur = dummyHead.next;  // 从dummyHead的下一个元素开始遍历
        for(int i = 0; i < index; i ++){
            cur = cur.next;
        }
        cur.e = e;
    }

    // 查找链表中是否存在元素
    public boolean contains(E e){
        Node cur = dummyHead.next;
        while (cur != null){
            if(cur.e.equals(e)){
                return true;
            }
            cur = cur.next;
        }
        return false;
    }

    @Override
    public String toString(){
        StringBuilder res = new StringBuilder();

//        Node cur = dummyHead.next;
//        while (cur != null){
//            res.append(cur + "->");
//            cur = cur.next;
//        }

        for(Node cur = dummyHead.next; cur != null; cur = cur.next){
            res.append(cur + "->" );
        }
        res.append("null");

        return res.toString();
    }

    public static void main(String[] args){
        LinkedList<Integer> linkedList = new LinkedList<>();
        for(int i = 0; i < 10; i ++){
            linkedList.addFirst(i);
            System.out.println(linkedList);
        }
        linkedList.add(2, 12);
        System.out.println(linkedList);
    }
}
