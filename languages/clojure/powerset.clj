; just for the hack of it

; my solution
(defn powerset [[x & xs]]
  (cond (nil? x) (()) 
        :else (let [ss (powerset xs)]
                (concat ss (map #(cons x %) ss))))

; austintaylor's solution at
; http://www.4clojure.com/problem/solutions/103
(defn powerset [s]
  (reduce (fn [ps x]
    (reduce (fn [ps s]
      (conj ps (conj s x))) ps ps)) #{#{}} s))
