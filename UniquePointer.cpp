
#include <iostream>

// copy constructor and copy assignment operator are deleted to prevent copying
class UniquePointer
{
public:
  UniquePointer(int* id)
  : m_id(id)
  {
    std::cout << "unique ptr created.." << std::endl;
  }
  
  UniquePointer(const UniquePointer& other) = delete;
  
  UniquePointer& operator=(UniquePointer) = delete;
  
  ~UniquePointer()
  {
    delete m_id;
    std::cout << "unique ptr destructed.." << std::endl;
  }

private:
  int* m_id;
};

int main() 
{
  {
    //int xOnStack = 10;
    int* ptr = new int(5);
    UniquePointer obj(ptr); // new int
  }


  return 0;
}
