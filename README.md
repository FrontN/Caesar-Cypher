# Caesar-Cypher
Questo progetto è un'implementazione del celebre Cifrario di Cesare, uno dei più antichi algoritmi di crittografia. Permette di cifrare e decifrare messaggi spostando ogni lettera di un numero fisso di posizioni nell'alfabeto.
🚀 Caratteristiche Cifratura e Decifratura: Gestite da un'unica funzione ottimizzata.
Gestione Simboli: Il programma ignora automaticamente numeri, spazi e caratteri speciali, mantenendoli inalterati.
Safe Shift: Supporta numeri di spostamento (shift) molto grandi grazie all'aritmetica modulare.
Interfaccia User-Friendly: Ciclo continuo per processare più messaggi senza riavviare il programma.
🛠️ Tecnologie Utilizzate Python 3.
xModulo string: Per una gestione sicura e standard dell'alfabeto ASCII.
Aritmetica Modulare: Per gestire il "wrap-around" della Z che torna alla A.
📖 Come Funziona (Algoritmo) L'utente inserisce la direzione (encode/decode), il testo e lo shift.Trasformazione: Se la scelta è decode, lo shift viene moltiplicato per -1.Iterazione: Il programma scorre ogni carattere:Se è una lettera, ne calcola la nuova posizione nell'alfabeto.Se non lo è (spazio, !, ?), lo aggiunge così com'è.Output: Restituisce la stringa finale ricomposta.
💻 Installazione e UtilizzoClona il repository:Bashgit clone https://github.com/FrontN/caesar-cipher.git
Naviga nella cartella:Bashcd caesar-cipher
Esegui il programma:Bashpython main.py
🧪 Esempi di EsecuzionePlaintextType 'encode' to encrypt, type 'decode' to decrypt: encode
Type your message: hello world!
Type the shift number: 5
Here's the result: mjqqt btwqi!
🤝 Contributi: I contributi sono benvenuti! Se hai suggerimenti per migliorare la gestione delle maiuscole o aggiungere nuovi cifrari, apri una Pull Request o un Issue.
