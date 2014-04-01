%Casey Gilray
%ASsignment 4 prolog
% this does all of the simple hill climb method reviously done in sceme

%use test case simple-hill-climb([[a,b],[a,b],[b,c]],[[a,false],[b,false],[c,false]],10,[[a,b],[a,b],[b,c]],X).



% eval var
% var, state
%Z gets the result of the tail of Y the head of Y matches X
eval-var(X,[[X,Z]|T],Z).

%case variable not at head, recursion
eval-var(X,[_|T],Z) :- eval-var(X,T,Z).

%base case, nothing left, false
eval-var(X,[],false).

%eval clause
%state,clause,result
%base case, no clause
eval-clause(S,[],false).

%case sub-list- evaluation is reversed
eval-clause(S,[[_,T]|R],Z) :- eval-var(T,S,X),(X =@= false ->
									(Z=true),!;
									eval-clause(S,R,Z)).

%case non-sub-list, evalutation is taken like normal
eval-clause(S,[T|R],Z) :- eval-var(T,S,X),(X =@= true ->
									(Z=true),!;
									eval-clause(S,R,Z)).


%get vars
%clause,result
%result has s ub list, appened the result of getvars and B
get-vars([[_,B]|T],Z) :- get-vars(T,X),append([B],X,P),sort(P,Z).

%result does not have sub list, append result of getvars and head
get-vars([H|T],Z) :- not(H=[_,_]),get-vars(T,X),append([H],X,P),sort(P,Z).

%base case, no list, do nothing
get-vars([Z],[Z])  :- !.
get-vars([[H|T]],T) :- !.
get-vars([],[]).

%get-all-vars
%clauses
%base case, empty clause list
get-all-vars([],[]).


%case still something left
get-all-vars([H|T],Z) :- get-vars(H,X),get-all-vars(T,Y),append(X,Y,P),sort(P,Z).

%unsat-clauses
%clauses,state,result
%base case, no list to check unsat clauses on
unsat-clauses([],S,[]).

%first clause splits off
unsat-clauses([H|T],S,Z) :- eval-clause(S,H,P), (P =@= false ->
                                                unsat-clauses(T,S,R),
                                                append([H],R,Z),!;
                                                unsat-clauses(T,S,Z)).


%flip-var
%var,state,result
%flip var when the var is true
flip-var(H,[[H,R]|T],[[H,Y]|T]):-
    (R==true ->
        Y=false;
        Y=true).


%flip var when var is not there.
flip-var(H,[B|T],X) :-
flip-var(H,T,Z), append([B],Z,X).
flip-var(H,[],[]).


%get-better-neighbor
%clauses,state,vars,num-unsat,return
get-beter-neighbor(C,S,[],N,false).
get-better-neighbor(C,S,[F|B],N,X) :-
    flip-var(F,S,P),
    unsat-clauses(C,P,T),
    length(T,M),
    (N > M ->
    X=P,!;
    get-better-neighbor(C,S,B,N,X)).


%simple-hill-climb
%clause, state, distance, unsat clauses, return

%bases cases, zero distance or empty var list
simple-hill-climb(C,S,0,_, S).
simple-hill-climb(C,S,_,[],S).

%non-base case,
simple-hill-climb(C,S,D,U,Z) :-
    get-all-vars(C,P),
    length(U,N),
    get-better-neighbor(C,S,P,N,B),
    (B=@= false ->
    Z = S,!;
    unsat-clauses(C,B,V),E is D-1,simple-hill-climb(C,B,E,V,Z),!).
