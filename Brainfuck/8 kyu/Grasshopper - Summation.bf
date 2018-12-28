//Sum to n
, //input at cell #0
//cell #1 will be the sum
[
[>+>+<<-] //transfer data from cell #0 to cell #1 and #2
>>- //go to cell #2 and decrement
[
-<<+>> //transfer data from cell #2 to cell #0
]
<< //go to cell #0
]
>. //output cell #1
