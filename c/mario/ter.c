#include <stdio.h>
#include <conio.h>
#include <windows.h>

void drawMenu(int selected) {
    system("cls");  // Clear screen
    printf("Use ↑↓ arrows to navigate, Enter to select:\n\n");
    
    char* options[] = {"Option 1", "Option 2", "Option 3", "Exit"};
    int n = 4;
    
    for(int i = 0; i < n; i++) {
        if(i == selected) {
            printf("➤ %s\n", options[i]);  // Visual highlight with ➤ arrow
        } else {
            printf("  %s\n", options[i]);
        }
    }
    printf("\n");
}

int main() {
    int selected = 0;
    
    while(1) {
        drawMenu(selected);  // Draw menu FIRST
        
        int key = _getch();  // Get key input
        
        if(key == 13) {  // Enter pressed
            if(selected == 3) break;  // Exit
            printf("You selected: %s\nPress any key...", 
                   selected == 0 ? "Option 1" : 
                   selected == 1 ? "Option 2" : 
                   selected == 2 ? "Option 3" : "Exit");
            _getch();  // Wait for key
        }
        else if(key == 224) {  // Arrow/special key
            int arrow = _getch();  // Get arrow direction
            if(arrow == 72) selected = (selected > 0) ? selected-1 : 0;  // Up
            else if(arrow == 80) selected = (selected < 3) ? selected+1 : 3;  // Down
        }
        // Visual updates IMMEDIATELY on arrow press due to drawMenu() call at top
    }
    return 0;
}
