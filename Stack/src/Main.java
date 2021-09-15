public class Main {
    public static void main(String[] args){
        // 测试 Stack
        ArrayStack<Integer> stack = new ArrayStack<>();

        for(int i=0; i<5; i++){
            stack.push(i);
        }
        System.out.println(stack);

        stack.pop();
        System.out.println(stack);

        // 测试 Solution_Isvalid_1
        Solution_Isvalid_1 isValid = new Solution_Isvalid_1();
        boolean result = isValid.isValid("()");
        System.out.println(result);

        // 测试 Solution_Isvalid_2
        Solution_Isvalid_2 isValid_2 = new Solution_Isvalid_2();
        boolean resul2 = isValid_2.isValid("guo(zi)jia");
        System.out.println(resul2);
    }
}
