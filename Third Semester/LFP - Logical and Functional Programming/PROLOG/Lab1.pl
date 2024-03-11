% Verifică dacă o listă este o mulțime (fără duplicări).
% H-head, T-tail
% flux(i,i)

% E - element, T - tail
% is_member(i,i)
is_member(E, [E|_]).
is_member(E, [_|T]) :- is_member(E, T).

% flux(i)
is_set([]). % Lista vidă este o mulțime.
% Verifică dacă H nu se găsește în coadă și apoi verifică recursiv coada.
is_set([H | T]) :- \+ is_member(H, T), is_set(T).

% Sterge primele 3 aparitii din lista sau pe toate daca nu sunt suficiente
% X - nr care trebuie sters
% T - lista
% H-head,T-tail, T1-sublista, N-contor
% flux: (i,i,o,i)
remove_first_3(_, [], [],_).
remove_first_3(X, [X|T], T1, N) :- N \= 3, N1 is N + 1, remove_first_3(X, T, T1, N1).
remove_first_3(X, [H|T], [H|T1], N) :- remove_first_3(X, T, T1, N).
% flux (i,i,o)
% E-element
% L1-sublista
apel(E,L,L1) :- remove_first_3(E, L, L1, 0).   