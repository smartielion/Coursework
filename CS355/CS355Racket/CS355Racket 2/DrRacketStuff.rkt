#lang racket
; number of variables are '(A B C D E F G H I J)
(define teststate '((A #f)(B #f)(C #f)(D #f)(E #f)(F #f)(G #f)(H #f)(I #f)(J #f)))
  
  
(define clauses1 '((F (NOT B) E) (C (NOT D) E) ((NOT G) F (NOT B)) (D C (NOT A)) (D F B)
   (D (NOT I) (NOT E)) ((NOT H) E I) ((NOT G) F I) (C F (NOT H)) (J G (NOT A))
   ((NOT H) E (NOT A)) (A (NOT F) E) ((NOT G) (NOT E) B) (E (NOT D) (NOT I))
   ((NOT G) I E) ((NOT G) (NOT B) E) (J D (NOT F)) (F (NOT H) E) (D (NOT H) E)
   ((NOT H) (NOT B) C) ((NOT E) I (NOT D)) (B (NOT F) (NOT A)) (E (NOT I) J)
   (E (NOT A) I) (D (NOT F) (NOT H)) (A H D) ((NOT D) G (NOT J)) (F D (NOT A))
   (C D F) ((NOT A) (NOT H) E)) )

(define clauses2 '((J (NOT C) D) (D (NOT G) (NOT H)) ((NOT D) (NOT E) (NOT G)) (F (NOT J) C)
   (D (NOT H) C) ((NOT G) C F) (A (NOT I) (NOT B)) ((NOT J) (NOT D) E) (H A C)
   (A C B) ((NOT B) I C) ((NOT J) (NOT G) (NOT B)) ((NOT H) A (NOT C))
   (F (NOT A) C) ((NOT H) G I) (F (NOT B) E) ((NOT C) (NOT B) I)
   ((NOT I) F (NOT D)) (B (NOT G) C) (J (NOT C) (NOT H)) (C F (NOT D))
   ((NOT J) (NOT D) (NOT C)) ((NOT J) E C) (E (NOT I) D) (C (NOT D) (NOT J))
   ((NOT G) F I) ((NOT D) B I) (B (NOT H) J) ((NOT G) (NOT D) B) ((NOT H) F I)
   (I F C) ((NOT A) D F) ((NOT D) (NOT F) (NOT J)) ((NOT J) I (NOT A))
   ((NOT E) (NOT H) I) (H (NOT B) J) (E F C) ((NOT D) E J) ((NOT A) J (NOT F))
   ((NOT D) (NOT H) (NOT F)) ((NOT B) H (NOT I)) (D (NOT H) C)
   ((NOT J) (NOT I) H) (J G F) (A G (NOT J)) (J (NOT D) (NOT H))
   ((NOT J) (NOT C) D) (I D E) ((NOT E) (NOT B) (NOT I)) (G D A)))

(define clauses3 '(((NOT I) (NOT H) (NOT F)) ((NOT B) E (NOT G)) (H (NOT C) E)
   ((NOT G) (NOT E) (NOT I)) ((NOT A) C (NOT J)) ((NOT G) (NOT A) H)
   ((NOT I) F (NOT H)) (I (NOT A) (NOT E)) ((NOT E) I J) (I (NOT J) (NOT A))
   (D I E) ((NOT B) C A) ((NOT G) E I) ((NOT G) (NOT A) F) ((NOT B) A (NOT I))
   ((NOT G) J E) (D (NOT G) C) (G (NOT B) (NOT C)) ((NOT H) F (NOT J)) (C D F)
   (B (NOT G) (NOT E)) (A (NOT D) I) (C A H) (F (NOT B) (NOT A))
   ((NOT J) (NOT F) (NOT D)) ((NOT A) E (NOT J)) ((NOT I) (NOT G) (NOT C))
   (J A C) (H (NOT G) (NOT E)) ((NOT H) (NOT I) (NOT E)) ((NOT H) D (NOT B))
   ((NOT D) E (NOT I)) (I (NOT G) C) (F (NOT G) (NOT A)) (G I E)
   (E (NOT B) (NOT G)) ((NOT C) (NOT I) D) ((NOT G) (NOT B) (NOT H))
   (D (NOT I) B) (H I A) ((NOT H) (NOT G) (NOT A)) ((NOT G) (NOT B) F)
   (E (NOT G) (NOT A)) (I (NOT H) (NOT A)) ((NOT J) E C) ((NOT B) (NOT A) F)
   (G J (NOT A)) ((NOT F) A D) (C D H) (F H E) (E J A) (J A F)
   ((NOT J) (NOT B) (NOT A)) (E A (NOT J)) ((NOT I) (NOT G) (NOT C))
   (I (NOT E) G) (I (NOT A) D) ((NOT F) E (NOT J)) ((NOT H) I D)
   (F (NOT B) (NOT H)) (E (NOT H) C) ((NOT F) (NOT D) I) (H (NOT J) (NOT D))
   (G (NOT A) (NOT F)) ((NOT E) C J) ((NOT C) E (NOT F)) (D (NOT E) (NOT F))
   ((NOT H) (NOT A) F) (F E (NOT G)) (D F (NOT J)) ((NOT A) (NOT J) (NOT I))
   (J (NOT F) (NOT H)) ((NOT I) (NOT H) J) (C G (NOT E)) (I C F) (I (NOT F) J)
   (A (NOT H) (NOT E)) (C (NOT A) (NOT H)) (D (NOT F) (NOT A))
   ((NOT E) (NOT G) I)))


