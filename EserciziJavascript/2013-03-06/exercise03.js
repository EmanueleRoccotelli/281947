write a script exercise03.js that prints in console the following identity matrix, then commit it and push it:

var matrix = "";

for(var i=1; i<11; i++){
	for(var j=1; j<11; j++){
		
		if(i===j)
			matrix += (1) + '\t';
		else
			matrix += (0) + '\t';
	

		}
	matrix += '\n';
}

console.log(matrix);
