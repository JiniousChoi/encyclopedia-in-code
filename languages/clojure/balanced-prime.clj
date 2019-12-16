(defn is-balanced-prime [x]
  (let [_primes (fn _primes [ps x]
                   (cond (some #(zero? (rem x %)) ps)
                           (_primes ps (+ 2 x))
                         :else
                           (lazy-seq (cons x (_primes (cons x ps) (+ 2 x))))))
        primes (fn primes []
                  (cons 2 (_primes (list 2) 3)))
        balanced (map second (filter (fn [[a b c]] (= (+ b b) (+ a c))) (map vector (primes) (->> (primes) next) (->> (primes) next next))))]
    (= x (first (drop-while #(< % x) balanced)))))
