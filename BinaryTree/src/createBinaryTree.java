import java.util.LinkedList;

// 递归创建二叉树
public class createBinaryTree {

    public static TreeNode createBinaryTree(LinkedList<Integer> list){
        // TODO 创建二叉树过程有问题 待修改
        TreeNode node = null;
        if(list == null || list.isEmpty()){
            return null;
        }
        Integer data = list.removeFirst();
        node = new TreeNode(data);

        if(data!=null){
            node.left = createBinaryTree(list);
            node.right = createBinaryTree(list);
        }
        return node;
    }

    public static void main(String[] args) {
        LinkedList<Integer> intList = new LinkedList<>();
        for(int i=0; i<= 10; i++) {
            intList.add(i);
        }

        TreeNode node = createBinaryTree(intList);
        System.out.println(node);
    }
}
