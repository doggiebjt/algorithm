# -*- coding: utf-8 -*- 
########################################################################################################################
# import random
# # random.seed(666)
#
# arr = [random.randint(0, 1000) for _ in range(20)]
# print(arr)
#
# arr = sorted(arr)
# s_num = arr[random.randint(0, len(arr))]
# print(arr)
# print(s_num)
#
# def binary_search(target, arr):
#     idx = _binary_search(target, arr, 0, len(arr))
#     return idx
#
# def _binary_search(target, arr, left, right):
#     # 左闭右开
#     if left >= right:
#         return -1
#     while left < right:
#         mid = int((left + right) / 2)
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         elif arr[mid] > target:
#             right = mid
#     return -1
#
# print(binary_search(s_num, arr))
# print(arr.index(s_num))

########################################################################################################################
# import random
#
# arr = [random.randint(0, 1000) for _ in range(20)]
#
# def quick_sort(arr):
#     _quick_sort(arr, 0, len(arr) - 1)
#
# def swap(arr, idx1, idx2):
#     arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
#
# def _quick_sort(arr, left, right):
#     # 区间左闭右闭
#     if left >= right:
#         return
#
#     # 增加随机性
#     random_idx = random.randint(left, right)
#     swap(arr, left, random_idx)
#
#     anchor = arr[left]
#     p_left = left + 1
#     p_right = right
#
#     while(True):
#         while p_left <= right and arr[p_left] <= anchor:
#             p_left += 1
#         while p_right > left and arr[p_right] >= anchor:
#             p_right -= 1
#         # 注意跳出 while 循环的 break 判断
#         if p_left >= p_right:
#             break
#         swap(arr, p_left, p_right)
#         p_left += 1
#         p_right -= 1
#
#     swap(arr, left, p_right)
#     _quick_sort(arr, left, p_right - 1)
#     _quick_sort(arr, p_right + 1, right)
#
# print(arr)
# quick_sort(arr)
# print(arr)

########################################################################################################################
# import random
#
# arr = [random.randint(0, 100) for _ in range(5)]
# reverse_cnt = 0
#
# def merge_sort(arr):
#     res = _merge_sort(arr, 0, len(arr))
#     return res
#
# def _merge_sort(arr, left, right):
#     if left >= right:
#         return []
#     if left == right - 1:
#         return arr[left:right]
#     # 区间左闭右开
#     mid = int((left + right) / 2)
#
#     merge_left = _merge_sort(arr, left, mid)
#     merge_right = _merge_sort(arr, mid, right)
#
#     res = _merge_arr(merge_left, merge_right)
#
#     return res
#
# def _merge_arr(arr_left, arr_right):
#     res = [0] * (len(arr_left) + len(arr_right))
#     p_left = 0
#     p_right = 0
#     p_res = 0
#
#     while (True):
#
#         while p_left < len(arr_left) and p_right < len(arr_right) and arr_left[p_left] <= arr_right[p_right]:
#             res[p_res] = arr_left[p_left]
#             p_left += 1
#             p_res += 1
#         while p_left < len(arr_left) and p_right < len(arr_right) and arr_right[p_right] <= arr_left[p_left]:
#             if arr_right[p_right] < arr_left[p_left]:
#                 print('REVERSED')
#             res[p_res] = arr_right[p_right]
#             p_right += 1
#             p_res += 1
#         if p_left == len(arr_left) or p_right == len(arr_right):
#             break
#
#     if p_left == len(arr_left):
#         res[p_res:] = arr_right[p_right:]
#         return res
#     if p_right == len(arr_right):
#         res[p_res:] = arr_left[p_left:]
#         return res
#
# print(arr)
# arr = merge_sort(arr)
# print(arr)
# print(reverse_cnt)

