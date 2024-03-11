;; x:nodul cautat, nod:nod curent, nivel:nivelul la care ne aflam
;; nrcopii: nr de copii pe care ii are nodul curent, l: lista subarborilor nodului curent
; nivelul radacinii se considera 0
(defun parcurge(x nod nivel nrcopii l)
        (cond
            ((eq x nod) nivel)
            ((null l) nil)
            ((= nrcopii 0) l)
            (t 
                (SETQ rez (parcurge x (car l) (+ nivel 1) (cadr l) (cddr l)))
                (cond 
                    ((listp rez) (parcurge x nod nivel (- nrcopii 1) rez))
                    (t rez)
                )
            )
        )
)

(defun rezolva(x l)
    (parcurge x (car l) 0 (cadr l) (cddr l))) 
(write(rezolva 'R '(A 2 B 1 D 1 E 1 F 2 G 0 H 2 J 0 K 0 C 2 L 2 N 0 Q 2 P 0 R 0 M 0)))
