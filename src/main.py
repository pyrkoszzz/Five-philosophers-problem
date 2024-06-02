from utils import analize, draw_histograms, draw_philosophers_requests, draw_unsuccessful_attempts, run_simulation
from draw_events_array import draw_events


if __name__ == "__main__":
    n = 5
    det_lambda_i = [5, 5, 5, 5, 5]  # Deterministyczne wartości lambda_i
    rand_lambda_i = [0.5, 0.5, 0.5, 0.5, 0.5]  # Losowe wartości lambda_i
    det_mi = 1  # Czas trwania jedzenia
    T = 100  # Czas trwania symulacji

    draw_events(n, T)

    philosophers_det = run_simulation(n, det_lambda_i, det_mi, T, deterministic=True)
    philosophers_rand = run_simulation(n, rand_lambda_i, det_mi, T, deterministic=False)

    draw_philosophers_requests(philosophers_det, 'Momenty zgłaszania się filozofów po jedzenie (Deterministyczne)')
    draw_philosophers_requests(philosophers_rand, 'Momenty zgłaszania się filozofów po jedzenie (Losowe)')

    unsuccessful_attempts_det, eating_times_det, request_times_det = analize(philosophers_det, 'Wartości Deterministyczne')
    unsuccessful_attempts_rand, eating_times_rand, request_times_rand = analize(philosophers_rand, 'Wartości Losowe')

    draw_histograms(eating_times_det, 'Czas trwania jedzenia (Deterministyczne)')
    draw_histograms(eating_times_rand, 'Czas trwania jedzenia (Losowe)')
    draw_unsuccessful_attempts(unsuccessful_attempts_det, unsuccessful_attempts_rand)
