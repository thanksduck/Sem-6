## set up the graphics on your device

### Windows
1. Install SDL2
    1. Download the development library from [here](https://www.libsdl.org/download-2.0.php)
    2. Extract the zip file
    3. Copy the SDL2 folder to C:\Program Files (x86)\
    4. Copy the SDL2.dll file to C:\Windows\System32\
    5. Copy the SDL2.lib file to C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.16.27023\lib\x64\


    
### Mac
1. Install SDL2
```bash
brew install sdl2
```

2. Install SDL2_image
```bash
brew install sdl2_image
```

### Linux
1. Install SDL2
```bash
sudo apt-get install libsdl2-dev
```

2. Install SDL2_image
```bash
sudo apt-get install libsdl2-image-dev
```

## Compile and run the program
### Mac
1. Compile the program
```bash
g++ -std=c++11 DDL.cpp -o DDA -lSDL2 -lSDL2_image
```

2. Run the program
```bash
./DDA
```

### Linux
1. Compile the program
```bash
g++ -std=c++11 DDL.cpp -o DDA -lSDL2 -lSDL2_image
```

2. Run the program
```bash
./DDA
```

## Compile and run the program with Xcode
1. Create a new project
2. Add the SDL2 framework

    1. Go to the project navigator
    2. Right click on the project name
    3. Click on add files to "project name"
    4. Go to the SDL2 framework folder
    5. Select the SDL2.framework
    6. Click on add

in program add 
```c++
#include <SDL2/SDL.h>
```
```bash
g++ -std=c++11 -I/Library/Frameworks/SDL2.framework/Headers -F/Library/Frameworks DDL.cpp -o DDA -framework SDL2
```