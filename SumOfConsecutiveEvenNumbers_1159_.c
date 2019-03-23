# include <stdio.h>

int main (){
	int X, sum = 0, i=1;
	
	while( 1 ){
		scanf("%d", &X);
		if( X == 0 ){
			return 0;
		}
		if( X % 2 == 0 ){
			sum = sum + X;
			while( i < 5 ){
				X = X + 2;
				sum = sum + X;
				i++;
			}	
		}else{
			X = X + 1;
			sum = sum + X;		
			while ( i < 5 ){
				X = X + 2;
				sum = sum + X;
				i++;
			}
		}
		printf("%d\n", sum);
		sum = 0;
		X = 0;
		i = 1;
	}
}
