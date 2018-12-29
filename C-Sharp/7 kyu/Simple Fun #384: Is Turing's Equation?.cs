using System;

public static class Kata
{
  public static bool IsTuringEquation(string str)
  { 
    char[] delimiters = {'+', '='};
    char[] chars = str.ToCharArray();
    Array.Reverse(chars);
    string rev = new string(chars);
    string[] words = rev.Split(delimiters);
    return Int32.Parse(words[2])+Int32.Parse(words[1])==Int32.Parse(words[0]);
  }
}
