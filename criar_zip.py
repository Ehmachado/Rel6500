#!/usr/bin/env python3
"""
Script para criar o ZIP do Sistema BB Final
Execute este arquivo para gerar o arquivo ZIP com todos os componentes
"""

import os
import zipfile
import datetime

def criar_zip_sistema():
    """Cria o ZIP final com todos os arquivos do sistema"""
    
    # Nome do arquivo ZIP
    nome_zip = 'sistema_bb_final.zip'
    
    # Lista de arquivos para incluir no ZIP
    arquivos_incluir = [
        'app.py',
        'analise_melhorada.py',
        'requirements.txt',
        'Procfile',
        'runtime.txt',
        'README.md',
        'INSTRUCOES_FINAIS.md',
        'templates/index.html'
    ]
    
    print("🚀 Criando ZIP do Sistema BB - Versão Final")
    print("=" * 60)
    print(f"📦 Arquivo: {nome_zip}")
    print(f"📅 Data: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print()
    
    # Remover ZIP anterior se existir
    if os.path.exists(nome_zip):
        os.remove(nome_zip)
        print(f"🗑️ ZIP anterior removido: {nome_zip}")
    
    # Criar novo ZIP
    try:
        with zipfile.ZipFile(nome_zip, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as zipf:
            
            arquivos_adicionados = 0
            arquivos_nao_encontrados = []
            
            # Adicionar arquivos principais
            for arquivo in arquivos_incluir:
                if os.path.exists(arquivo):
                    zipf.write(arquivo)
                    print(f"✅ Adicionado: {arquivo}")
                    arquivos_adicionados += 1
                else:
                    arquivos_nao_encontrados.append(arquivo)
                    print(f"⚠️ Arquivo não encontrado: {arquivo}")
            
            print()
            print("📊 RESUMO:")
            print(f"   • Arquivos adicionados: {arquivos_adicionados}")
            print(f"   • Arquivos não encontrados: {len(arquivos_nao_encontrados)}")
            
            if arquivos_nao_encontrados:
                print(f"   ⚠️ Arquivos faltantes: {', '.join(arquivos_nao_encontrados)}")
        
        # Verificar tamanho do ZIP
        if os.path.exists(nome_zip):
            tamanho = os.path.getsize(nome_zip)
            print(f"   • Tamanho do arquivo: {tamanho:,} bytes ({tamanho/1024:.1f} KB)")
            print()
            print("🎉 ZIP criado com sucesso!")
            print(f"📁 Local: {os.path.abspath(nome_zip)}")
        else:
            print("❌ Erro: ZIP não foi criado")
            
    except Exception as e:
        print(f"❌ Erro ao criar ZIP: {str(e)}")
        return False
    
    # Exibir instruções finais
    print()
    print("📋 INSTRUÇÕES DE USO:")
    print("   1. Extrair o ZIP em uma pasta")
    print("   2. Instalar dependências: pip install -r requirements.txt")
    print("   3. Executar: python app.py")
    print("   4. Abrir navegador: http://localhost:5000")
    print()
    print("🌐 PARA DEPLOY:")
    print("   - Railway: Conectar repositório GitHub")
    print("   - Heroku: heroku create app-name && git push heroku main")
    print("   - Veja INSTRUCOES_FINAIS.md para detalhes")
    
    return True

if __name__ == "__main__":
    criar_zip_sistema()