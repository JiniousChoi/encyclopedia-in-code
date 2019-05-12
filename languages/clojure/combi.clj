; http://www.4clojure.com/problem/solutions/103

; my solution; O(nCr); is it the most efficient among the solutions here
(defn combis [[x & t :as xs] r]
 (cond (or (nil? x) (empty? xs) (< r 0) (< (count xs) r)) ()
       (zero? r) '(())
       (= (count xs) r) (list xs)
       :else (concat (map #(cons x %) (combis t (dec r)))
                     (combis t r))))

; 1067's solution; O(nCr)
(fn combi [r xs]
  (if (zero? r)
    #{#{}}
    (set (for [x xs
               s (combi (dec r) (disj xs x))]
           (conj s x)))))

; daowen's solution; O(nCr)
(fn combi [r items]
  (if (zero? r) [#{}]
    ((comp set mapcat)
      #(for [i (combi (dec r) (disj items %))] (conj i %))
      items)))

; maximental's solution; O(|s|**r); 비효율적
; 특징 tail recursion
(defn combi [n s]
  (loop [n n a #{#{}}]
    (if (> n 0)
      (recur (dec n) (set (for [x a y s :when (not (x y))] (conj x y))))
      a))) 
