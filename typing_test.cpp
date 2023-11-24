
#include <iostream>
#include <string>
#include <chrono>
#include <cstdlib>

using namespace std;
using namespace std::chrono;

double calculateWPM(const string& text, long long elapsedMillis) {
    int wordCount = 1; // Start with 1 to count the first word
    for (char c : text) {
        if (c == ' ') {
            ++wordCount;
        }
    }
    double elapsedMinutes = elapsedMillis / 60000.0;
    return wordCount / elapsedMinutes;
}

int main() {
    string username;
    cout << "Welcome to Typing Master! Please enter your username: ";
    getline(cin, username);

    const string testSentence = "The quick brown fox jumps over the lazy dog";
    string typedText;
    auto start = high_resolution_clock::now(); // Declare start here

    do {
        system("cls"); // Clears the screen. Use "clear" if you're on Unix/Linux.
        cout << "Hello, " << username << "! Type the following sentence:" << endl;
        cout << testSentence << endl;

        start = high_resolution_clock::now(); // Reset start time
        getline(cin, typedText);
        if (typedText != testSentence) {
            cout << "There was a mistake, please try again." << endl;
            system("pause"); // Pauses the screen until the user presses a key.
        }

    } while (typedText != testSentence);

    auto end = high_resolution_clock::now(); // Declare end here
    auto duration = duration_cast<milliseconds>(end - start).count();
    double wpm = calculateWPM(testSentence, duration);

    cout << username << ", your typing speed is " << wpm << " WPM." << endl;
    return 0;
}
