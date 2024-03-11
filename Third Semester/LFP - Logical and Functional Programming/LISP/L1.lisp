(defun elimina-element (lista n)
  (if (or (null lista) (< n 0))
      lista
      (append (subseq lista 0 n)
	      (subseq lista (1+ n)))))

;; Exemplu de utilizare:
(setq my-list '(1 2 3 4 5))
(setq my-list (elimina-element my-list 2))
(print my-list)

(defun elimina-element-la-pozitie (lista pozitie)
  (if (or (null lista) (< pozitie 0))
      lista
      (if (= pozitie 0)
          (cdr lista)  ; dacă poziția este 0, eliminăm primul element
          (cons (car lista)  ; păstrăm primul element
                (elimina-element-la-pozitie (cdr lista) (1- pozitie)))))) ; recursivitate pentru restul listei

(setq lista-originala '(1 2 3 4 5))
(setq pozitie-de-eliminat 2)
(setq lista-noua (elimina-element-la-pozitie lista-originala pozitie-de-eliminat))
(print lista-noua)


;;b
(defun reverse-list (lista)
  (labels ((reverse-aux (rest reversed)
             (if (null rest)
                 reversed
                 (reverse-aux (cdr rest) (cons (car rest) reversed)))))
    (reverse-aux lista '())))

(defun succesor (numar)
  (let* ((carry 1)
         (rezultat '()))
    (dolist (cifra (reverse-list numar) (reverse-list rezultat))
      (let ((suma (+ cifra carry)))
        (setq carry (if (< suma 10) 0 1))
        (setq rezultat (cons (mod suma 10) rezultat))))
    (if carry (cons carry rezultat) rezultat)))

;; Exemplu de utilizare:
(setq numar '(1 9 3 5 9 9))
(setq rezultat (succesor numar))
(print rezultat)

(defun succesor-numar (numar)
  (reverse (succesor-numar-rec (reverse numar) 1)))

(defun succesor-numar-rec (numar carry)
  (if (null numar)
      (if (zerop carry)
          '()  ; Dacă nu există transport, rezultatul este lista goală
          (list carry))  ; Altfel, adăugăm carry-ul ca o nouă cifră
      (let* ((suma (+ (car numar) carry))  ; Adunăm cifra curentă și carry-ul
             (restul (mod suma 10))  ; Calculăm cifra rezultatului
             (noul-carry (/ suma 10)))  ; Calculăm carry-ul pentru următoarea cifră
        (cons restul (succesor-numar-rec (cdr numar) noul-carry)))))
(setq numar '(1 9 3 5 9 9))
(setq rezultat (succesor-numar numar))
(print rezultat)




(defun is_member (elem lista)
  (cond
    ((null lista) nil)
    ((eql elem (car lista)) t)
    (t (is_member elem (cdr lista)))))

(defun este-multime (lista)
  (labels ((verifica-multime (restante lista)
             (cond
               ((null lista) t)
               ((is_member (car lista) restante) nil)
               (t (verifica-multime (cons (car lista) restante) (cdr lista))))))
    (verifica-multime '() lista)))

;; Exemplu de utilizare:
(setq multime-valida '(1 2 3 4))
(setq multime-invalida '(1 2 3 4 1))

(print (este-multime multime-valida))   ; ar trebui să afișeze T
(print (este-multime multime-invalida)) ; ar trebui să afișeze NIL







