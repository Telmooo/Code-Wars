// Hello World!
//ASCII Values: 
//  H~72; e~101
//  l~108; o~111
//  " "~32; W~87
//  r~114; d~100
//  !~33
//generate cell #0 with value 10
++++++++++
//we multiples of ten generate close values for characters
//let's consider close values also has 1 character
[
> +++++++ //H character in cell #1
> ++++++++++ //d & e characters in cell #2
> +++++++++++ //l & o & r characters in cell #3
> +++++++++ //W character in cell #4
> +++ //" " & ! character in cell #5
<<<<<- //go to cell #0 and decrement
]
//characters are basically set, let's say Hello now :)
>++. //H character
>+. //e character
>--.. //l character (2 l's)
+++. // o character
>>++. //space
<---. //W character
<. //o character
+++. //r character
------. //l character
<-. //d character
>>>+. //! character
//finish
