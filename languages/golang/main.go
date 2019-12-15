type Trie struct {
    chr string
    is_word bool
    children map[string]Trie{}
}

func Constructor() Trie {
    return Trie {
        chr: "",
        is_word: false
    }
}

func (this *Trie) Insert(word string) {
    if str == nil {
        return
    }
    h, t = word[0], word[1:]
    if _, ok := this[children][h]; not ok {
        this[h] := Trie {
            chr: h
            is_word: t==nil
        }
    }
    this[children][h].Insert(t)
}

func (this *Trie) Search(word string) bool {
    if word==nil { return this[is_word] }
    h, t = word[0], word[1:]
    if _, ok := this[children][h]; not ok { return false }
    return this[children][h].Search(t)
}

func (this *Trie) StartsWith(prefix string) bool {
    if prefix==nil { return true }
    h, t := prefix[0], prefix[1:]
    if _, ok := this[children][h]; not ok {
        return false 
    }
    return this[children][h].StartsWith(t)
}

