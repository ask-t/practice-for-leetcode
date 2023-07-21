#include <iostream>
#include <map>

int main()
{
    std::map<std::string, std::string> dict;
    dict["brand"] = "ford";
    dict["model"] = "Mustang";
    dict["year"] = "1964";

    std::string x = "brand";

    // Check if x is a key in the dictionary
    bool isKeyPresent = (dict.find(x) != dict.end());

    // Print the result
    std::cout << std::boolalpha << isKeyPresent << std::endl;

    return 0;
}
