# 合并K个排序链表
# 题目:
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

# 示例:

# 输入:
#   [
#     1->4->5,
#     1->3->4,
#     2->6
#   ]
# 输出: 1->1->2->3->4->4->5->6

# Solution Code
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap=[]
        res=None
        node_map={}#{index：node} 
        val_map={}#{val：[index]}
        
        #生成node和val字典的同时，把头节点放入heap            
        for (index,node) in enumerate(lists):
            #生成node字典
            if not node:#空时继续
                continue
            node_map[index]=node
            # 生成val字典
            if node.val in val_map:
                val_map[node.val].append(index)
            else:
                val_map[node.val]=[index]
            #把头节点放入heap    
            heapq.heappush(heap,node.val)

        #循环直到堆中没有元素，返回res   
        while heap:
            small=heapq.heappop(heap)#pop出heap里的最小值
            node_index=val_map[small].pop()#这里pop用得好，得到index并从字典的值里删除
                       
            #设置res为开头，而dummy用来next接收遍历
            if res is None:                
                res=node_map[node_index]
                dummy=res                                             
            else:
                dummy.next=node_map[node_index]
                dummy=dummy.next
            
            #判断node非空，并值加入堆
            if node_map[node_index].next:                
                node_map[node_index]=node_map[node_index].next
                #命名 “_” 为了减少代码量，(提升程序效率?)
                #“_”就是需要新加入堆的值
                _=node_map[node_index].val
                if _ in val_map:
                    val_map[_].append(node_index)
                else:
                    val_map[_]=[node_index]
                heapq.heappush(heap,_)
        return res
