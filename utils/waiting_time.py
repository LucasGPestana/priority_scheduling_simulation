from typing import Dict, List


from src.process import Process

def countWaitingTimes(waiting_time: Dict[str, int], 
                      processes: List[Process],
                      ready_queue: List[Process]) -> Dict[str, int]:

  ready_queue_processes_name = [process.name for process in ready_queue]

  for process in processes:

    if process.name in ready_queue_processes_name:

      waiting_time[process.name] += 1
  
  return waiting_time