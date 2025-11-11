#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Análise de Mobilizadores - Banco do Brasil
API Flask com interface web para análise de rankings
"""

from flask import Flask, request, jsonify, render_template, send_file
from analise_melhorada import AnalisadorMobilizadoresMelhorado
import os
import io
import base64
from datetime import datetime
import logging

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Instância global do analisador
analisador = AnalisadorMobilizadoresMelhorado()

@app.route('/')
def index():
    """Página principal com interface de upload"""
    return render_template('index.html')

@app.route('/api/analisar', methods=['POST'])
def analisar_planilha():
    """Endpoint para análise da planilha"""
    try:
        if 'arquivo' not in request.files:
            return jsonify({'erro': 'Nenhum arquivo enviado'}), 400
        
        arquivo = request.files['arquivo']
        if arquivo.filename == '':
            return jsonify({'erro': 'Nenhum arquivo selecionado'}), 400
        
        if not arquivo.filename.endswith(('.xlsx', '.xls')):
            return jsonify({'erro': 'Formato de arquivo inválido. Use .xlsx ou .xls'}), 400
        
        # Processar o arquivo
        resultado = analisador.processar_planilha(arquivo)
        
        if resultado['sucesso']:
            return jsonify(resultado)
        else:
            return jsonify({'erro': resultado.get('erro', 'Erro desconhecido')}), 500
            
    except Exception as e:
        logger.error(f"Erro na análise: {str(e)}")
        return jsonify({'erro': f'Erro interno: {str(e)}'}), 500

@app.route('/api/download/<grupo>')
def download_ranking(grupo):
    """Download da imagem do ranking"""
    try:
        imagem_bytes = analisador.gerar_imagem_ranking(grupo)
        if imagem_bytes:
            return send_file(
                io.BytesIO(imagem_bytes),
                mimetype='image/png',
                as_attachment=True,
                download_name=f'ranking_{grupo.replace(" ", "_").lower()}.png'
            )
        else:
            return jsonify({'erro': 'Ranking não encontrado'}), 404
    except Exception as e:
        logger.error(f"Erro no download: {str(e)}")
        return jsonify({'erro': f'Erro no download: {str(e)}'}), 500

@app.route('/api/status')
def status():
    """Status da aplicação"""
    return jsonify({
        'status': 'online',
        'versao': '2.0',
        'timestamp': datetime.now().isoformat(),
        'correcoes': {
            'agro_registros': 12,
            'regulariza_agro_registros': 22,
            'criterio_ranking': 'percentual_atingimento'
        }
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)