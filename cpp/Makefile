CXX=g++
LD=g++
CXXFLAGS=-std=c++14 -Wall -pthread
OBJ=obj
OUT=out

thread: $(OBJ)/thread_example.o
	@echo "=== Building Thread Example ==="
	mkdir -p $(OUT)
	$(LD) $(CXXFLAGS) $^ -o $(OUT)/$@

clean:
	rm -rf obj out


$(OBJ)/%.o: %.cpp
	@echo "=== Compiling cpp files ==="
	mkdir -p $(OBJ)
	$(CXX) -c $(CXXFLAGS) $< -o $@
