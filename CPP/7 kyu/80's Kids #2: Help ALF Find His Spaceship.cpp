using namespace std;

class EightiesKids2
{
public:
    static string findSpaceship(const string map)
    {
        int i = count(map.begin(), map.end(), '\n');
        int j = 0;
        for (int k=0; k<map.size(); k++) {
          if (map[k]=='\n') {
            i--; 
            j=0;
          } else if (map[k]=='X') {
            return "[" + to_string(j) + ", " + to_string(i) + "]";
          } else j++;
        }
        return "Spaceship lost forever.";
    }
};
