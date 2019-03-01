#include <vector>

std::vector<int> tribonacci(std::vector<int> signature, int n) {
    std::vector<int> result;
    for (int i = 0; i < n; i++) {
      if (i < 3)
        result.push_back(signature.at(i));
      else
        result.push_back(result.at(i - 1) + result.at(i - 2) + result.at(i - 3));
    }
    return result;
}
