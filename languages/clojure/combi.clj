; http://www.4clojure.com/problem/solutions/103

; my solution; O(nCr)
(defn combis [[x & t :as xs] r]
 (cond (or (nil? x) (empty? xs) (< r 0) (< (count xs) r)) ()
       (zero? r) '(())
       (= (count xs) r) (list xs)
       :else (concat (map #(cons x %) (combis t (dec r)))
                     (combis t r))))

; daowen's solution; O(nCr)
(defn k-combos [n items]
  (if (zero? n) #{#{}}
    ((comp set mapcat)
      #(for [i (k-combos (dec n) (disj items %))] (conj i %))
      items)))

; maximental's solution; O(|s|**r); 비효율적
; 특징 tail recursion
(defn your-combi [n s]
  (loop [n n a #{#{}}]
    (if (> n 0)
      (recur (dec n) (set (for [x a y s :when (not (x y))] (conj x y))))
      a))) 
