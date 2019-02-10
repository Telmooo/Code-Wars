int points(char* games[]) {
    int home, away, score = 0;
    for (int i = 0; i < 10; i++) {
      home = **(games + i);
      away = *(*(games + i)+ 2);
      score += 3 * (home > away) + (home == away);
    }
    return score;
}
