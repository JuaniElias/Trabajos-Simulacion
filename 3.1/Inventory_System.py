import numpy as np
import matplotlib.pyplot as plt

amount = bigs = initial_inv_level = inv_level = next_event_type = num_events = num_months = num_value_demand = smalls = 0
a_holding = a_shortage = holding_cost = incremental_cost = maxlag = mean_interdemand = minlag = setup_cost = shortage_cost = sim_time = time_last_event = total_ordering_cost = 0.0
prob_distrib_demand = [0.0] * 26
time_next_event = [0.0] * 4


def timing():
    global next_event_type, sim_time
    sim_time = min(time_next_event)
    next_event_type = np.argmin(time_next_event)


def initialize():
    global sim_time, inv_level, total_ordering_cost, a_holding, a_shortage, time_last_event, time_next_event
    sim_time = 0  # inicializa el reloj de simulación

    # inicializa las variables de estado
    inv_level = initial_inv_level
    time_last_event = 0

    total_ordering_cost = a_holding = a_shortage = 0  # inicializa los contadores estadísticos

    # inicializa la lista de eventos
    time_next_event[0] = 10 ** 30
    time_next_event[1] = sim_time + np.random.exponential(mean_interdemand)
    time_next_event[2] = num_months
    time_next_event[3] = 1


def order_arrival():
    global inv_level, time_next_event, amount
    inv_level += amount
    time_next_event[0] = 10 ** 30  # Ya que no va a llegar otro pedido se saca este evento de la lista


def random_integer(prob):
    u = np.random.random()  # Genera un número con dist uniforme entre (0, 1)
    i = 1
    while u >= prob[i]:
        i += 1
    return i


def demand():
    global inv_level, time_next_event, mean_interdemand, prob_distrib_demand
    inv_level -= random_integer(prob_distrib_demand)
    time_next_event[1] = sim_time + np.random.exponential(mean_interdemand)


def evaluate():
    global inv_level, time_next_event, amount, total_ordering_cost, smalls, bigs
    if inv_level < smalls:  # evalúa si el stock es menor al minimo
        # se realiza un pedido
        amount = bigs - inv_level
        total_ordering_cost += setup_cost + incremental_cost * amount
        # se pone en la lista de eventos el pedido
        time_next_event[0] = sim_time + np.random.uniform(minlag, maxlag)
    time_next_event[3] += 1  # se pone en la lista de eventos la sig evaluación


def report(z):
    global holding_cost, total_ordering_cost, num_months, shortage_cost, a_shortage, a_shortage
    costos_o[z] = total_ordering_cost / num_months  # Promedio de costos por orden
    costos_h[z] = holding_cost * a_holding / num_months  # Promedio de costos por holding
    costos_s[z] = shortage_cost * a_shortage / num_months  # Promedio de costos por falta de inventario
    costos_t[z] = costos_o[z] + costos_h[z] + costos_s[z]  # Total de costos

    # print("("+str(smalls)+", "+str(bigs)+")     "+str(tot)+"    "+str(avg_ordering_cost)+"  "+str(
    # avg_holding_cost)+"   "+str(avg_shortage_cost))


def update_time_avg_stats():
    global time_last_event, a_shortage, a_holding
    # Determian el tiempo desde el último evento y actualiza el tiempo del último evento al tiempo actual
    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time

    # Determina el estado del nivel de inventario durante el intervalo previo
    if inv_level < 0:
        a_shortage -= inv_level * time_since_last_event
    elif inv_level > 0:
        a_holding += inv_level * time_since_last_event


def ploteano():
    fig, axs = plt.subplots(2, 2)
    fig.suptitle('Promedio de costos en 10 corridas --> s=' + str(smalls) + ' S=' + str(bigs))
    axs[0, 0].plot(costos_o)
    axs[0, 0].set_title('Costos por Orden')
    axs[0, 1].plot(costos_h, 'tab:orange')
    axs[0, 1].set_title('Costos de Retención')
    axs[1, 0].plot(costos_s, 'tab:green')
    axs[1, 0].set_title('Costos por falta de stock')
    axs[1, 1].plot(costos_t, 'tab:red')
    axs[1, 1].set_title('Total costos')
    for ax in axs.flat:
        ax.set(xlabel='nro corridas', ylabel='precio')
    fig.tight_layout()
    plt.show()


costos_o = [0] * 10
costos_h = [0] * 10
costos_s = [0] * 10
costos_t = [0] * 10
for z in range(10):
    num_events = 4  # Número de eventos para la función del tiempo
    initial_inv_level = 60
    num_months = 120
    num_policies = 9
    num_values_demand = 4
    mean_interdemand = 0.10
    setup_cost = 32
    incremental_cost = 3
    holding_cost = 1
    shortage_cost = 5
    minlag = 0.5
    maxlag = 1
    prob_distrib_demand = [0, 1 / 6, 3 / 6, 5 / 6, 1]
    small = [0, 20, 20, 20, 20, 40, 40, 40, 60, 60]
    big = [0, 40, 60, 80, 100, 60, 80, 100, 80, 100]

    smalls = small[2]
    bigs = big[2]
    initialize()
    flag = True
    while flag:
        timing()
        update_time_avg_stats()
        if next_event_type == 0:
            order_arrival()
        elif next_event_type == 1:
            demand()
        elif next_event_type == 3:
            evaluate()
        else:
            report(z)
            flag = False
ploteano()
