/*
exercise02

exercise02a

write a function that pushes into an array n random integer numbers

exercise02b

filter even numbers and return the odd ones

exercise02c

sort obtained numbers from the smallest to the largest

*/

function function_pushRandomNumbers (n) {
	var naturalNumbers = [];

	for(var i=0; i<n; i++){
		naturalNumbers[i] = Math.floor(Math.random()*11);
	}

	return naturalNumbers;
}

function function_filterEven(n){
		var arrayFiltered = [];
		arrayFiltered = function_pushRandomNumbers(n);

		arrayFiltered = arrayFiltered.filter(function(item, index, array){
			return ((item%2)===1);
		});

		return arrayFiltered;  
		}

function function_sortSmallestLargest(n){
		var arrayCompare = [];
		arrayCompare = function_filterEven(n);

		arrayCompare.sort(function(value1, value2){
							return value1 - value2;
							});

		return arrayCompare;

}
