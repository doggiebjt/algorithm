public class Main {
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
