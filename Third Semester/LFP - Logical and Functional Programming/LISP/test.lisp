;;;l - lista e:element cu care fac perechi

(defun perechi(l e)
  (cond
    ((null l) nil)
    ((not(numberp(car l))) (append (list(list  e (car l)) ) (perechi(cdr l) e)))
    (t (perechi(cdr l) e))
  )
)

(print (perechi '(A 2 B 3 C D 1) 'A))


;;; l -lista de elemente
(defun perechi_main(l)
  (cond
    ((null l) nil)
    ((not (numberp(car l))) (append (perechi(cdr l) (car l) ) (perechi_main(cdr l))))
    (t (perechi_main(cdr l)))
   )
)

(print (perechi_main '(1 A 2 B 3 4 5 C)))
