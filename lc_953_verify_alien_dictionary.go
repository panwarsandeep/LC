

package main

import (
	"fmt"
)

func isAlienSorted(words []string, order string) bool {
	cm := make(map[byte]int)
	for i := 0; i < 26; i++ {
	    cm[order[i]] = i
	}
	prev := words[0]
	for _, wd := range words[1:] {
        if isGreater(wd, prev, &cm) < 0 {
			return false
		}
		prev = wd
	}
	return true
}

func isGreater(w1 string, w2 string, cm *map[byte]int) int {
    l2 := len(w2)
    l1 := len(w1)
    ml := l1
    if l2 < l1 {
        ml = l2
    }
    res := 0
    for i := 0; i < ml; i++ {
        res = (*cm)[w1[i]] - (*cm)[w2[i]]
        if res != 0 {
            return res
        }
    }
    if l1 != l2 {
        return l1 - l2
    }    
    return 0
}

func main() {
	//words := []string{"hello", "leetcode"}
	//order := "hlabcdefgijkmnopqrstuvwxyz"
	//words := []string{"word","world","row"}
	//order := "worldabcefghijkmnpqstuvxyz"
	words := []string{"apple","app"}
	order := "abcdefghijklmnopqrstuvwxyz"
	res := isAlienSorted(words, order)
	fmt.Printf("Result: %v",res)
}