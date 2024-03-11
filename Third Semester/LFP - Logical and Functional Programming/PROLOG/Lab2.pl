% Predicatul pentru a găsi pozițiile elementului maxim într-o listă
% List - lista initiala, Positions - pozitiile elementului maxim, Max - elementul maxim
% poz(i,o)
poz([], []).
poz(List, Positions) :- max_list(List, Max), poz(List, Max, 1, Positions).

% Regulă pentru a găsi pozițiile elementului maxim în listă
% H - head, T - tail, Max - el maxim, Index - index in lista
% poz(i,i,i,o)
poz([], _, _, []).
poz([H|T], Max, Index, [Index|Rest]) :-
    H =:= Max,
    NewIndex is Index + 1,
    poz(T, Max, NewIndex, Rest).
poz([H|T], Max, Index, Positions) :-
    H =\= Max,
    NewIndex is Index + 1,
    poz(T, Max, NewIndex, Positions).

% Predicat auxiliar pentru a găsi valoarea maximă dintr-o listă
% H - head, T - tail
% Max - nr maxim, X - element
% max_list(i,o)
max_list([], _) :- fail.
% Caz de baza: Cand lista are un singur element, elementul este maxim
max_list([X], X).

% Caz recursiv: compara maximul cozii listei cu H
max_list([H|T], Max) :-
    max_list(T, RestMax),
    (H > RestMax -> Max = H ; Max = RestMax).



%%%% b
% Predicatul pentru găsirea pozițiilor maxime într-o listă
% List - lista initiala, Max - el maxim, PozMax - pozitia maxima
% poz_max(i,i,o)
poz_max(List, Max, PozMax) :-
    poz(List, Max, 1, PozMax).

% Predicatul pentru înlocuirea sublistelor cu pozițiile elementului maxim\
% H-head, T-tail, Max-el max
inlocuire([], []).
inlocuire([H|T], [Rezultat|Rezultate]) :-
    is_list(H), % Dacă elementul este o listă
    max_list(H, Max), % Găsim maximul în sublistă
    poz_max(H, Max, PozitiiMaxime), % Găsim pozițiile maxime în sublistă
    inlocuire(T, Rezultate), % Continuăm cu restul listei
    Rezultat = PozitiiMaxime. % Înlocuim sublistă cu pozițiile maxime
inlocuire([H|T], [H|Rezultate]) :- % Dacă elementul nu este o listă, îl păstrăm nemodificat
    \+ is_list(H),
    inlocuire(T, Rezultate).



