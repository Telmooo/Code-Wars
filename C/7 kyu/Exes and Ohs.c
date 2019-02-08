int xo(const char* str) {
	int oc = 0, xc = 0, i = 0;
	char c;
	while((c = *(str + i++)) != '\0') {
		if (c == 'o' || c == 'O')
			oc++;
		else if (c == 'x' || c == 'X')
			xc++;
	}
	return oc == xc;
}
