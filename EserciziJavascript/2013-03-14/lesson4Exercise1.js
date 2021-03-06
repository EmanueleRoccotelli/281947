/*
exercise01a

write a function that pushes into an array the first n natural numbers

exercise01b

filter out odd number and return the even ones

exercise01c

double each even number obtained

exercise01d

return only numbers divisible by four

exercise01e

sum all the remaining numbers
*/

function pushfirstnatural(n){
		var arrayNatural=[];
		for(var i=1; i<=n; i++)	{
			arrayNatural.push(i);
		}
		return arrayNatural;
	}

function filterOdd(n){
		var arrayFiltered = [];
		arrayFiltered = pushfirstnatural(n);

		arrayFiltered = arrayFiltered.filter(function(item, index, array){
			return ((item%2)===0);
		});

		return arrayFiltered;  
		}

function doubleEachNumber(n){
		var doubleNumbers= [];
		doubleNumbers = filterOdd(n);

		doubleNumbers = doubleNumbers.map(function(item, index, array){
			return (item*2);
		});

		return doubleNumbers;
}

function divisibleFour(n){
		var divisible = []
		divisible = doubleEachNumber(n);

		divisible = divisible.filter(function(item, index, array){
			return ((item%4)===0);
		})

		return divisible;
}

function sumAllDivisibleFour(n){
	var somma = 0;

	sumAll = divisibleFour(n);

	somma = sumAll.reduce(function(prev, cur, index, array){
		return prev + cur;
	});

	return somma;
}


