#include <iostream>
#include <fstream>
#include <string>

int main()
{
    // Open the file
    std::ifstream inputFile("./input.txt");

    // Check if the file is open
    if (!inputFile.is_open())
    {
        std::cerr << "Error opening the file!" << std::endl;
        return 1; // Return an error code
    }

    // Read the file line by line
    std::string line;
    while (std::getline(inputFile, line))
    {
        // Process each line (you can print it or do other operations)
        std::cout << line << std::endl;
    }

    // Close the file
    inputFile.close();

    return 0; // Return success
}
