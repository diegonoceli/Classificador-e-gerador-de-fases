import numpy as np


def geraMatrix():
	matrix=np.random.choice([0,1],size=(4,4),p=[1./3,2./3])
	matrix[0,3]=2
	matrix[3,0]=2
	print (matrix)
	nota=input('Digite um nota de 0 a 5 para a fase :')
	print(nota)
	#arquivo = np.loadtxt("arquivo.csv", delimiter=",")
	linhacompleta=np.asarray(matrix).reshape(-1)
	linhacompleta=np.insert(linhacompleta,len(linhacompleta),nota,axis=0)
	print(linhacompleta)
	import csv
	with open('arquivo.csv', 'a') as csvfile:
	    spamwriter = csv.writer(csvfile,dialect='excel',delimiter=',',
	                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	    spamwriter.writerow(linhacompleta)

def classifica():
	# Create your first MLP in Keras
	from keras.models import Sequential
	from keras.layers import Dense
	import numpy as np


	
	teste=np.array([1,0,0,2,0,1,0,0,1,0,0,0,2,0,0,0])
	dataset = np.loadtxt("arquivo.csv", delimiter=",")
	X = dataset[:,0:16]
	Y = dataset[:,16]

	model = Sequential()
	model.add(Dense(16, input_dim=16, activation='relu'))
	model.add(Dense(8, activation='relu'))
	model.add(Dense(1, activation='sigmoid'))

	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

	model.fit(X, Y, epochs=150, batch_size=10)

	teste=np.asmatrix(teste)
	result=model.predict(teste)
	print(teste,' previsto: ',result[0])



geraMatrix()
classifica()