########################################################################################################################
# import random
# import copy
#
# class max_heap():
#     # 实现参考 liuyubobobo 数据结构部分代码
#     def __init__(self, cmp_meth=None, cnt_max=None):
#         # TODO 未加入 cnt_max 功能
#         self.heap_array = []
#         self.cmp_meth = cmp_meth
#         self.cnt_max = cnt_max
#
#     @staticmethod
#     def swap(arr, idx1, idx2):
#         arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
#
#     def _get_parent(self, idx):
#         return int((idx - 1) / 2)
#
#     def _left_child(self, idx):
#         return idx * 2 + 1
#
#     def _right_child(self, idx):
#         return idx * 2 + 2
#
#     def compare(self, idx1, idx2):
#         if self.cmp_meth == None:
#             # 自定义 compare 函数
#             if self.heap_array[idx1] > self.heap_array[idx2]:
#                 return True
#             return False
#         return self.cmp_meth(self.heap_array, idx1, idx2)
#
#     def add_item(self, item):
#         # 堆中添加元素
#         self.heap_array.append(item)
#         self._sift_up()
#
#     def _sift_up(self):
#         idx = len(self.heap_array) - 1
#         p_idx = self._get_parent(idx)
#         while p_idx >= 0 and self.compare(idx, p_idx):
#             self.swap(self.heap_array, idx, p_idx)
#             idx = p_idx
#             p_idx = self._get_parent(idx)
#
#     def extract_max(self):
#         # 堆中取出最大元素
#         heap_length = len(self.heap_array)
#         self.swap(self.heap_array, 0, heap_length - 1)
#         max_item = self.heap_array.pop()
#         self._sift_down(0)
#         return max_item
#
#     def _sift_down(self, pos_idx):
#         # 从 pos_idx 位置开始 sift_down
#         heap_length = len(self.heap_array)
#         left_idx = self._left_child(pos_idx)
#         right_idx = self._right_child(pos_idx)
#
#         while left_idx < heap_length:
#             max_idx = left_idx
#             if right_idx < heap_length and self.compare(right_idx, left_idx):
#                 max_idx = right_idx
#             if self.compare(pos_idx, max_idx):
#                 return
#             self.swap(self.heap_array, max_idx, pos_idx)
#             pos_idx = max_idx
#             left_idx = self._left_child(pos_idx)
#             right_idx = self._right_child(pos_idx)
#
#     def replace(self, item):
#         # 替换堆顶元素并 sift down
#         self.heap_array[0] = item
#         self._sift_down(0)
#
#     def peek(self):
#         # 返回堆顶元素
#         return self.heap_array[0]
#
#     def heapify(self):
#         last_idx = len(self.heap_array) - 1
#         parent_idx = self._get_parent(last_idx)
#         while parent_idx >= 0:
#             self._sift_down(parent_idx)
#             parent_idx -= 1
#
# random_list = [random.randint(0, 100) for _ in range(100)]
# print(random_list)
#
# # 1. 建堆方法一 堆中添加元素 O(nlogn)
# def c_meth_max(heap_array, idx1, idx2):
#     # 自定义 compare 函数
#     if heap_array[idx1] > heap_array[idx2]:
#         return True
#     return False
#
# p_queue = max_heap(c_meth_max)
# for _ in random_list:
#     p_queue.add_item(_)
# print(p_queue.heap_array)
#
# # 排序
# sortde_list = []
# for _ in range(len(p_queue.heap_array)):
#     max_item = p_queue.extract_max()
#     sortde_list.append(max_item)
# print(sortde_list)
#
# # 2. 建堆方法二 heapify O(n)
# def c_meth_min(heap_array, idx1, idx2):
#     # 自定义 compare 函数
#     if heap_array[idx1] < heap_array[idx2]:
#         return True
#     return False
#
# p_queue = max_heap(c_meth_min)
# p_queue.heap_array = copy.deepcopy(random_list)
# p_queue.heapify()
# print(p_queue.heap_array)
#
# # 排序
# sortde_list = []
# for _ in range(len(p_queue.heap_array)):
#     max_item = p_queue.extract_max()
#     sortde_list.append(max_item)
# print(sortde_list)
#
# # 3. topn 问题
# topn = 10
# topn_queue = max_heap()
# for idx, item in enumerate(random_list):
#     if idx < topn:
#         topn_queue.add_item(item)
#         continue
#     if item < topn_queue.heap_array[0]:
#         topn_queue.replace(item)
#
# print(sorted(topn_queue.heap_array, reverse=True))
#
# # 4. 数据流中位数问题
# topn = 5
# topn_max_queue = max_heap(c_meth_max, 10)
# topn_min_queue = max_heap(c_meth_min, 10)
#
# for idx, item in enumerate(random_list):
#     flag = idx % 2
#     if flag == 0:
#         # 奇数写入大顶堆
#         if len(topn_min_queue.heap_array) != 0 and topn_min_queue.peek() <= item:
#             # 先在小顶堆替换最小元素
#             min_queue_peek = topn_min_queue.peek()
#             topn_min_queue.replace(item)
#             item = min_queue_peek
#         topn_max_queue.add_item(item)
#         print(topn_max_queue.peek())
#     else:
#         # 偶数写入小顶堆
#         if len(topn_max_queue.heap_array) != 0 and topn_max_queue.peek() >= item:
#             # 先在大顶堆替换最大元素
#             max_queue_peek = topn_max_queue.peek()
#             topn_max_queue.replace(item)
#             item = max_queue_peek
#         topn_min_queue.add_item(item)
#         print((topn_max_queue.peek()+topn_min_queue.peek())/2)
#
# print(sortde_list[49], sortde_list[50])
# print(topn_max_queue.heap_array)
# print(topn_min_queue.heap_array)
#
########################################################################################################################
# import random
# import math
# # random.seed(666)
# arr = [random.randint(0, 100) for _ in range(20)]
#
# arr = sorted(arr)
# print(arr)
#
# sum_num = arr[random.randint(0, len(arr))] + arr[random.randint(0, len(arr))]
# print(sum_num)
#
# res = []
#
# def find_sum(arr, sum_num):
#     _find_sum(arr, sum_num, 0, len(arr) - 1)
#
# def _find_sum(arr, sum_num, p0, p1):
#     # 左闭右闭
#     while p0 < p1:
#         if arr[p0] + arr[p1] == sum_num:
#             res.append((arr[p0], arr[p1]))
#             p0 += 1
#             p1 -= 1
#         elif arr[p0] + arr[p1] < sum_num:
#             p0 += 1
#         else:
#             # arr[p0] + arr[p1] > sum_num
#             p1 -= 1
#
# find_sum(arr, sum_num)
# print(res)

