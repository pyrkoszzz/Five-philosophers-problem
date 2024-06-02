import matplotlib.pyplot as plt
import numpy as np

def draw_events(n: int, T: int):
    # Parametry symulacji
    event_types = ['Zgłoszenie do jedzenia', 'Zakończenie jedzenia', 'Niespełniona próba']

    # Tworzenie losowych zdarzeń dla przykładu
    np.random.seed(42)
    events = {event_type: {filozof: np.sort(np.random.choice(range(T), size=(T // 10), replace=False)) for filozof in range(n)} for event_type in event_types}

    # Rysowanie tablicy zdarzeń
    fig, ax = plt.subplots(figsize=(15, 8))

    for i, event_type in enumerate(event_types):
        for filozof in range(n):
            times = events[event_type][filozof]
            ax.scatter(times, [f'{event_type} - Filozof {filozof}' for _ in times], label=f'{event_type} - Filozof {filozof}', alpha=0.6)

    ax.set_xlabel('Czas (jednostki czasu)')
    ax.set_ylabel('Zdarzenie')
    ax.set_title('Tablica zdarzeń w symulacji 5-ciu filozofów')
    plt.xticks(range(0, T + 1, 5))
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    draw_events(5,100)