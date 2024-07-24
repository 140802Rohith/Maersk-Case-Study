# Maersk-Case-Study
1. I used a  'simpy' and 'random' library for generating random vessel arrival times.
2. Then constants is been set such as
    Number of container per vessel = 150
    CRANE MOVE TIME = 3 
    TRUCK CYCLE TIME = 6
   Number of berths = 2
   Number of CRANES = 2
   Number of TRUCKS = 3
   SIMULATION_TIME = 24 * 60
   AVG_ARRIVAL_INTERVAL = 5 * 60
3. Then created a function (Vessel_arrival)to generate vessels arriving at the terminal. And assigning the number to the veseel that arriving .
4.  Then created a another function to handle the arrival, docking, and unloading of a vessel. When a vessel arrives, it requests a berth. If all berths are occupied, it waits until one becomes available
5.  Then noted the time of vessel arrival and docking using env.now to get the current simulation time.
6.  For each container on the vessel, request a crane resource, log the unloading operation, and simulate the time taken to move the container.
7.  After a container is moved by a crane, request a truck resource to transport the container to the yard block

  