########################################################################################################################
# # 二维数组中的查找
# arr_2d = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15], [9, 10, 16, 18]]
# target = 10
#
# def find_target_2d(arr_2d, target):
#     rows = len(arr_2d) - 1
#     cols = len(arr_2d[0]) - 1
#
#     i = 0
#     j = cols
#
#     while i <= rows and j >= 0:
#         if target == arr_2d[i][j]:
#             return i, j
#         elif target > arr_2d[i][j]:
#             i += 1
#         else:
#             # target > arr_2d[i][j]:
#             j -= 1
#
#     return -1, -1
#
# row, col = find_target_2d(arr_2d, target)
# print(target)
# print(arr_2d[row][col])

########################################################################################################################
# # 模拟创建链表方法
# from copy import deepcopy
#
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#     @staticmethod
#     def visit(node):
#         # 访问节点
#         print(node.val, end=' ')
#
# def Creat_Link_List(Data_Input):
#     p1 = ListNode(Data_Input.pop())
#     while len(Data_Input) != 0:
#         p0 = ListNode(Data_Input.pop())
#         p0.next = p1
#         p1 = p0
#     return p0
#
# Data_Input_0 = [1, 3, 5, 7]
# Data_Input_1 = [2, 4, 4, 6, 6, 8]
# Data_Input_2 = [2, 4, 6, 8]
# head_0 = Creat_Link_List(Data_Input_0)
# head_1 = Creat_Link_List(Data_Input_1)
# head_2 = Creat_Link_List(Data_Input_2)

