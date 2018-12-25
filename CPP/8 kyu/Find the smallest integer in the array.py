#include <vector>

using namespace std; 

int findSmallest(vector<int> list)
{
  int min;
  for (int i=0; i<list.size(); i++) {
    if (list[i] < min || !min) {
      min = list[i];
    }
  }
  return min;
}
