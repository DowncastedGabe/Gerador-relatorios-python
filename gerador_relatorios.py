from typing import Generator, Dict, Any, Optional

class GeradorRelatorios:
    def __init__(self, transacoes: list[Dict[str, Any]]):
        """
        Inicializa o gerador com a lista de transações.
        
        Args:
            transacoes: Lista de dicionários contendo as transações
                        Cada transação deve ter pelo menos:
                        - 'tipo': str (ex: 'saque', 'deposito', 'transferencia')
                        - 'valor': float
                        - 'data': str (data/hora no formato ISO)
        """
        self.transacoes = transacoes
    
    def gerar_relatorio(self, tipo_filtro: Optional[str] = None) -> Generator[Dict[str, Any], None, None]:
        """
        Gera um relatório iterável das transações, com filtro opcional por tipo.
        
        Args:
            tipo_filtro: Tipo de transação para filtrar (None para todas)
            
        Yields:
            Dicionário contendo os dados de cada transação que corresponde ao filtro
        """
        for transacao in self.transacoes:
            if tipo_filtro is None or transacao['tipo'].lower() == tipo_filtro.lower():
                yield transacao

# Exemplo de dados de transações
transacoes_conta = [
    {'tipo': 'deposito', 'valor': 1000.0, 'data': '2023-01-01T10:00:00'},
    {'tipo': 'saque', 'valor': 200.0, 'data': '2023-01-02T14:30:00'},
    {'tipo': 'transferencia', 'valor': 300.0, 'data': '2023-01-03T09:15:00'},
    {'tipo': 'deposito', 'valor': 500.0, 'data': '2023-01-04T16:45:00'}
]

# Criar o gerador
gerador = GeradorRelatorios(transacoes_conta)

# Iterar sobre todas as transações
print("Todas as transações:")
for transacao in gerador.gerar_relatorio():
    print(transacao)

# Filtrar apenas depósitos
print("\nApenas depósitos:")
for transacao in gerador.gerar_relatorio(tipo_filtro='deposito'):
    print(transacao)