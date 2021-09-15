public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    public TreeNode(int val){
        this.val = val;
        this.left = null;
        this.right = null;
    }

    @Override
    public String toString(){
        StringBuilder res = new StringBuilder();
        if(left == null){
            res.append(String.format("TreeNode: val = %s, left = null, right = %s\n", val, right.val));
        }else if(right == null){
            res.append(String.format("TreeNode: val = %s, left = %s, right = null\n", val, left.val));
        }else{
            res.append(String.format("TreeNode: val = %s, left = %s, right = %s\n", val, left.val, right.val));
        }

        return res.toString();
    }

    public static void main(String[] args) {
        // 测试 TreeNode 类
        TreeNode tree1 = new TreeNode(0);
        TreeNode tree2 = new TreeNode(1);
        TreeNode tree3 = new TreeNode(2);
        tree1.left = tree2;
        tree1.right = tree3;
        System.out.println(tree1);
    }
}
