class Process:

  """

  Representa um processo do sistema computacional

  """

  def __init__(self, name: str, size: int, priority: int, arrival_time: int) -> None:

    """
    
    Parâmetros:

      name: Nome do processo
      size: Tamanho do processo (em unidades)
      priority: Número de prioridade de execução (Quanto menor, mais prioritário)
      arrival_time: Tempo de chegada do processo na fila de pronto

    """

    self.__name = name
    self.__size = size
    self.__priority = priority
    self.__arrival_time = arrival_time
  
  @property
  def name(self) -> str:

    return self.__name
  
  @property
  def size(self) -> str:

    return self.__size
  
  @property
  def priority(self) -> str:

    return self.__priority
  
  @property
  def arrival_time(self) -> str:

    return self.__arrival_time
  
  def reduceSize(self, size_reduced: int) -> None:

    """
    Reduz a quantidade de unidades de tamanho passada como argumento do tamanho do processo
    """

    if self.__size - size_reduced < 0:

      return

    self.__size -= size_reduced