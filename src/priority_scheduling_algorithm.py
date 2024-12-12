from typing import List, Tuple


from src.process import Process


class PrioritySchedulingAlgorithm:

  """
  Representa um algoritmo que implementa o critério de escalonamento por prioridade.
  """

  @staticmethod
  def execute(execution_process: Process, 
              ready_queue: List[Process]) -> Tuple[Process, List[Process]]:
    
    """
    Executa o critério de escalonamento por prioridade.

    Parâmetros:

      execution_process: Processo que está sendo executado pela CPU
      ready_queue: Fila de processos que se encontram no estado de pronto
    """
    
    # Se todas as unidades de tamanho do processo em execução forem executadas, o processo foi finalizado e a cpu fica livre
    if execution_process and execution_process.size == 0:

        execution_process = None
    
    if ready_queue:

      # Ordenar por prioridade
      ready_queue = sorted(ready_queue, key=lambda x: x.priority)

      """
      Se o primeiro processo for mais prioritário que o processo em execução, o processo da fila será removido dela e entrará em execução, enquanto que o processo que estava em execução será adicionado ao final da fila.
      
      Caso não haja processos em execução, apenas a etapa de remoção do processo mais prioritário da fila e adição a cpu será realizada.
      """
      if not execution_process or ready_queue[0].priority < execution_process.priority:

        process_aux = execution_process # Auxiliar para não perder o conteúdo

        execution_process: Process = ready_queue.pop(0)

        if process_aux:

          ready_queue.append(process_aux)

    if execution_process:

      execution_process.reduceSize(1)
    
    return execution_process, ready_queue