########################################################################################################################
# # 从头到位打印链表
# def Traverse(node):
#     while node is not None:
#         ListNode.visit(node)
#         node = node.next
#
# print('head_0')
# Traverse(head_0)
# print('#')
# print('head_1')
# Traverse(head_1)
# print('#')
# print('head_2')
# Traverse(head_2)
# print('#')

########################################################################################################################
# 合并两个有序链表
# def mergeTwoLists(l1, l2):
#     dummy_head = ListNode(None)
#     cur = dummy_head
#     while l1 and l2:
#         if l1.val <= l2.val:
#             cur.next = l1
#             l1 = l1.next
#         else:
#             cur.next = l2
#             l2 = l2.next
#         cur = cur.next
#     cur.next = l1 or l2
#     return dummy_head.next
#
# Traverse(mergeTwoLists(head_0, head_1))

########################################################################################################################
# 删除排序链表中的重复元素
# def deleteDuplicates(head):
#     dummy_head = ListNode(None)
#     dummy_head.next = head
#     p0 = dummy_head
#     p1 = dummy_head.next
#     while p1 is not None:
#         if p0.val == p1.val:
#             p0.next = p1.next
#             tmp = p1.next
#             p1.next = None
#             p1 = tmp
#         p0 = p0.next
#         p1 = p1.next
#
#     return dummy_head.next
#
# Traverse(deleteDuplicates(head_1))

########################################################################################################################
# 判断环形链表
# print('check LinkList')
# Traverse(head_1)
# print('init cycle')
# head_cycle = head_1
# while head_cycle and head_cycle.next:
#     print(head_cycle.val)
#     head_cycle = head_cycle.next
# print(head_cycle.val)
# head_cycle.next = head_1.next
# # Traverse(head_1)  # 死循环
# Traverse(head_2)
#
# def hasCycle(head):
#     fast = head
#     slow = head
#     while fast and fast.next:
#         fast = fast.next.next
#         slow = slow.next
#         if slow == fast:
#             return True
#     return False
#
# print(hasCycle(head_0))
# print(hasCycle(head_2))

########################################################################################################################
# 相交链表
# Data_Input_0 = [1, 3, 5, 7]
# Data_Input_1 = [2, 4, 6, 8]
# Data_Input_2 = [9, 10, 11, 12]
# head_0 = Creat_Link_List(Data_Input_0)
# head_1 = Creat_Link_List(Data_Input_1)
# head_2 = Creat_Link_List(Data_Input_2)
#
# temp_head = head_0
# while temp_head and temp_head.next:
#     temp_head = temp_head.next
# temp_head.next = head_2
#
# temp_head = head_1
# while temp_head and temp_head.next:
#     temp_head = temp_head.next
# temp_head.next = head_2
#
# Traverse(head_0)
# Traverse(head_1)
#
# def getIntersectionNode(headA, headB):
#     p0 = headA
#     p1 = headB
#     while p0 != p1:
#         if p0 is None:
#             p0 = headA
#         else:
#             p0 = p0.next
#         if p1 is None:
#             p1 = headB
#         else:
#             p1 = p1.next
#     return p0
#
# print(getIntersectionNode(head_0, head_2).val)

########################################################################################################################
# 移除链表元素
# print('before remove element')
# Traverse(head_2)
#
# def removeElements(head, val):
#     dummy_head = ListNode(None)
#     dummy_head.next = head
#     p0 = dummy_head
#     p1 = dummy_head.next
#     while p1 is not None:
#         if p1.val == val:
#             tmp = p1
#             p0.next = p1.next
#             tmp.next = None
#         else:
#             p0 = p0.next
#         p1 = p1.next
#     return dummy_head.next
#
# removeElements(head_2, 4)
#
# print('after remove element')
# Traverse(head_2)

