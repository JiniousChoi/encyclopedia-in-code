; efficient
(defn fibo
  ([] (fibo 1 1))
  ([a b] (lazy-seq (cons a (fibo b (+ a b))))))

; inefficient
(defn fibo2 []
  (lazy-cat [1 1] (map + (fibo2) (rest (fibo2)))))
