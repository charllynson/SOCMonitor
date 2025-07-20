# core/alert_manager.py

def generate_alerts(analyzed_data, threshold=50):
    """
    Gera alertas para itens que excedem um limiar de risco.
    """
    print("🚨 Gerando alertas para itens de alto risco...\n")
    alert_count = 0

    for item in analyzed_data:
        if item['risk_score'] >= threshold:
            alert_count += 1
            print("------------------------- ALERTA DE ALTO RISCO -------------------------")
            print(f"  Score de Risco: {item['risk_score']}")
            print(f"  Fonte: {item['source']}")
            print(f"  Motivo: {item['analysis_reason']}")
            print(f"  URL/Local: {item.get('url') or item.get('permalink')}")
            print("------------------------------------------------------------------------\n")
    
    if alert_count == 0:
        print("Nenhum alerta de alto risco gerado.")
    else:
        print(f"Total de {alert_count} alertas de alto risco gerados.")