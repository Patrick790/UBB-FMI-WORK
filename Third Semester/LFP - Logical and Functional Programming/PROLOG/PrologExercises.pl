%ex1P1a - dif a doua multimi
is_member(E, [E|_]) :- !.
is_member(E, [_|T]) :- is_member(E, T).

diferenta([], _, []).
diferenta([H|T], Lista, T1) :-
    is_member(H, Lista),
    !,
    diferenta(T, Lista, T1).
diferenta([H|T], Lista, [H|T1]) :-
    \+ is_member(H, Lista),
    diferenta(T, Lista, T1).

%ex1P1b - dupa fiecare par val 1
adauga_1([], []).
adauga_1([H|T], [H,1|T1]):- 0 is H mod 2, !, adauga_1(T, T1).
adauga_1([H|T], [H|T1]):- 1 is H mod 2, adauga_1(T, T1).


%ex2P2a - sortare fara eliminare dubluri
sortare([],[]).
sortare([X|T], T1):- sortare(T, Sorted), insert_sorted(X, Sorted, T1).

insert_sorted(X, [], [X]). % Dacă lista este vidă, adaugăm X ca singur element
insert_sorted(X, [H|T], [X,H|T]) :- X =< H, !. % Dacă X este mai mic decât primul element, X devine primul element
insert_sorted(X, [H|T], [H|T1]):- insert_sorted(X, T, T1).

%ex2P1a - cmmmc al el unei liste
% Calculul celui mai mic multiplu comun între două numere
cmmmc(X, Y, Result) :- Result is X * Y // gcd(X, Y).
gcd(X, 0, X) :- X > 0, !.
gcd(X, Y, Result) :- Z is X mod Y, gcd(Y,Z, Result).

cmmmc_lista([], 0).
cmmmc_lista([X], X).
cmmmc_lista([H|T], Result) :- cmmmc_lista(T, R), !, cmmmc(H, R, Result).

%ex2P1b - adauga dupa primul, al doilea, al 4-lea, al8-lea...
adauga_v([], _, [], _, _).
adauga_v([H|T], V, [H,V|T1], N, M):- N =:= M, N1 is N + 1, M1 is 2*M, !, adauga_v(T,V,T1,N1,M1).
adauga_v([H|T], V, [H|T1], N, M):- N1 is N + 1, adauga_v(T, V, T1,N1,M).
apel(L, V, R) :- adauga_v(L, V, R, 1, 1).

%ex3P1a - transf lista in multime, in ord primei ap
transf([], [], []).
transf([H|T], A, T1):- is_member(H, A), !, transf(T,A,T1).
transf([H|T], [H|A], [H|T1]):- \+ is_member(H, A), transf(T,A,T1).
transf(L, Rez):- transf(L, [], Rez).

%ex3P1b - [[lista pare][lista impare]]
pareSiImpare([],[[], []], P, I, P, I).
pareSiImpare([H | T], [[H | T1], T2], P, I, PR, IR):- H mod 2 =:= 0, P1 is P + 1,  !, pareSiImpare(T, [T1, T2], P1, I, PR, IR).
pareSiImpare([H | T], [ T1, [H|T2]], P, I, PR, IR):- H mod 2 =:= 1, I1 is I + 1, pareSiImpare(T, [T1, T2], P, I1, PR, IR).
apel(L, R, P, I):- pareSiImpare(L, R, 0, 0, P, I).

%ex4P1b - elim elem de pe poz n
elim_poz([], [], _, _).
elim_poz([_|T], T1, N, C):- N =:= C, C1 is C + 1, !, elim_poz(T, T1, N, C1).
elim_poz([H|T], [H|T1], N, C):- C1 is C + 1, elim_poz(T, T1, N, C1).
elim_poz(L, R, N) :- elim_poz(L, R, N, 1).

%ex4P1a - subst elem prin lista
subst_elem([],[],_,_).
subst_elem([H|T], [L|T1], N, L):- H =:= N, !, subst_elem(T, T1, N, L).
subst_elem([H|T], [H|T1], N, L):- subst_elem(T, T1, N, L).

%ex5P1b - lista de perechi(nr, ap)
nr_aparitii(_, [], N, N).
nr_aparitii(E, [E|T], N, M):- N1 is N+1, nr_aparitii(E, T, N1, M).
nr_aparitii(E, [_|T], N, M):- nr_aparitii(E, T, N, M), !.
nr_aparitii(E, L, N):- nr_aparitii(E, L, 0, N).

