public class Main {

    public static void main(String[] args) {
        // Java 原生数组为静态数组
        int [] arr = new int[10];  // 使用数组必须声明数组长度 默认为零
        for(int i = 0; i < arr.length; i++){
            arr[i] = i;
        }

        int[] scores = new int[] {100, 98, 86};  // 直接声明数组元素
        for(int i = 0; i < scores.length; i++){
            System.out.println(scores[i]);
        }

        for(int score: scores){  // 数组为可遍历/可叠代对象
            System.out.println(score);
        }

        // Java 动态数组
        Array<Integer> arr2 = new Array<Integer>();  // 包装类
        for(int i = 0; i < 16; i++){
            arr2.addLast(i);
        }
        System.out.println(arr2);

        arr2.add(0, 5);
        System.out.println(arr2);

        arr2.addFirst(10);
        System.out.println(arr2);

        arr2.remove(2);
        System.out.println(arr2);

        arr2.removeElement(4);
        System.out.println(arr2);
    }
}
