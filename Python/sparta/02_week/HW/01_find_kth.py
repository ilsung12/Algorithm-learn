class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        length = 1
        cur = self.head

        # 카운트 세면서 끝까지 가봄
        while cur.next is not None: 
            cur = cur.next
            length += 1 
        
        # 끝에서 - k 하고,
        # 다시 처음부터 해야하니까 cur을 초기화해줌
        end_length = length - k
        cur = self.head
        
        # end_length 만큼 또 cur.next를 한다.
        for i in range(end_length):
            cur = cur.next

        return cur # 출력

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)
linked_list.append(10)
linked_list.append(11)

print(linked_list.get_kth_node_from_last(2).data)  # 10이 나와야 합니다!