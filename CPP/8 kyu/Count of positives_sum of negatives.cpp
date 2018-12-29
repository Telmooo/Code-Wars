#include <vector>

std::vector<int> countPositivesSumNegatives(std::vector<int> input)
{
    if (input.empty()) return {};
    int i = 0, sum = 0;
    for (int n: input)
      (n>0) ? i++: (n<0 ? sum+=n: 0);
    return {i, sum};
}
