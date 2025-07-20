def analyze_logs(logs):
    alerts = []
    for log in logs:
        # Exemplo simples: se conter "error" no log, gera alerta
        if "error" in log.lower():
            alerts.append(f"Erro detectado no log: {log}")
    return alerts

def run_analysis(data):
    alerts = analyze_logs(data)
    return alerts
