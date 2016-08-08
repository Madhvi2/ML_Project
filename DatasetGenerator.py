from fileSplitter import SplitFile


def create():
	
	SplitFile( '0' , '20' , '29' , 'S1' )
	SplitFile( '0' , '80.5' , '88.3' , 'S2' )
	SplitFile( '0' , '29.5' , '49.14' , 'W1' )
	SplitFile( '0' , '52' , '80' , 'W2' )
	
	SplitFile( '8' , '4.18' , '12.43' , 'S1' )
	SplitFile( '8' , '64.3' , '76.78' , 'S2' )
	SplitFile( '8' , '16.25' , '38.7' , 'W1' )
	SplitFile( '8' , '45.07' , '60.63' , 'W2' )
	
	SplitFile( '23' , '14.83' , '26.3' , 'J1' )
	SplitFile( '23' , '29.5' , '39.16' , 'J2' )
	SplitFile( '23' , '43.01' , '56.69' , 'R1' )
	SplitFile( '23' , '57.6' , '66.8' , 'R2' )
	
	SplitFile( '2' , '3.5' , '19.7' , 'S1' )
	SplitFile( '2' , '55.9' , '69.13' , 'S2' )
	SplitFile( '2' , '20' , '36.5' , 'W1' )
	SplitFile( '2' , '39' , '53' , 'W2' )
	
	SplitFile( '16' , '8.18' , '26.54' , 'J1' )
	SplitFile( '16' , '39.54' , '50.87' , 'J2' )
	SplitFile( '16' , '29.33' , '37.5' , 'R1' )
	SplitFile( '16' , '53.67' , '61.98' , 'R2' )
	
	SplitFile( '14' , '12.9' , '23.52' , 'J1' )
	SplitFile( '14' , '27.3' , '35.5' , 'J2' )
	SplitFile( '14' , '40' , '53' , 'R1' )
	SplitFile( '14' , '54' , '65' , 'R2' )
	
	
if __name__ == "__main__":
	create()