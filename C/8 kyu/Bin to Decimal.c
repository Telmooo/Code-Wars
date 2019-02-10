unsigned bin_to_decimal(const char *bin) {
    unsigned decimal = 0;
    while (*bin != '\0') {
        decimal = (*bin++ - '0') + (decimal << 1);
    }
    return decimal;
}