numar([], []).
numar([H|T], [[H, Count]|T1]) :- count_and_remove(H, [H|T], Count, NewList), numar(NewList, T1).

count_and_remove(_, [], 0, []).
count_and_remove(E, [E|T], Count, Result) :- count_and_remove(E, T, PrevCount, Result), Count is PrevCount + 1, !.
count_and_remove(E, [H|T], Count, [H|Result]) :- E \= H, count_and_remove(E, T, Count, Result).


%ex6P1b - elimina toate aparitiile nr max
max_lista([], M,M).
max_lista([H|T], M, N):- H > M, !, max_lista(T, H, N).
max_lista([H|T], M, N) :- H =< M, max_lista(T, M, N).
max_lista(L, M):- max_lista(L, 0, M).

el_ap([], []).
el_ap(List, T1) :- max_lista(List, M), el(List , T1, M).

el([], [], _).
el([H|T], T1, M) :- H =:= M,!, el(T, T1, M).
el([H|T], [H|T1], M) :- el(T, T1, M).

%ex10P1b - cmmdc
cmmdc(A, 0, A) :- !.
cmmdc(A, B, Result) :- A >= B, Mod is A mod B, cmmdc(B, Mod, Result).
cmmdc(A, B, Result) :- A < B, cmmdc(B, A, Result).

cmmdc_lista([H|T], Result) :- cmmdc_lista(T, H, Result).
cmmdc_lista([], Result, Result).
cmmdc_lista([H|T], Current, Result) :- cmmdc(H, Current, Cmmdc), !, cmmdc_lista(T, Cmmdc, Result).


%ex3P2a - sortare fara dubluri

% Predicatul pentru eliminarea duplicatelor
remove_duplicates([], []).
remove_duplicates([H | T], Result) :-
    is_member(H, T),
    remove_duplicates(T, Result).
remove_duplicates([H | T], [H | Result]) :-
    \+ is_member(H, T),
    remove_duplicates(T, Result).

% Predicatul principal pentru sortare și eliminare duplicate
sort_and_remove_duplicates(InputList, SortedResult) :-
    sortare(InputList, SortedList),
    remove_duplicates(SortedList, SortedResult).


%ex11P2a - dublare prim

% Predicatul pentru verificarea primarității unui număr
prim(2) :- !.
prim(3) :- !.
prim(N) :-
    N > 3,
    prim(N, 2).

prim(N, Div) :-
    DivSquared is Div * Div,
    DivSquared > N,
    !.
prim(N, Div) :-
    N mod Div =\= 0,
    NextDiv is Div + 1,
    prim(N, NextDiv).

dublu_prim([], []).
dublu_prim([H|T], [H,H|T1]):- prim(H), !, dublu_prim(T, T1).
dublu_prim([H|T], [H|T1]):- dublu_prim(T, T1).

%ex13P2a - 
divizori([], []).
divizori([H|T], Result) :-
    divizori_element(H, Divizori),
    adauga_divizori(H, Divizori, HWithDivizori),
    divizori(T, Rest),
    append(HWithDivizori, Rest, Result).

divizori_element(X, Divizori) :-
    findall(D, (between(1, X, D), 0 is X mod D), Divizori).

adauga_divizori(_, [], []).
adauga_divizori(E, [D|Divizori], [D, E | Rest]) :-
    adauga_divizori(E, Divizori, Rest).



%Ex7P2a

%mul_number_in_list(i, i, o);
mul_number_in_list(L, P, R):- list_to_number(L, 0, N), N0 is N * P, number_to_list(N0, R). 

%list_to_number(i, i, o);
list_to_number([], E, E). 
list_to_number([H | T], E, R):- E0 is E * 10 + H, list_to_number(T, E0, R).

%number_to_list(i, o);
number_to_list(0, []):- !.
number_to_list(E, T):- E1 is E div 10, number_to_list(E1, T1), H is E mod 10, adaugaSf(T1, H, T).

%adaugaSf(i, i, o);
adaugaSf([], E, [E]):- !.
adaugaSf([H | T], E, [H | R]):- adaugaSf(T, E, R).



prodLista([], 1).
prodLista([H|T], P):- prodLista(T, Rest), P is H * Rest.






suma([], 0).
suma([H|T], S):- suma(T, Rest), !, S is H + Rest.



       