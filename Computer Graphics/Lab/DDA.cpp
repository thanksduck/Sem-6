#include <iostream>
#include <SDL2/SDL.h>

int main(int argc, char* argv[]) {
    // initialize SDL2
    SDL_Init(SDL_INIT_VIDEO);

    // create a window
    SDL_Window* window = SDL_CreateWindow("DDA Line Drawing",
        SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
        640, 480, SDL_WINDOW_SHOWN);

    // create a renderer
    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1,
        SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);

    // clear the renderer
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
    SDL_RenderClear(renderer);

    // define two points for the line
    int x1 = 50;
    int y1 = 50;
    int x2 = 200;
    int y2 = 200;

    // calculate the slope and intercept
    float slope = (float)(y2 - y1) / (float)(x2 - x1);
    float intercept = y1 - slope * x1;

    // draw the line using the DDA algorithm
    int x = x1;
    float y = y1;
    while (x <= x2) {
        // put the pixel on the screen
        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
        SDL_RenderDrawPoint(renderer, x, (int)y);

        // increment the x and y values
        x++;
        y += slope;
    }

    // present the renderer
    SDL_RenderPresent(renderer);

    // wait for user to quit
    bool quit = false;
    SDL_Event event;
    while (!quit) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                quit = true;
            }
        }
    }

    // clean up and exit
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}

