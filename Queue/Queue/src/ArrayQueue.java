public class ArrayQueue<E> implements Queue<E>{
    private Array<E> array;

    public ArrayQueue(int capacity){
        array = new Array<E>(capacity);
    }

    public ArrayQueue(){
        array = new Array<E>();
    }

    @Override
    public int getSize(){
        return array.getSize();
    }

    @Override
    public boolean isEmpty(){
        return array.isEmpty();
    }

    public int getCapacity(){
        return array.getCapacity();
    }

    @Override
    public void enqueue(E e){
        // 时间复杂度 O(1) 级别
        array.addLast(e);
    }

    @Override
    public E dequeue(){
        // 时间复杂度 O(n) 级别
        return array.removeFirst();
    }

    @Override
    public E getFront(){
        return array.getFirst();
    }

    @Override
    public String toString(){
        StringBuilder res = new StringBuilder();
        res.append("Stack: ");
        res.append("front [");
        for(int i=0; i < array.getSize(); i ++){
            res.append(array.get(i));
            res.append(", ");
        }
        res.append("] tail");
        return res.toString();
    }
    
    public static void main(String[] args){
        ArrayQueue<Integer> queue = new ArrayQueue<>();

        for(int i = 0; i < 10; i ++){
            queue.enqueue(i);
            System.out.println(queue);

            if(i % 3 == 2){
                queue.dequeue();
                System.out.println(queue);
            }
        }
    }

}
