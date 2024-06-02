import numpy as np
import matplotlib.pyplot as plt
import simpy

from objects import Philosoph, Fork


def run_simulation(n, lambdas, mi, T, deterministic=True):
    env = simpy.Environment()
    
    chopsticks = [Fork(env, i) for i in range(n)]
    philosophers = [Philosoph(env, i, chopsticks[i], chopsticks[(i+1)%n], lambdas[i], mi, deterministic) for i in range(n)]
    
    env.run(until=T)
    
    return philosophers

def analize(philosophers, title):
    unsuccessful_attempts = [philosoph.unsuccessful_attempts for philosoph in philosophers]
    eating_times = [philosoph.eating_times for philosoph in philosophers]
    request_times = [philosoph.request_times for philosoph in philosophers]

    print(f'\n{title}')
    for philosoph in philosophers:
        print(f'philosoph {philosoph.id}:')
        print(f'  Liczba niespełnionych prób: {philosoph.unsuccessful_attempts}')
        print(f'  Czas trwania jedzenia: {philosoph.eating_times}')
        print(f'  Moment zgłoszeń po jedzenie: {philosoph.request_times}')
    
    return unsuccessful_attempts, eating_times, request_times

def draw_philosophers_requests(philosophers, title):
    plt.figure(figsize=(12, 6))
    for philosoph in philosophers:
        request_times = philosoph.request_times
        filozof_id = philosoph.id
        plt.scatter(request_times, [filozof_id] * len(request_times), label=f'Filozof {filozof_id}', alpha=0.6)
    
    plt.xlabel('Czas (jednostki czasu)')
    plt.ylabel('Filozofowie')
    plt.yticks(range(len(philosophers)), [f'Filozof {i}' for i in range(len(philosophers))])
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

def draw_histograms(eating_times, title):
    plt.figure(figsize=(10, 4))
    for i, times in enumerate(eating_times):
        plt.hist(times, bins=10, alpha=0.5, label=f'Filozof {i}')
    plt.xlabel('Czas trwania jedzenia')
    plt.ylabel('Częstotliwość')
    plt.title(title)
    plt.legend()
    plt.show()

def draw_unsuccessful_attempts(unsuccessful_attempts_det, unsuccessful_attempts_rand):
    ind = np.arange(len(unsuccessful_attempts_det))
    width = 0.35

    fig, ax = plt.subplots()
    ax.bar(ind - width/2, unsuccessful_attempts_det, width, label='Deterministyczne')
    ax.bar(ind + width/2, unsuccessful_attempts_rand, width, label='Losowe')

    ax.set_xlabel('Filozofowie')
    ax.set_ylabel('Niespełnione próby')
    ax.set_title('Niespełnione próby dla wartości deterministycznych i losowych')
    ax.set_xticks(ind)
    ax.set_xticklabels([f'Filozof {i}' for i in range(len(unsuccessful_attempts_det))])
    ax.legend()

    plt.show()