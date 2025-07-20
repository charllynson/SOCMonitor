# main.py

import os
from dotenv import load_dotenv
from core.collector import run_collectors
from core.analyzer import analyze_data
from core.alert_manager import generate_alerts
from core.utils import load_config, save_json
from loguru import logger

def main():
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()

    config = load_config("config/config.yaml")

    # Pega o token da variável de ambiente e o adiciona ao dicionário de config
    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
        logger.error("A variável de ambiente GITHUB_TOKEN não foi encontrada!")
        logger.error("Certifique-se de criar um arquivo .env com seu token ou exportar a variável.")
        return # Encerra a execução se o token não for encontrado

    # Injeta o token no objeto de configuração para que os outros módulos possam usá-lo
    config['github_token'] = github_token
    
    logger.info("🔎 Iniciando coleta OSINT...")
    collected_data = run_collectors(config)
    logger.info(f"✅ {len(collected_data)} resultados brutos encontrados.")

    if not collected_data:
        logger.info("Nenhum dado foi coletado. Encerrando.")
        return

    logger.info("⚙️  Analisando dados coletados e calculando risco...")
    analyzed_data = analyze_data(collected_data)
    
    save_json("data/analyzed_data.json", analyzed_data)
    
    risk_threshold = 50 
    generate_alerts(analyzed_data, threshold=risk_threshold)


if __name__ == "__main__":
    main()