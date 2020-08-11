

package main

import (
	"fmt"
)

func partitionLabels(S string) []int {
	res := make([]int, 0)
	cm := make(map[byte]int)
	for i := 0; i < len(S); i++ {
	    cm[S[i]] = i
	}

	maxSoFar := 0
	ctr := 0
	for i := 0; i < len(S); i++ {
	    ctr++
	    if cm[S[i]] > maxSoFar {
		maxSoFar = cm[S[i]]
	    }
	    if maxSoFar == i {
	        maxSoFar = 0
			res = append(res, ctr)
			ctr = 0
	    }
	}

	return res
}

func main() {
	s := "ababcbacadefegdehijhklij"
	res := partitionLabels(s)
	fmt.Printf("Result: %v",res)
}