########################################################################################################################
# 反转链表
# print('before reverse list')
# Traverse(head_2)
#
# def reverseList(head):
#     if head is None:
#         return head
#     p0 = head
#     p1 = head.next
#     p0.next = None
#     while p1:
#         tmp = p1.next
#         p1.next = p0
#         p0 = p1
#         p1 = tmp
#     return p0
#
# head_2 = reverseList(head_2)
#
# print('after reverse list')
# Traverse(head_2)

########################################################################################################################
# 删除链表中的节点
# def deleteNode(node):
#     node.val = node.next.val
#     node.next = node.next.next

########################################################################################################################
# 回文链表

########################################################################################################################
# # 模拟创建二叉树方法
# from copy import deepcopy
#
# class TreeNode(object):
#     def __init__(self, x):  # 初始化变量
#         self.data = x
#         self.left = None  # 左孩子
#         self.right = None  # 右孩子
#
#     @staticmethod
#     def visit(Root):
#         # 访问节点
#         print(Root.data, end=' ')
#
# def Creat_Binary_Tree(Data_Input):
#     # 类似先序遍历的建树过程
#     if len(Data_Input) == 0:
#         return
#     if Data_Input[0] != 0:
#         Root = TreeNode(Data_Input[0])  # 给Root赋给空间并且初始化
#         Data_Input.pop(0)  # pop处第一个数据，这样第一个数据就是原来的第二个位置上的数据如原来是[1,2,3]这样就变成[2,3]
#         # print(Data_Input)  # 输出当前列表中的元素
#         Root.left = Creat_Binary_Tree(Data_Input)
#         Root.right = Creat_Binary_Tree(Data_Input)
#         return Root  # 将得到的节点返回
#     else:
#         Data_Input.pop(0)
#         # print(Data_Input)
#         return
#
# AVL_Input = [8, 6, 4, 0, 5, 0, 0, 0, 12, 10, 0, 0, 14, 0, 0]  # 创建二叉树需要的数据当 data=0 的时候就递归停止
# Root0 = Creat_Binary_Tree(AVL_Input)
# Root1 = deepcopy(Root0)
# AVL_Input = [6, 5, 3, 0, 4, 0, 0, 0, 11, 8,  0, 0, 24, 0, 0]
# Root2 = Creat_Binary_Tree(AVL_Input)

########################################################################################################################
# # 递归遍历二叉树
#
# # 先序遍历二叉树
# def PreOrderTraverse(Root):
#     if Root == None:
#         return
#     TreeNode.visit(Root)
#     PreOrderTraverse(Root.left)
#     PreOrderTraverse(Root.right)
#
# # 中序遍历二叉树
# def InOrderTraverse(Root):
#     if Root == None:
#         return
#     InOrderTraverse(Root.left)
#     TreeNode.visit(Root)
#     InOrderTraverse(Root.right)
#
# # 后序遍历二叉树
# def PostOrderTraverse(Root):
#     if Root == None:
#         return
#     PostOrderTraverse(Root.left)
#     PostOrderTraverse(Root.right)
#     TreeNode.visit(Root)
#
# print('PreOrderTraverse')
# PreOrderTraverse(Root1)
# print('#')
# print('InOrderTraverse')
# InOrderTraverse(Root1)
# print('#')
# print('PostOrderTraverse')
# PostOrderTraverse(Root1)
# print('#')

########################################################################################################################
# # 层序遍历二叉树
# from queue import Queue, PriorityQueue
#
# def LevelTraverse(root):
#     if root == None:
#         return
#     level_queue = Queue()
#     level_queue.put(root)
#     while not level_queue.empty():
#         root_temp = level_queue.get()
#         TreeNode.visit(root_temp)
#         if root_temp.left is not None:
#             level_queue.put(root_temp.left)
#         if root_temp.right is not None:
#             level_queue.put(root_temp.right)
#
# print('LevelTraverse')
# LevelTraverse(Root1)
# print('#')

########################################################################################################################
# 二叉树中的节点个数
# def GetNodeNum(root):
#     if root == None:
#         return 0
#     return GetNodeNum(root.left) + GetNodeNum(root.right) + 1
#
# print(GetNodeNum(Root1))

