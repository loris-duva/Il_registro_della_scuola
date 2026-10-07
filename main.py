def leggi_studenti(nome_file):
    """Legge gli studenti dal file CSV."""
    studenti = []
    with open(nome_file, "r", encoding="utf-8") as f:
        next(f, None)
        for riga in f:
            riga = riga.strip()
            if not riga:
                continue
            parti = riga.split(",")
            studente = {
                "id": int(parti[0].strip()),
                "cognome": parti[1].strip(),
                "nome": parti[2].strip(),
                "classe": parti[3].strip(),
                "media": float(parti[4].strip())
            }
            studenti.append(studente)
    return studenti


def leggi_richieste(nome_file):
    """Legge le richieste dal file."""
    with open(nome_file, "r", encoding="utf-8") as f:
        righe = [riga.strip() for riga in f if riga.strip()]

    lista_id = [int(x.strip()) for x in righe[0].split(",") if x.strip()]
    cognome = righe[1]
    classe = righe[2]
    return lista_id, cognome, classe


def cerca_per_id(studenti, id_cercato):
    """Cerca uno studente per ID."""
    for studente in studenti:
        if studente["id"] == id_cercato:
            return studente
    return None


def stampa_studente(studente):
    """Stampa i dati di uno studente."""
    print(f"{studente['id']} {studente['cognome']} {studente['nome']} {studente['classe']} {studente['media']}")


def cerca_per_cognome(studenti, cognome_cercato):
    """Cerca gli studenti per cognome."""
    risultati = []
    for studente in studenti:
        if studente["cognome"].lower() == cognome_cercato.lower():
            risultati.append(studente)
    return risultati


def calcola_media_classe(studenti, classe_cercata):
    """Calcola la media dei voti di una classe."""
    somma = 0.0
    conteggio = 0
    for studente in studenti:
        if studente["classe"].upper() == classe_cercata.upper():
            somma += studente["media"]
            conteggio += 1

    if conteggio == 0:
        return 0, 0.0
    return conteggio, somma / conteggio


def main():
    file_studenti = "studenti.csv"
    file_richieste = "richieste.txt"

    studenti = leggi_studenti(file_studenti)
    lista_id, cognome, classe = leggi_richieste(file_richieste)

    print("--- Ricerca per ID ---")
    for id_studente in lista_id:
        studente = cerca_per_id(studenti, id_studente)
        if studente is not None:
            stampa_studente(studente)
        else:
            print(f"ID {id_studente} non trovato")

    print()

    print(f"--- Ricerca per cognome: {cognome} ---")
    studenti_trovati = cerca_per_cognome(studenti, cognome)
    if studenti_trovati:
        for studente in studenti_trovati:
            stampa_studente(studente)
    else:
        print("Nessuno studente trovato")

    print()

    print(f"--- Media della classe {classe} ---")
    num_studenti, media = calcola_media_classe(studenti, classe)
    if num_studenti > 0:
        print(f"Studenti considerati: {num_studenti}")
        print(f"Media: {media:.2f}")
    else:
        print(f"Nessuno studente nella classe {classe}")


if __name__ == "__main__":
    main()
