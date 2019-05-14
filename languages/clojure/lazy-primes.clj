; my own impl. for lazy-seq for prime numbers

(defn primes []
  (letfn [(_primes [ps x]
             (cond (some #(zero? (rem x %)) ps)
                     (_primes ps (+ 2 x))
                   :else
                     (lazy-seq (cons x (_primes (cons x ps) (+ 2 x))))))]
    (cons 2 (_primes (list 2) 3))))