########################################################################################################################
# 二叉树的深度
# def GetDepth(root):
#     if root == None:
#         return 0
#     left_depth = GetDepth(root.left)
#     right_depth = GetDepth(root.right)
#     return max(left_depth, right_depth) + 1
#
# print(GetDepth(Root1))

########################################################################################################################
# 二叉树第 K 层节点数量
# def GetNodeNumKthLevel(root, k):
#     if k == 0 or root ==None:
#         return 0
#     if k == 1:
#         return 1
#     left_num = GetNodeNumKthLevel(root.left, k-1)
#     right_num = GetNodeNumKthLevel(root.right, k-1)
#     return left_num + right_num
#
# print(GetNodeNumKthLevel(Root1, 3))

########################################################################################################################
# 二叉树中叶子节点的个数
# def GetLeafNodeNum(root):
#     if root == None:
#         return 0
#     if root.left == None and root.right == None:
#         return 1
#     left_num = GetLeafNodeNum(root.left)
#     right_num = GetLeafNodeNum(root.right)
#     return left_num + right_num
#
# print(GetLeafNodeNum(Root1))

########################################################################################################################
# 判断两棵二叉树是否结构相同
# def StructureCmp(root0, root1):
#     if root0 == root1:
#         return True
#     if root0 == None and root1 == None:
#         return True
#     if root0 == None or root1 == None:
#         return False
#     # if root0.data != root1.data:
#     #     # 是否完全相同判断
#     #     return False
#     res_left = StructureCmp(root0.left, root1.left)
#     res_right = StructureCmp(root0.right, root1.right)
#     return (res_left and res_right)
#
# print(StructureCmp(Root0, Root1))
# print(StructureCmp(Root0, Root2))

########################################################################################################################
# TODO 判断二叉树是不是平衡二叉树
# def IsAvl(root):
#     if root == None:
#         return True, 0
#     left_predict, left_depth = IsAvl(root.left)
#     right_predict, right_depth = IsAvl(root.right)
#     if left_predict and right_predict and abs(left_depth - right_depth) <= 1:
#         return True, max(left_depth, right_depth) + 1
#     else:
#         return False, max(left_depth, right_depth) + 1
#
# print(IsAvl(Root2))

########################################################################################################################
# 二叉树的镜像
# def mirror(root):
#     if root == None:
#         return
#     pleft = mirror(root.left)
#     pright = mirror(root.right)
#
#     root.left = pright
#     root.right = pleft
#
#     return root
#
# mirror(Root0)

########################################################################################################################
# TODO 二叉树中两个节点的最低公共祖先节点
# def FindNode(src_root, des_root):
#     if src_root == None or des_root == None:
#         return False
#     if src_root == des_root:
#         return True
#     if FindNode(src_root.left, des_root):
#         return True
#     return FindNode(src_root.right, des_root)
#
# # print(FindNode(Root1, Root0.left.left))
# def GetLastCommonParent(src_root, des_root0, des_root1):
#     # 层序遍历二叉树并倒顺取节点
#     pass
#
#
# print(GetLastCommonParent(Root1, Root1.left.left, Root1.left))

########################################################################################################################
# TODO 二叉查找树变为有序的双向链表

########################################################################################################################
# 判断树 root1 是否是树 root0 的一部分
# def isPart(root0, root1):
#     if root1 is None:
#         return True
#     if root0 is None:
#         return False
#     if root0.data == root1.data and isPart(root0.left, root1.left) and isPart(root0.right, root1.right):
#         return True
#     if isPart(root0.left, root1):
#         return True
#     if isPart(root0.right, root1):
#         return True
#     return False
#
# print(isPart(Root0, Root1))

########################################################################################################################
# 二叉树最大路径
# def maxPathSum(root):
#     if root is None:
#         return 0
#     l = max(0, maxPathSum(root.left))
#     r = max(0, maxPathSum(root.right))
#     return root.data + max(l, r)
#
# print(maxPathSum(Root1))

