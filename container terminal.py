import simpy
import random


AVG_ARRIVAL_INTERVAL = 5 * 60  
CONTAINERS_PER_VESSEL = 150
CRANE_MOVE_TIME = 3  
TRUCK_CYCLE_TIME = 6  
NUM_BERTHS = 2
NUM_CRANES = 2
NUM_TRUCKS = 3
SIMULATION_TIME = 24 * 60  

def vessel_arrival(env, terminal):
    """Generate vessels arriving at the terminal"""
    vessel_id = 0
    while True:
        yield env.timeout(random.expovariate(1.0 / AVG_ARRIVAL_INTERVAL))
        vessel_id += 1
        env.process(vessel_process(env, vessel_id, terminal))

def vessel_process(env, vessel_id, terminal):
    """Process of a vessel arriving and being handled at the terminal"""
    print(f"{env.now}: Vessel {vessel_id} arrives at the terminal.")
    
    with terminal['berths'].request() as req:
        yield req
        print(f"{env.now}: Vessel {vessel_id} docks at a berth.")
        
        for container in range(CONTAINERS_PER_VESSEL):
            with terminal['cranes'].request() as crane_req:
                yield crane_req
                print(f"{env.now}: Crane starts unloading container {container + 1} from vessel {vessel_id}.")
                yield env.timeout(CRANE_MOVE_TIME)
                
                with terminal['trucks'].request() as truck_req:
                    yield truck_req
                    print(f"{env.now}: Container {container + 1} from vessel {vessel_id} is being transported by a truck.")
                    yield env.timeout(TRUCK_CYCLE_TIME)
                    
        print(f"{env.now}: Vessel {vessel_id} has unloaded all containers and leaves the terminal.")

def main():
    random.seed(42)  
    env = simpy.Environment()

    terminal = {
        'berths': simpy.Resource(env, NUM_BERTHS),
        'cranes': simpy.Resource(env, NUM_CRANES),
        'trucks': simpy.Resource(env, NUM_TRUCKS)
    }

    env.process(vessel_arrival(env, terminal))
    env.run(until=SIMULATION_TIME)

if __name__ == "__main__":
    main()
