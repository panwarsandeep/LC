package main

import (
	"fmt"
)

type ListNode struct {
     Val int
     Next *ListNode
}

func hasCycle(head *ListNode) bool {
    if head == nil {
        return false
    }
    fnode := head
    snode := head
    for fnode != nil && fnode.Next != nil {
        fnode = fnode.Next.Next
        snode = snode.Next
        if snode == fnode {
            return true
        }
        
    }
    return false
}

func buildLL(elm []int, li int) *ListNode{
     var head *ListNode
     var ln *ListNode

     for _, v := range elm {
         tl := &ListNode {
             Val: v,
             Next: nil,
         }
         if head == nil {
              head = tl
              continue
         }
         th := head
         for th.Next != nil {
              th = th.Next
         }
         th.Next = tl
         ln = tl
     }
	 th := head
	 if li == -1 {
		 th = nil
	 }
     for i :=0; i<= li; i++ {
          th = th.Next
     }
     ln.Next = th
     return head
}

func printLL(head *ListNode) {
    for head != nil {
        fmt.Printf("%v ",head.Val)
        head = head.Next
    }
}
func main() {
	fmt.Println("Hello, playground")
	head := buildLL([]int{1,2,3,4}, -1)
	//printLL(head)
	r := hasCycle(head)
	fmt.Printf("LL has cycle: %v\n", r)
}
