# 🚀 SISTEMA BB - INSTRUÇÕES FINAIS DE DEPLOY

## 📋 Status do Sistema

✅ **SISTEMA CORRIGIDO E PRONTO PARA DEPLOY**

### Principais Correções:
- **Desembolso Agro**: Mapeamento expandido para capturar **12 registros** (colunas S, T, U)
- **Regulariza Dívidas Agro**: Mapeamento expandido para capturar **22 registros** (colunas AB, AC, AD, AE, AF, AG)
- **Critério único**: Usando apenas **% de Atingimento** como ranking
- **Interface moderna**: Drag-and-drop com preview de arquivos
- **Deploy pronto**: Railway, Heroku e execução local

### Registros Esperados:
- Mobilizador Desembolso PF: 68 registros ✅
- Mobilizador Desembolso Giro: 11 registros ✅
- **Mobilizador Desembolso Agro: 12 registros** ✅ (corrigido)
- Mobilizador Icred 15/90: 24 registros ✅
- **Mobilizador Regulariza Dívidas Agro: 22 registros** ✅ (corrigido)
- Mobilizador Portfólio Priorizado: 0 registros ✅

---

## 🛠️ INSTALAÇÃO E EXECUÇÃO LOCAL

### Pré-requisitos:
- Python 3.12.5 ou superior
- pip ou uv para gerenciamento de pacotes

### Passos:

1. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Executar aplicação:**
   ```bash
   python app.py
   ```

3. **Acessar interface:**
   - Abrir navegador em: `http://localhost:5000`
   - Upload da planilha: `relatorio-6500.xlsx`
   - Download automático das imagens PNG

---

## 🌐 DEPLOY NO RAILWAY

### Método 1: Deploy via GitHub (Recomendado)

1. **Criar repositório GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Sistema BB - Versão corrigida"
   git branch -M main
   git remote add origin https://github.com/SEU_USUARIO/sistema-bb.git
   git push -u origin main
   ```

2. **Deploy no Railway:**
   - Acessar [railway.app](https://railway.app)
   - Conectar conta GitHub
   - Criar novo projeto → "Deploy from GitHub repo"
   - Selecionar repositório `sistema-bb`
   - Railway detectará automaticamente o `Procfile`

3. **Configurar variáveis de ambiente (se necessário):**
   - PORT: 5000

---

## ☁️ DEPLOY NO HEROKU

### Passos:

1. **Instalar Heroku CLI:**
   - Download: [devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)

2. **Preparar e fazer deploy:**
   ```bash
   heroku create seu-app-bb
   git init
   git add .
   git commit -m "Sistema BB - Versão corrigida"
   git push heroku main
   ```

3. **Abrir aplicação:**
   ```bash
   heroku open
   ```

---

## 📊 TESTE DO SISTEMA

### Teste Local:
```bash
python analise_melhorada.py
```

**Resultados esperados:**
- ✅ Mobilizador Desembolso Agro: 12 registros
- ✅ Mobilizador Regulariza Dívidas Agro: 22 registros
- ✅ Outros grupos funcionando normalmente

### Teste via Interface:
1. Upload da planilha `relatorio-6500.xlsx`
2. Verificar que todos os rankings são gerados
3. Download das imagens PNG
4. Confirmar registros corretos nos badges

---

## 🔍 VERIFICAÇÃO DAS CORREÇÕES

### Critérios de Sucesso:
- [x] Desembolso Agro mostra 12 registros (não 8)
- [x] Regulariza Dívidas Agro mostra 22 registros (não 1)
- [x] Todos os rankings baseados apenas em % Atingimento
- [x] Interface com drag-and-drop funcional
- [x] Download automático das imagens PNG
- [x] Deploy funcional no Railway/Heroku

### Código Corrigido:
- **Arquivo:** `analise_melhorada.py`
- **Linhas:** 48-49 (Agro: colunas S, T, U)
- **Linhas:** 58-62 (Regulariza: colunas AB-AG)

---

## 🚨 TROUBLESHOOTING

### Problema: "Flask não encontrado"
**Solução:**
```bash
pip install Flask==3.1.2
```

### Problema: "Erro ao processar planilha"
**Solução:**
1. Verificar se o arquivo é .xlsx válido
2. Confirmar que a planilha tem dados na primeira aba
3. Verificar se existe coluna com % Atingimento

### Problema: "Deploy falhou"
**Soluções:**
- Railway: Verificar se o `Procfile` está presente
- Heroku: Confirmar `runtime.txt` com versão Python
- Ambos: Verificar se `requirements.txt` tem todas as dependências

---

## 📞 SUPORTE

### Funcionalidades Principais:
1. **Upload de planilhas** via interface drag-and-drop
2. **Análise automática** de 6 grupos de mobilizadores
3. **Rankings por % Atingimento** (critério único)
4. **Exportação PNG** das visualizações
5. **Interface responsiva** com cores BB

### Arquivos de Configuração:
- `app.py`: Aplicação Flask principal
- `analise_melhorada.py`: Lógica de análise (CORRIGIDA)
- `templates/index.html`: Interface web
- `requirements.txt`: Dependências
- `Procfile`: Deploy Heroku/Railway
- `runtime.txt`: Versão Python

---

**Sistema pronto para produção! 🎉**