;;TEST CASES PROVIDED +_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_


(define eval-var (lambda(var state) ;;#1
  (if(equal? (car (car state) ) var);if the first symbol matches
                   (car (cdr (car state))) ;;return the value of the first symbol
                   (eval-var var (cdr state)));;otjerwise recurse using the next set of the state
                 ))
(define eval-clause (lambda (clause state) ;#2
                      (if(empty? clause);;if the table is empty
                         #f;;return false
                         (if (list? (car clause));otherwise check the first element of the clause
                             (if (not (eval-var (car(cdr(car clause ))) state));;if the list evaluates as true, return true, otherwise recurse
                                #t ;retrun true
                                (eval-clause (cdr clause) state));otherwise recurse
                             (if (eval-var (car clause) state);;if the non-list evaluates true, truen true, otherwise recurse
                                 #t;return true
                                 (eval-clause (cdr clause) state))));otherwise recurse
                     ))
(define get-vars (lambda (clause);#3
            (if (empty? clause);;if the clause is empty, return a list of no emlements
                '();return the list of no elemetns
                (if (list? (car clause));;if the first thing is a list
                    (flatten(list(car(cdr(car clause)))(get-vars (cdr clause))));return the the carcdrcar of the list concatenated with the getcars of the cdr
                    (flatten(list (car clause) (get-vars (cdr clause))))));;otherwise return the car of the clause listed with the get cars of the cdr
  ))
      
(define get-all-vars (lambda (clause);#4
                       (if (empty? clause);;if the clause is empty, return an empty list
                           '()
                           (remove-duplicates(flatten (list(get-vars (car clause))(get-all-vars(cdr clause)))))
                       )))


(define unsat-clauses(lambda (clause state);#5
                       (if (not(empty? clause));;if its NOT blank
                           (if (eval-clause(car clause)state);;check the truth value of the ifrst cluase
                               (unsat-clauses (cdr clause) state);;if the clause is true, skip it, and check the next clause
                               (cons (car clause)(unsat-clauses (cdr clause) state)))
                           '()
                       )))

(define flip-var (lambda (var state);#6
                   (if (empty? state);if the state is empty
                       '();;return empty list if empty
                       (if(equal? (car(car state)) var);if car matches the car
                          (cons (flatten(cons var (not(eval-var var state)))) (cdr state));;true, cons with the flipped value and the rest of the state
                          (cons (car state) (flip-var var (cdr state)))));;false, cons with the rest of the state
                   ))



(define get-better-neighbors (lambda (clause state var num-unsat)
                               (if (empty? var);;if the var list is empty
                                   #f ;;return false, no better neighbors
                                   (if (< (length(unsat-clauses clause (flip-var (car var) state))) num-unsat) ;;if the flipped variable yields less unsatisfied nieghbors,
                                       (flip-var (car var) state) ;;return the flipped state
                                       (get-better-neighbors clause state (cdr var) num-unsat)
                                   )
                               ) ;;otherwise try the next var
                               ))


(define simple-hill-climb(lambda (clause state dist unsat)
                           (if (= dist 0) ; if distance is zero, were done trying
                               state ;return the state
                               (if (equal? (get-better-neighbors clause state (get-all-vars clause) (length (unsat-clauses clause state))) #f);otherwise check if there is a better neighbor
                                   state ;;returned false, so there is no better neibor, return the state
                                   ;;otherwise hill climb using the clause, the next best nieghbor, the distance decremented, and the list of unsatisfied clauses
                                   (simple-hill-climb clause (get-better-neighbors clause state (get-all-vars clause) (length (unsat-clauses clause state))) (- dist 1)(unsat-clauses clause (get-better-neighbors clause state (get-all-vars clause) (length (unsat-clauses clause state)))))))
                           ))