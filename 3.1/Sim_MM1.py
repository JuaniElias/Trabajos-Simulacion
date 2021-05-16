from termcolor import colored
import numpy as np

Q_LIMIT = 100  # Limit on queue length.
BUSY = 1  # Mnemonics for server's being busy
IDLE = 0  # and idle.

# Ints
next_event_type = num_custs_delayed = num_delays_required = num_events = num_in_q = server_status = 0
# Floats
area_num_in_q = area_server_status = mean_interarrival = mean_service = sim_time = time_last_event = \
    total_of_delays = 0.0

time_arrival = [0] * (Q_LIMIT + 1)
time_next_event = [0] * 3


def initialize():
    global sim_time, server_status, num_in_q, time_last_event, time_next_event, num_custs_delayed, total_of_delays, \
        area_num_in_q, area_server_status

    # Inicia el reloj de la sim
    sim_time = 0.0

    # Inicializa el estado de las variable
    server_status = IDLE
    num_in_q = 0
    time_last_event = 0.0

    # Inicializa los contadores estadísticos
    num_custs_delayed = 0
    total_of_delays = 0.0
    area_num_in_q = 0.0
    area_server_status = 0.0

    # Inicializa la lista de eventos. Como no hay ningún cliente, el evento de partida no se considera
    time_next_event[1] = sim_time + np.random.exponential(mean_interarrival)
    time_next_event[2] = 1.0e+30


def timing():
    global next_event_type, sim_time, num_events
    min_time_next_event = 1.0e+29
    next_event_type = 0
    # Determinar que tipo de evento es el siguiente a ocurrir
    for i in range(0, num_events):
        if time_next_event[i] < min_time_next_event:
            min_time_next_event = time_next_event[i]
            next_event_type = i

    # Verifica si la lista de eventos esta vacía o no.
    if next_event_type == 0:
        # La lista de eventos esta vacía y se detiene la sim.
        print("Lista de eventos vacía en el tiempo ", sim_time)
        exit(1)

    # La lista de eventos no esta vacía entonces se avanza el reloj de simulación
    sim_time = min_time_next_event


def arrive():
    global num_in_q, time_arrival, time_next_event, server_status, total_of_delays
    # Planea el siguiente arrivo
    time_next_event[1] = sim_time + np.random.exponential(mean_interarrival)

    # Valida si el servidor esta ocupado
    if server_status == BUSY:
        # El servidor esta ocupado, se incrementa el nro de clientes en cola
        num_in_q += 1
        # VAlida si hubo overflow en la cola
        if num_in_q > Q_LIMIT:
            # La cola se sobrepaso de clientes en espera, se frena la sim
            print("Overflow del arreglo time_arrival en el tiempo ", sim_time)
            exit(2)

        # Todavía hay lugar en la cola, se guarda el tiempo de arrivo del cliente que llega en el final de time_arrival
        time_arrival[num_in_q] = sim_time
    else:
        # El servidor esta sin trabajar, entonces el cliente que llega tiene delay de 0
        delay = 0.0
        total_of_delays += delay
        # Incrementa el numero de clientes en espera y se pone al servidor en estado de ocupado
        server_status = BUSY
        # Asigna un tiempo de partida para fin de servicio
        time_next_event[2] = sim_time + np.random.exponential(mean_service)


def depart():
    global num_in_q, server_status, time_next_event, sim_time, time_arrival, total_of_delays, num_custs_delayed

    # Valida si la cola esta vacía
    if num_in_q == 0:
        # La cola esta vacía, se pone el servidor como ocioso y se deja de considerar el evento de partida
        server_status = IDLE
        time_next_event[2] = 1.0e+30

    else:
        # La cola no esta vacía, se decrementa el numero de clientes en cola
        num_in_q -= 1
        # Se calcula el delay del cliente que empieza el servicio y se actualiza el acumulador de delay
        delay = sim_time - time_arrival[1]
        total_of_delays += delay

        # Incrementa el numero de clientes demorado y se programa la partida
        num_custs_delayed += 1
        time_next_event[2] = sim_time + np.random.exponential(mean_service)
        # Mueve a cada cliente en cola una posición para arriba
        # / * Move each customer in queue ( if any) up one place.* /
        for i in range(0, num_in_q):
            time_arrival[i] = time_arrival[i + 1]


def report():
    global total_of_delays, num_custs_delayed, area_num_in_q, sim_time, area_server_status
    # Calcula y muestra los estimados de las medidas de performance
    print("Average delay in queue minutes", total_of_delays / num_custs_delayed, '\n')
    print("Average number in queue", area_num_in_q / sim_time, '\n')
    print("Server utilization", area_server_status / sim_time, '\n')
    print("Time simulation ended minutes", sim_time, '\n')


def update_time_avg_stats():
    global sim_time, time_last_event, num_in_q, area_num_in_q, area_server_status, server_status
    # Calcula el tiempo desde el último evento y actualiza el marcador del ultimo evento
    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time

    # Actualiza el area debajo de la función Numero en cola
    area_num_in_q += num_in_q * time_since_last_event
    # Actualiza el area debajo de la función Servidor ocupado
    area_server_status += server_status * time_since_last_event


def main():
    global mean_interarrival, mean_service, num_delays_required, num_custs_delayed, next_event_type, num_events
    mean_interarrival = 1
    mean_service = 0.5
    num_delays_required = 1000

    num_events = 3

    initialize()

    while num_custs_delayed < num_delays_required:
        # Determinar el siguiente evento.
        timing()
        # Actualizar el tiempo de sim - promedio de acumuladores estadísticos.
        update_time_avg_stats()

        # Llamar a la función que corresponda luego.
        if next_event_type == 1:
            arrive()
            break
        elif next_event_type == 2:
            depart()
            break

    # Generar reporte y terminar la sim
    report()


main()
