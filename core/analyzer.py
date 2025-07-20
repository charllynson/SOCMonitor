def analyze_data(collected_data):
    """
    Analisa os dados coletados e atribui uma pontuação de risco.
    """
    analyzed_results = []

    for item in collected_data:
        risk_score = 0
        reasons = []

        # Regras baseadas na fonte
        if item['source'] == 'dark_web':
            risk_score += 50
            reasons.append("Encontrado em fonte da Dark Web")
        elif item['source'] == 'github':
            risk_score += 30
            reasons.append("Encontrado em código no GitHub (risco de credencial/código vazado)")
        elif item['source'] == 'reddit':
            risk_score += 10
            reasons.append("Menção em discussão pública no Reddit")

        # Regras baseadas na palavra-chave
        keyword = item.get('matched_keyword') or item.get('keyword', '')
        if 'password' in keyword.lower():
            risk_score += 25
            reasons.append("Palavra-chave 'password' detectada")
        if 'leak' in keyword.lower():
            risk_score += 25
            reasons.append("Palavra-chave 'leak' detectada")
        if 'gov.br' in keyword.lower():
            risk_score += 15
            reasons.append("Termo relacionado a 'gov.br' encontrado")

        item['risk_score'] = risk_score
        item['analysis_reason'] = ", ".join(reasons)
        analyzed_results.append(item)

    # Ordena os resultados pelo maior risco
    sorted_results = sorted(analyzed_results, key=lambda x: x['risk_score'], reverse=True)
    
    return sorted_results