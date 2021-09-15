import java.util.Stack;

public class Solution_Isvalid_1 {

    public boolean isValid(String s){
        // 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s
        Stack<Character> stack = new Stack<Character>();

        for(int i = 0; i < s.length(); i ++){
            char c = s.charAt(i);
            if(c == '(' || c == '[' || c == '{'){
                stack.push(c);
            }else{
                if(stack.isEmpty()){
                    return false;
                }

                char topChar = stack.pop();
                if(c == ')' && topChar != '('){
                    return false;
                }
                if(c == ']' && topChar != '['){
                    return false;
                }
                if(c == '}' && topChar != '{'){
                    return false;
                }
            }
        }

        return stack.isEmpty();
    }

    public static void main(String[] args){
        // 本地测试程序
        System.out.println((new Solution_Isvalid_2()).isValid("([{}])"));
        System.out.println((new Solution_Isvalid_2()).isValid("({}])"));
    }
}
