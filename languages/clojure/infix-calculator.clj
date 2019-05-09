; inorder arithmetic expression evaluator
; it takes account of operator precedence

; usage
; ($= 1 - 2 + 3)
; 2
; ($= 10 - 2 * 3)
; 4

(defn $= [& xs]
 (cond 
  (= (count xs) 1) (first xs)
  (= (count xs) 3) (let [[a o b] xs] (o a b))
  :else (let [[[a o b] t] (split-at 3 xs)]
         (cond 
          (contains? #{* /} o) (apply $= (cons (o a b) t))
          (= o +) (+ a (apply $= (drop 2 xs)))
          :else (apply $= (concat (list a +) (list (unchecked-negate-int b)) t))))))  
