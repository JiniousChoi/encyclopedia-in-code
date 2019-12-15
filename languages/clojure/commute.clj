; Note that commute will ALWAYS run the update function TWICE. 
; Example courtesy of "Clojure for the Brave and True"
; https://github.com/flyingmachine/brave-clojure-web

(defn now []
  (System/currentTimeMillis))

(defn sleep-print-update
    [sleep-time thread-name update-fn]
    (fn [state]
          (println (str "(before) " thread-name ": " state " and now is " (now)))
          (Thread/sleep sleep-time)
          (println (str "(after) " thread-name ": " state " and now is " (now)))
          (update-fn state)
    ))

(def counter (ref 0))
(println "start at " (now))
(future (dosync (commute counter (sleep-print-update 100 "Commute Thread A" inc))))
(future (dosync (commute counter (sleep-print-update 150 "Commute Thread B" inc))))

(def counter (ref 0))
(println "start at " (now))
(future (dosync (commute counter (sleep-print-update 150 "Commute Thread B" inc))))
(future (dosync (commute counter (sleep-print-update 100 "Commute Thread A" inc))))

(def counter (ref 0))
(future (dosync (commute counter (sleep-print-update 150 "Commute Thread B" inc))))
(println "result: " (time @(future (dosync (commute counter (sleep-print-update 100 "Commute Thread A" inc))))))

(def counter (ref 0))
(future (dosync (commute counter (sleep-print-update 100 "Commute Thread A" inc))))
(println "result: " (time @(future (dosync (commute counter (sleep-print-update 150 "Commute Thread B" inc))))))

(future (dosync (commute counter (sleep-print-update 100 "Commute Thread A" inc))))
(future (dosync (commute counter (sleep-print-update 130 "Commute Thread C" inc))))
(println "result: " (time @(future (dosync (commute counter (sleep-print-update 150 "Commute Thread B" inc))))))


(def my_num (ref 0))
 
(defn inc_alter []
  (dosync
    (try
      (println "Alter: " (alter my_num inc)) 
      (catch Throwable t (do
          (println "Caught " (.getClass t)) 
          (throw t))))))
 
(defn test_alter []
  (let [threads (for [x (range 0 50)] (Thread. #(inc_alter)))]
    (do
      (println "---- Alter ----")
      (doall (map #(.start %) threads))
      (doall (map #(.join %) threads))
      (println "---- After loop: ----") 
      (inc_alter))))
 
(test_alter)


(def my_num (ref 0))
 
(defn inc_commute []
  (dosync
    (try
      (println "Commute: " (commute my_num inc)) 
      (catch Throwable t 
        (do
          (println "Caught " (.getClass t)) 
          (throw t))))))
 
(defn test_commute []
  (let [threads (for [x (range 0 50)] (Thread. #(inc_commute)))]
    (do
      (println "---- Alter ----")
      (doall (map #(.start %) threads))
      (doall (map #(.join %) threads))
      (println "---- After loop: ----") 
      (inc_commute))))
 
(test_commute)
