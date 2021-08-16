'''
Exercise 3b
'''

import numpy as np
from matplotlib import pyplot as plt
import simulator_class as sim

np.random.seed(42)

if __name__ == '__main__':
    
    tot_loss_pr = []
    tot_time_sys = []
    tot_th_av_time_sys_list = []
    tot_pB_list = []
    LOADS = np.linspace(1e-5,13,100).tolist()
    FOG_NODES_VALS = [1,2,4,5]
    BUFFER_SIZES = np.linspace(0,29,30).tolist()
    
    # Buf = [5, inf], FOG_NODES = 2
    for FOG_NODES in FOG_NODES_VALS:
        
        load_list=[]
        loss_pr = []
        time_sys = []
        pB_list = []
        th_av_time_sys_list = []
        
        for BUFFER_SIZE in BUFFER_SIZES:
            
            # DATA OBJECT
            data = sim.Measure(0,0,0,0,0,0,0,0,0,0,[],[],0)
            
            # SIMULATION PARAMETERS
            LOAD = 4
            SERVICE = 1000.0
            ARRIVAL = SERVICE/LOAD
            #FOG_NODES = 2
            SIM_TIME = 300000
    
            # simulator
            s = sim.Simulator(data, LOAD, SERVICE, ARRIVAL, 
                              BUFFER_SIZE, FOG_NODES, SIM_TIME)
            print_everything = False
            data, time, _, _ = s.simulate(print_everything)
            
            # cumulate statistics
            load_list.append(LOAD)
            loss_pr.append(data.toCloud/data.arr)
            time_sys.append(data.delay/data.dep)
            
        tot_loss_pr.append(loss_pr)
        tot_time_sys.append(time_sys)
        tot_th_av_time_sys_list.append(th_av_time_sys_list)
        tot_pB_list.append(pB_list)
        
    colors = [['orangered','deepskyblue','lime','orange'],
              ['maroon','navy','darkgreen','chocolate']]
    # Loss probability vs Load
    for i in range(len(tot_loss_pr)):
        plt.plot(BUFFER_SIZES, tot_loss_pr[i], '.-', linewidth=.7, c=colors[1][i], label=f'Fog={FOG_NODES_VALS[i]}')
    plt.grid()
    plt.legend()
    plt.xlabel("Buffer size")
    plt.ylabel("Loss probability")
    plt.ylim([-0.05,1])
    plt.title('Loss probability vs Buffer size')
    plt.show()
    
    # Avg time spent in system vs Load
    for i in range(len(tot_time_sys)):
        plt.plot(BUFFER_SIZES, tot_time_sys[i], '.-', linewidth=0.5, c=colors[1][i], label=f'Fog={FOG_NODES_VALS[i]}')
    plt.grid()
    plt.legend()
    plt.xlabel("Buffer size")
    plt.ylabel("Avgerage time [ms]")
    #plt.xlim([0,4])
    plt.title('Avg time spent in system vs Buffer size')
    plt.show()


