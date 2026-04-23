#include <iostream>
#include <string>


int main()
{
    bool exitFlag = false;;
    int runCount = 0;
    std::string userInput;

    std::cout << "Welcome to the program. I'll count how many times you press the enter key!" << std::endl;


    do
    {
        std::cout << "Press ENTER to continue or type EXIT to quit:" << std::endl;

        std::getline(std::cin, userInput);

        if (userInput == "EXIT")
        {
            exitFlag = true;
            std::cout << "Aww :( goodbye friend!" << std::endl;
        }
        else
        {
            runCount++;
            std::cout << "Enter pressed " << runCount << " times!" << std::endl;
        }

    } while (!exitFlag);

    return 0;
}

