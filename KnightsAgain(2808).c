#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(){
	int lin = 0, col = 0, lin2 = 0, col2 = 0;
	char str[6];

	scanf("%[^\n]", str);
	
	if( str[0] == 'a' ){
		col = 1;
	}					
	else if( str[0] == 'b' ){
		col = 2;
	}
	else if( str[0] == 'c' ){
		col = 3;
	}
	else if( str[0] == 'd' ){
		col = 4;
	}
	else if( str[0] == 'e' ){
		col = 5;
	}
	else if( str[0] == 'f' ){
		col = 6;
	}
	else if( str[0] == 'g' ){
		col = 7;
	}
	else if( str[0] == 'h' ){
		col = 8;
	}
	
	if( str[3] == 'a' ){
		col2 = 1;
	}					
	else if( str[3] == 'b' ){
		col2 = 2;
	}
	else if( str[3] == 'c' ){
		col2 = 3;
	}
	else if( str[3] == 'd' ){
		col2 = 4;
	}
	else if( str[3] == 'e' ){
		col2 = 5;
	}
	else if( str[3] == 'f' ){
		col2 = 6;
	}
	else if( str[3] == 'g' ){
		col2 = 7;
	}
	else if( str[3] == 'h' ){
		col2 = 8;
	} 

	lin = (int)str[1] - 48;
	lin2 =  (int)str[4] - 48;
	
	if( (lin2 - 2 == lin) && (col2 + 1 == col) ){
		printf("VALIDO\n");
		return 0;
	}else if( (lin2 - 1 == lin ) && (col2 + 2 == col) ){
		printf("VALIDO\n");
		return 0;
	}else if( (lin2 + 1 == lin ) && (col2 + 2 == col) ){
		printf("VALIDO\n");
		return 0;
	}else if( (lin2 + 2 == lin ) && (col2 + 1 == col) ){
		printf("VALIDO\n");
		return 0;
	}else if( (lin2 + 2 == lin ) && (col2 - 1 == col) ){
		printf("VALIDO\n");
		return 0;
	}else if( (lin2 + 1 == lin ) && (col2 - 2 == col) ){
		printf("VALIDO\n");
		return 0;
	}else if( (lin2 - 1 == lin ) && (col2 - 2 == col) ){
		printf("VALIDO\n");
		return 0;
	}else if( (lin2 - 2 == lin ) && (col2 - 1 == col) ){
		printf("VALIDO\n");
		return 0;

	}else{
		printf("INVALIDO\n");
		return 0;
	}
}












