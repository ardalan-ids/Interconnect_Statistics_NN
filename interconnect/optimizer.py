'''
optimizations fucntions
'''
from itertools import permutations
import numpy as np


def ext_placement_search(func, B, find_max=False):
    '''
    trys out all possible discrete placements
    and finds the one that minimzes(or maximizes,
    if "max"=True the return value of "func()".
    '''
    perm = set(range(B))
    cost = func(perm)
    for i in permutations(range(B)):
        perm_neu = i
        cost_neu = func(i)

        if (find_max is True and cost_neu > cost) or (find_max is False
                                                      and cost_neu < cost):
            perm, cost = perm_neu, cost_neu
    return {'placement': perm, 'cost': cost}


def routing_length_placement(M, N,  d_t, perm, h_d, d_d):
    '''
    manhatten distances for each driver output to the tsv for a given
    assignment perm. Symetrie is considered and always the one with the lowest
    maximum is returned
    M : TSV array rows
    N : TSV array columns
    d_tsv: min TSV spacing
    perm : assignment
    h_drive: spacing of the driver outputs (std_cell height)
    d_drive: min. spacing between drivers and output
    consider that counting starts here at 0!!!!
    '''
    NB = M*N
    # # position of the input drivers
    # x_d = np.zeros(NB) (not required)
    y_d = np.array([((NB-1)/2 - i)*h_d for i in range(NB)])
    y_d = np.array([y_d[perm[i]] for i in range(NB)])  # do the permutation
    # # position of the tsvs
    # y when starting in the top row
    y_up = np.array([((M-1)/2 - np.floor(i/N))*d_t for i in range(NB)])
    # y when starting in the bottom row
    y_bot = -y_up
    # x when starting left
    x_left = [np.mod(i, N)*d_t + d_d for i in range(NB)]
    x_right = [(N-1)*d_t - np.mod(i, N)*d_t + d_d for i in range(NB)]
    cost_max = np.max(x_left + np.abs(y_up - y_d))
    rl = (x_left + np.abs(y_up - y_d))
    for x in [x_left, x_right]:
        for y in [y_up, y_bot]:
            rl_temp = x + np.abs(y - y_d)
            if np.max(rl_temp) < cost_max:
                cost_max = np.max(rl_temp)
                rl = rl_temp
    return rl


def routing_length_all_placements(M, N,  d_t, h_d, d_d):
    rl_list = []
    for perm in permutations(range(M*N)):
        rl_list.append(routing_length_placement(M, N,  d_t, perm, h_d, d_d))
    return rl_list


def get_the_wc_routing_increase(M, N,  d_t, h_d, d_d):
    rl_vec = routing_length_all_placements(M, N,  d_t, h_d, d_d)
    longest_route = []
    mean_route = []
    for i in range(len(rl_vec)):
        longest_route.append(np.max(rl_vec[i]))
        mean_route.append(np.mean(rl_vec[i]))
    best_peak = np.min(longest_route)
    best_mean = np.min(mean_route)
    worst_peak = np.max(longest_route)
    worst_mean = np.max(mean_route)
    mean_mean_incr = np.mean(mean_route - best_mean)
    mean_wc_incr = np.mean(longest_route - best_peak)
    std_mean_incr = np.std(mean_route - best_mean)
    std_wc_incr = np.std(longest_route - best_peak)
    return {'best_peak': best_peak, 'best_mean': best_mean,
            'worst_peak': worst_peak, 'worst_mean': worst_mean,
            'mean_wc_incr': mean_wc_incr, 'mean_mean_incr': mean_mean_incr,
            'std_wc_incr': std_wc_incr, 'std_mean_incr': std_mean_incr}
