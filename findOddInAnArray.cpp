// Online C++ compiler to run C++ program online
#include <iostream>
#include <vector>
#include <algorithm>

std::uint32_t findOddInTheArray(std::vector<std::uint32_t>& input)
{
  std::sort(input.begin(), input.end());
  std::uint32_t oddValue = 0;

  for(auto it = input.begin(); it != input.end(); ++it)
  {
    if(it != input.end()) 
    {
      if(*it == *(it+1))
      {
        ++it;  
        continue;
      }
    }
    oddValue = *it;   
  }
  
  return oddValue;
}

int main() 
{
  std::vector<std::uint32_t> test{5, 10, 15, 5, 25, 25, 10, 15, 2, 10, 10};
  std::uint32_t result = findOddInTheArray(test);
  std::cout << "result: " << result << std::endl;
  return 0;
}
