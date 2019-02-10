int enough(int cap, int on, int wait) {
    int diff;
    return ((diff = cap - on) >= wait) ? 0 : (wait - diff);
}
