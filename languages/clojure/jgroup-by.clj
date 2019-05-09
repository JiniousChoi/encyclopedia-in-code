; my impl. for built-in `group-by` fn
 
; usage
; (jgroup-by count [[1] [1 2] [1 2 3]])
; {3 [[1 2 3]], 2 [[1 2]], 1 [[1]]}

; (jgroup-by #(= 3 (count %)) [[1] [1 2] [1 2 3]])
; {true [[1 2 3]], false [[1 2] [1]]}

; normal recursion
(defn jgroup-by [f xs]
 (let [h (first xs) t (next xs)]
  (if (nil? xs)
   {}
   (let [sub-map (jgroup-by f t)
         val (f h)
         keys (sub-map val)]
    (if (contains? sub-map val)
     (assoc sub-map val (conj keys h))
     (assoc sub-map val [h]))))))

; tail recursion
(defn jgroup-by [f xs]
 (loop [xs xs
        sub-map {}]
  (if (nil? xs)
   sub-map
   (let [h (first xs)
         t (next xs)
         v (f h)
         keys (sub-map v)]
    (if (contains? sub-map v)
     (recur t (assoc sub-map v (conj keys h)))
     (recur t (assoc sub-map v [h])))))))
