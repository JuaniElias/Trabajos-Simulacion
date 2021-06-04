import matplotlib.pyplot as plt
import numpy as np




def initialize():
    global sim_time, server_status, num_in_q, time_last_event, time_next_event, num_custs_delayed, total_of_delays_q, \
        total_of_delays_s, num_custs_served, area_num_in_q, area_num_in_s, area_server_status

    # Inicia el reloj de la sim
    sim_time = 0.0

    # Inicializa el estado de las variable
    server_status = IDLE
    num_in_q = [0]
    time_last_event = 0.0

    # Inicializa los contadores estadísticos
    num_custs_delayed = 0
    num_custs_served = 0
    total_of_delays_q = 0.0
    total_of_delays_s = 0.0
    area_num_in_q = 0.0
    area_num_in_s = 0.0
    area_server_status = 0.0

    # Inicializa la lista de eventos. Como no hay ningún cliente, el evento de partida no se considera
    time_next_event[0] = sim_time + np.random.exponential(mean_interarrival)
    time_next_event[1] = 1.0e+30


def timing():
    global next_event_type, sim_time
    sim_time = min(time_next_event)
    next_event_type = np.argmin(time_next_event)


def arrive():
    global num_in_q, time_arrival, time_next_event, server_status, total_of_delays_q, total_of_delays_s, f
    # Planea el siguiente arrivo
    time_next_event[0] = sim_time + np.random.exponential(mean_interarrival)

    # Valida si el servidor esta ocupado
    if server_status == BUSY:

        # VAlida si hubo overflow en la cola
        if num_in_q[-1] + 1 > Q_LIMIT:
            # La cola se sobrepaso de clientes en espera, se frena la sim
            print("No se pudo tomar al cliente en el tiempo de simulación= ", sim_time)
            f += 1
        else:
            # El servidor esta ocupado, se incrementa el nro de clientes en cola
            num_in_q.append(num_in_q[-1] + 1)
            # Todavía hay lugar en la cola, se guarda el tiempo de arrivo del cliente que llega en el final de time_arrival
            time_arrival[num_in_q[-1]] = sim_time


    else:
        # El servidor esta sin trabajar, entonces el cliente que llega tiene delay de 0
        delay = 0.0
        total_of_delays_q += delay
        # Incrementa el numero de clientes en espera y se pone al servidor en estado de ocupado
        server_status = BUSY
        # Asigna un tiempo de partida para fin de servicio
        service = np.random.exponential(mean_service)
        total_of_delays_s += delay + service
        time_next_event[1] = sim_time + service
        return True


def depart():
    global num_in_q, server_status, time_next_event, sim_time, time_arrival, total_of_delays_q, total_of_delays_s, num_custs_delayed, num_custs_served
    num_custs_served += 1
    # Valida si la cola esta vacía
    if num_in_q[-1] == 0:
        # La cola esta vacía, se pone el servidor como ocioso y se deja de considerar el evento de partida
        server_status = IDLE
        time_next_event[1] = 1.0e+30

    else:
        # La cola no esta vacía, se decrementa el numero de clientes en cola
        num_in_q.append(num_in_q[-1] - 1)
        # Se calcula el delay del cliente que empieza el servicio y se actualiza el acumulador de delay
        delay = sim_time - time_arrival[1]  # wtf por qué 1?
        total_of_delays_q += delay

        # Incrementa el numero de clientes demorado y se programa la partida
        num_custs_delayed += 1
        service = np.random.exponential(mean_service)
        total_of_delays_s += delay + service
        time_next_event[1] = sim_time + service
        # Mueve a cada cliente en cola una posición para arriba
        # / * Move each customer in queue ( if any) up one place.* /
        for i in range(0, num_in_q[-1]):
            time_arrival[i] = time_arrival[i + 1]


def report(z):
    global total_of_delays_q, num_custs_delayed, num_custs_served, area_num_in_q, area_num_in_s, sim_time, area_server_status, ok
    if num_custs_delayed == 0 or num_custs_served == 0:
        num_custs_delayed = 1
        num_custs_served = 1
    delay_q[z] = total_of_delays_q / num_custs_delayed
    delay_s[z] = total_of_delays_s / num_custs_served
    number_q[z] = area_num_in_q / sim_time
    number_s[z] = area_num_in_s / sim_time
    server_u[z] = area_server_status / sim_time
    time[z] = sim_time
    prob[z] = np.bincount(num_in_q)


