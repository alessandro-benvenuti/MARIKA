"""
Modulo di configurazione per HealthcareMAS
Gestisce la lettura delle variabili d'ambiente dal file .env
"""

import os
from pathlib import Path
from typing import Optional, Dict, Any
import warnings


class Config:
    """
    Classe per gestire la configurazione dell'applicazione.
    Legge le variabili d'ambiente dal file .env e le rende disponibili.
    """
    
    def __init__(self, env_file: str = ".env"):
        """
        Inizializza la configurazione caricando il file .env
        
        Args:
            env_file (str): Percorso del file .env (default: ".env")
        """
        self._config_data = {}
        self._env_file = env_file
        self._load_env_file()
    
    def _load_env_file(self) -> None:
        """Carica le variabili dal file .env"""
        env_path = Path(self._env_file)
        
        if not env_path.exists():
            warnings.warn(f"File {self._env_file} non trovato. Usando solo variabili d'ambiente del sistema.")
            return
        
        try:
            with open(env_path, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, 1):
                    line = line.strip()
                    
                    # Salta righe vuote e commenti
                    if not line or line.startswith('#'):
                        continue
                    
                    # Parsing della riga KEY=VALUE
                    if '=' in line:
                        key, value = line.split('=', 1)
                        key = key.strip()
                        value = value.strip()
                        
                        # Rimuovi virgolette se presenti
                        if value.startswith('"') and value.endswith('"'):
                            value = value[1:-1]
                        elif value.startswith("'") and value.endswith("'"):
                            value = value[1:-1]
                        
                        self._config_data[key] = value
                        
                        # Imposta anche come variabile d'ambiente del sistema
                        os.environ[key] = value
                    else:
                        warnings.warn(f"Riga {line_num} nel file {self._env_file} ignorata: formato non valido")
                        
        except Exception as e:
            warnings.warn(f"Errore nel caricamento del file {self._env_file}: {e}")
    
    def get(self, key: str, default: Optional[str] = None) -> Optional[str]:
        """
        Recupera il valore di una variabile di configurazione
        
        Args:
            key (str): Nome della variabile
            default (Optional[str]): Valore di default se la variabile non esiste
            
        Returns:
            Optional[str]: Valore della variabile o default
        """
        # Prima cerca nei dati caricati dal file .env
        if key in self._config_data:
            return self._config_data[key]
        
        # Poi cerca nelle variabili d'ambiente del sistema
        return os.environ.get(key, default)
    
    def get_required(self, key: str) -> str:
        """
        Recupera il valore di una variabile obbligatoria
        
        Args:
            key (str): Nome della variabile
            
        Returns:
            str: Valore della variabile
            
        Raises:
            ValueError: Se la variabile non è definita
        """
        value = self.get(key)
        if value is None:
            raise ValueError(f"Variabile di configurazione obbligatoria '{key}' non trovata")
        return value
    
    def get_bool(self, key: str, default: bool = False) -> bool:
        """
        Recupera il valore di una variabile come boolean
        
        Args:
            key (str): Nome della variabile
            default (bool): Valore di default
            
        Returns:
            bool: Valore booleano
        """
        value = self.get(key)
        if value is None:
            return default
        
        return value.lower() in ('true', '1', 'yes', 'on', 'enabled')
    
    def get_int(self, key: str, default: int = 0) -> int:
        """
        Recupera il valore di una variabile come intero
        
        Args:
            key (str): Nome della variabile
            default (int): Valore di default
            
        Returns:
            int: Valore intero
        """
        value = self.get(key)
        if value is None:
            return default
        
        try:
            return int(value)
        except ValueError:
            warnings.warn(f"Impossibile convertire '{value}' in intero per '{key}'. Usando default: {default}")
            return default
    
    def get_float(self, key: str, default: float = 0.0) -> float:
        """
        Recupera il valore di una variabile come float
        
        Args:
            key (str): Nome della variabile
            default (float): Valore di default
            
        Returns:
            float: Valore float
        """
        value = self.get(key)
        if value is None:
            return default
        
        try:
            return float(value)
        except ValueError:
            warnings.warn(f"Impossibile convertire '{value}' in float per '{key}'. Usando default: {default}")
            return default
    
    def list_all(self) -> Dict[str, str]:
        """
        Restituisce tutte le variabili di configurazione caricate
        
        Returns:
            Dict[str, str]: Dizionario con tutte le variabili
        """
        # Combina i dati del file .env con le variabili d'ambiente del sistema
        all_vars = dict(os.environ)
        all_vars.update(self._config_data)
        return all_vars
    
    def reload(self) -> None:
        """Ricarica la configurazione dal file .env"""
        self._config_data.clear()
        self._load_env_file()
    
    @property
    def openai_key(self) -> str:
        """Proprietà di convenienza per la chiave OpenAI"""
        return self.get_required('OPEN_AI_KEY')


# Istanza globale della configurazione
config = Config()


# Funzioni di convenienza per accesso rapido
def get_config(key: str, default: Optional[str] = None) -> Optional[str]:
    """Funzione di convenienza per ottenere una variabile di configurazione"""
    return config.get(key, default)


def get_required_config(key: str) -> str:
    """Funzione di convenienza per ottenere una variabile obbligatoria"""
    return config.get_required(key)


def get_openai_key() -> str:
    """Funzione di convenienza per ottenere la chiave OpenAI"""
    return config.openai_key


def reload_config() -> None:
    """Ricarica la configurazione"""
    config.reload()


if __name__ == "__main__":
    # Test del modulo
    print("=== Test del modulo di configurazione ===")
    print(f"OpenAI Key presente: {'Sì' if config.get('OPEN_AI_KEY') else 'No'}")
    print(f"Numero totale variabili caricate: {len(config._config_data)}")
    
    # Mostra tutte le variabili caricate (nascondendo valori sensibili)
    print("\nVariabili caricate dal file .env:")
    for key, value in config._config_data.items():
        if 'key' in key.lower() or 'password' in key.lower() or 'secret' in key.lower():
            masked_value = value[:8] + "..." if len(value) > 8 else "***"
            print(f"  {key}: {masked_value}")
        else:
            print(f"  {key}: {value}")