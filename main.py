from core.collector import run_collectors
from core.analyzer import analyze
from core.alert_manager import send_alerts
from core.utils import load_config, log

def main():
    config = load_config("config/config.yaml")
    log.info("Iniciando coleta de dados...")

    data = run_collectors(config)
    findings = analyze(data, config)
    send_alerts(findings, config)

if __name__ == "__main__":
    main()