########################################################################################################################
# 两个堆栈实现队列
# class queue(object):
#     def __init__(self):
#         self.arr0 = []
#         self.arr1 = []
#
#     def push(self, x):
#         self.arr0.append(x)
#
#     def pop(self):
#         if len(self.arr1) == 0:
#             while len(self.arr0) != 0:
#                 self.arr1.append(self.arr0.pop())
#         if len(self.arr1) != 0:
#             return self.arr1.pop()
#         return None
#
# queue0 = queue()
# queue0.push(0)
# print(queue0.pop())
# queue0.push(0)
# queue0.push(1)
# print(queue0.pop())
# print(queue0.pop())
# print(queue0.pop())

########################################################################################################################
# python 原生栈队列

########################################################################################################################
# 最长无重复元素子串 (verified)
# def lengthOfLongestSubstring(arr):
#     if len(arr) <= 1:
#         return len(arr)
#     res = [1] * len(arr)
#     note = {}
#     note[arr[0]] = [0]
#     for i in range(1, len(arr), 1):
#         res[i] = res[i - 1] + 1
#         if arr[i] in note:
#             temp = i - note[arr[i]][-1]
#             res[i] = min(res[i], temp)
#         note[arr[i]] = [i]
#     return max(res)
#
# print(lengthOfLongestSubstring("wobgrovw"))

########################################################################################################################
# 把数组排成最小的数
# import operator
# from functools import cmp_to_key
#
# def PrintMinNumber(numbers):
#     if not len(numbers):
#         return ""
#     arr = [str(x) for x in numbers]
#     arr.sort(key=cmp_to_key(lambda x, y: operator.le(int(x + y), int(y + x))))
#     return int("".join(arr))
#
# print(PrintMinNumber([32, 23, 323]))

# def PrintMinNumber(numbers):
#     # write code here
#     if len(numbers) == 0:
#         return ''
#     compare = lambda a, b: cmp(str(a) + str(b), str(b) + str(a))
#     min_string = sorted(numbers, cmp=compare)
#     return ''.join(str(s) for s in min_string)

########################################################################################################################
# # 大数相乘
# def multiply_t(num, arr):
#     carry = 0
#     res = []
#     for idx in range(len(arr)-1, -1, -1):
#         mul_s = str(num*arr[idx]+carry)
#         res.insert(0, int(mul_s[-1]))
#         if len(mul_s) >= 2:
#             carry = int(mul_s[0])
#         else:
#             carry = 0
#     if carry != 0:
#         res.insert(0, carry)
#     return res
#
# def addition_t(arr0, arr1):
#     len0 = len(arr0)
#     len1 = len(arr1)
#
#     if len0 >= len1:
#         arr0 = [0] + arr0
#         arr1 = [0]*(len0-len1+1) + arr1
#     else:
#         arr1 = [0] + arr1
#         arr0 = [0]*(len1-len0+1) + arr0
#
#     addr = 0
#     res = [0] * len(arr0)
#     for idx in range(len(arr0)-1, -1, -1):
#         add_ = arr0[idx] + arr1[idx] + addr
#         if add_ >= 10:
#             addr = 1
#         else:
#             addr = 0
#         res[idx] = add_ % 10
#     if res[0] == 0:
#         res.pop(0)
#     return res
#
# def multiply(item0: str, item1: str):
#     arr0 = [int(_) for _ in item0]
#     arr1 = [int(_) for _ in item1]
#
#     res = [0]
#     for idx in range(len(arr0)-1, -1, -1):
#         res_t = multiply_t(arr0[idx], arr1)
#         res_t += [0]*(len(arr0)-idx-1)
#         res = addition_t(res, res_t)
#
#     while len(res) > 1 and res[0] == 0:
#         res.pop(0)
#
#     return ''.join([str(_) for _ in res])
#
# print(multiply_t(4, [3, 3, 4]))
# print(addition_t([3, 4, 5], [7, 8, 9]))
# print(multiply('3456776543', '123456789987654321'))

########################################################################################################################