def update_time_avg_stats():
    global sim_time, time_last_event, num_in_q, area_num_in_q, area_num_in_s, area_server_status, server_status
    # Calcula el tiempo desde el último evento y actualiza el marcador del ultimo evento
    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time

    # Actualiza el area debajo de la función Numero en cola
    area_num_in_q += num_in_q[-1] * time_since_last_event
    area_num_in_s += (num_in_q[-1] + 1) * time_since_last_event
    # Actualiza el area debajo de la función Servidor ocupado
    area_server_status += server_status * time_since_last_event





def prob_n_custs(prob):
    probability = [0]
    for i in range(len(prob)):
        p = prob[i]
        for j in range(len(p)):
            if len(probability) <= j:
                probability.append(p[j])
            else:
                probability[j] += p[j]
    tot = sum(probability)
    for i in range(len(probability)):
        probability[i] /= tot
    return probability


def ploteano(prob):
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle("Tiempos promedios en 10 corridas")
    ax1.plot(delay_q)
    ax1.set_title("En Cola")
    ax2.plot(delay_s, 'tab:orange')
    ax2.set_title("En el Sistema")
    fig.tight_layout()
    avg_delay_q = sum(delay_q) / len(delay_q)
    avg_delay_s = sum(delay_s) / len(delay_s)

    fig2, (ax3, ax4) = plt.subplots(2)
    fig2.suptitle("Número promedio de Clientes en 10 corridas")
    ax3.plot(number_q)
    ax3.set_title("En Cola")
    ax4.plot(number_s, 'tab:orange')
    ax4.set_title("En el Sistema")
    fig2.tight_layout()
    avg_number_q = sum(number_q) / len(number_q)
    avg_number_s = sum(number_s) / len(number_s)

    probability = prob_n_custs(prob)
    fig3, (ax5, ax6) = plt.subplots(2)
    ax5.plot(probability)
    ax5.set_title("Probabilidad de N clientes en cola en 10 corridas")
    ax6.plot(server_u, 'tab:orange')
    ax6.set_title("Utilización del sistema en 10 corridas")
    fig3.tight_layout()
    avg_server_u = sum(server_u) / len(server_u)

    plt.show()
    print("promedio delay q ", avg_delay_q)
    print("promedio delay s ", avg_delay_s)
    print("promedio number q ", avg_number_q)
    print("promedio number s ", avg_number_s)
    print("promedio server u ", avg_server_u)


def main(z):
    global mean_interarrival, mean_service, num_delays_required, num_custs_delayed, next_event_type, num_events
    p = [0.25, 0.50, 0.75, 1, 1.25]
    mean_service = 0.5  # 2
    mean_interarrival = 0.66666
    num_delays_required = 1000

    num_events = 3

    initialize()

    while num_custs_served < num_delays_required:
        # Determinar el siguiente evento.
        timing()
        # Actualizar el tiempo de sim - promedio de acumuladores estadísticos.
        update_time_avg_stats()

        # Llamar a la función que corresponda luego.
        if next_event_type == 0:
            arrive()
        elif next_event_type == 1:
            depart()

    # Generar reporte y terminar la sim
    report(z)


Q_LIMIT = 1000000
BUSY = 1  # Mnemonics for server's being busy
IDLE = 0  # and idle.

# Ints
next_event_type = num_custs_delayed = num_custs_served = num_delays_required = num_events = server_status = 0
# Floats
area_num_in_q = area_num_in_s = area_server_status = mean_interarrival = mean_service = sim_time = time_last_event = \
    total_of_delays_q = total_of_delays_s = 0.0

num_in_q = [0]

time_arrival = [0] * (Q_LIMIT + 1)
time_next_event = [0] * 2

delay_q = [0] * 10
delay_s = [0] * 10
number_q = [0] * 10
number_s = [0] * 10
server_u = [0] * 10
time = [0] * 10
prob = [0] * 10
f = 0
tot = 0
for i in range(10):
    main(i)
    tot += num_custs_served
ploteano(prob)
print('F', f)
