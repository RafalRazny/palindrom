# palindrom
Pisząc ten pogram oparłem się na schemacie stworzenia dwóch list i stosując operator "if", przetestowaniu ich instrukcją warunkową równości.
Pierwsza lista zawierać będzie znaki testowanego wyrazu w normalnej kolejności, druga w kolejności odwrotnej, od końca. Jeśli znaki wyrazu będą identyczne w obydwu listach, zarówno standardnowo jak i odwortnie, listy będą spełniać warunek równości co oznacza, że wyraz jest palidromem.
Znaki w liście będą uzupełniane przy użyciu pętli "for" iterującej wyraz będący parametrem funkcji. Do stworzenia listy odwrotnej użyłem funkcji "reversed()"
Funkcja "palindrom" będzie uznawać jeden argument pozycjny i tekstowy "word", który będzie wyrazem testowanym do warunku bycia palindromem.
