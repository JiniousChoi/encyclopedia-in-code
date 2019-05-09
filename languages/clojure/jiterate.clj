; my own impl. for the built-in `iterate` fn

(defn jiter [f x]
 (lazy-cat [x] (map f (jiter f x))))

; more efficient impl.
(defn jiter2 [f x]
 (lazy-seq (cons x (jiter2 f (f x)))))

; call stack
; (jiter f x)
; 
; = (lazy-cat [x] (map f (jiter f x)))
; 
; = (lazy-cat [x] (map f (lazy-cat [x] (map f (jiter f x)))))
; = (lazy-cat [x] (map f (lazy-cat [x] [..] )
; = (lazy-cat [x] (map f [x ..]))
; = (lazy-cat [x] [(f x) ??])
; = [x (f x) ???]
; 
; = (lazy-cat [x] (map f (lazy-cat [x] (map f (lazy-cat [x] (map f (jiter f x)))))))
; = (lazy-cat [x] (map f (lazy-cat [x] (map f (lazy-cat [x] ???)))))
; = (lazy-cat [x] (map f [x (f x) ???]))
; = (lazy-cat [x] [(f x) (f (f x)) ???])
; = [x (f x) (f (f x)) ???]


