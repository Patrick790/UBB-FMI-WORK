(defun adancime(L)
    (cond
       ((null L) 0)
       ( (atom L) -1)
       (t (+ 1 (apply #'max (mapcar #' adancime L))))
    )
)

(print (adancime '(1 (2 (3) (3 (4))) (5 (7)))))
(print (adancime '(1 2 3 4 5)))
