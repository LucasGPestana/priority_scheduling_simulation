from src.priority_scheduling_algorithm import PrioritySchedulingAlgorithm
from src.process import Process
from utils.waiting_time import countWaitingTimes

if __name__ == "__main__":

  ready_queue = []
  execution_process = None
  clock = 0
  time_line: str = ""

  processes = [
    Process('K', 5, 2, 0),
    Process('L', 3, 2, 2),
    Process('M', 4, 1, 3),
    Process('N', 1, 2, 3),
  ]

  total_clocks = sum(list(map(lambda x: x.size, processes)))

  waiting_time = {process.name: 0 for process in processes}

  while clock < total_clocks:

    for process in processes:

      if clock == process.arrival_time:

        ready_queue.append(process)
    
    execution_process, ready_queue = PrioritySchedulingAlgorithm.execute(execution_process, ready_queue)

    waiting_time = countWaitingTimes(waiting_time, processes, ready_queue)

    if execution_process:

      time_line += execution_process.name
    
    print("---"*20)
    print(f"Clock {clock}".center(60))
    print("Fila de Pronto:", [process.name for process in ready_queue])
    
    print("Processo em Execução:", execution_process.name if execution_process else "Nenhum")
    print("---"*20)

    input("Aperte qualquer tecla para gerar um sinal de clock...")

    clock += 1
  
  print("---"*20)
  print("Resultados".center(60))
  print("Linha do Tempo:", time_line)
  print("Tempo de espera:", ", ".join([f"{name} - {time}" for name, time in waiting_time.items()]))
  print("---"*20)
