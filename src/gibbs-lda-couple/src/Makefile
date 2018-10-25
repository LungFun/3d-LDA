CC=		g++

OBJS=		strtokenizer.o dataset.o utils.o model.o
MAIN=		lda
 
all:	$(OBJS) $(MAIN).cpp
	$(CC)  -o   $(MAIN) $(MAIN).cpp $(OBJS) -g
	strip $(MAIN)

strtokenizer.o:	strtokenizer.h strtokenizer.cpp
	$(CC) -c -g -o  strtokenizer.o strtokenizer.cpp

dataset.o:	dataset.h dataset.cpp
	$(CC) -c -g -o  dataset.o dataset.cpp

utils.o:	utils.h utils.cpp
	$(CC) -c -g -o   utils.o utils.cpp

model.o:	model.h model.cpp
	$(CC) -c -g -o model.o model.cpp

test:
	

clean:
	rm $(OBJS) 
	rm $(MAIN)

